#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phân tích Glints TP.HCM + so trùng công ty giữa 3 sàn, sinh shortlist.

Đầu vào : 02f_glints_jobs_2026-11-20.csv, 02e_itviec_hcm_salary_2026-11-20.csv,
          02d_linkedin_jobs_2026-11-20.csv
Đầu ra  : 02f_glints_shortlist_2026-11-20.csv, 02f_glints_stats_2026-11-20.json,
          02i_cross_platform_companies_2026-11-20.csv
"""
import csv
import json
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
DATA = HERE / "data"

IT = re.compile(r"developer|engineer|java|backend|back-end|back end|software|tester|qa|"
                r"lập trình|devops|data|fullstack|full-stack|frontend|front-end|mobile|"
                r"android|ios|architect|technical", re.I)
TECH = re.compile(r"java|spring|backend|back-end|software|developer|engineer|tester|lập trình", re.I)


def mid(salary: str):
    v = [int(n.replace(",", "")) for n in re.findall(r"([\d,]+)\s*VND", salary or "")]
    return (min(v) + max(v)) / 2 if v else None


def norm(name: str) -> str:
    n = re.sub(r"\s+", " ", (name or "").lower()).strip()
    n = re.sub(r"^(công ty|cty|tnhh|cp|cổ phần|trách nhiệm hữu hạn|liability|company)\s+", "", n)
    return n.replace(".", "").replace(",", "")


def main():
    rows = list(csv.DictReader((DATA / "02f_glints_jobs_2026-11-20.csv").open(encoding="utf-8")))
    it = [r for r in rows if IT.search(r["title"]) and TECH.search(r["title"] + " " + r["tags"])]
    entry = [r for r in it if r["min_years"] in ("0", "1")]
    with_sal = [r for r in entry if r["salary"] != "Not disclosed"]
    mids = sorted(m for m in (mid(r["salary"]) for r in with_sal) if m and m > 3_000_000)

    # Shortlist: entry-level IT, ưu tiên có lương
    sl = sorted(entry, key=lambda r: (-(mid(r["salary"]) or 0), r["title"]))
    out = DATA / "02f_glints_shortlist_2026-11-20.csv"
    cols = ["title", "company", "min_years", "max_years", "salary", "worktype",
            "location", "posted", "tags", "url"]
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, quoting=csv.QUOTE_ALL, extrasaction="ignore")
        w.writeheader()
        w.writerows(sl)

    stats = {
        "raw_rows": len(rows),
        "companies_raw": len({r["company"] for r in rows}),
        "it_rows": len(it),
        "entry_0_1y": len(entry),
        "entry_with_salary": len(with_sal),
        "entry_salary_median_mid_trieu": round(mids[len(mids) // 2] / 1e6, 1) if mids else None,
        "entry_salary_min_trieu": round(mids[0] / 1e6, 1) if mids else None,
        "entry_salary_max_trieu": round(mids[-1] / 1e6, 1) if mids else None,
        "java_tag_in_it": sum(1 for r in it if "java" in r["tags"].lower()),
        "spring_tag_in_it": sum(1 for r in it if "spring" in r["tags"].lower()),
        "sql_tag_in_it": sum(1 for r in it if re.search(r"sql", r["tags"], re.I)),
        "english_tag_in_it": sum(1 for r in it if re.search(r"english", r["tags"], re.I)),
        "worktype": Counter(r["worktype"] for r in it).most_common(),
        "districts": Counter(r["location"].split(" - ")[0] for r in it).most_common(8),
        "top_companies": Counter(r["company"] for r in it).most_common(10),
    }

    # Trùng công ty giữa các sàn
    sets = {}
    for name, path, col in [
        ("glints", "02f_glints_jobs_2026-11-20.csv", "company"),
        ("itviec", "02e_itviec_hcm_salary_2026-11-20.csv", "company"),
        ("linkedin", "02d_linkedin_jobs_2026-11-20.json", None),
    ]:
        p = DATA / path
        if not p.exists():
            continue
        if col:
            names = [r[col] for r in csv.DictReader(p.open(encoding="utf-8"))]
        else:
            d = json.loads(p.read_text(encoding="utf-8"))
            items = d if isinstance(d, list) else d.get("rows", d.get("jobs", []))
            names = [x.get("company") or "" for x in items]
        sets[name] = {norm(n) for n in names if n}
    overlap = {}
    keys = list(sets)
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = keys[i], keys[j]
            both = sets[a] & sets[b]
            overlap[f"{a}_{b}"] = sorted(both)
    stats["companies_per_source"] = {k: len(v) for k, v in sets.items()}
    stats["overlap_counts"] = {k: len(v) for k, v in overlap.items()}

    with (DATA / "02i_cross_platform_companies_2026-11-20.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(["cap_san", "so_cong_ty_trung", "ten_cong_ty"])
        for k, v in overlap.items():
            w.writerow([k, len(v), "; ".join(v)])

    (DATA / "02f_glints_stats_2026-11-20.json").write_text(
        json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
