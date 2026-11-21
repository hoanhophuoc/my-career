# Phase 4.2 — Danh mục tài nguyên (chỉ miễn phí, đã kiểm chứng)

**Ngày kiểm chứng:** 20/11/2026, kiểm lại **21/11/2026** (cả 4 mục từng "chưa kiểm chứng"/403 nay trả **200**), bằng `curl -L` (theo dõi redirect, giả lập trình duyệt). Mã `200` = sống; `403` = chặn bot (vẫn mở được bằng trình duyệt).

**Nguyên tắc chọn (R6 + R7):**
1. **Ưu tiên tài liệu chính thức** (spring.io, dev.java, postgresql.org) — vì đó là thứ người phỏng vấn cũng đọc.
2. **Không có khóa học trả phí, không có "bootcamp"** trong danh mục này.
3. **Tận dụng tài sản đã có:** sách *Learning Spring Boot 4* + 200 sách + 1.861 bookmark của Hoàn — dùng làm **tra cứu khi kẹt**, không đọc tuần tự.
4. Mỗi tài nguyên phải trả lời được: *"tuần nào dùng, cho việc gì"*. Không có mục "đọc cho biết".

Chi tiết máy đọc được: `04_resources_catalog.csv` (27 dòng, 9 cột).

---

## 1. Tài nguyên **chính** — 11 thứ, đủ cho cả 24 tuần

| Giai đoạn | Tài nguyên | Dùng đúng chỗ nào |
|---|---|---|
| W1–W2 | **dev.java/learn** (`language/oop`, `language/fp`, `api/collections-and-streams`, `api/io`, `api/virtual-threads`, `jvm/core-tools`) | Mỗi ngày một chương, **đọc rồi gõ lại ngay** — không đọc quá 40' liên tục |
| W2, W14 | **postgresql.org/docs** + **using-explain** + **use-the-index-luke** | SQL nền và đọc query plan; đây là bộ ba tốt nhất miễn phí |
| W3–W16 | **docs.spring.io/spring-boot** (bản **4.2.x**) + **docs.spring.io/spring-framework/reference** | Đọc **theo mục**, khi cần làm một việc cụ thể. Không đọc từ đầu đến cuối |
| W3–W9 | **spring.io/guides** + **start.spring.io** | Khi cần bản chạy được trong 20' để thấy hình dạng đúng |
| W4–W8 | **testcontainers.com** (Java → PostgreSQL) | Bắt buộc — điều kiện B1 của rubric |
| W1–W24 | **neetcode.io** (danh sách pattern miễn phí) hoặc **exercism.org/tracks/java** | DSA 40'/ngày; Exercism tốt hơn ở giai đoạn đầu vì có test tự chấm |
| W4, W9 | **docs.docker.com** (Get started, multi-stage) | Dockerfile + compose |
| S0–W4 | **git-scm.com/book/en/v2** (chương 2–3, 6) | Branch/rebase/conflict — thứ bị hỏi gián tiếp qua "em làm việc nhóm thế nào" |
| W7, W18 | **refactoring.guru/design-patterns** (5 pattern: Strategy, Factory, Adapter, Observer, Template Method) | Đủ để trả lời "em đã dùng pattern nào" mà không nói dối |
| W12 | **kafka.apache.org/documentation** (Introduction + Quickstart) **hoặc** RabbitMQ | Chọn **một**; mục tiêu là hiểu async + retry, không phải thành chuyên gia |
| W17–W22 | **github.com/donnemartin/system-design-primer** | Chỉ phần Index + 2–3 case nhỏ (URL shortener, rate limiter) |

## 2. Tài nguyên **tùy chọn** — chỉ mở khi có câu hỏi cụ thể

