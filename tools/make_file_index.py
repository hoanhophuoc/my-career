#!/usr/bin/env python3
"""Sinh lại mục "Danh sách file" trong README.md từ đĩa.

Chạy sau mỗi lần thêm/xoá/đổi tên file:
    python3 tools/make_file_index.py

Chỉ ghi lại phần giữa hai dấu <!-- BEGIN FILE INDEX --> và <!-- END FILE INDEX -->,
nên không thể lệch với thực tế và không đụng phần văn bản khác của README.
"""
import csv
import io
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
BEGIN = "<!-- BEGIN FILE INDEX -->"
END = "<!-- END FILE INDEX -->"
SKIP_DIRS = {".git", "dist_clean", ".local_private", "__pycache__", ".cloud-attachments"}
ORDER = ["", "cv", "plan", "research", "learning", "data", "tools"]
LABEL = {
    "": "Gốc pack — điều hướng & nhật ký",
    "cv": "`cv/` — hồ sơ, CV, LinkedIn, kỹ năng",
    "plan": "`plan/` — chiến lược, lộ trình, vận hành",
    "research": "`research/` — thị trường, nguồn, giới hạn",
    "learning": "`learning/` — học gì, học thế nào, luyện tập",
    "data": "`data/` — dữ liệu crawl (nhóm D, chỉ script đọc)",
    "tools": "`tools/` — script crawl/audit/xuất bản",
}


def title(p: Path) -> str:
    """Tiêu đề = dòng tiêu đề đầu tiên của chính file (nên không thể lệch nội dung)."""
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return "—"
    if p.suffix == ".md":
        for line in text.splitlines():
            if line.startswith("# "):
                return line[2:].strip()[:110]
        return "—"
    if p.suffix == ".py":
        m = re.search(r'"""(.*?)\n', text, re.S)
        if m:
            return m.group(1).strip().strip('"').splitlines()[0][:110]
        return "script Python"
    if p.suffix in {".sh", ".conf"}:
        m = re.search(r"^# (.+)$", text, re.M)
        return m.group(1)[:110] if m else "script shell"
    if p.suffix == ".csv":
        first = next(csv.reader(io.StringIO(text)))[:4] if text.strip() else []
        return ("cột: " + ", ".join(first))[:110] if first else "CSV"
    if p.suffix == ".json":
        return "dữ liệu JSON"
    if p.suffix == ".tsv":
        return "bộ thẻ TSV (import Anki)"
    return p.name


def tracked_files() -> list[Path]:
    """Chỉ file ĐANG ĐƯỢC GIT THEO DÕI — file cục bộ bị ignore không lọt vào README."""
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True).stdout
    files = [ROOT / p for p in out.decode("utf-8").split("\0") if p]
    return [p for p in files if p.exists()]  # bỏ file đã xoá nhưng còn trong index


def main() -> None:
    groups: dict[str, list[Path]] = {}
    for p in tracked_files():
        rel = p.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if p.name == "README.md" and len(rel.parts) == 1:
            continue
        d = rel.parts[0] if len(rel.parts) > 1 else ""
        groups.setdefault(d, []).append(p)

    out = []
    for d in ORDER:
        files = sorted(groups.pop(d, []), key=lambda p: p.relative_to(ROOT).as_posix())
        if not files:
            continue
        out.append(f"### {LABEL[d]} — {len(files)} file\n")
        out.append("| File | Nội dung (tiêu đề trong file) |")
        out.append("|---|---|")
        for p in files:
            rel = p.relative_to(ROOT).as_posix()
            out.append(f"| `{rel}` | {title(p).replace('|', '/')} |")
        out.append("")
    for d in sorted(groups):
        files = sorted(groups[d], key=lambda p: p.relative_to(ROOT).as_posix())
        out.append(f"### `{d}/` — {len(files)} file\n")
        out.append("| File | Nội dung |")
        out.append("|---|---|")
        for p in files:
            out.append(f"| `{p.relative_to(ROOT).as_posix()}` | {title(p).replace('|', '/')} |")
        out.append("")

    block = "\n".join(out).rstrip() + "\n"
    readme = README.read_text(encoding="utf-8")
    if BEGIN not in readme or END not in readme:
        raise SystemExit(f"README.md thiếu dấu {BEGIN} / {END}")
    head, rest = readme.split(BEGIN, 1)
    _, tail = rest.split(END, 1)
    README.write_text(f"{head}{BEGIN}\n\n{block}\n{END}{tail}", encoding="utf-8")
    print(f"OK: đã sinh lại danh sách file trong README.md ({len(tracked_files())} file đang theo dõi)")


if __name__ == "__main__":
    main()
