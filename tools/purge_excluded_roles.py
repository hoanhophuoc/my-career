#!/usr/bin/env python3
"""Xoá khỏi DỮ LIỆU THÔ mọi tin thuộc role Hoàn KHÔNG muốn làm.

Bộ lọc nằm trong `_src/excluded_roles.conf` (sửa file đó, không sửa script).
Chỉ xét cột `title` — không xét mô tả, để không xoá oan tin dev có chữ
"unit test"/"support" trong kỹ năng.

Chạy: python3 _src/purge_excluded_roles.py
Ghi log các dòng bị loại vào `_src/purge_log_2026-11-20.csv`.
Sau khi chạy PHẢI chạy lại: analyze_linkedin_jobs.py, analyze_glints_platforms.py,
analyze_itviec_hcm.py, build_commute_15km.py, make_title_inventory.py.
"""
import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONF = ROOT / "tools" / "excluded_roles.conf"
LOG = ROOT / "tools" / "purge_log_2026-11-20.csv"
DATA = ROOT / "data"

TARGETS = [
    "02d_linkedin_jobs_2026-11-20.csv",
    "02e_itviec_hcm_salary_2026-11-20.csv",
    "02f_glints_jobs_2026-11-20.csv",
    "02g_topdev_jobs_2026-11-20.csv",
    "02h_vietnamworks_jobs_2026-11-20.csv",
]
TARGETS_JSON = ["02d_linkedin_jobs_2026-11-20.json", "02f_glints_jobs_2026-11-20.json"]


def load_rules():
    rules = []
    for line in CONF.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        name, _, pat = line.partition(":")
        rules.append((name.strip(), re.compile(pat.strip(), re.I)))
    return rules


# Nhóm "cứng": nghề khác hẳn → loại ngay, không xét gì thêm.
HARD_GROUPS = {"tester/QA", "PHP", "IT Support/Helpdesk",
               "BrSE/cầu nối Nhật-Hàn", "Hardware/embedded"}

# Chốt bảo vệ dev: tin dev thuộc nhóm "mềm" chỉ bị loại khi tiêu đề bắt đầu
# bằng từ khoá của nghề khác (xem _src/excluded_roles.conf).
DEV_RX = re.compile(
    r"\b(software|backend|back-end|frontend|front-end|fullstack|full[ -]?stack|developer|engineer"
    r"|programmer|devops|architect|sre|data scientist|data engineer)\b"
    r"|lập trình|kỹ sư phần mềm|phần mềm",
    re.I,
)
SOFT_START_RX = re.compile(
    r"^\W*(?:senior |junior |middle |lead |staff |principal |fresher |intern )*"
    r"(?:sales|sale|kinh doanh|business development|marketing|content|designer|graphic|thiết kế"
    r"|kế toán|accountant|accounting|\bhr\b|human resource|recruit|tuyển dụng"
    r"|giáo viên|teacher|tutor|giảng viên|customer service|chăm sóc khách hàng|\bcskh\b"
    r"|tư vấn|trợ lý|admin|hành chính)",
    re.I,
)


def match(rules, title):
    for name, rx in rules:
        if rx.search(title):
            if name in HARD_GROUPS:
                return name
            # nhóm mềm: giữ lại nếu đây là tin dev thật
            if DEV_RX.search(title) and not SOFT_START_RX.search(title):
                continue
            return name
    return None


def main(dry_run=False):
    rules = load_rules()
    log = []
    summary = Counter()
    print(f"== Bộ lọc: {len(rules)} nhóm role ==")
    for name in TARGETS:
        p = DATA / name
        if not p.exists():
            print(f"  - {name}: không có")
            continue
        rows = list(csv.reader(p.open(encoding="utf-8-sig")))
        head, body = rows[0], rows[1:]
        if "title" not in head:
            print(f"  ! {name}: không có cột title → bỏ qua")
            continue
        i = head.index("title")
        kept, removed = [], []
        for r in body:
            grp = match(rules, r[i])
            if grp:
                removed.append(r)
                log.append({"file": name, "nhom_bi_loai": grp, "title": r[i],
                            "company": r[head.index("company")] if "company" in head else "",
                            "url": r[head.index("url")] if "url" in head else ""})
            else:
                kept.append(r)
        for r in removed:
            summary[(name, match(rules, r[i]))] += 1
        if not dry_run:
            with p.open("w", newline="", encoding="utf-8") as f:
                w = csv.writer(f, quoting=csv.QUOTE_ALL)
                w.writerow(head)
                w.writerows(kept)
        print(f"  {name}: {len(body)} → {len(kept)} (bỏ {len(removed)})")
    for name in TARGETS_JSON:
        p = DATA / name
        if not p.exists():
            continue
        raw = json.loads(p.read_text(encoding="utf-8"))
        # 02f (Glints) là dict {..., "rows": [...]}; 02d là list
        wrap = None
        if isinstance(raw, list):
            data = raw
        elif isinstance(raw, dict) and isinstance(raw.get("rows"), list):
            data = raw["rows"]
            wrap = raw
        else:
            print(f"  ! {name}: cấu trúc lạ → bỏ qua")
            continue
        kept, removed = [], []
        for d in data:
            grp = match(rules, str(d.get("title", "")))
            if grp:
                removed.append(d)
                log.append({"file": name, "nhom_bi_loai": grp, "title": d.get("title", ""),
                            "company": d.get("company", ""), "url": d.get("url", "")})
            else:
                kept.append(d)
        for d in removed:
            summary[(name, match(rules, d.get("title", "")))] += 1
        if not dry_run:
            if wrap is not None:
                wrap["rows"] = kept
                p.write_text(json.dumps(wrap, ensure_ascii=False, indent=1), encoding="utf-8")
            else:
                p.write_text(json.dumps(kept, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  {name}: {len(data)} → {len(kept)} (bỏ {len(data) - len(kept)})")

    if not dry_run:
        with LOG.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["file", "nhom_bi_loai", "title", "company", "url"],
                               quoting=csv.QUOTE_ALL)
            w.writeheader()
            w.writerows(log)
        print(f"\nLog {len(log)} dòng bị loại → {LOG.name}")
    print("\n== Bị loại theo file × nhóm ==")
    for (f, g), n in sorted(summary.items()):
        print(f"  {f:44} {g:32} {n:4}")
    print("\n== Tổng theo nhóm role ==")
    for g, n in Counter(k[1] for k in summary.elements()).most_common():
        print(f"  {g:32} {n:4}")


if __name__ == "__main__":
    import sys
    main(dry_run="--dry-run" in sys.argv)
