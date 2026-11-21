"""Đếm công ty trùng nhau giữa 3 sàn (ad-hoc, không sinh file)."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"


def comps(f):
    return {r["company"].strip().lower() for r in csv.DictReader(open(f, encoding="utf-8-sig"))
            if r.get("company", "").strip()}


li = comps(DATA / "02d_linkedin_jobs_2026-11-20.csv")
gl = comps(DATA / "02f_glints_jobs_2026-11-20.csv")
it = comps(DATA / "02e_itviec_hcm_salary_2026-11-20.csv")
print("công ty: linkedin", len(li), "glints", len(gl), "itviec", len(it))
print("itviec∩linkedin", len(it & li), "glints∩linkedin", len(gl & li), "glints∩itviec", len(gl & it))
print("\nJobStreet còn lại:")
for r in csv.DictReader(open(DATA / "02j_jobstreet_jobs_2026-11-20.csv", encoding="utf-8-sig")):
    print("  -", r["title"][:60], "|", r.get("location", "")[:30])
print("\nVNWorks:")
v = list(csv.DictReader(open(DATA / "02h_vietnamworks_jobs_2026-11-20.csv", encoding="utf-8-sig")))
print("  tổng", len(v), "| có lương", sum(1 for r in v if (r.get("salary") or "").strip()))
