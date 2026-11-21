#!/usr/bin/env python3
"""Lọc tin theo khoảng cách tới một điểm gốc — điểm gốc KHÔNG nằm trong repo.

Điểm gốc và bán kính đọc từ `config.local.json` (đã nằm trong .gitignore):

    { "home": [0.0, 0.0], "max_km": 15 }  # điền toạ độ thật trong config.local.json

Chạy:  python3 tools/build_commute.py 02f_glints_jobs_2026-11-20.csv

Script chỉ là công cụ; mọi file kết quả cũng phải để trong thư mục bị ignore
(`.local_private/`), không commit — vì chúng suy ra được vị trí nơi ở.
"""
import csv
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config.local.json"
OUT_DIR = ROOT / ".local_private" / "near_home"

# Toạ độ tâm quận (dữ liệu công khai, không tiết lộ vị trí người dùng).
DISTRICT = {
    "Quận Một": (10.7769, 106.7009), "Quận Hai": (10.7870, 106.7490),
    "Quận Ba": (10.7840, 106.6840), "Quận Bốn": (10.7570, 106.7020),
    "Quận Năm": (10.7540, 106.6660), "Quận Sáu": (10.7480, 106.6350),
    "Quận Bảy": (10.7340, 106.7210), "Quận Tám": (10.7450, 106.6690),
    "Quận Chín": (10.8420, 106.8280), "Quận Mười": (10.7740, 106.6670),
    "Quận Mười Một": (10.7630, 106.6500), "Quận Mười Hai": (10.8670, 106.6420),
    "Quận Tân Bình": (10.8010, 106.6520), "Quận Tân Phú": (10.7900, 106.6280),
    "Quận Phú Nhuận": (10.7990, 106.6800), "Quận Bình Thạnh": (10.8100, 106.7090),
    "Quận Gò Vấp": (10.8380, 106.6650), "Quận Bình Tân": (10.7660, 106.6000),
    "Quận Thủ Đức": (10.8500, 106.7700), "Bình Chánh": (10.6900, 106.5900),
    "Nhà Bè": (10.6950, 106.7300),
}


def haversine(a, b):
    r = 6371.0
    p1, p2 = math.radians(a[0]), math.radians(b[0])
    dp, dl = p2 - p1, math.radians(b[1] - a[1])
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(h))


def district_of(location: str) -> str:
    for name in DISTRICT:
        if name.lower() in (location or "").lower():
            return name
    return ""


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    if not CONFIG.exists():
        print(f"Thiếu {CONFIG.name} — tạo từ config.local.example.json trước.")
        return 2
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    origin, max_km = tuple(cfg["home"]), float(cfg["max_km"])
    src = ROOT / sys.argv[1]
    out = []
    with src.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            d = district_of(row.get("location", ""))
            if not d:
                continue
            km = haversine(origin, DISTRICT[d])
            if km <= max_km:
                out.append({**row, "quan": d, "km_uoc_tinh": round(km, 1)})
    out.sort(key=lambda r: r["km_uoc_tinh"])
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dest = OUT_DIR / f"{src.stem}_within_{int(max_km)}km.csv"
    fields = list(out[0].keys()) if out else []
    with dest.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(out)
    print(f"{len(out)} tin ≤ {max_km:g} km → {dest.relative_to(ROOT)} (không commit)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