| Tài nguyên | Khi nào mở | Khi nào **không** mở |
|---|---|---|
| MIT OCW 6.006 | Khi DSA pattern không vào đầu, cần hiểu gốc | Khi chỉ cần qua vòng screening — 40 bài pattern đủ |
| CMU 15-445 | Khi bị hỏi "vì sao index nhanh" và muốn trả lời ở mức ấn tượng | Trước W20 — không cần cho fresher |
| roadmap.sh/java | W5 và W22 để **tự rà lỗ hổng** | Không học tuần tự theo nó (nó là bản đồ, không phải lộ trình) |
| Vlad Mihalcea (blog) | Khi gặp N+1/lazy/transaction khó | Không đọc tuần tự |
| Baeldung | Tra cứu nhanh 1 annotation | **Không** dùng làm tài liệu chính: dễ đọc thụ động. Trả 403 với `curl` mặc định nhưng **200** với User-Agent trình duyệt (21/11/2026) |
| Sách *Learning Spring Boot 4* của Hoàn | W3–W16, khi cần giải thích dài hơn docs | Không đọc từ chương 1 → hết (sẽ mất 6 tuần chỉ để đọc) |

## 3. Tài nguyên **bị loại** (và lý do — để không mất thời gian quay lại)

| Loại | Lý do loại |
|---|---|
| Khóa học/bootcamp trả phí | R6: ngân sách 0. Và nội dung tương đương có miễn phí |
| "Học 10 framework trong 30 ngày" | Không khớp mục tiêu: cần **1 stack sâu**, không phải 10 stack nông |
| Kênh YouTube "roadmap Java 2026" | Không kiểm chứng được nội dung, không có bài tập, tạo cảm giác đã học |
| LeetCode premium / NeetCode premium | Không cần cho mức fresher VN; danh sách bài miễn phí là đủ |
| Sách JVM/GC chuyên sâu | Chưa cần ở 6 tháng đầu; quay lại sau khi có việc |
| Chứng chỉ (OCP Java, AWS) | Tốn tiền, không thay được dự án. Chỉ cân nhắc **sau khi có việc** nếu công ty trả |

## 4. Một cảnh báo về cách dùng tài nguyên

Có **hai kiểu học** và chỉ một kiểu tạo ra kỹ năng:

| Kiểu | Dấu hiệu | Kết quả |
|---|---|---|
| **Đọc để hiểu** | Mở docs, đọc, gật gù, đóng lại | Quên sau 3 ngày; phỏng vấn không trả lời được |
| **Làm để biết** | Đọc 20', gõ code, làm vỡ nó, sửa, viết lại từ trí nhớ | Ở lại; trả lời được "vì sao" |

Toàn bộ lộ trình này được thiết kế theo kiểu thứ hai: mỗi ngày có **bài phải nộp** và **60' viết lại không nhìn**. Nếu một ngày trôi qua mà không có commit nào — ngày đó không tính là đã học, dù đã đọc 4 tiếng.

---

## Checkpoint Phase 4.2

- 27 tài nguyên, **27/27 trả HTTP 200** khi kiểm lại ngày **21/11/2026** (4 mục trước đây "chưa kiểm chứng"/403: Flyway, Vlad Mihalcea, Baeldung, freeCodeCamp). Baeldung vẫn trả 403 với `curl` mặc định — cần User-Agent trình duyệt.
- **11 tài nguyên chính** là đủ cho 24 tuần; không cần mua gì.
- Sách *Learning Spring Boot 4* của Hoàn **dùng được** (đúng thế hệ Boot 4), nhưng chỉ để tra cứu — không đọc tuần tự.

**Quyết định đề xuất:** bỏ hẳn ý định "đọc lại 200 sách"; chỉ dùng 1 sách của Hoàn + 11 tài nguyên trên.
**Vì sao:** R7 (tối giản) và vì đọc thêm không sửa được vấn đề thật — vấn đề là **chưa tự viết**.
**Điều gì sẽ khiến tôi đổi ý:** nếu W4 kiểm tra cho thấy lỗ hổng lý thuyết cụ thể (ví dụ không giải thích được GC hoặc index) → thêm đúng 1 tài nguyên cho lỗ hổng đó, không thêm cả bộ.

> **URL bấm được:** mỗi tài nguyên có link đầy đủ ở cột `url` của `04_resources_catalog.csv` (kèm cột `trang_thai_http` và `ngay_kiem_chung`). Bản .md này chỉ tóm tắt nội dung.
