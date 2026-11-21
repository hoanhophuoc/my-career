# Phase 5.6 — Bộ tài nguyên miễn phí cốt lõi (đối chiếu với 212 sách + 1.861 bookmark)

**Câu hỏi file này trả lời:** trong **212 sách** và 1.454 link học nghề, **cái gì thật sự cần**, và cái gì có thể thay bằng tài nguyên miễn phí chính thức?

**Nguyên tắc (R6 + R7):** tài nguyên chính thức của nhà sản xuất > sách dày > blog > video. Lý do: docs luôn khớp phiên bản bạn đang dùng; sách in năm 2022 dạy Boot 3 trong khi bạn code Boot 4.2.

---

## 1. Mười bốn tài nguyên miễn phí — đủ cho 24 tuần

| # | Tài nguyên | Thay cho sách nào | Tuần |
|---|---|---|---|
| 1 | **dev.java/learn** (Oracle) | 5 sách nhập môn Java | W1–W2 |
| 2 | **docs.spring.io/spring-boot** (bản **4.2.x**) | *Spring in Action*, *Cam nang Spring Boot* | W3–W16 |
| 3 | **docs.spring.io/spring-framework/reference** | *Spring Start Here* (khi cần lý thuyết sâu) | W3–W12 |
| 4 | **spring.io/guides** | các chương "làm thử" trong sách | W3–W9 |
| 5 | **start.spring.io** | chương "tạo project" của mọi sách Spring | W3 |
| 6 | **testcontainers.com** | sách testing (bạn chỉ có 2 cuốn Testing-QA) | W4, W8 |
| 7 | **postgresql.org/docs** + **using-explain** | *Fundamentals of Database Systems* (1.100 trang) | W2, W14 |
| 8 | **use-the-index-luke.com** | *High Performance MySQL* (sai DB) | W2, W14 |
| 9 | **neetcode.io** (danh sách pattern) hoặc **exercism.org/tracks/java** | CLRS + Knuth (5 cuốn) | W1–W24 |
| 10 | **docs.docker.com** | *Kubernetes in Action* (chưa cần) | W4, W9 |
| 11 | **git-scm.com/book** | không có sách Git trong thư viện | S0–W4 |
| 12 | **refactoring.guru/design-patterns** | GoF (khô), *Head First Design Patterns* | W7, W18 |
| 13 | **kafka.apache.org/documentation** (hoặc RabbitMQ docs) | *Spring Microservices in Action* (W12) | W12 |
| 14 | **github.com/donnemartin/system-design-primer** | *Microservices Patterns* (đọc sau) | W17–W22 |

Đã kiểm chứng sống ngày 20/11/2026 — chi tiết HTTP status trong `04_resources_catalog.csv`.

## 2. Đối chiếu: 12 cuốn MVS **có còn cần** khi đã có 14 tài nguyên miễn phí?

| Cuốn trong MVS | Vẫn cần? | Vì sao |
|---|---|---|
| Learning Spring Boot 4 | **Có** | Docs nói *cái gì*, sách nói *theo thứ tự nào* — hữu ích cho người mới |
| Spring Start Here | Có (phụ) | Lời giải thích thứ hai khi docs quá cô đọng |
| Java Persistence with Spring Data and Hibernate | **Có** | Docs Spring Data không dạy Hibernate sâu |
| High-Performance Java Persistence | **Có** | Không có nguồn miễn phí tương đương cho fetch/batching |
| Effective Java | **Có** | Chuẩn mực + ví dụ; không có bản miễn phí hợp pháp |
| Core Java Vol I | Tra cứu | Có thể thay bằng dev.java + API docs nếu bạn thấy đủ |
| Cam_nang_SQL_toan_tap | **Có** | Tiếng Việt → nhanh hơn cho W2 |
| Dive Into Design Patterns | **Có** (W7) | refactoring.guru là bản web của cùng tác giả — nếu đọc web thì **bỏ cuốn này** |
| **A Philosophy of Software Design** (thay Clean Code) | **Có** (W1, 3h) | 190 trang, 4.22★; không có nguồn miễn phí tương đương. *Clean Code* chỉ còn là tra cứu 1 chương |
| Spring Security in Action | **Có** | Docs bảo mật của Spring rất khô; đây là chỗ dễ sai nhất |
| Official Cambridge Guide IELTS | **Có** | Không có nguồn miễn phí tương đương cho Speaking band |
| Just Use Postgres | **Có** (W14) | Ngắn, 2026, thực dụng |

