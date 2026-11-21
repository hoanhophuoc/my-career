#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Crawl Glints VN (server-rendered __NEXT_DATA__ JSON), chỉ giữ tin TP.HCM.

Nguồn: https://glints.com/vn/opportunities/jobs/explore?keyword=<kw>&country=VN&page=<n>
Không đăng nhập, không cookie, 1 request/trang, nghỉ 1,2s giữa các trang.
Đầu ra: 02f_glints_jobs_2026-11-20.csv (+ .json)
"""
import csv
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
DATA = HERE / "data"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
KEYWORDS = ["java", "spring boot", "backend", "fresher java"]
MAX_PAGES = 6
HCM = ("ho chi minh", "hồ chí minh", "hcm", "sai gon", "sài gòn")


def fetch(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept-Language": "vi,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml",
    })
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8", "ignore")


def next_data(html):
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    return json.loads(m.group(1)) if m else None


def is_hcm(job):
    loc = job.get("location") or {}
    names = [loc.get("name") or "", loc.get("formattedName") or ""]
    for p in loc.get("parents") or []:
        names += [p.get("name") or "", p.get("formattedName") or "", p.get("slug") or ""]
    for key in ("city", "citySubDivision"):
        v = job.get(key)
        if isinstance(v, dict):
            names += [v.get("name") or ""]
    blob = " ".join(names).lower()
    return any(k in blob for k in HCM)


def location_text(job):
    loc = job.get("location") or {}
    parts = [loc.get("name") or ""]
    for p in loc.get("parents") or []:
        if p.get("administrativeLevelName") in ("City", "Province"):
            parts.append(p.get("name") or "")
    return " - ".join([p for p in parts if p])


def _skill_name(s):
    """Glints trả skill dưới nhiều dạng: str, {'skill': str}, {'skill': {'name': str}}."""
    if isinstance(s, str):
        return s
    if isinstance(s, dict):
        v = s.get("skill", s)
        if isinstance(v, str):
            return v
        if isinstance(v, dict):
            return v.get("name") or v.get("displayName") or ""
    return ""


def salary_text(job):
    s = job.get("salaries") or []
    if not s:
        return "Not disclosed"
    out = []
    for x in s:
        cur = x.get("CurrencyCode") or ""
        lo, hi = x.get("minAmount"), x.get("maxAmount")
        mode = (x.get("salaryMode") or "MONTH").lower()
        unit = "/tháng" if mode == "month" else "/năm"
        if lo and hi:
            out.append(f"{lo:,.0f} - {hi:,.0f} {cur}{unit}")
        elif hi:
            out.append(f"Up to {hi:,.0f} {cur}{unit}")
    return " | ".join(out)


def main():
    rows, seen = [], set()
    log = []
    for kw in KEYWORDS:
        for page in range(1, MAX_PAGES + 1):
            url = ("https://glints.com/vn/opportunities/jobs/explore?"
                   + urllib.parse.urlencode({"keyword": kw, "country": "VN", "page": page}))
            try:
                html = fetch(url)
            except Exception as e:  # noqa: BLE001
                log.append(f"{kw} p{page} ERR {e}")
                break
            d = next_data(html)
            if not d:
                log.append(f"{kw} p{page} NO_DATA")
                break
            jp = d["props"]["pageProps"]["initialJobs"]
            jobs = jp.get("jobsInPage") or []
            new = 0
            for j in jobs:
                jid = j.get("id")
                if not jid or jid in seen:
                    continue
                if (j.get("country") or {}).get("code") != "VN":
                    continue
                if not is_hcm(j):
                    continue
                seen.add(jid)
                new += 1
                comp = j.get("company") or {}
                skills = ";".join(_skill_name(s) for s in (j.get("skills") or []))
                rows.append({
                    "search": kw,
                    "url": f"https://glints.com/vn/opportunities/jobs/{jid}",
                    "title": j.get("title") or "",
                    "company": comp.get("name") or "",
                    "salary": salary_text(j),
                    "worktype": (j.get("workArrangementOption") or "").title(),
                    "location": location_text(j),
                    "posted": (j.get("createdAt") or "")[:10],
                    "tags": skills,
                    "level": "",
                    "min_years": j.get("minYearsOfExperience"),
                    "max_years": j.get("maxYearsOfExperience"),
                    "job_type": j.get("type") or "",
                })
            log.append(f"{kw} p{page} jobs={len(jobs)} new_hcm={new}")
            if not jp.get("hasMore") or len(jobs) < 20:
                break
            time.sleep(1.2)

    out = DATA / "02f_glints_jobs_2026-11-20.csv"
    cols = list(rows[0].keys()) if rows else ["search"]
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)
    (DATA / "02f_glints_jobs_2026-11-20.json").write_text(
        json.dumps({"rows": rows, "log": log}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"rows={len(rows)}")
    print("\n".join(log))
    return 0


if __name__ == "__main__":
    sys.exit(main())
