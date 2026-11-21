#!/usr/bin/env python3
"""Analyse crawled LinkedIn jobs -> stats + ranked shortlist for a fresher
Java/Spring Boot candidate in HCMC. Reads 02d_linkedin_jobs_2026-11-20.json."""
import csv
import json
import re
from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
SRC = DATA / "02d_linkedin_jobs_2026-11-20.json"
OUT_SHORT = DATA / "02d_linkedin_shortlist_2026-11-20.csv"
OUT_STATS = DATA / "02d_linkedin_stats_2026-11-20.json"

SENIOR_BAD = r"\b(senior|sr\.?|principal|lead|leader|manager|head|director|architect|expert|staff|chuyên gia|trưởng)\b"
JUNIOR = r"\b(intern|internship|thực tập|fresher|junior|jr\.?|graduate|entry[\s-]*level|trainee|mới tốt nghiệp)\b"
QA = r"\b(qa|qc|tester|test engineer|sdet|automation test|quality assurance|kiểm thử)\b"
JAVA_T = r"\b(java|spring)\b"
DOTNET_T = r"\b(\.net|c#|dotnet)\b"
OFF_TRACK = r"\b(ios|android|flutter|mobile|php|ruby|golang|\.net|c#|embedded|data engineer|data scientist|machine learning|mlops|ai engineer|devops|sre|salesforce|odoo|sap consultant|pmo|sales engineer|penetration|security engineer|qc computer vision|frontend|front-end|react native)\b"


def years_required(text):
    t = text.lower()
    cands = []
    for m in re.finditer(r"(\d{1,2})\s*(?:\+|plus)?\s*(?:-\s*(\d{1,2}))?\s*(?:years?|yrs?|yoe|năm)\b", t):
        hi = m.group(2)
        cands.append(int(hi) if hi else int(m.group(1)))
    for m in re.finditer(r"(?:at least|tối thiểu|min(?:imum)?)\s*(\d{1,2})\s*(?:years?|năm)", t):
        cands.append(int(m.group(1)))
    cands = [c for c in cands if 0 < c <= 15]
    return min(cands) if cands else None


def salary_text(row):
    """Only keep plausible monthly pay (>=5M VND or >=500 USD). LinkedIn often
    shows a 'Base pay range' label with the number elsewhere, so prefer desc."""
    t = row.get("desc", "")
    cands = []
    for m in re.finditer(r"(\d{1,3}(?:[.,]\d{3})+)\s*(?:-|–|\u2013|to|đến)\s*(\d{1,3}(?:[.,]\d{3})+)\s*(vnd|vnđ|đ|triệu|tr)\b", t, re.I):
        lo = int(m.group(1).replace(".", "").replace(",", ""))
        unit = m.group(3).lower()
        if unit in ("triệu", "tr"):
            lo *= 1000000
        if lo >= 5000000:
            cands.append(m.group(0).strip())
    for m in re.finditer(r"(?:(usd|\$)\s*(\d{1,2}[.,]\d{3})|(\d{1,2}[.,]\d{3})\s*(?:usd|us\$))", t, re.I):
        val = (m.group(2) or m.group(3)).replace(",", "").replace(".", "")
        if val.isdigit() and 500 <= int(val) <= 20000:
            cands.append(m.group(0).strip())
    for m in re.finditer(r"(\d{1,3}(?:[.,]\d{3})+)\s*(?:triệu|tr)\b", t, re.I):
        lo = int(m.group(1).replace(".", "").replace(",", ""))
        if 5 <= lo <= 100:
            cands.append(m.group(0).strip())
    return cands[0] if cands else ("" if "base pay range" in (row.get("salary") or "").lower() else row.get("salary", ""))


