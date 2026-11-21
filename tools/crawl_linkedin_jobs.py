#!/usr/bin/env python3
"""Crawl LinkedIn public job search (guest API) -> CSV + JSON for the career pack.

No login/cookie used. Public endpoints only, throttled.
"""
import csv
import json
import re
import time
import html
import urllib.parse
import urllib.request
from pathlib import Path

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")
BASE = "https://www.linkedin.com"
DATA = Path(__file__).resolve().parent.parent / "data"
OUT_CSV = DATA / "02d_linkedin_jobs_2026-11-20.csv"
OUT_JSON = DATA / "02d_linkedin_jobs_2026-11-20.json"

KEYWORDS = ["java", "spring boot", "backend developer", "java fresher",
            "java intern", "software engineer", ".net developer",
            "qa automation", "tester", "backend engineer", "java developer"]
LOCATIONS = ["Ho Chi Minh City, Vietnam"]

TECH = {
    "java": r"\bjava\b", "spring": r"\bspring\b", "spring boot": r"spring\s*boot",
    "spring mvc": r"spring\s*mvc", "hibernate": r"hibernate", "jpa": r"\bjpa\b",
    "javascript": r"javascript", "typescript": r"typescript", "python": r"\bpython\b",
    "node": r"\bnode\.?js\b", "c#": r"c#|c\s*sharp", ".net": r"\.net\b",
    "sql": r"\bsql\b", "mysql": r"mysql", "postgresql": r"postgres", "oracle": r"\boracle\b",
    "mongodb": r"mongo", "redis": r"redis", "kafka": r"kafka", "rabbitmq": r"rabbitmq",
    "microservices": r"microservices?", "rest api": r"rest(ful)?\s*api", "graphql": r"graphql",
    "docker": r"docker", "kubernetes": r"kubernetes|\bk8s\b", "aws": r"\baws\b",
    "gcp": r"\bgcp\b|google cloud", "azure": r"\bazure\b", "ci/cd": r"ci/cd|jenkins|github actions",
    "git": r"\bgit\b", "linux": r"\blinux\b", "unit test": r"unit\s*test|junit|mockito",
    "selenium": r"selenium", "playwright": r"playwright", "test automation": r"automation test|test automation",
    "agile": r"\bagile\b|scrum", "english": r"\benglish\b",
}


def get(url, tries=3):
    for i in range(tries):
        req = urllib.request.Request(url, headers={
            "User-Agent": UA,
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml",
        })
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001
            code = getattr(e, "code", None)
            if code == 429:
                time.sleep(8 * (i + 1))
            elif code in (403, 404):
                return ""
            else:
                time.sleep(2 * (i + 1))
    return ""


