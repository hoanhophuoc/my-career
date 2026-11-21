#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phân tích dữ liệu ITviec TP.HCM đã đăng nhập (có lương).

Đầu vào : 02e_itviec_hcm_salary_2026-11-20.csv  (83 tin, crawl 20/11/2026)
Đầu ra  : 02e_itviec_shortlist_2026-11-20.csv
          02e_itviec_stats_2026-11-20.json
          02e_itviec_market_snapshot_2026-11-20.md
Quy ước : 1 USD = 26.000 VND (tỷ giá giả định, ghi rõ trong báo cáo).
"""
import csv
import json
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
DATA = HERE / "data"
SRC = DATA / "02e_itviec_hcm_salary_2026-11-20.csv"
RATE = 26000

MASK = re.compile(r"love it|discuss|high paid|attractive|negotiable|competitive|cạnh", re.I)
NUM = re.compile(r"(\d[\d.,]*)\s*(usd|vnd|m\b|mil|triệu|\$)?", re.I)


def to_usd(text: str):
    """Trả về (thấp, cao) quy ra USD/tháng, hoặc (None, None) nếu không đọc được."""
    if not text or MASK.search(text):
        return None, None
    t = text.lower().replace(",", "")
    nums = [float(x) for x in re.findall(r"\d+(?:\.\d+)?", t)]
    if not nums:
        return None, None
    usd = "usd" in t or "$" in text
    vnd = ("vnd" in t) or ("mil" in t) or ("triệu" in t) or re.search(r"\d\s*m\b", t)
    if usd:
        vals = [n for n in nums]
    elif vnd:
        vals = [n * 1_000_000 / RATE for n in nums]
    else:
        vals = [n for n in nums]  # "Up to 28M" đã bắt ở nhánh vnd
    vals = [v for v in vals if 100 <= v <= 20000]
    if not vals:
        return None, None
    vals.sort()
    if len(vals) == 1:
        return None, round(vals[0])
    return round(vals[0]), round(vals[-1])


def main():
    rows = list(csv.DictReader(SRC.open(encoding="utf-8")))
    stats = {"total": len(rows)}

    numeric, unmasked = [], []
    for r in rows:
        lo, hi = to_usd(r["salary"])
        r["_lo"], r["_hi"] = lo, hi
        if lo or hi:
            numeric.append(r)
            unmasked.append((lo, hi))
    stats["companies"] = len({r["company"] for r in rows})
    stats["salary_visible"] = len(numeric)
    stats["salary_visible_pct"] = round(100 * len(numeric) / len(rows), 1)
    stats["levels"] = Counter(r["level"] for r in rows).most_common()
    stats["worktype"] = Counter(r["worktype"] for r in rows).most_common()
    stats["cities"] = Counter(r["location"] for r in rows).most_common()
    stats["queries"] = Counter(r["search"] for r in rows).most_common()

    tops = [hi for _, hi in unmasked if hi]
    if tops:
        stats["salary_usd_median_ceiling"] = round(sorted(tops)[len(tops) // 2])
        stats["salary_usd_min"] = min(tops)
        stats["salary_usd_max"] = max(tops)

    def is_entry(r):
        lv = r["level"].lower()
        return (
            "fresher" in lv
            or "internship" in lv
            or re.search(r"fresher|intern|junior|entry|graduate|thực tập", r["title"], re.I)
            or re.search(r"fresher|intern", r["tags"], re.I)
        )

    entry = [r for r in rows if is_entry(r)]
    stats["entry_level"] = len(entry)
    stats["entry_pct"] = round(100 * len(entry) / len(rows), 1)

    # Shortlist: ưu tiên entry-friendly, Java/backend, sắp theo lương trần giảm dần
    order = {"Fresher Accepted": 0, "Internship Accepted": 1}
    sl = sorted(
        entry,
        key=lambda r: (order.get(r["level"], 2), -(r["_hi"] or 0), r["title"]),
    )
    out = DATA / "02e_itviec_shortlist_2026-11-20.csv"
    cols = ["title", "company", "level", "salary", "salary_usd_ceiling", "worktype",
            "location", "posted", "tags", "url"]
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(cols)
        for r in sl:
            w.writerow([r["title"], r["company"], r["level"], r["salary"],
                        r["_hi"] or "", r["worktype"], r["location"], r["posted"],
                        r["tags"], r["url"]])

    (DATA / "02e_itviec_stats_2026-11-20.json").write_text(
        json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = []
    md.append("# ITviec TP.HCM — ảnh chụp thị trường (đã đăng nhập, có lương)\n")
    md.append("> Thu thập: 20/11/2026, khi đã đăng nhập tài khoản ITviec trong trình duyệt.")
    md.append("> Nguồn: `https://itviec.com/it-jobs/ho-chi-minh-hcm?query=...` (5 truy vấn: java, spring boot, backend, fresher java, java intern).")
    md.append("> Dữ liệu thô: `02e_itviec_hcm_salary_2026-11-20.csv` (" + str(len(rows)) + " tin).")
    md.append("> Quy ước tiền: 1 USD = 26.000 VND; lương là lương tháng, gross trừ khi tin ghi *net*.\n")
    md.append("## 1. Quy mô mẫu\n")
    md.append(f"- **{len(rows)} tin**, **{stats['companies']} công ty**, tất cả đều có mặt tại TP.HCM.")
    md.append(f"- Truy vấn: java {dict(stats['queries']).get('java',0)} · backend {dict(stats['queries']).get('backend',0)} (spring boot, fresher java, java intern trùng hoàn toàn với 2 truy vấn trên; `java intern` bị ITviec trả 429 nên bỏ).")
    md.append(f"- Địa điểm: " + " · ".join(f"{c} ({n})" for c, n in stats["cities"]) + ".\n")
    md.append("## 2. Lương — đây là lý do phải đăng nhập\n")
    md.append(f"- Tin hiện lương đọc được: **{stats['salary_visible']}/{len(rows)} ({str(stats['salary_visible_pct']).replace('.', ',')}%)**, trước khi đăng nhập chỉ 4/109 (3,7%).")
    md.append("- Còn lại vẫn bị che vì **nhà tuyển dụng tự chọn ẩn** (“You'll love it”, “Let's discuss”, “High paid job”, “Very attractive!!!”) — không phải lỗi đăng nhập.")
    if tops:
        md.append(f"- Dải lương trần: thấp nhất ~{stats['salary_usd_min']} USD, cao nhất ~{stats['salary_usd_max']} USD, **trung vị ~{stats['salary_usd_median_ceiling']} USD/tháng** (chỉ trên các tin có số).\n")
        md.append("| Vị trí | Lương ghi trong tin | Công ty |")
        md.append("|---|---|---|")
        for r in sorted(numeric, key=lambda x: -(x["_hi"] or 0))[:12]:
            md.append(f"| {r['title'][:52]} | {r['salary']} | {r['company'][:34]} |")
        md.append("")
    md.append("## 3. Cấp bậc và hình thức làm việc\n")
    md.append("- Cấp bậc (nhãn ITviec): " + " · ".join(f"{k} ({v})" for k, v in stats["levels"][:8]) + ".")
    md.append(f"- **{stats['entry_level']} tin ({str(stats['entry_pct']).replace('.', ',')}%)** nhận fresher/thực tập/junior — đây là cửa vào thật của thị trường.")
    md.append("- Hình thức: " + " · ".join(f"{k} ({v})" for k, v in stats["worktype"]) + ".\n")
    md.append("## 4. Shortlist cho fresher backend Java tại TP.HCM\n")
    md.append(f"{len(sl)} tin trong `02e_itviec_shortlist_2026-11-20.csv`. Đọc theo thứ tự trong file.\n")
    md.append("| # | Tin | Công ty | Cấp | Lương | Hình thức |")
    md.append("|---|---|---|---|---|---|")
    for i, r in enumerate(sl[:15], 1):
        md.append(f"| {i} | {r['title'][:52]} | {r['company'][:28]} | {r['level']} | {r['salary'][:22]} | {r['worktype']} |")
    md.append("")
    md.append("## 5. Giới hạn của mẫu này\n")
    md.append("- Chỉ 5 truy vấn, tối đa 5 trang/truy vấn; ITviec có thể còn tin không khớp từ khóa.")
    md.append("- Nhãn cấp bậc do ITviec gán theo tiêu đề tin, không phải theo yêu cầu kinh nghiệm thực tế trong JD.")
    md.append("- Lương là lương tin đăng, chưa thương lượng; nhiều công ty trả cao hơn mức công bố.")
    md.append("- Ảnh chụp 20/11/2026 — tin đăng trôi nhanh, dùng trong 2–3 tuần rồi làm mới.\n")
    (HERE / "research" / "02e_itviec_market_snapshot_2026-11-20.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"OK rows={len(rows)} visible={stats['salary_visible']} entry={len(sl)}")


if __name__ == "__main__":
    main()