def score_rows(rows):
    for r in rows:
        title_l = r["title"].lower()
        text = (r["title"] + " " + r.get("seniority", "") + " " + r.get("desc", "")).lower()
        tech = set((r.get("tech") or "").split(";")) - {""}
        r["tech"] = ";".join(sorted(tech))
        r["is_senior_title"] = bool(re.search(SENIOR_BAD, title_l))
        r["is_junior"] = bool(re.search(JUNIOR, text))
        r["is_qa"] = bool(re.search(QA, title_l))
        r["years_req"] = years_required(r["title"] + " " + r.get("desc", "")[:4000])
        r["salary_found"] = salary_text(r)

        if re.search(JAVA_T, title_l) or "java" in tech or "spring" in tech:
            cat = "A. Java/Spring"
        elif re.search(DOTNET_T, title_l) or ".net" in tech or "c#" in tech:
            cat = "B. .NET"
        elif r["is_qa"]:
            cat = "C. QA/SDET"
        else:
            cat = "D. Khác"
        r["category"] = cat

        score = 0
        if r["is_junior"]:
            score += 3
        if r["is_senior_title"]:
            score -= 5
        y = r["years_req"]
        if y is None:
            score += 1
        elif y <= 1:
            score += 3
        elif y == 2:
            score += 1
        elif y >= 3:
            score -= 3
        if cat == "A. Java/Spring":
            score += 3
        if "spring boot" in tech:
            score += 2
        elif "spring" in tech:
            score += 1
        if cat == "B. .NET":
            score += 1
        if "sql" in tech:
            score += 1
        if "english" in tech:
            score += 1
        # a third language penalises only when it is a REQUIREMENT, not a perk
        r["lang3"] = bool(
            re.search(r"(mandarin|japanese|chinese|tiếng trung|tiếng nhật)", title_l)
            or re.search(r"(proficiency|fluent|required?|must have|ability to communicat\w*|communicat\w+ (?:in|with))[^.]{0,60}(mandarin|japanese|chinese|tiếng trung|tiếng nhật)", text)
            or re.search(r"(mandarin|japanese|chinese)[^.]{0,40}(required?|proficiency|fluent|native)", text)
            or re.search(r"\bN[23]\b", text[:1500])
        )
        if r["lang3"]:
            score -= 3
        if re.search(OFF_TRACK, title_l):
            score -= 4
        if "ho chi minh" in r["location"].lower():
            score += 1
        else:
            score -= 1
        if r["posted_date"] >= "2026-11-01":
            score += 1
        r["score"] = score
    return rows


def main():
    rows = score_rows(json.load(open(SRC, encoding="utf-8")))
    json.dump(rows, open("_work_linkedin_scored.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    reach = [r for r in rows if not r["is_senior_title"]
             and (r["years_req"] is None or r["years_req"] <= 2)]
    reach_java = [r for r in reach if r["category"] == "A. Java/Spring"]
    stats = {
        "total": len(rows),
        "with_salary": sum(1 for r in rows if r["salary_found"]),
        "junior_flags": sum(1 for r in rows if r["is_junior"]),
        "senior_title": sum(1 for r in rows if r["is_senior_title"]),
        "reachable": len(reach),
        "reachable_java": len(reach_java),
        "reachable_qa": len([r for r in reach if r["category"] == "C. QA/SDET"]),
        "reachable_dotnet": len([r for r in reach if r["category"] == "B. .NET"]),
        "hcm": sum(1 for r in rows if "ho chi minh" in r["location"].lower()),
        "java": sum(1 for r in rows if "java" in r["tech"]),
        "spring": sum(1 for r in rows if "spring" in r["tech"]),
        "spring_boot": sum(1 for r in rows if "spring boot" in r["tech"]),
        "dotnet": sum(1 for r in rows if ".net" in r["tech"]),
        "years_none": sum(1 for r in rows if r["years_req"] is None),
        "years_0_1": sum(1 for r in rows if r["years_req"] is not None and r["years_req"] <= 1),
        "years_2": sum(1 for r in rows if r["years_req"] == 2),
        "years_3p": sum(1 for r in rows if r["years_req"] is not None and r["years_req"] >= 3),
        "seniority": Counter(r.get("seniority") or "(none)" for r in rows).most_common(10),
        "top_tech": Counter(t for r in rows for t in r["tech"].split(";") if t).most_common(25),
        "top_companies": Counter(r["company"] for r in rows if r["company"]).most_common(20),
        "entry_companies": Counter(r["company"] for r in reach if r["company"]).most_common(20),
    }
    json.dump(stats, open(OUT_STATS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    ranked = sorted(reach, key=lambda r: r["posted_date"], reverse=True)
    ranked = sorted(ranked, key=lambda r: -r["score"])[:30]
    cols = ["rank", "score", "category", "title", "company", "location",
            "salary_found", "years_req", "seniority", "posted_date", "is_qa",
            "lang3", "tech", "url"]
    with open(OUT_SHORT, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for i, r in enumerate(ranked, 1):
            w.writerow([i, r["score"], r["category"], r["title"], r["company"],
                        r["location"], r["salary_found"], r["years_req"],
                        r["seniority"], r["posted_date"], r["is_qa"],
                        r["lang3"], r["tech"][:200], r["url"]])
    print("shortlist rows:", len(ranked), "| reachable:", len(reach),
          "| reachable java:", len(reach_java))
    print(json.dumps(stats, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
