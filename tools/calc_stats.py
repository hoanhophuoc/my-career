"""Kiểm tra nhanh số liệu thô từng sàn (ad-hoc, không sinh file)."""
import csv
import json
import re
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

w = json.load(open("_work_linkedin_scored.json", encoding="utf-8"))
reach = [r for r in w if not r["is_senior_title"] and (r["years_req"] is None or r["years_req"] <= 2)]
rj = [r for r in reach if r["category"] == "A. Java/Spring"]
print("linkedin total", len(w))
print("reach", len(reach), "reach_java", len(rj))
print("spring boot in reach_java", sum(1 for r in rj if "spring boot" in r["tech"]))
print("aws in all", sum(1 for r in w if "aws" in r["tech"]))
print("companies", len({r["company"] for r in w if r["company"]}))
print("salary", sum(1 for r in w if r["salary_found"]))
print("senior", sum(1 for r in w if r["is_senior_title"]))
print("dotnet reach", sum(1 for r in reach if r["category"] == "B. .NET"))
print("years3p", sum(1 for r in w if r["years_req"] is not None and r["years_req"] >= 3))

g = list(csv.DictReader(open(DATA / "02f_glints_jobs_2026-11-20.csv", encoding="utf-8-sig")))
print("glints", len(g), "hcm", sum(1 for r in g if "hồ chí minh" in (r.get("location") or "").lower()))
v = list(csv.DictReader(open(DATA / "02h_vietnamworks_jobs_2026-11-20.csv", encoding="utf-8-sig")))
print("vnw", len(v), "hcm", sum(1 for r in v if "hồ chí minh" in (r.get("location") or "").lower()))
t = list(csv.DictReader(open(DATA / "02g_topdev_jobs_2026-11-20.csv", encoding="utf-8-sig")))
print("topdev", len(t), "hcm", sum(1 for r in t if "hồ chí minh" in (r.get("location") or "").lower()))
e = list(csv.DictReader(open(DATA / "02e_itviec_hcm_salary_2026-11-20.csv", encoding="utf-8-sig")))
j = list(csv.DictReader(open(DATA / "02j_jobstreet_jobs_2026-11-20.csv", encoding="utf-8-sig")))
print("itviec", len(e), "jobstreet", len(j), "TOTAL", len(w) + len(g) + len(e) + len(v) + len(t) + len(j))
print("glints salary", sum(1 for r in g if (r.get("salary") or "").strip() and "disclose" not in (r.get("salary") or "").lower()))
