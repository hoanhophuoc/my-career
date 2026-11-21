#!/usr/bin/env python3
"""Tính MỌI con số tiêu đề từ 02_postings_master.csv.

Đây là nguồn duy nhất cho các con số của pack. File .md chỉ được trích lại từ output này.
Chạy: python3 tools/02_stats.py
"""
import csv
import json
import re
import statistics
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
MASTER = DATA / "02_postings_master.csv"
OUT_JSON = DATA / "02_stats_2026-11-20.json"

JAVA = re.compile(r"\bjava\b|spring", re.I)
DOTNET = re.compile(r"\.net\b|c#|dotnet", re.I)
JUNIOR = re.compile(r"\b(intern|internship|thực tập|fresher|junior|graduate|entry[ -]?level|trainee)\b", re.I)
SENIOR = re.compile(r"\b(senior|principal|lead|manager|architect|director|head|staff)\b", re.I)


def rows():
    with MASTER.open(encoding="utf-8", newline="") as f:
        return [r for r in csv.DictReader(f)]


def pct(a, b):
    return round(100 * a / b, 1) if b else 0.0


def main():
    all_rows = rows()
    live = [r for r in all_rows if not r["excluded_reason"]]          # sau khi loại nhóm vai trò
    for r in live:
        r["java"] = bool(JAVA.search((r["title"] or "") + " " + (r["skills_must"] or "")))
        r["dotnet"] = bool(DOTNET.search((r["title"] or "") + " " + (r["skills_must"] or "")))

    by_src = Counter(r["source"] for r in live)
    entry = [r for r in live if r["true_entry_level"] == "True"]
    entry_java = [r for r in entry if r["java"]]
    salary = [int(r["salary_min"]) for r in live if r["salary_min"]]
    entry_salary = [int(r["salary_min"]) for r in entry if r["salary_min"]]

    ok_levels = {"Entry level", "Internship", "Associate", "Not Applicable", ""}
    reach = [r for r in live if r["level_label"] in ok_levels and not SENIOR.search(r["title"])]

    def norm_district(s: str) -> str:
        s = (s or "").split(" - ")[0].strip()
        return {"Quận Một": "Quận 1", "Quận Hai": "Quận 2", "Quận Ba": "Quận 3", "Quận Bốn": "Quận 4",
                "Quận Năm": "Quận 5", "Quận Sáu": "Quận 6", "Quận Bảy": "Quận 7", "Quận Tám": "Quận 8",
                "Quận Chín": "Quận 9", "Quận Mười": "Quận 10", "Quận Mười Một": "Quận 11",
                "Quận Mười Hai": "Quận 12"}.get(s, s)

    levels = Counter()
    for r in live:
        t = (r["title"] or "").lower()
        if JUNIOR.search(t):
            levels["junior/fresher/intern"] += 1
        elif SENIOR.search(t):
            levels["senior+"] += 1
        else:
            levels["không ghi"] += 1

    stats = {
        "nguon_du_lieu": "02_postings_master.csv",
        "ngay_du_lieu_goc": "2026-11-20",
        "tong_dong_master": len(all_rows),
        "tong_tin_sau_loc_role": len(live),
        "tin_theo_san": dict(by_src),
        "tin_bi_loai_nhom_role": len(all_rows) - len(live),
        "loai_theo_nhom": dict(Counter(r["excluded_reason"] for r in all_rows if r["excluded_reason"])),
        "trung_lap_ten_cong_ty": sum(1 for r in live if r["ghost_duplicate_agency"] == "True"),
        "true_entry_level": len(entry),
        "true_entry_level_pct": pct(len(entry), len(live)),
        "true_entry_level_java": len(entry_java),
        "reachable_theo_level": len(reach),
        "reachable_java": sum(1 for r in reach if r["java"]),
        "linkedin_reachable": sum(1 for r in reach if r["source"] == "linkedin"),
        "linkedin_reachable_java": sum(1 for r in reach if r["source"] == "linkedin" and r["java"]),
        "title_inflation": sum(1 for r in live if r["title_inflation"] == "True"),
        "co_luong_cong_khai": len(salary),
        "co_luong_pct": pct(len(salary), len(live)),
        "luong_trung_vi_trieu": round(statistics.median(salary) / 1e6, 1) if salary else None,
        "entry_luong_trung_vi_trieu": round(statistics.median(entry_salary) / 1e6, 1) if entry_salary else None,
        "co_java": sum(1 for r in live if r["java"]),
        "co_java_pct": pct(sum(1 for r in live if r["java"]), len(live)),
        "co_dotnet": sum(1 for r in live if r["dotnet"]),
        "level_theo_tieu_de": dict(levels),
        "top_quan": dict(Counter(norm_district(r["location"]) for r in live
                                 if norm_district(r["location"]).startswith(("Quận", "TP Thủ", "Bình"))).most_common(12)),
        "luong_theo_san": {s: sorted(int(r["salary_min"]) for r in live if r["source"] == s and r["salary_min"])
                           for s in sorted({r["source"] for r in live})},
        "top_ky_nang": dict(Counter(
            s.strip().lower() for r in live for s in (r["skills_must"] or "").split(";") if s.strip()
        ).most_common(15)),
    }
    OUT_JSON.write_text(json.dumps(stats, ensure_ascii=False, indent=1), encoding="utf-8")

    # In bảng số tiêu đề — dùng để đối chiếu với mọi file .md
    w = max(len(k) for k in stats)
    for k, v in stats.items():
        print(f"{k:<{w}} : {v}")

    print("\n--- Bảng số liệu gốc (copy vào 02_market_report.md) ---")
    print("| Con số | Giá trị | Định nghĩa | Bộ dữ liệu | Ngày | Tính bằng |")
    print("|---|---|---|---|---|---|")
    print(f"| Tổng tin sau lọc nhóm vai trò | {len(live)} | dòng không có excluded_reason | 02_postings_master.csv | 20/11/2026 | 02_stats.py |")
    print(f"| Số dòng bị loại (nhóm vai trò) | {stats['tin_bi_loai_nhom_role']} | có excluded_reason | 02_postings_master.csv | 20/11/2026 | 02_stats.py |")
    print(f"| true_entry_level | {len(entry)} ({stats['true_entry_level_pct']}%) | years_exp_min = 0 | 02_postings_master.csv | 20/11/2026 | 02_stats.py |")
    print(f"| true_entry_level + Java | {len(entry_java)} | cờ true_entry + kỹ năng Java/Spring | 02_postings_master.csv | 20/11/2026 | 02_stats.py |")
    print(f"| Reachable (level không phải mid-senior + tiêu đề không có senior) | {len(reach)} | level_label ∈ Entry/Internship/Associate/Not Applicable | 02_postings_master.csv | 20/11/2026 | 02_stats.py |")
    print(f"| Reachable + Java | {stats['reachable_java']} | reachable ∩ Java/Spring | 02_postings_master.csv | 20/11/2026 | 02_stats.py |")
    print(f"| LinkedIn reachable | {stats['linkedin_reachable']} | reachable ∩ source=linkedin | 02_postings_master.csv | 20/11/2026 | 02_stats.py |")
    print(f"| Có lương công khai | {len(salary)} ({stats['co_luong_pct']}%) | salary_min không rỗng | 02_postings_master.csv | 20/11/2026 | 02_stats.py |")
    print(f"| Lương trung vị | {stats['luong_trung_vi_trieu']} triệu | trung vị salary_min | 02_postings_master.csv | 20/11/2026 | 02_stats.py |")


if __name__ == "__main__":
    main()
