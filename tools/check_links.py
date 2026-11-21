"""Rà mọi tên file được nhắc trong .md xem có tồn tại thật không."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAT = re.compile(r"(?<!/)\b(\d{2}[a-z]?_[A-Za-z0-9_\-\.]+\.(?:md|csv|json|py|tsv|conf))\b")
missing = {}
# Nhật ký lịch sử nhắc tên file cũ theo đúng trạng thái tại thời điểm đó → bỏ qua khi kiểm.
SKIP_FILES = {"REVIEW_FIX_LOG.md"}
SKIP_SECTIONS = ("Dọn file", "CHANGELOG", "Gộp", "đã xoá")

for p in sorted(ROOT.rglob("*.md")):
    if p.name in SKIP_FILES or p.relative_to(ROOT).parts[0] in {"dist_clean", ".local_private"}:
        continue
    lines, keep, skip = p.read_text(encoding="utf-8", errors="ignore").splitlines(), [], False
    for line in lines:
        if line.startswith("## "):
            skip = any(k.lower() in line.lower() for k in SKIP_SECTIONS)
        if not skip and "đã xoá" not in line.lower():
            keep.append(line)
    text = "\n".join(keep)
    for name in set(PAT.findall(text)):
        if "*" in name:
            continue
        if not (ROOT / name).exists() and not list(ROOT.glob(f"**/{name}")):
            missing.setdefault(p.relative_to(ROOT).as_posix(), set()).add(name)
if not missing:
    print("OK: không có tên file nào trỏ vào chỗ không tồn tại")
else:
    for f, names in missing.items():
        print(f"{f}:")
        for n in sorted(names):
            print("   -", n)