**Kết luận:** chỉ **2 cuốn có thể bỏ** nếu chấp nhận dùng web thay thế: *Dive Into Design Patterns* (→ refactoring.guru) và *Core Java Vol I* (→ dev.java + API docs). Tức MVS có thể co **10 cuốn** mà không mất gì.

## 3. Những gì **chắc chắn không cần mua/không cần thêm**

| Loại | Lý do |
|---|---|
| Khóa học trả phí (Udemy/Coursera/bootcamp) | 14 tài nguyên trên phủ 100% lộ trình |
| Sách Boot 3 hoặc cũ hơn | Bạn code Boot 4.2; sách cũ dạy API đã đổi |
| Sách chứng chỉ (OCP) | Chỉ khi công ty yêu cầu |
| Premium LeetCode/NeetCode | Danh sách pattern miễn phí đủ cho fresher VN |
| Sách "system design interview" | Chưa cần ở mức fresher; primer miễn phí đủ |

## 4. Ngân sách

**0 đồng.** Không có mục nào trong Phase 5 cần chi tiền. Nếu sau này cần chi, thứ tự ưu tiên: (1) tài khoản lưu trữ/backup, (2) một khóa ngắn **sau khi** đã có việc và biết mình thiếu gì, (3) không bao giờ: sách mới trước khi đọc hết 12 cuốn MVS.

---

## Checkpoint Phase 5.6

- **14 tài nguyên miễn phí** phủ toàn bộ 24 tuần, đã kiểm chứng sống; mỗi cái gắn với sách cụ thể nó thay thế.
- MVS có thể co từ **12 → 10 cuốn** nếu dùng refactoring.guru và dev.java thay 2 cuốn.
- Ngân sách 0 đồng cho cả Phase 5.

**Quyết định đề xuất:** giữ 12 cuốn MVS nhưng đánh dấu 2 cuốn "có thể bỏ" — quyết định ở W3 dựa trên việc bạn có mở chúng hay không.
**Vì sao:** bỏ sách trước khi thử là quyết định bằng cảm giác; bỏ sau 2 tuần là quyết định bằng dữ liệu.
**Điều gì sẽ khiến tôi đổi ý:** nếu refactoring.guru bị chặn/đổi cấu trúc → giữ *Dive Into Design Patterns* vĩnh viễn trong MVS.

---

## Link bấm được (kiểm tra HTTP 200 ngày 21/11/2026)

| Tài nguyên | Dùng cho | Link |
|---|---|---|
| dev.java | Java core, Collections, Generics, IO, concurrency | https://dev.java/learn/ |
| Spring Boot docs | Cấu hình, Web, Data, Security, Testing | https://docs.spring.io/spring-boot/ |
| Spring Framework reference | IoC, AOP, transaction | https://docs.spring.io/spring-framework/reference/ |
| PostgreSQL tutorial | SQL, JOIN, index | https://www.postgresql.org/docs/current/tutorial.html |
| Use The Index, Luke | Index & EXPLAIN | https://use-the-index-luke.com/ |
| Testcontainers | Test tích hợp với DB thật | https://testcontainers.com/guides/ |
| Docker — multi-stage builds | Dockerfile, compose | https://docs.docker.com/build/building/multi-stage/ |
| Pro Git (sách miễn phí) | Git | https://git-scm.com/book/vi/v2 |
| NeetCode | DSA theo pattern | https://neetcode.io/roadmap |
| Exercism (Java track) | Bài tập có test tự chấm | https://exercism.org/tracks/java |
| start.spring.io | Tạo project Boot | https://start.spring.io/ |
| Adoptium (Temurin JDK) | JDK 25 | https://adoptium.net/ |

Toàn bộ 27 tài nguyên + mã HTTP: `04_resources_catalog.csv`.
