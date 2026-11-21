# 01.1 — MA TRẬN KỸ NĂNG CÓ BẰNG CHỨNG

**Ngày:** 20/11/2026 · **Phiên bản:** v1 (mọi mức L là **ƯỚC LƯỢNG**, chốt lại sau khi Hoàn làm bộ test ở `learning/01_diagnostic_tests/`)
**Nguồn bằng chứng dùng trong file này:**
- `[ĐC]` đề cương học phần (`DeCuongTomTat_CNTT_CLC.txt`, trích theo mã môn) — *Sự thật*
- `[GPA]` bảng điểm (B2 của prompt; ảnh cổng trường không đọc được — xem `00_file_inventory.md`)
- `[GH]` GitHub REST API, truy vấn 20/11/2026 — *Sự thật* (ngôn ngữ, ngày push, tác giả commit)
- `[TĐ]` Hoàn tự đánh giá (B5/B6) — *ý kiến của chính chủ*
- `[CV]`/`[LI]` CV và LinkedIn hiện tại

## Thang L (dùng thống nhất cả pack)

| Mức | Nghĩa | Kiểm tra bằng |
|---|---|---|
| L0 | Chưa học / không nhớ | không giải thích được gì |
| L1 | Nhận ra thuật ngữ | nói được "để làm gì", không nói được "như thế nào" |
| L2 | Giải thích đúng bằng lời + đọc hiểu code | không tự viết được từ đầu |
| L3 | Tự viết được khi có docs, debug lỗi thường gặp | làm được trong 1 buổi có Google |
| L4 | Viết từ trí nhớ, giải thích trade-off, dạy lại được | làm được trong phỏng vấn, không tra cứu |

> **Cột "L thị trường (tạm)"** = mức tôi cho là nhà tuyển dụng TP.HCM thực sự chấm cho **fresher/junior Java**. Đây là **giả thuyết làm việc**, sẽ hiệu chỉnh bằng dữ liệu Phase 2 và ghi rõ nếu đổi.

---

## A. Java & ngôn ngữ

| Kỹ năng | CV/LI nói | Bằng chứng thật | L hiện tại (ước lượng) | L thị trường (tạm) | Khoảng cách | Ưu tiên |
|---|---|---|---|---|---|---|
| **Java core** (syntax, OOP, IO, exceptions) | CV: Java · LI: Java | `[ĐC]` CSC13102 (4 TC, 45 LT + 30 TH) **9.7**, HK1 24-25. Nội dung: Java IO, Generic/Collection, Exception, Swing, JDBC, Multithread, Network, **JUnit**. `[ĐC]` CSC10003 OOP **7.3**. Hoàn nói đã học hết core trên dev.java. `[TĐ]` "chưa chắc áp dụng được". **`nexus` KHÔNG tính** (AI viết 100%, Hoàn xác nhận không hiểu) | **L2** (giải thích/đọc hiểu; **chưa có bằng chứng tự viết**) | **L3** | **1 bậc** | 🔴 P0 |
| **OOP / SOLID / design patterns** | CV: OOP, SOLID, Design Patterns | `[ĐC]` CSC10003 **7.3** (điểm thấp nhất nhóm lập trình) + CSC13010 Thiết kế PM **7.7** | **L2** | L3 (OOP chắc, SOLID nói được) | 1 bậc | 🔴 P0 |
| **Collections / Generics / Streams** | CV: Java (không tách) | `[ĐC]` CSC13102 có "Generic, Collection". Không có repo luyện tập (DSA-Practice đã 404) | **L2** | **L3** | 1 bậc | 🔴 P0 |
| **Concurrency (thread, Executor, CompletableFuture)** | Không nêu | `[ĐC]` CSC13102 "Multithreaded programming" (1 buổi lý thuyết). Repo `java-multithreading-concurrency` **404**. Bookmark có 4 link concurrency | **L1–L2** | L2 (fresher hiếm khi bị hỏi sâu) | 0.5 bậc | 🟡 P1 |
| **JVM (GC, memory model, classloading)** | Không nêu | Không có môn nào dạy JVM. Sách có (Core Java II, Optimizing Cloud Native Java, Troubleshooting Java) nhưng chưa đọc | **L1** | L1–L2 | 0.5–1 | 🟢 P2 (sau khi có việc) |
| **JUnit 5 / Mockito / testing** | CV: "xUnit unit tests" (.NET) | `[ĐC]` CSC13102 có JUnit (1 phần của môn). `[GH]` IT-Tools: xUnit + Playwright (repo thật). **`nexus` KHÔNG tính** (AI viết, kể cả phần test) | **L1–L2** (Java: biết khái niệm, chưa tự viết nhiều) · **L2** (.NET) | L3 | **1–1.5** | 🔴 P0 *(nâng từ P1)* |

