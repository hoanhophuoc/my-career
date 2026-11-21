#!/usr/bin/env python3
"""Gộp dữ liệu từng nền tảng thành MỘT bộ dữ liệu chuẩn: 02_postings_master.csv

Nguồn (chỉ đọc, không sửa):
  02d_linkedin_jobs_2026-11-20.csv   Glints: 02f_glints_jobs_2026-11-20.csv
  02e_itviec_hcm_salary_2026-11-20.csv  02h_vietnamworks_jobs_2026-11-20.csv
  02g_topdev_jobs_2026-11-20.csv
  .local_private/raw_jds/02d_linkedin_jobs_2026-11-20.json  (tuỳ chọn: JD gốc, không commit)
  tools/purge_log_2026-11-20.csv      (nhóm vai trò đã loại → excluded_reason)

Mọi trường suy ra đều ghi rõ cách suy ra trong 02_methodology_and_limits.md §5.
Số liệu tiêu đề CHỈ được tính từ file master này bằng 02_stats.py.
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = DATA / "02_postings_master.csv"
RAW_LI = ROOT / ".local_private" / "raw_jds" / "02d_linkedin_jobs_2026-11-20.json"

FIELDS = [
    "id", "source", "url", "posted", "title", "company", "company_type", "location",
    "work_mode", "level_label", "years_exp_min", "years_exp_max", "salary_min", "salary_max",
    "skills_must", "skills_nice", "english_req", "true_entry_level", "title_inflation",
    "ghost_duplicate_agency", "excluded_reason",
]

JUNIOR_RE = re.compile(r"\b(intern|internship|thực tập|fresher|fresh grad|junior|jr\.?|graduate|entry[ -]?level|trainee|mới tốt nghiệp)\b", re.I)
SENIOR_RE = re.compile(r"\b(senior|sr\.?|principal|lead|leader|manager|head|director|architect|staff|expert)\b", re.I)
YEARS_RE = re.compile(r"(\d{1,2})\s*(?:\+|plus|-\s*\d{1,2})?\s*(?:years?|yrs?|yoe|năm)\b", re.I)
ENGLISH_RE = re.compile(r"\benglish|tiếng anh|toeic|ielts\b", re.I)
MONEY_RE = re.compile(r"(\d[\d.,]{2,})")


def to_int(money: str):
    """'24,000,000' / '24.000.000' -> 24000000; None nếu không phải số hợp lý."""
    digits = re.sub(r"[^\d]", "", money or "")
    if not digits:
        return None
    v = int(digits)
    return v if 1_000_000 <= v <= 500_000_000 else None


USD_VND = 26_000  # tỷ giá quy đổi cố định, ghi rõ trong 02_methodology_and_limits.md


def parse_salary(text: str):
    t = (text or "").strip()
    if not t or re.search(r"not disclosed|thương lượng|login to view|you'll love|^$", t, re.I):
        return None, None
    usd = bool(re.search(r"usd|us\$", t, re.I))
    nums = []
    for m in MONEY_RE.findall(t):
        v = to_int(m)
        if v:
            nums.append(v)
        elif usd and m.replace(".", "").replace(",", "").isdigit():
            n = int(m.replace(".", "").replace(",", ""))
            if 100 <= n <= 20000:
                nums.append(n * USD_VND)
    if not nums:
        return None, None
    return min(nums), max(nums)


def years_from(text: str):
    hits = [int(m.group(1)) for m in YEARS_RE.finditer(text or "")]
    hits = [h for h in hits if 0 < h <= 15]
    return (min(hits), max(hits)) if hits else (None, None)


def work_mode(raw: str):
    r = (raw or "").lower()
    if "remote" in r:
        return "remote"
    if "hybrid" in r:
        return "hybrid"
    if "onsite" in r or "office" in r or "at office" in r:
        return "onsite"
    return ""


def add(rows, **kw):
    row = {f: "" for f in FIELDS}
    row.update({k: ("" if v is None else v) for k, v in kw.items()})
    rows.append(row)


def load_raw_desc():
    if RAW_LI.exists():
        data = json.loads(RAW_LI.read_text(encoding="utf-8"))
        return {str(r.get("id")): r.get("desc", "") for r in data if isinstance(r, dict)}
    return {}


def build():
    rows = []
    desc_by_id = load_raw_desc()

    # LinkedIn
    with (DATA / "02d_linkedin_jobs_2026-11-20.csv").open(encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            desc = desc_by_id.get(r["id"], "")
            lo, hi = years_from(desc)
            smin, smax = parse_salary(r.get("salary"))
            add(rows, id=f"li-{r['id']}", source="linkedin", url=r["url"], posted=r.get("posted_date"),
                title=r["title"], company=r["company"], location=r.get("location"),
                work_mode=work_mode(r.get("employment")), level_label=r.get("seniority"),
                years_exp_min=lo, years_exp_max=hi, salary_min=smin, salary_max=smax,
                skills_must=r.get("tech"), english_req=int(bool(ENGLISH_RE.search((r.get("tech") or "") + " " + desc))),
                excluded_reason="")

    # Glints
    with (DATA / "02f_glints_jobs_2026-11-20.csv").open(encoding="utf-8-sig", newline="") as f:
        for i, r in enumerate(csv.DictReader(f), 1):
            smin, smax = parse_salary(r.get("salary"))
            add(rows, id=f"gl-{i:03d}", source="glints", url=r["url"], posted=r.get("posted"),
                title=r["title"], company=r["company"], location=r.get("location"),
                work_mode=work_mode(r.get("worktype")), level_label=r.get("level"),
                years_exp_min=r.get("min_years"), years_exp_max=r.get("max_years"),
                salary_min=smin, salary_max=smax, skills_must=r.get("tags"),
                english_req=int(bool(ENGLISH_RE.search((r.get("tags") or "") + " " + (r.get("title") or "")))),
                excluded_reason="")

    # ITviec
    with (DATA / "02e_itviec_hcm_salary_2026-11-20.csv").open(encoding="utf-8-sig", newline="") as f:
        for i, r in enumerate(csv.DictReader(f), 1):
            smin, smax = parse_salary(r.get("salary"))
            lo, hi = years_from(r.get("title"))
            add(rows, id=f"it-{i:03d}", source="itviec", url=r["url"], posted=r.get("posted"),
                title=r["title"], company=r["company"], location=r.get("quan") or r.get("location"),
                work_mode=work_mode(r.get("worktype")), level_label=r.get("level"),
                years_exp_min=lo, years_exp_max=hi, salary_min=smin, salary_max=smax,
                skills_must=r.get("tags"),
                english_req=int(bool(ENGLISH_RE.search((r.get("tags") or "") + " " + (r.get("title") or "")))),
                excluded_reason="")

    # VietnamWorks
    with (DATA / "02h_vietnamworks_jobs_2026-11-20.csv").open(encoding="utf-8-sig", newline="") as f:
        for i, r in enumerate(csv.DictReader(f), 1):
            smin, smax = parse_salary(r.get("salary"))
            lo, hi = years_from(r.get("title"))
            add(rows, id=f"vnw-{i:03d}", source="vietnamworks", url=r["url"], posted=r.get("posted"),
                title=r["title"], company=r["company"], location=r.get("location"),
                years_exp_min=lo, years_exp_max=hi, salary_min=smin, salary_max=smax,
                skills_must=r.get("skills"),
                english_req=int(bool(ENGLISH_RE.search((r.get("skills") or "") + " " + (r.get("title") or "")))),
                excluded_reason="")

    # TopDev
    with (DATA / "02g_topdev_jobs_2026-11-20.csv").open(encoding="utf-8-sig", newline="") as f:
        for i, r in enumerate(csv.DictReader(f), 1):
            smin, smax = parse_salary(r.get("salary"))
            lo, hi = years_from(r.get("title"))
            add(rows, id=f"td-{i:03d}", source="topdev", url=r["url"], posted=r.get("posted"),
                title=r["title"], company=r["company"], location=r.get("location"),
                years_exp_min=lo, years_exp_max=hi, salary_min=smin, salary_max=smax,
                skills_must=r.get("tags"),
                english_req=int(bool(ENGLISH_RE.search((r.get("tags") or "") + " " + (r.get("title") or "")))),
                excluded_reason="")

    # Nhóm vai trò đã loại (chỉ còn nhật ký purge — dữ liệu thô đã bị xoá)
    purge = ROOT / "tools" / "purge_log_2026-11-20.csv"
    if purge.exists():
        with purge.open(encoding="utf-8-sig", newline="") as f:
            for i, r in enumerate(csv.DictReader(f), 1):
                vals = list(r.values())
                src_file, group, title, company, url = (vals + [""] * 5)[:5]
                source = {"02d": "linkedin", "02f": "glints", "02e": "itviec", "02b": "itviec",
                          "02h": "vietnamworks", "02j": "jobstreet", "02g": "topdev"}.get(
                              src_file[:3], "unknown")
                add(rows, id=f"x-{i:03d}", source=source, url=url, title=title, company=company,
                    excluded_reason=group)

    # Cờ dẫn xuất
    seen = {}
    for r in rows:
        t = (r["title"] or "").lower()
        lo = int(r["years_exp_min"]) if str(r["years_exp_min"]).isdigit() else None
        r["true_entry_level"] = bool(lo == 0 and not r["excluded_reason"])
        r["title_inflation"] = bool(JUNIOR_RE.search(t) and lo is not None and lo >= 1)
        key = (re.sub(r"\W+", " ", t).strip(), re.sub(r"\W+", " ", (r["company"] or "").lower()).strip())
        dup = key in seen and not r["excluded_reason"]
        r["ghost_duplicate_agency"] = dup
        seen.setdefault(key, r["id"])

    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    print(f"Đã ghi {len(rows)} dòng → {OUT.name}")
    return rows


if __name__ == "__main__":
    build()
