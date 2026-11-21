#!/usr/bin/env python3
"""Sinh `11_all_job_titles_2026-11-20.csv` từ dữ liệu thô ĐÃ LỌC role.

Chạy sau purge_excluded_roles.py + các analyzer.
"""
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = [
    ("LinkedIn", "02d_linkedin_jobs_2026-11-20.csv"),
    ("Glints", "02f_glints_jobs_2026-11-20.csv"),
    ("ITviec", "02e_itviec_hcm_salary_2026-11-20.csv"),
    ("VietnamWorks", "02h_vietnamworks_jobs_2026-11-20.csv"),
    ("TopDev", "02g_topdev_jobs_2026-11-20.csv"),
]
DATA = ROOT / "data"
OUT = DATA / "11_all_job_titles_2026-11-20.csv"


def main():
    rows = []
    for name, f in SRC:
        p = DATA / f
        if not p.exists():
            continue
        for r in csv.DictReader(p.open(encoding="utf-8-sig")):
            rows.append({"source": name, "title": r.get("title", "").strip(),
                         "company": r.get("company", "").strip(),
                         "location": r.get("location", "").strip(),
                         "url": r.get("url", "").strip()})
    rows.sort(key=lambda x: (x["source"], x["title"].lower()))
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["source", "title", "company", "location", "url"],
                           quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)
    print(f"{OUT.name}: {len(rows)} dòng | "
          f"{len({r['title'].lower() for r in rows})} title khác nhau")
    for k, v in Counter(r["source"] for r in rows).most_common():
        print(f"  {k:22} {v:4}")


if __name__ == "__main__":
    main()