## B. Dữ liệu

| Kỹ năng | CV/LI nói | Bằng chứng thật | L hiện tại | L thị trường | Khoảng cách | Ưu tiên |
|---|---|---|---|---|---|---|
| **SQL nền (JOIN, GROUP BY, subquery)** | CV: SQL · LI: SQL | `[ĐC]` CSC10006 Cơ sở dữ liệu **9.0**, HK3 23-24 (2 năm trước). `[GH]` Chat-System dùng Hibernate/PostgreSQL (11–12/2024, AI 20–40%). `nexus` không tính | **L2** | **L3** | 1 | 🔴 P0 |
| **SQL nâng (window function, EXPLAIN, index)** | Không nêu | Không có bằng chứng. Bookmark có "Database System" 31 link nhưng chưa dùng | **L1** | L2 (hay bị hỏi) | 1 bậc | 🟡 P1 |
| **JPA / Hibernate** | LI: Hibernate/JPA | `[GH]` Chat-System (Java, 2024, có commit của Hoàn + `NgocAnhDo26`) dùng Hibernate/PostgreSQL. Sách *High-Performance Java Persistence* có sẵn nhưng chưa đọc | **L1–L2** (đã dùng, đã quên) | **L3** | 1–1.5 bậc | 🔴 P0 |
| **PostgreSQL vận hành (index, transaction isolation)** | CV: PostgreSQL | Dùng trong 3 dự án do AI viết | **L2** | L2–L3 | 0.5 | 🟡 P1 |

## C. Spring (đúng hướng mục tiêu — và là lỗ hổng lớn nhất)

| Kỹ năng | CV/LI nói | Bằng chứng thật | L hiện tại | L thị trường | Khoảng cách | Ưu tiên |
|---|---|---|---|---|---|---|
| **Spring Boot tổng (IoC/DI, auto-config, profiles)** | **LI: Spring Boot** · CV: **không có** | **Không có repo Spring nào** (`[GH]` đã kiểm 9 repo chính). Đang đọc *Learning Spring Boot 4*, xong **chương 4/…** (`[TĐ]`) | **L1** | **L3** | **2 bậc** | 🔴 **P0 — quan trọng nhất** |
| **Spring MVC / REST controller** | LI: Spring MVC | Như trên | **L1** | L3 | 2 bậc | 🔴 P0 |
| **Spring Data / JPA trong Spring** | LI: Hibernate/JPA | Như trên | **L1** | L3 | 2 bậc | 🔴 P0 |
| **Spring Security (filter chain, JWT, OAuth2)** | LI: Spring Security | Sách chương 4 vừa học. JWT đã làm trong **ASP.NET Core** (IT-Tools), không phải Spring. Bookmark 8 link Spring Security | **L1** | L2–L3 | 1.5 bậc | 🔴 P0 |
| **Spring test (@SpringBootTest, MockMvc, Testcontainers)** | Không nêu | Không có | **L0–L1** | L2–L3 | 1.5–2 | 🟡 P1 |
| **Spring AI / LLM app** | CV: Gemini API integration | Learnix (NestJS + Gemini), không phải Spring | **L1** | L1 (mới nổi, chưa phải must-have) | — | 🟢 P2 |

## D. Web / API

