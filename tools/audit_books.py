#!/usr/bin/env python3
"""Audit thu vien sach cua Hoan (books.txt) -> 05_library_audit.csv

Chay lai moi khi books.txt doi:
    python3 tools/audit_books.py
Mac dinh: ../books.txt -> 05_library_audit.csv (tuong doi voi thu muc pack)

Chi doc TEN FILE/THU MUC, khong doc noi dung PDF.
MVS o day = 12 cuon CO SAN TRONG TU (khong de xuat mua them).
"""
import csv
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "..", "books.txt")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, "05_library_audit.csv")

# 12 cuon tren ke — TAT CA deu co san trong books.txt (kiem chung bang grep ten file)
MVS = {
    "learning spring boot 4": ("W3-W16", "Sach chinh Boot 4 + Java 25", 12),
    "pro spring boot 4": ("W6-W13 tra cuu", "Ban doi chieu Boot 4 khi sach chinh kho hieu", 4),
    "java persistence with spring data and hibernate": ("W4-W6", "Mapping, N+1, repository, transaction", 5),
    "high-performance java persistence": ("W14", "Chi chuong select/fetch de toi uu JPA", 3),
    "spring security in action": ("W5", "JWT + filter chain", 3),
    "effective java": ("W2/W11", "Chon ~15 item, khong doc het", 5),
    "core java, volume i - fundamentals": ("Tra cuu", "Ngon ngu co ban: tra khi ket", 0),
    "just use postgres": ("W2/W14", "Postgres: index, EXPLAIN, pagination", 3),
    "unit testing - principles": ("W4", "Test cai gi: behavior vs implementation", 5),
    "a philosophy of software design": ("W1", "Quan ly do phuc tap, deep module (190 trang)", 3),
    "dive into design patterns": ("W7", "5 pattern hay duoc hoi", 3),
    "spring start here": ("W4-W6", "Du phong khi Boot 4 kho doc (Boot 2.x, chi khai niem)", 3),
}

TOPIC = [
    (r"java(?!script)", "Java", 3),
    (r"spring", "Spring", 3),
    (r"hibernate|\bjpa\b|persistence", "JPA/Hibernate", 3),
    (r"postgres|\bsql\b|mysql|database", "SQL/DB", 3),
    (r"algorithm|data structure|\bdsa\b", "DSA", 2),
    (r"clean|refactor|design pattern|architecture", "Code craft", 2),
    (r"test|junit|mockito|tdd", "Testing", 3),
    (r"docker|kubernetes|devops|\bci\b|\bcd\b|observability", "DevOps", 2),
    (r"\bgit\b|linux|bash|shell", "Git/Linux", 2),
    (r"ielts|english|vocabulary|grammar", "English", 2),
    (r"interview|\bcv\b|resume|career|job|salary", "Career", 2),
    (r"microservice|system design|distributed|concurren", "Architecture", 2),
    (r"security|cryptograph|auth", "Security", 1),
    (r"operating system|computer system|network|compiler|computer science", "CS core", 1),
    (r"c\+\+|\bc\b|go\b|golang|python|rust|dotnet|\.net|c#|kotlin|scala|php|javascript|typescript",
     "Stack khac", 0),
    (r"machine learning|\bai\b|deep learning|llm|data science|pandas|numpy|rag", "Data/AI", 1),
    (r"math|physics|calculus|linear algebra|statistic", "Toan/Ly", 0),
    (r"manual|device|cmnd|cccd|passport|hoa don|invoice|screencapture|thuoc|no fap", "Ca nhan", 0),
]

# Cuon lien quan nhung KHONG dua vao ke 12, kem ly do
LATER = {
    "clean code": "Thay bang A Philosophy of Software Design (chi tra cuu 3 chuong khi can)",
    "cloud native spring in action": "W20+ (K8s chua can cho fresher)",
    "spring in action": "Trung Learning Spring Boot 4 -> chi tra cuu khai niem",
    "spring microservices in action": "Chi doc chuong API gateway o W12",
    "spring ai in action": "Ngoai muc tieu 12 thang",
    "ocp oracle certified": "Chi hoc khi cong ty yeu cau chung chi",
    "design patterns - elements of reusable": "Chi tra cuu; Dive Into Design Patterns de doc hon",
    "head first design patterns": "Trung Dive Into Design Patterns",
    "refactoring to patterns": "Nang cao, sau 12 thang",
    "clean architecture": "Sau 12 thang (da co APoSD)",
    "kubernetes in action": "Chi khi JD nhac K8s",
    "system design interview": "Khi phong van >= mid",
    "docker": "Chi tra cuu lenh khi can",
    "troubleshooting java": "Tra cuu khi debug that",
    "optimizing cloud native java": "Sau 12 thang",
    "core java, volume ii": "Tra cuu sau khi xong tap I",
    "head first java": "Da qua muc nhap mon",
    "java - a beginner": "Da qua muc nhap mon",
    "java - the complete reference": "Trung Core Java",
}


def classify(path):
    low = path.lower()
    for key, (week, why, hours) in MVS.items():
        if key in low:
            return "MVS", week, why, hours
    for key, why in LATER.items():
        if key in low:
            return "LATER", "", why, 0
    for rx, topic, prio in TOPIC:
        if re.search(rx, low):
            if topic in ("Ca nhan", "Toan/Ly", "Stack khac"):
                return "NGOAI PHAM VI", "", topic, 0
            if prio >= 3:
                return "REFERENCE", "", topic, 0
            return "LATER", "", topic, 0
    return "REFERENCE", "", "(khong khop chu de nao)", 0


def main():
    lines = [ln.rstrip("\n") for ln in open(BOOKS, encoding="utf-8")]
    files = [ln for ln in lines if ln.lower().endswith((".pdf", ".epub", ".mobi", ".djvu", ".chm"))]
    rows = []
    for p in files:
        decision, week, why, hours = classify(p)
        rows.append({
            "path": p,
            "folder": p.split("/")[0],
            "subfolder": "/".join(p.split("/")[:2]),
            "file": p.split("/")[-1],
            "decision": decision,
            "week": week,
            "reason": why,
            "hours": hours,
        })
    with open(OUT, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["path", "folder", "subfolder", "file",
                                          "decision", "week", "reason", "hours"])
        w.writeheader()
        w.writerows(rows)

    c = Counter(r["decision"] for r in rows)
    print("books.txt:", len(lines), "dong |", len(files), "file")
    for k in ("MVS", "REFERENCE", "LATER", "NGOAI PHAM VI"):
        print(f"  {k:14s} {c.get(k,0):3d}")
    print("  gio MVS (co san trong tu):", sum(r["hours"] for r in rows))
    print("  top folder:", Counter(r["folder"] for r in rows).most_common(9))
    print("  java files:", sum(1 for r in rows if r["folder"] == "1_Programming"
                                and ("java" in r["path"].lower() or "spring" in r["path"].lower()
                                     or "jpa" in r["path"].lower() or "hibernate" in r["path"].lower())))
    mvs_missing = [k for k in MVS if not any(k in r["path"].lower() for r in rows)]
    print("  MVS khong tim thay trong books.txt:", mvs_missing or "KHONG (du 12/12)")
    print("  ->", OUT)


if __name__ == "__main__":
    main()
