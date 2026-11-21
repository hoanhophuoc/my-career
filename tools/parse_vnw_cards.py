#!/usr/bin/env python3
"""Parse 42 thẻ VietnamWorks (đã đăng nhập, trích từ trình duyệt 20/11/2026).

Input : _src/vnw_raw_2026-11-20.b64  (gzip+base64 của JSON [{href, t:[...], id}])
Output: 02h_vietnamworks_jobs_2026-11-20.csv, 02h_vietnamworks_stats_2026-11-20.json

Cách trích (đã dùng khi crawl ITviec/LinkedIn): chỉ lấy dữ liệu công khai trên
thẻ tin, không lưu tên người liên hệ / SĐT / email.
"""
import base64
import csv
import gzip
import json
import re
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
RAW = ROOT / "tools" / "vnw_raw_2026-11-20.b64"
OUT_CSV = DATA / "02h_vietnamworks_jobs_2026-11-20.csv"
OUT_JSON = DATA / "02h_vietnamworks_stats_2026-11-20.json"
OUT_SHORT = DATA / "02h_vietnamworks_shortlist_2026-11-20.csv"

# Loại các tin TP.HCM không phải backend Java (BA, IT support, lead, đòi tiếng Trung)
NOT_BACKEND = re.compile(r"business analyst|\bBA\b|lead|chinese required|specialist", re.I)
BACKEND = re.compile(r"java|backend|back-end|spring", re.I)

BADGES = {
    "Rất đông ứng viên",
    "Hãy là 1 trong 20 ứng viên đầu tiên",
    "Urgent",
    "Nghỉ T7-CN",
    "Có xe đưa đón",
}
POSTED_RE = re.compile(r"^(Cập nhật|Đăng)\b")
SALARY_RE = re.compile(r"(tháng|năm|Thương lượng|USD|\$|€)", re.I)


def load_cards():
    return json.loads(gzip.decompress(base64.b64decode(RAW.read_text().strip())).decode())


def parse_card(card):
    t = [s.strip() for s in card["t"] if s.strip()]
    title = re.sub(r"^Mới\s+", "", t[0])
    i = 1
    while i < len(t) and t[i] in BADGES:
        i += 1
    company = t[i] if i < len(t) else ""
    i += 1
    salary = t[i] if i < len(t) and SALARY_RE.search(t[i]) else "Thương lượng"
    if SALARY_RE.search(salary):
        i += 1
    location = t[i] if i < len(t) and not POSTED_RE.match(t[i]) else ""
    if location:
        i += 1
    posted = next((x for x in t[i:] if POSTED_RE.match(x)), "")
    skills = []
    for x in t[i:]:
        if POSTED_RE.match(x) or x in BADGES:
            continue
        skills.append(x)
    url = "https://www.vietnamworks.com" + card["href"].split("?")[0] if card["href"] else ""
    return {
        "title": title,
        "company": company,
        "salary": salary,
        "location": location,
        "posted": posted,
        "skills": ", ".join(skills[:8]),
        "url": url,
    }


def salary_mid_vnd(text):
    """Trung vị quy đổi thô: '20tr-30tr ₫/tháng', '$ 500-2,000 /tháng', 'Tới 30tr ₫/tháng'."""
    if not text or "Thương lượng" in text:
        return None
    nums = [float(n.replace(",", "").replace(".", "")) for n in re.findall(r"\d[\d.,]*", text)]
    if not nums:
        return None
    val = statistics.mean([nums[0], nums[-1]]) if len(nums) > 1 else nums[0]
    if "$" in text:
        return val * 26000  # 1 USD = 26.000 VND (quy ước ghi trong file)
    if "/năm" in text or "năm" in text:
        return val / 12
    return val * 1_000_000 if val < 1000 else val


def main():
    cards = [parse_card(c) for c in load_cards()]

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f, fieldnames=["title", "company", "salary", "location", "posted", "skills", "url"],
            quoting=csv.QUOTE_ALL,
        )
        w.writeheader()
        w.writerows(cards)

    hcm = [c for c in cards if "Hồ Chí Minh" in c["location"]]
    shortlist = [
        c for c in hcm
        if BACKEND.search(c["title"] + " " + c["skills"]) and not NOT_BACKEND.search(c["title"])
    ]
    with OUT_SHORT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f, fieldnames=["title", "company", "salary", "location", "posted", "skills", "url"],
            quoting=csv.QUOTE_ALL,
        )
        w.writeheader()
        w.writerows(shortlist)
    with_salary = [c for c in cards if "Thương lượng" not in c["salary"]]
    mids = [m for m in (salary_mid_vnd(c["salary"]) for c in with_salary) if m]
    junior_kw = re.compile(r"\b(junior|fresher|intern|middle|assistant manager)\b", re.I)
    junior = [c for c in cards if junior_kw.search(c["title"])]

    stats = {
        "nguon": "vietnamworks.com/viec-lam?q=java (đã đăng nhập, cuộn hết)",
        "ngay": "2026-11-20",
        "tong_tin_hien_thi": 42,
        "tong_tin_thu_duoc": len(cards),
        "tin_tai_tp_hcm": len(hcm),
        "tin_co_luong": len(with_salary),
        "ty_le_co_luong_pct": round(100 * len(with_salary) / len(cards), 1),
        "trung_vi_luong_vnd": int(statistics.median(mids)) if mids else None,
        "tin_junior_fresher_middle": len(junior),
        "shortlist_backend_java_tp_hcm": len(shortlist),
        "tin_hcm_co_luong": sum(1 for c in hcm if "Thương lượng" not in c["salary"]),
        "ghi_chu": "Trang chỉ render đủ 42 thẻ sau khi đăng nhập + cuộn; khách chỉ thấy 9 thẻ.",
    }
    OUT_JSON.write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    print(f"\n--- SHORTLIST backend Java TP.HCM: {len(shortlist)} ---")
    for c in shortlist:
        print(f"{c['title'][:55]:55} | {c['company'][:30]:30} | {c['salary']}")
    print("\n--- TP.HCM ---")
    for c in hcm:
        print(f"{c['title'][:60]:60} | {c['company'][:32]:32} | {c['salary']:22} | {c['posted']}")


if __name__ == "__main__":
    main()