| Kỹ năng | CV/LI nói | Bằng chứng thật | L hiện tại | L thị trường | Khoảng cách | Ưu tiên |
|---|---|---|---|---|---|---|
| **HTTP & REST API design** | CV: RESTful API · LI: RESTful APIs | `[ĐC]` CSC13008 **9.0** + CSC13114 **8.8**. `[GH]` IT-Tools REST API + JWT thật, Learnix, Calolator | **L2–L3** | **L3** | 0.5 | 🔴 P0 |
| **Git (branch, commit, PR)** | CV: Git | `[GH]` commit message có cấu trúc conventional commits, chủ đề GPG signing, merge branch → dùng thật, không chỉ "biết" | **L3** | L3 | ✅ đủ | 🟢 giữ |
| **Linux CLI** | CV: Linux | `[ĐC]` CSC10007 Hệ điều hành **9.4**. Bookmark *The Linux Command Line* | **L2** | L2 | 0.5 | 🟡 P1 |
| **Docker / Docker Compose** | CV: Docker | `[GH]` IT-Tools "containerized entire stack with Docker Compose" (repo thật). **`nexus` không tính** (AI viết) | **L1–L2** | L2 | 0.5–1 | 🟡 P1 |
| **CI/CD (GitHub Actions)** | CV: GitHub Actions, Tekton, Argo CD | Helios/Learnix (AI), IT-Tools | **L1–L2** | L2 | 1 | 🟡 P1 |
| **Kubernetes / Operators / Argo CD / CUE** | CV: rất nhiều | Helios (AI 100%, `[TĐ]` nhớ 5–10%) | **L0–L1** | L1 (không ai đòi fresher) | — | ⚪ **Xoá khỏi CV** |

## E. Nền tảng CS (điểm cao, nhưng 2–4 năm trước)

| Kỹ năng | CV/LI nói | Bằng chứng thật | L hiện tại | L thị trường | Khoảng cách | Ưu tiên |
|---|---|---|---|---|---|---|
| **DSA cơ bản (array, hash, two-pointer, stack/queue)** | CV: DSA (coursework) | `[ĐC]` CSC10004 **8.0**, HK3 22-23 (**4 năm**). Repo `DSA-Practice` 404 | **L2** | **L3** | 1 | 🔴 P0 |
| **Cây / đồ thị / đệ quy** | Không nêu | Như trên | **L1–L2** | L2–L3 | 1 | 🟡 P1 |
| **DP** | Không nêu | Như trên | **L1** | L2 (fresher VN hay hỏi DP nhập môn) | 1 | 🟡 P1 |
| **OS nền (process, thread, memory, scheduling)** | Không nêu | `[ĐC]` CSC10007 **9.4**, HK2 23-24. `[ĐC]` CSC10009 Hệ thống máy tính **8.0** | **L2** (đã học tốt, đã quên) | L2 | 0.5–1 | 🟡 P1 |
| **Mạng (TCP/IP, HTTP, DNS)** | Không nêu | `[ĐC]` CSC10008 **7.6** | **L1–L2** | L2 | 0.5 | 🟡 P1 |
| **CSDL nội tại (B+tree, transaction, index)** | Không nêu | `[ĐC]` CSC10006 **9.0**. Sách *Database Internals* có sẵn, chưa đọc | **L1** | L1–L2 | 1 | 🟢 P2 |
| **System design cơ bản** | Không nêu | `[ĐC]` CSC13106 **10** + Helios. Nhưng Helios do AI viết | **L1–L2** | L1 (fresher) → L2 (junior) | 0.5–1 | 🟡 P1 |

## F. Ngôn ngữ / stack khác (đừng đầu tư thêm)

