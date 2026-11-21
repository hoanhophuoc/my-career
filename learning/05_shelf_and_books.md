# 05 — Kệ sách: đọc gì, thứ tự nào (gộp)

**Cập nhật lần cuối:** 21/11/2026

> Gộp ngày **20/11/2026** từ: `05_shelf_and_books.md`, `05_shelf_and_books.md`, `05_shelf_and_books.md`. Nội dung giữ nguyên; chỉ đổi cấp tiêu đề (thêm 1 dấu #) để không phá mục lục.

---

## Phần 1 — Kiểm kê 212 tài liệu

## Phase 5.2 — Kiểm toán thư viện sách (**212 file**, books.txt cập nhật 20/11/2026 11:30)

**Nguồn:** `books.txt` = **701 dòng: 212 file sách** + 489 dòng thư mục.
**Cách làm:** `python3 tools/audit_books.py` → `05_library_audit.csv` (**212 dòng, 8 cột**). Chạy lại được mỗi khi `books.txt` đổi.
**Giới hạn:** tôi **chỉ đọc tên file và tên thư mục**, không đọc nội dung PDF. Đánh giá dựa trên chủ đề + năm xuất bản trong tên file + mức khớp lộ trình 24 tuần.

> **Đính chính bản trước (do Hoàn phát hiện):** bản cũ audit trên **200 file** và coi *A Philosophy of Software Design*, *SQL Performance Explained*, *Unit Testing (Khorikov)*, *Pro Spring Boot 4* là "sách ngoài cần mua". **Sai** — cả 4 cuốn đã có trong tủ. Bản này tính lại trên 212 file và **kệ 12 cuốn lấy 100% từ sách đã có**.

---

### 1. Kết quả kiểm toán

| Quyết định | Số file | Nghĩa là |
|---|---|---|
| **MVS** (kệ 12 cuốn) | **12** | Dùng trong 24 tuần — **tất cả đều đã có trong tủ** |
| **REFERENCE** | **37** | Giữ, chỉ tra cứu theo mục khi kẹt |
| **LATER** | **112** | Liên quan nhưng để sau (English 22 · DSA 19 · Data/AI 14 · Code craft 10 · CS core 9 …) |
| **NGOÀI PHẠM VI** | **51** | Cá nhân, toán/lý, stack khác (Go/C++/Python/Rust), nhập môn đã qua |
| **Tổng** | **212** | |

**Kệ 12 cuốn = 49 giờ đọc** trong 24 tuần (~576 giờ học) → **8,5%** thời gian. Đúng luật 40/60: phần lớn thời gian là gõ code, không phải đọc.

### 2. Phân bố thư viện (đếm thật từ books.txt)

| Thư mục | File |
|---|---|
| `1_Programming` | **64** (Go 20 · Java 20 · C/C++ 10 · Python 6 · .NET 2 · Others 4 · …) |
| `2_CS-Fundamentals` | 35 |
| `3_Software-Engineering` | 34 |
| `9_Personal-Docs` | 21 |
| `6_English-IELTS` | 20 |
| `4_Data-AI` | 15 |
| `8_Non-Technical` | 10 |
| `7_Career-Selfdev` | 7 |
| `5_Math-Science` | 6 |

**Điểm mạnh thật của tủ:** 20 file Java (7 Spring, 2 OCP, 2 Core Java, 2 JPA/Hibernate, *Troubleshooting Java* 2026, *Optimizing Cloud Native Java*, *High-Performance Java Persistence*), **19 sách DSA**, và một khối kiến trúc mạnh bất thường: *DDIA 2nd ed (2026)*, *Database Internals*, *Fundamentals of Software Architecture 2nd (2025)*, *Software Engineering at Google*, *Learning DDD*, *Microservices Patterns (Java)*, *Software Architecture: The Hard Parts*.

**Điểm lệch:** **20 sách Go** (nhiều nhất trong `1_Programming`) trong khi dữ liệu 392 tin LinkedIn (sau khi bỏ tin tester) chỉ có 0 tin Go fresher và ITviec có 18 tin Go (2,4%, gần như toàn senior). Không phải lỗi — nhưng 12 tháng tới Go đứng ngoài kệ.

### 3. Mười hai cuốn trên kệ — đều đã có trong tủ

| # | Cuốn (đúng tên file trong books.txt) | Tuần | Giờ |
|---|---|---|---|
| 1 | **Learning Spring Boot 4** (4th ed, 2026) — sách chính, đúng Boot 4.2 + Java 25 | W3–W16 | 12 |
| 2 | **Pro Spring Boot 4** (4th ed, 2026) — đối chiếu khi sách chính khó hiểu | W6–W13 (tra cứu) | 4 |
| 3 | **Java Persistence with Spring Data and Hibernate** (2023) — mapping, N+1, transaction | W4–W6 | 5 |
| 4 | **High-Performance Java Persistence** (2020) — **chỉ** chương select/fetch | W14 | 3 |
| 5 | **Spring Security in Action** 2nd (2024) — JWT + filter chain | W5 | 3 |
| 6 | **Effective Java** 3rd (2018) — **chọn ~15 item**, không đọc hết | W2/W11 | 5 |
| 7 | **Core Java, Volume I** 14th (2026) — tra khi kẹt ngôn ngữ | tra cứu | 0 |
| 8 | **Just Use Postgres** (2026) — index, EXPLAIN, pagination | W2/W14 | 3 |
| 9 | **Unit Testing: Principles, Practices, and Patterns** (Khorikov, 2020) | W4 | 5 |
| 10 | **A Philosophy of Software Design** 2nd (2021) — 190 trang | W1 | 3 |
| 11 | **Dive Into Design Patterns** (Shvets, 2021) — 5 pattern hay bị hỏi | W7 | 3 |
| 12 | **Spring Start Here** (2021) — dự phòng khi Boot 4 khó đọc (Boot 2.x, chỉ khái niệm) | W4–W6 | 3 |

**Tổng: 49 giờ.** Không cuốn nào phải mua, không cuốn nào phải tải.

### 4. Vì sao loại những cuốn người ta hay khuyên

| Cuốn | Vì sao **không** lên kệ 12 |
|---|---|
| *Spring in Action* 6e (2022) | Spring 5.3/Boot 2.4 — trùng *Learning Spring Boot 4*; chỉ tra khái niệm DI/MVC/AOP |
| *Clean Code* (2026) | Đã thay bằng *APoSD*; chỉ đọc 3 chương khi có code thật để soi |
| *Head First Java* / *Java: A Beginner's Guide* | Đã qua mức nhập môn |
| *Cloud Native Spring in Action*, *Kubernetes in Action* | K8s chưa cần cho fresher; mở khi JD nhắc |
| *System Design Interview* 1–2 | Chỉ hữu ích từ vòng mid; để sau 12 tháng |
| *Clean Architecture*, *Refactoring to Patterns* | Nâng cao; *APoSD* + *Dive Into Design Patterns* đã đủ cho 24 tuần |
| 19 sách DSA | Dùng **1** (bài tập theo lịch), phần còn lại là tra cứu — không đọc tuần tự |

### 5. Cách dùng file này

- Cần biết "cuốn X có nên đọc bây giờ không?" → tra `05_library_audit.csv` cột `decision`.
- `books.txt` đổi → chạy lại script (5 giây), đừng sửa CSV bằng tay.
- Không thêm sách vào kệ 12 trừ khi bỏ một cuốn ra. Kệ là **hợp đồng**, không phải danh sách mong muốn.

**Checkpoint:**
- 212 file, không phải 200 — bản cũ lệch 12 file và đã bị bỏ.
- Kệ 12 cuốn: **12/12 đã có trong tủ**, 49 giờ, không mua gì.
- 4 cuốn tôi từng gọi là "sách ngoài" đều nằm trong tủ — đã sửa ở `05_shelf_and_books.md`.
- Không có sách nào bị đề xuất mua trong 12 tháng tới.

---

## Phần 2 — Sách hay toàn cầu

## Phase 5.7 — Sách tốt nhất thế giới: **bạn đã có gần hết**

**Yêu cầu của Hoàn:** nếu ngoài có sách tốt hơn thì giới thiệu, miễn được cộng đồng quốc tế đánh giá cao.
**Kết quả sau khi đối chiếu lại với `books.txt` (212 file, 20/11/2026):** **0 cuốn cần mua.** Bốn cuốn tôi từng giới thiệu ở bản trước đều **đã nằm trong tủ của bạn**.

---

### 0. Đính chính

| Cuốn tôi từng gọi là "sách ngoài" | Thực tế trong `books.txt` |
|---|---|
| A Philosophy of Software Design (Ousterhout, 2nd) | **dòng 144** — `3_Software-Engineering/Clean-Code/` |
| SQL Performance Explained (Winand) | **dòng 94** — `2_CS-Fundamentals/Databases/` |
| Unit Testing: Principles, Practices, and Patterns (Khorikov) | **dòng 178** — `3_Software-Engineering/Testing-QA/` |
| Pro Spring Boot 4 (Apress, 2026) | **dòng 56** — `1_Programming/Java/Spring/` |

Thêm hai cuốn tôi từng xếp "để sau" cũng đã có: **Designing Data-Intensive Applications 2nd ed (2026)** — dòng 195, và **Database Internals** — dòng 88.

→ Nguyên nhân sai: bản audit cũ chạy trên `books.txt` **197–200 file** trước khi bạn cập nhật lên **212 file**, và tôi không đối chiếu lại từng tựa trước khi đề xuất. Đã sửa: mọi đề xuất sách từ nay phải qua `05_library_audit.csv` trước.

---

### 1. Sách hay nhất thế giới — và bạn đã có

| Cuốn | Rating cộng đồng | Trong tủ? | Dùng thế nào |
|---|---|---|---|
| **Designing Data-Intensive Applications**, 2nd ed (Kleppmann & Riccomini, 2026) | Goodreads **4,69** (11.441 ratings) — cao nhất dòng sách kỹ thuật | ✅ dòng 195 | **Sau 6–12 tháng đi làm.** Không giúp qua phỏng vấn fresher |
| **Unit Testing** (Khorikov) | Goodreads **4,57** · Amazon 4,7 (223) | ✅ dòng 178 | **W4** — lỗ hổng P0 của bạn |
| **SQL Performance Explained** (Winand) | Goodreads **4,41** (361) | ✅ dòng 94 | **W2** — index/EXPLAIN/pagination |
| **A Philosophy of Software Design** (Ousterhout, 2nd) | Goodreads **4,22** (4.930) · chỉ 190 trang | ✅ dòng 144 | **W1** — đọc 1 buổi là xong |
| **Software Engineering at Google** (Winters et al.) | Goodreads **4,32** | ✅ dòng 142 | Năm 2 |
| **Fundamentals of Software Architecture**, 2nd (2025) | Goodreads **4,23** | ✅ dòng 137 | Năm 2 |
| **Learning Domain-Driven Design** (Khononov) | Goodreads **4,43** | ✅ dòng 136 | Khi gặp domain phức tạp |
| **Database Internals** (Petrov) | Goodreads **4,27** | ✅ dòng 88 | Sau 6 tháng |
| **The Pragmatic Programmer** (20th Anniversary) | Goodreads **4,33** | ✅ dòng 146 | Đọc rải, 10'/ngày |
| **Microservices Patterns** (Richardson, ví dụ Java) | Goodreads **4,33** | ✅ (Architecture/Microservices) | W12+, đọc chương API gateway/saga |

### 2. Thật sự **chưa có** trong tủ — và có đáng mua không

| Cuốn | Rating | Đáng mua? |
|---|---|---|
| **Java Concurrency in Practice** (Goetz) | kinh điển, chưa kiểm chứng rating trong phiên này | **Không mua.** W11–W12 chỉ cần chương 2–4; bản PDF hợp pháp không có, thư viện trường/`dev.java` đủ để hiểu memory model |
| **Refactoring**, 2nd ed (Fowler) | Goodreads **4,24** | **Không mua.** Bạn đã có *Dive Into Refactoring* + *Refactoring to Patterns*; Fowler dùng khi review code thật, lúc đó mua cũng chưa muộn |
| **Java Performance**, 2nd ed (Oaks & Beckwith) | Goodreads **4,48** | **Không mua trong 12 tháng.** Chỉ cần khi phải tối ưu GC/heap thật |
| **Grokking Algorithms** (Bhargava) | 4,41 | **Không mua.** Bạn có 19 sách DSA — thiếu bài tập, không thiếu sách |

→ **Quy tắc từ nay:** không đề xuất mua sách nào cho tới khi (a) đã đọc hết 12 cuốn trên kệ, và (b) tự thấy thiếu một chủ đề cụ thể mà không cuốn nào trong 212 file nói tới.

### 3. Nếu chỉ đọc 3 cuốn trong 24 tuần

1. **Learning Spring Boot 4** — 12h, W3–W16 (sách chính, đúng phiên bản).
2. **Unit Testing** (Khorikov) — 5h, W4 (bù lỗ hổng P0).
3. **A Philosophy of Software Design** — 3h, W1 (đổi cách viết code, đọc nhanh nhất).

**Checkpoint:**
- 0 đồng cho sách trong 12 tháng — không phải vì tiết kiệm, mà vì **không thiếu cuốn nào**.
- 4/4 "sách ngoài" ở bản trước đã được xác nhận nằm trong tủ (kèm số dòng).
- 3 cuốn ưu tiên đều đã có file trong `books.txt`.

---

## Phần 3 — Kệ sách tối thiểu

## Phase 5.4 — Kệ sách tối thiểu: **12 cuốn, 49 giờ, 0 đồng**

**Ngày:** 20/11/2026 · **Nguồn:** `books.txt` (212 file) · **Đối chiếu:** `05_library_audit.csv`
**Nguyên tắc:** kệ là **hợp đồng** — 12 cuốn, không hơn. Muốn thêm một cuốn thì phải bỏ một cuốn ra.

> **Không còn "kệ B" mua ngoài.** Bản trước có 3 cuốn ngoài; đối chiếu lại thì cả 3 (và cuốn thứ 4) **đã có trong tủ**. Nay 12/12 cuốn đều là file bạn đang có.

---

### 1. Mười hai cuốn — tuần, chương, số giờ thật

| # | Cuốn (tên file trong `books.txt`) | Tuần | Đọc gì | Giờ |
|---|---|---|---|---|
| 1 | **Learning Spring Boot 4** (4th ed, 2026) | W3–W16 | Sách chính: Boot 4.2 + Java 25. Đọc song song với TaskFlow, không đọc trước | **12** |
| 2 | **Pro Spring Boot 4** (4th ed, 2026) | W6–W13 | Chỉ mở khi sách #1 khó hiểu; đối chiếu native image/internals | 4 |
| 3 | **Java Persistence with Spring Data and Hibernate** (2023) | W4–W6 | Mapping, N+1, repository, transaction | 5 |
| 4 | **High-Performance Java Persistence** (2020) | W14 | **Chỉ** chương select/fetch — tối ưu JPA | 3 |
| 5 | **Spring Security in Action** 2nd (2024) | W5 | JWT + filter chain (chương authentication/authorization) | 3 |
| 6 | **Effective Java** 3rd (2018) | W2 + W11 | **15 item**, không đọc hết: equals/hashCode, immutability, builder, try-with-resources | 5 |
| 7 | **Core Java, Volume I** 14th (2026) | tra cứu | Không đọc tuần tự — tra khi vướng ngôn ngữ | 0 |
| 8 | **Just Use Postgres** (2026) | W2 + W14 | Index, EXPLAIN, pagination | 3 |
| 9 | **Unit Testing: Principles, Practices, and Patterns** (Khorikov, 2020) | W4 | Test **behavior**, không test implementation; test double | 5 |
| 10 | **A Philosophy of Software Design** 2nd (2021) | W1 | 190 trang, đọc trong 1–2 buổi: deep module, complexity | 3 |
| 11 | **Dive Into Design Patterns** (Shvets, 2021) | W7 | 5 pattern hay bị hỏi: Strategy, Factory, Observer, Decorator, Adapter | 3 |
| 12 | **Spring Start Here** (2021) | W4–W6 | Dự phòng khi Boot 4 khó đọc. Boot 2.x → **chỉ lấy khái niệm, không copy code** | 3 |

**Tổng: 49 giờ** trong ~576 giờ của 24 tuần = **8,5%**. Phần còn lại: docs chính thức + gõ code + test.

### 2. Vì sao đúng 12 cuốn này

| Tiêu chí | Cách kiểm |
|---|---|
| Đúng phiên bản đang code | #1 và #2 viết cho Boot 4 (2026); #5 cho Boot 3.x; các cuốn còn lại là khái niệm/ngôn ngữ nên không lỗi thời |
| Phủ đúng 4 lỗ hổng đo được | Java core (#6, #7) · SQL/JPA (#3, #4, #8) · testing (#9) · Spring Boot (#1, #2, #5, #12) · code craft (#10, #11) |
| Không trùng lặp | Mỗi chủ đề tối đa 2 cuốn (1 chính + 1 đối chiếu) |
| Không cuốn nào chỉ để "đọc cho biết" | Cột "Đọc gì" ghi chương cụ thể; nếu không ghi được chương thì cuốn đó không lên kệ |

### 3. Cách đọc để không phí 49 giờ

1. **Đọc sau khi đã gõ, không đọc trước.** Sai thứ tự này là lý do 3 cuốn Spring cũ "đọc mà không vào".
2. **Mỗi chương → 1 commit.** Không commit = chưa đọc.
3. **Ghi giờ đọc thật** vào `09_kpi_tracker.csv` cột `gio_doc_sach`. Ngưỡng: **≤3h/tuần**.
4. Nếu 2 tuần liền đọc >50% thời gian học → cắt sách, tăng code. Đây là luật, không phải gợi ý.

### 4. Những cuốn **không** lên kệ (nhưng vẫn giữ trong tủ)

- *Spring in Action* 6e, *Clean Code*, *Head First Java*, *Core Java Vol II*, 19 sách DSA, *Clean Architecture*, *DDIA*, *Database Internals*, *Software Engineering at Google* — lý do từng cuốn ở `05_library_audit.csv` cột `reason`. Không xoá file, chỉ không đọc trong 24 tuần.

**Checkpoint:**
- Kệ 12 cuốn = **12/12 file đã có trong `books.txt`**, tổng **49 giờ**, chi phí **0 đồng**.
- Không còn danh sách "sách ngoài cần mua" — đã xoá hẳn khỏi pack.
- Mỗi cuốn có tuần + chương cụ thể; cuốn nào không ghi được chương thì không thuộc kệ.

---

## Nguồn có link cho các khẳng định về sách/tài liệu

| Nội dung | Nguồn | Link |
|---|---|---|
| Danh mục tài liệu trong tủ (212 mục) | kiểm kê cục bộ, `05_library_audit.csv` | (file trong repo) |
| JPA/Hibernate: N+1, lazy, transaction | Vlad Mihalcea | https://vladmihalcea.com/ |
| Spring tra cứu nhanh | Baeldung | https://www.baeldung.com/ |
| Design pattern (miễn phí) | Refactoring Guru | https://refactoring.guru/design-patterns |
| Kiến trúc & thực hành | Martin Fowler | https://martinfowler.com/ |

Sách giấy không có link: ghi theo bản trong tủ, không cần mua thêm (ngân sách 0 đồng).