def clean(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def parse_cards(raw):
    out = []
    for chunk in raw.split('data-entity-urn="urn:li:jobPosting:')[1:]:
        jid = re.match(r"(\d+)", chunk)
        if not jid:
            continue
        card = {"id": jid.group(1)}
        m = re.search(r'base-search-card__title[^>]*>([\s\S]*?)</h3>', chunk)
        card["title"] = clean(m.group(1)) if m else ""
        m = re.search(r'base-search-card__subtitle[^>]*>\s*<a[^>]*>([\s\S]*?)</a>', chunk)
        card["company"] = clean(m.group(1)) if m else ""
        m = re.search(r'job-search-card__location[^>]*>([\s\S]*?)</span>', chunk)
        card["location"] = clean(m.group(1)) if m else ""
        m = re.search(r'<time[^>]*datetime="([^"]+)"', chunk)
        card["posted"] = m.group(1) if m else ""
        out.append(card)
    return out


def parse_detail(raw):
    d = {}
    m = re.search(r'top-card-layout__title[^>]*>([\s\S]*?)</h[12]>', raw) or \
        re.search(r'<h1[^>]*>([\s\S]*?)</h1>', raw)
    d["title"] = clean(m.group(1)) if m else ""
    m = re.search(r'topcard__org-name-link[^>]*>([\s\S]*?)</a>', raw)
    d["company"] = clean(m.group(1)) if m else ""
    m = re.search(r'topcard__flavor--bullet[^>]*>([\s\S]*?)</span>', raw)
    d["location"] = clean(m.group(1)) if m else ""
    m = re.search(r'compensation__salary[^>]*>([\s\S]*?)</', raw)
    d["salary"] = clean(m.group(1)) if m else ""
    m = re.search(r'posted-time-ago__text[^>]*>([\s\S]*?)</span>', raw)
    d["posted_ago"] = clean(m.group(1)) if m else ""
    crit = dict(re.findall(
        r'description__job-criteria-subheader[^>]*>([\s\S]*?)</h3>\s*<span[^>]*description__job-criteria-text[^>]*>([\s\S]*?)</span>',
        raw))
    crit = {clean(k).lower(): clean(v) for k, v in crit.items()}
    d["seniority"] = crit.get("seniority level", "")
    d["employment"] = crit.get("employment type", "")
    d["function"] = crit.get("job function", "")
    d["industries"] = crit.get("industries", "")
    m = re.search(r'num-applicants__caption[^>]*>([\s\S]*?)</', raw)
    d["applicants"] = clean(m.group(1)) if m else ""
    m = re.search(r'description__text([\s\S]*)', raw)
    body = m.group(1) if m else raw
    cut = body.find("description__job-criteria")
    if cut > 0:
        body = body[:cut]
    d["desc"] = clean(body)[:12000]
    return d


def tags(text):
    t = text.lower()
    return ";".join(k for k, rx in TECH.items() if re.search(rx, t))


def main():
    seen, rows = {}, []
    for kw in KEYWORDS:
        for loc in LOCATIONS:
            for start in range(0, 250, 10):
                url = (BASE + "/jobs-guest/jobs/api/seeMoreJobPostings/search?"
                       + urllib.parse.urlencode({"keywords": kw, "location": loc,
                                                 "f_TPR": "r7776000", "start": start}))
                cards = parse_cards(get(url))
                if not cards:
                    break
                new = 0
                for c in cards:
                    if c["id"] in seen:
                        if kw not in seen[c["id"]]["keywords"]:
                            seen[c["id"]]["keywords"].append(kw)
                        continue
                    c["keywords"] = [kw]
                    seen[c["id"]] = c
                    new += 1
                print(f"{kw:22s} start={start:3d} cards={len(cards):2d} new={new:2d} total={len(seen)}", flush=True)
                if new == 0:
                    break
                time.sleep(0.6)
            time.sleep(0.4)

    print(f"unique cards: {len(seen)}", flush=True)
    for i, (jid, c) in enumerate(seen.items(), 1):
        raw = get(BASE + "/jobs-guest/jobs/api/jobPosting/" + jid)
        d = parse_detail(raw) if raw else {}
        text = " ".join([c["title"], d.get("desc", "")])
        row = {
            "id": jid,
            "keywords": "|".join(c["keywords"]),
            "url": f"https://www.linkedin.com/jobs/view/{jid}/",
            "title": c["title"] or d.get("title", ""),
            "company": c["company"] or d.get("company", ""),
            "location": c["location"] or d.get("location", ""),
            "salary": d.get("salary", ""),
            "posted_date": c["posted"],
            "posted_ago": d.get("posted_ago", ""),
            "seniority": d.get("seniority", ""),
            "employment": d.get("employment", ""),
            "function": d.get("function", ""),
            "industries": d.get("industries", ""),
            "applicants": d.get("applicants", ""),
            "tech": tags(text),
            "desc": d.get("desc", ""),
        }
        rows.append(row)
        if i % 25 == 0:
            print(f"details {i}/{len(seen)}", flush=True)
        time.sleep(0.7)

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
    cols = ["id", "keywords", "url", "title", "company", "location", "salary",
            "posted_date", "posted_ago", "seniority", "employment", "function",
            "industries", "applicants", "tech", "desc"]
    with open(OUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({k: (r[k][:600] if k == "desc" else r[k]) for k in cols})
    print("WROTE", OUT_CSV, len(rows), "rows", flush=True)


if __name__ == "__main__":
    main()