| Kỹ năng | CV nói | Bằng chứng thật | L hiện tại | Ghi chú |
|---|---|---|---|---|
| **Go** | CV: Go (đầu tiên!) | 20 sách Go; `hw-learn-go` **404**; `task-tracker` chỉ **5 KB**; Helios (AI 100%); 1 tháng startup 04/2025. `[TĐ]` tự nhận 30–50% | **L1–L2** | Giữ như "đã từng", **không** là hướng chính (Phase 2: 18 tin, toàn senior) |
| **C# / .NET** | CV: C# (.NET) | `[GH]` IT-Tools (ASP.NET Core 10, EF Core, xUnit, JWT, Docker Compose) — **repo thật, 2,1 MB**; CoolWear (WinUI 3) | **L2–L3** | Đây là **stack mạnh thứ hai có sản phẩm chạy được** — dùng làm "chân thứ hai" nếu .NET có nhiều tin fresher hơn (Phase 2 sẽ quyết) |
| **React / TypeScript** | CV: React, Next.js, TS | Learnix, Calolator, IT-Tools, 4 repo Odin | **L2** | Đủ để không bị loại ở vị trí full-stack |
| **Python** | CV: Python | CS50P, CS50AI, Calolator (FastAPI), Linear-Regression | **L2** | Không ưu tiên |
| **AI-assisted development** | CV: "AI-First Mindset" | `[TĐ]` 100% code AI từ 2025 | **L3 về kỹ năng dùng** nhưng **L1 về kiểm chứng** | Đây là **con dao hai lưỡi**: kỹ năng thật nhưng đang che lỗ hổng nền tảng |

---

## Tổng hợp: 8 dòng quan trọng nhất (dùng cho Phase 4)

| # | Kỹ năng | L hiện tại | L cần | Số bậc phải lên |
|---|---|---|---|---|
| 1 | Spring Boot lõi (DI/MVC/Data/Security) | L1 | L3 | **2** |
| 2 | JPA/Hibernate thực chiến | L1–L2 | L3 | **1–1.5** |
| 3 | Java core + Collections/Generics/Streams | **L2** | L3 | **1** |
| 4 | SQL (nền + EXPLAIN/index/window) | **L2** | L3 | **1** |
| 5 | DSA cơ bản theo pattern | L2 | L3 | 1 |
| 6 | Testing (JUnit/MockMvc/Testcontainers) | **L1–L2** | L3 | **1–1.5** |
| 7 | OOP/SOLID + design patterns | L2 | L3 | 1 |
| 8 | Docker + CI cơ bản | **L1–L2** | L2 | **0.5–1** |

**Đọc bảng này thế nào:** không có kỹ năng nào ở L0 — nghĩa là Hoàn **không phải học lại từ đầu**, mà là *làm cho kiến thức đã có trở nên tự động*. Nhưng sau khi loại `nexus` (AI viết 100%), **4/8 dòng đã hạ 1 bậc** so với bản v1: Java core L2, SQL L2, testing L1–L2, Docker L1–L2. Hệ quả cho Phase 4: **nhiều giờ viết code tay hơn**, ít giờ đọc sách hơn — và điểm khởi đầu thật là "đã học, chưa tự làm", không phải "đã làm được".

## 3 điều đã được trả lời (20/11/2026) — và hệ quả

1. **`nexus`: AI viết 100%, Hoàn không hiểu.** → Không dùng làm bằng chứng. `nexus` **ra khỏi CV** và ra khỏi mọi bảng "tài sản". Đây là thông tin làm **giảm** đánh giá, không phải tăng.
2. **Hoàn đã có bằng tốt nghiệp** (portal trường chưa cập nhật). → Rủi ro M1/M7/M9 đóng — 20/11/2026 xác nhận: **tốt nghiệp loại Giỏi**, **IELTS 6.5 đã được Trường công nhận**. CV ghi "Graduated" + ngày cấp bằng.
3. **Chưa biết:** Hoàn có tự viết được một endpoint Spring Boot CRUD + JWT từ repo trống trong 4 giờ không → **chính là bài test T4**, và là câu hỏi quyết định của toàn bộ lộ trình.

**Hệ quả lên 8 dòng ưu tiên:** không đổi thứ hạng, nhưng **Java core tụt từ L2–L3 xuống L2** và **testing tụt từ L2–L3 xuống L1–L2** — nghĩa là Stage 1 (Phase 4) phải có **nhiều giờ viết code tay hơn** so với dự tính ban đầu.
