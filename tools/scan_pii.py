#!/usr/bin/env python3
"""Quét PII / bí mật trong các file ĐANG ĐƯỢC THEO DÕI.

Chạy: python3 tools/scan_pii.py        (thoát 1 nếu có kết quả)

Bỏ qua: .local_private/ (dữ liệu cục bộ, không commit), .git/, dist_clean/.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXT_EXT = {".md", ".csv", ".json", ".py", ".sh", ".tsv", ".conf", ".txt", ".yml", ".yaml"}

PATTERNS = {
    "CCCD 12 số": re.compile(r"(?<!\d)\d{12}(?!\d)"),
    "SĐT VN": re.compile(r"(?<!\d)(?:\+84|0)(?:2\d{9}|[35789]\d{8})(?!\d)"),
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "mã sinh viên": re.compile(r"(?<!\d)22(?!0{6})\d{6}(?!\d)"),  # (?!0{6}) để bỏ mức lương 22.000.000
    "địa danh nhà": re.compile(r"Bảy Hiền|Bay Hien|Hoàng Hoa Thám|Hoang Hoa Tham", re.I),
    "toạ độ": re.compile(r"\b10\.7\d{2,}\s*[,;]\s*106\.[5-9]\d{2,}|\b106\.[5-9]\d{2,}\s*[,;]\s*10\.7\d{2,}"),
    "đường dẫn máy": re.compile(r"(/home/[A-Za-z0-9._-]+|~/Downloads|C:\\\\Users)"),
    "cookie/token/key": re.compile(
        r"(li_at=|JSESSIONID=|Bearer\s+[A-Za-z0-9._-]{20,}|"
        r"(?i:api[_-]?key|secret|password|token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,})"),
}

# Dòng mẫu/placeholder được phép (không phải dữ liệu thật)
ALLOW = re.compile(r"\[email\]|\[phone\]|\[điện thoại\]|config\.local\.json|POSTGRES_PASSWORD=dev|"
                   r"api[_-]?key.*<|your[_-]?key|placeholder|example\.com|@example|"
                   r"DISTRICT|tâm quận|công khai|Toạ độ tâm quận|^\s*\"Quận |users\.noreply\.github\.com", re.I)
# File định nghĩa chính các mẫu — không tự quét chính nó.
SELF = "tools/scan_pii.py"


def tracked_files():
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True)
    return [f for f in out.stdout.decode().split("\0") if f]


def main() -> int:
    hits = []
    for rel in tracked_files():
        p = ROOT / rel
        if rel == SELF or p.suffix.lower() not in TEXT_EXT or not p.is_file():
            continue
        for i, line in enumerate(p.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            if ALLOW.search(line):
                continue
            for name, pat in PATTERNS.items():
                m = pat.search(line)
                if m:
                    hits.append(f"{rel}:{i}: [{name}] {m.group(0)[:60]}")
    if hits:
        print(f"{len(hits)} kết quả:")
        print("\n".join(hits[:60]))
        return 1
    print("OK: 0 kết quả (CCCD, SĐT, email, mã SV, địa danh nhà, toạ độ, đường dẫn máy, cookie/token).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
