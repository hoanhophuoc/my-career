# Phase 4.1 — Lộ trình tổng 24 tuần (bản 6h/ngày)

**Ngày viết:** 20/11/2026 · **Người:** Hồ Phước Hoàn · **Hướng:** Java / Spring Boot backend (Phase 3, tổng 3,80 — hạng 1)
**Trạng thái xuất phát thật:** Java core **L2**, SQL **L2**, testing **L1–L2**, Spring Boot **L1**; **0 dòng Spring Boot trên CV**; `nexus` đã bị loại khỏi hồ sơ (AI viết 100%).

---

## 0. Thông số đã chốt (kiểm chứng 20/11/2026)

| Hạng mục | Quyết định | Nguồn / ghi chú |
|---|---|---|
| JDK | **Java 25 (LTS)** | Spring Framework 7 gọi Java 25 là "latest LTS"; dev.java trỏ tài liệu tới Java 27 (bản mới nhất, không LTS) |
| Spring Boot | **4.2.0** (GA **19/11/2026** `[S23]`) | `docs.spring.io/spring-boot/` — dùng cho TaskFlow và MiniWallet. 4.2 **deprecate `RestTemplate`/`TestRestTemplate`** → dùng `RestClient`/`RestTestClient` (khớp câu S4). 4.1.x vẫn còn OSS tới 31/07/2027 nên không có rủi ro nếu phải lùi |
| Yêu cầu tối thiểu | Java 17+, Spring Framework 7.0.x | Boot 4.0.0 phát hành 20/11/2025; **Boot 4.0 hết OSS support 31/12/2026**, Boot 3.5 chỉ còn commercial từ 30/06/2026 |
| Hệ sinh thái đi kèm | Jakarta EE 11 (Servlet 6.1, JPA 3.2, Validation 3.1), **JUnit 6.0**, Jackson 3.0 | Spring Framework 7.0 GA 13/11/2025 |
| Sách của Hoàn | *Learning Spring Boot 4* **không lỗi thời** — đúng thế hệ Boot 4 | Đối chiếu version ở trên |
| Vẫn phải đọc được | Java 8/11/17, Spring Boot 2.x/3.x | Công ty VN còn nhiều dự án 3.x; 3.5 commercial support tới 2032 |
| Thời lượng | **6h/ngày × 6 ngày/tuần = 36h/tuần** (bản 3h/ngày ở mục 8) | Giả định B11 trong `00_START_HERE.md` |
| Ngân sách | **0 đồng** — chỉ tài nguyên miễn phí đã kiểm chứng | R6; danh mục ở `04_resources_catalog.md` |

> **Điều quan trọng nhất trong cả file này:** vì `nexus` bị loại, 4 tuần đầu **không phải "ôn lại"** mà là **"viết lại từ tay"**. Mỗi ngày phải có **code do Hoàn gõ, không AI**, và phải **viết lại được từ trí nhớ** vào cuối ngày. Đọc hiểu mà không gõ = 0.

---

## 1. Khung một ngày (6h) — dùng cho mọi ngày làm việc

| Thời lượng | Việc | Vì sao đúng thứ tự này |
|---|---|---|
| 40' | **DSA** (1 bài, có hẹn giờ) | Làm lúc não tỉnh nhất; đây là thứ dễ bị bỏ nhất nếu để cuối ngày |
| 20' | **Anki** (thẻ của hôm trước + thẻ đến hạn) | Chống quên — xem `05_how_to_learn.md` |
| 3h30 | **Học + code theo bài của ngày** (chia 2 block 1h45, nghỉ 15') | Khối lớn nhất, không bị ngắt |
| 60' | **Viết lại từ trí nhớ, không nhìn tài liệu** + commit | Đây là bước biến "đã đọc" thành "biết làm" |
| 30' | Ghi `LEARNING.md` (3 dòng: học gì / vướng gì / mai làm gì) + tạo 3–5 thẻ Anki | Tự tạo tài liệu ôn cho chính mình |

**Ngày 7 mỗi tuần:** nghỉ hoặc chỉ 60' (ôn Anki + đọc lại `LEARNING.md` của tuần). Không học bài mới.

---

## 2. LỊCH CHUẨN W0–W24 (nguồn sự thật duy nhất)

> **Đây là bảng lịch duy nhất của pack.** Mọi file khác (`09_executive_summary.md`, `00_START_HERE.md`, `README.md`,
> `04_projects_spec.md`, `05_how_to_learn.md`, `09_kpi_tracker.csv`) **chỉ trỏ link tới bảng này**, không chép lại.
> Nếu hai chỗ nói khác nhau, chỗ này đúng.
>
> - **Ngày:** W1 = **24/11/2026** (thứ Ba), W24 = **04/05/2027**.
> - **Tết Nguyên đán Đinh Mùi 2027:** mùng 1 là **06/02/2027**; nghỉ chính thức **04/02–10/02/2027** (7 ngày, Thông báo 11483/TB-BNV ngày 09/10/2026), đi làm lại **11/02/2027** → rơi vào **W11**.
> - **Tên dự án:** **TaskFlow** = dự án 1 (tự viết tay) · **MiniWallet** = dự án 2. Không còn `java-backend-lab` / "TaskFlow".
> - **Quy tắc CV:** `nexus` chỉ vào CV **sau G6a + G6b**; trước đó CV chỉ gồm dự án đã qua bài bảo vệ (TaskFlow khi xong, Chat-System nếu qua T6).
> - **Nộp đơn:** W1–W7 **0 đơn** (chưa có gì để nộp) · W8–W12 **5 đơn/tuần** chỉ vào công ty **không phải mục tiêu** · W13–W16 **10 đơn/tuần** · W17+ **10–15 đơn/tuần**.
>   Các "cửa thật" (Netcompany, EPAM, KMS, MoMo) **giữ lại tới sau Readiness #1 (W10)**.

| Tuần | Bắt đầu | Stage | Nội dung chính | Dự án | Cổng / mốc | Đơn/tuần | KPI tuần |
|---|---|---|---|---|---|---|---|
| **S0** | 21/11/2026 | 0 — Chuẩn bị | Môi trường, T1 + T6, sửa 8 dòng CV | `java-backend-lab` | **G1** (môi trường chạy) | 0 | môi trường xanh, 1 commit |
| **W1** | 24/11/2026 | 1 — Java core | OOP, Generics, Collections, Streams, Exceptions | — | — | 0 | code tay ≥20h · 6 DSA · Anki 100% |
| **W2** | 01/12/2026 | 1 | IO/NIO, concurrency, JVM, SQL nền | — | — | 0 | như trên · 5 bài code |
| **W3** | 08/12/2026 | 2 — Spring | Boot 4.2, DI, MVC, REST, lỗi, JPA nhập môn | `java-backend-lab` | — | 0 | CRUD chạy Postgres |
| **W4** | 15/12/2026 | 2 | JPA sâu (N+1, transaction), test 3 tầng, Docker, Security | `java-backend-lab` | **G2** (T1 ≥80%) · **G3** (T2 ≥8/10) | 0 | `docker compose up` chạy |
| **W5** | 22/12/2026 | 2 | JWT, phân quyền, API design | **TaskFlow** | — | 0 | spec 1 trang xong |
| **W6** | 29/12/2026 | 2 | TaskFlow: domain, schema, repository, service | TaskFlow | — | 0 | 5 migration + 8 unit test |
| **W7** | 05/01/2027 | 2 | TaskFlow: endpoint, validation, phân quyền owner | TaskFlow | — | 0 | 14 endpoint chạy |
| **W8** | 12/01/2027 | 2 | TaskFlow: test tích hợp, coverage ≥70% | TaskFlow | **G4** (TaskFlow chạy) | **5** (chỉ công ty không mục tiêu) | CI xanh |
| **W9** | 19/01/2027 | 2 | TaskFlow: Docker, GitHub Actions, README + ADR | TaskFlow | — | 5 | README đọc 3' là chạy |
| **W10** | 26/01/2027 | 2 | TaskFlow: hoàn thiện, video 3', tự bảo vệ 2' | TaskFlow | **G5 — Readiness #1** | 5 | rubric đạt ngưỡng "nộp được" |
| **W11** | 02/02/2027 | 3 — Production | **Tết 04–10/02: mục tiêu 50%** — chỉ Anki + 1 DSA/ngày | TaskFlow | — | 3 | không đứt chuỗi Anki |
| **W12** | 09/02/2027 | 3 | Redis cache-aside + đo trước/sau | TaskFlow | — | 5 | số đo p50/p95 |
| **W13** | 16/02/2027 | 3 | Messaging (RabbitMQ/Kafka) + outbox (hiểu) | TaskFlow | — | **10** | 1 luồng async chạy |
| **W14** | 23/02/2027 | 3 | Observability: log JSON, Actuator, Micrometer | TaskFlow | **G6a** (giải thích 6 cổng `nexus`) | 10 | `/actuator/health` + log JSON |
| **W15** | 02/03/2027 | 3 | Hiệu năng + **MiniWallet** spec/domain | **MiniWallet** | — | 10 | `PERF_REPORT.md` có số |
| **W16** | 09/03/2027 | 3 | MiniWallet hoàn thiện + CI + demo | MiniWallet | **G6b** (tự thêm 1 tính năng `nexus`) · **Readiness #2** | 10 | test đồng thời + idempotency xanh |
| **W17** | 16/03/2027 | 4 — Nộp & phỏng vấn | Nộp đơn + 3 buổi mock | — | — | **10–15** | ≥1 phản hồi |
| **W18** | 23/03/2027 | 4 | DSA theo pattern, system design nhẹ, STAR | — | — | 10–15 | 8 câu STAR |
| **W19** | 30/03/2027 | 4 | Phỏng vấn tiếng Anh, CV may đo theo JD | — | — | 10–15 | 3 bản CV may đo |
| **W20** | 06/04/2027 | 4 | Vòng lặp nộp → phản hồi → sửa **một** thứ | — | mốc: **≥1 phỏng vấn** | 10–15 | tỉ lệ phản hồi ≥10% |
| **W21** | 13/04/2027 | 4 | Bù đúng lỗ hổng bị hỏi, hoặc tăng chất MiniWallet | MiniWallet | — | 5–10 | 1 tính năng có test |
| **W22** | 20/04/2027 | 4 | Ôn hệ thống: Java + Spring + SQL + DB internals | — | — | 5–10 | làm lại T1/T2/T4 |
| **W23** | 27/04/2027 | 4 | Phỏng vấn có áp lực thời gian + câu hỏi ngược | — | — | 5–10 | 5 câu hỏi cho NTD |
| **W24** | 04/05/2027 | 4 | **Quyết định**: tiếp Java hay kích hoạt ngưỡng đổi hướng (mục 9) | — | — | 5 | checklist mục 9 |

**KPI tuần (áp dụng mọi tuần, trừ W11):** code tay không AI **≥20h** (≥15h từ W13) · **6 bài DSA** có hẹn giờ ·
**Anki 100%** thẻ đến hạn · giờ đọc sách **≤3h**. Ghi vào `09_kpi_tracker.csv` mỗi Chủ nhật.

---

## 3. Stage 0 — 3 ngày chuẩn bị (làm ngay, trước tuần 1)

| Ngày | Việc | Cách làm (miễn phí) | Đạt khi |
|---|---|---|---|
| **S0-1** | Cài **JDK 25** (Eclipse Temurin), **Maven**, **IntelliJ IDEA Community**; tạo project Maven đầu tiên | Temurin: adoptium.net · IntelliJ CE: jetbrains.com/idea/download (bản Community) | `java -version` ra 25; `mvn -v` chạy; 1 test JUnit xanh |
| **S0-2** | **Docker** + Postgres container + `psql`; tạo repo `java-backend-lab` (public, có README) | `docker run --name pg -e POSTGRES_PASSWORD=dev -p 5432:5432 -d postgres:17` · Git book: git-scm.com/book/en/v2 | `psql` kết nối được, tạo 1 bảng, commit đầu tiên |
| **S0-3** | Làm **T1** (Java core, 90') + **T6** (Chat-System, 45', nói thành tiếng, không mở code); chấm bằng `09_answer_key.md`; sửa 8 dòng CV | `learning/01_diagnostic_tests/` + `01_cv_linkedin_audit.md` mục 3 | Có điểm T1/T6 ghi vào `01_skills_matrix.md`; CV bản 2 xuất PDF |

> **Luật Stage 0:** không học gì mới trong 3 ngày này. Mục tiêu là **biết mình đang ở đâu bằng số**, và có môi trường chạy được. Người hay bỏ qua bước này sẽ học lại từ đầu ở tuần 6.

---

## 4. Tuần 1–4: lộ trình **từng ngày**

Cột "Tài liệu" chỉ ghi chương/mục cụ thể — không phải "đọc cả trang". Mọi link đã kiểm tra sống ngày 20/11/2026 (xem `04_resources_catalog.md`).
Ký hiệu: **dev.java** = `dev.java/learn/...` · **Boot docs** = `docs.spring.io/spring-boot/` · **SF docs** = `docs.spring.io/spring-framework/reference/`

### Tuần 1 — Java core phần 1: ngôn ngữ, OOP, Generics, Collections, Streams, Exceptions

| Ngày | Việc chính (≤3) | Tài liệu | Bài tập phải nộp | Tự kiểm |
|---|---|---|---|---|
| **1** | (1) OOP: interface vs abstract class, composition over inheritance (2) viết `Shape`/`Circle`/`Rectangle` có `area()` (3) giải thích khi nào dùng cái nào trong 5 câu | dev.java → *Language* → **Object-Oriented Programming** | `oop/Shape.java` + 1 test JUnit cho `area()` | Giải thích được **vì sao** interface thay vì abstract — không nhìn tài liệu |
| **2** | (1) Generics: `T`, bounded type, wildcard `? extends` / `? super`, type erasure (2) viết `Box<T>`, `max(List<? extends Comparable<T>>)` (3) đọc lại phần erasure | dev.java → *Language* → **Generics, Lambda, and Pattern Matching** | `generics/Box.java`, `generics/MaxUtil.java` + test | Trả lời: vì sao không được `new T[]`? |
| **3** | (1) Collections: `ArrayList`/`LinkedList`/`HashMap`/`HashSet`, `equals`+`hashCode` contract (2) nhóm từ theo độ dài (3) vẽ tay cấu trúc `HashMap` (bucket + collision) | dev.java → *API* → **Collections and Streams** (phần Collections) | `collections/WordGroups.java` + test; `Employee` có `equals/hashCode` đúng | Giải thích được chuyện gì xảy ra khi `equals` đúng mà `hashCode` sai |
| **4** | (1) Streams: `filter/map/sorted/collect`, `groupingBy`, `toMap`, khi nào **không** nên dùng stream (2) viết lại bài 3 bằng stream (3) so sánh 2 bản | dev.java → *API* → **Collections and Streams** (phần Streams) | `streams/EmployeeReports.java`: lương TB theo phòng, top 3, `groupingBy` | Viết lại 1 pipeline từ trí nhớ, không nhìn |
| **5** | (1) Exceptions: checked vs unchecked, `try-with-resources`, exception wrapping, không nuốt lỗi (2) tạo `AppException` có `errorCode` (3) viết `wordcount` đọc file, lỗi file thiếu phải có message rõ | dev.java → *Language* → **Annotations and Exceptions** | `exceptions/WordCount.java` (đọc file, đếm từ, xử lý IOException) | Nêu 2 lỗi mình từng mắc khi `catch` |
| **6** | (1) **Ôn + viết lại C1–C3 từ trí nhớ, không AI, không tài liệu, có hẹn giờ 90'** (2) chấm bằng `09_answer_key.md` (3) ghi 5 thẻ Anki cho phần hay quên | — | 3 file trong repo, commit message mô tả *mình hiểu gì* | **Làm lại được C2 mà không mở code cũ** — nếu không, lặp lại ngày 4 |
| **7** | Nghỉ / 60' nhẹ: Anki + đọc `LEARNING.md` tuần | — | — | — |

**DSA tuần 1 (40'/ngày, 6 bài):** Array/Two-pointer/String — 2 easy + 1 medium mỗi 2 ngày. Nguồn: `neetcode.io` (lộ trình miễn phí) hoặc `exercism.org/tracks/java` (bài có test sẵn, chấm tự động).

**Tiêu chí qua tuần 1:** tự viết được từ trắng — 1 lớp có OOP hợp lý, 1 generic method, 1 pipeline stream có `groupingBy`, 1 khối `try-with-resources` — trong 90 phút, không AI.

### Tuần 2 — Java core phần 2 (IO, concurrency, JVM) + SQL nền

| Ngày | Việc chính (≤3) | Tài liệu | Bài tập phải nộp | Tự kiểm |
|---|---|---|---|---|
| **8** | (1) `Path`/`Files`/`BufferedReader`, encoding UTF-8 (2) đọc CSV có header → `List<Record>` (3) xử lý dòng lỗi mà không crash | dev.java → *API* → **Managing Out-of-Memory Data** (IO) | `io/CsvReader.java` + test với file mẫu có 2 dòng hỏng | Đọc file 100k dòng không `OutOfMemory` (dùng stream, không `readAllLines`) |
| **9** | (1) `Thread`, `Runnable`, `ExecutorService`, `Future`, `CompletableFuture` (2) `synchronized`/`volatile`/`AtomicInteger` (3) viết `SafeCounter` và chứng minh bản không `synchronized` bị sai | dev.java → *API* → **Virtual Threads** (phần đầu) + `docs.oracle.com` → `java.util.concurrent` | `concurrency/SafeCounter.java` + test đa luồng; `BoundedQueue` tự viết bằng `wait/notify` | Chạy test 20 lần liên tiếp vẫn xanh |
| **10** | (1) JVM: heap/stack, GC là gì (không cần tuning), classloading (2) `jps`, `jstack`, `jcmd` đọc trạng thái app đang chạy (3) gây và đọc 1 `NullPointerException` có stack trace đầy đủ | dev.java → *JVM* → **The Core JDK Tools** | `NOTES_jvm.md` 1 trang: 5 lệnh mình đã chạy + output thật | Giải thích được vì sao `StackOverflowError` khác `OutOfMemoryError` |
| **11** | (1) SQL: `SELECT`/`WHERE`/`JOIN` (inner/left)/`GROUP BY`+`HAVING`/`ORDER BY`/`LIMIT` (2) tạo schema 3 bảng (users, orders, order_items) có FK (3) viết 8 truy vấn | `postgresql.org/docs/current/tutorial.html` | `sql/01_basics.sql` + `schema.sql`, chạy được bằng `psql -f` | 8/8 truy vấn ra đúng kết quả mong đợi |
| **12** | (1) Subquery, `EXISTS`, window function (`ROW_NUMBER`, `RANK`, `SUM OVER`) (2) `EXPLAIN ANALYZE`: đọc `Seq Scan` vs `Index Scan` (3) tạo index và **đo** trước/sau | `use-the-index-luke.com` (miễn phí, đọc chương 1–3) + `postgresql.org/docs/current/using-explain.html` | `sql/02_advanced.sql` + `sql/03_index_report.md` có số mili-giây trước/sau | Chỉ ra được 1 truy vấn chậm và giải thích **vì sao** index giúp |
| **13** | (1) **T2 (SQL) 60'** không tài liệu (2) sửa các câu sai (3) viết lại 3 truy vấn khó nhất từ trí nhớ | `learning/01_diagnostic_tests/02_sql.md` | Điểm T2 ghi vào `01_skills_matrix.md` | **≥ 8/10** — dưới 8 thì lặp ngày 11–12 |
| **14** | Nghỉ / nhẹ | — | — | — |

**DSA tuần 2:** Hash map + Stack/Queue — 6 bài (LeetCode/NeetCode medium đầu tiên).

### Tuần 3 — Spring Boot nhập môn + REST + JPA cơ bản

| Ngày | Việc chính (≤3) | Tài liệu | Bài tập phải nộp | Tự kiểm |
|---|---|---|---|---|
| **15** | (1) `start.spring.io` → project `java-backend-lab`: Web, Validation, Data JPA, PostgreSQL, Actuator; Java 25, Boot 4.2.0 (2) hiểu `@SpringBootApplication`, cấu trúc package, `application.yml` (3) chạy `GET /hello` | `start.spring.io` + Boot docs → **Reference → Getting started / Developing with Spring Boot** | Repo `java-backend-lab`, chạy `mvn spring-boot:run` | App khởi động, log có port; giải thích được auto-configuration làm gì (1 câu) |
| **16** | (1) DI/IoC: `@Component`, `@Service`, `@Repository`, `@Configuration`+`@Bean`, **constructor injection** (2) bean scope, vòng đời (khái niệm) (3) tách `TaskService` + `TaskRepository` in-memory | Boot docs → **Core Features → Spring Beans and Dependency Injection**; SF docs → *The IoC Container* (mục 1) | `java-backend-lab` có 3 tầng, không `new` trong controller | Không còn `new` nào trong code; giải thích vì sao constructor injection tốt hơn field |
| **17** | (1) `@RestController`, `@GetMapping/@PostMapping/@PutMapping/@DeleteMapping`, `@PathVariable/@RequestParam/@RequestBody` (2) DTO tách khỏi entity (3) `@Valid` + `@NotBlank/@Size` | Boot docs → **Web → Spring MVC**; SF docs → *Web on Servlet Stack* | CRUD in-memory đủ 5 endpoint + 4 DTO có validation | Gửi body thiếu field → trả 400, không phải 500 |
| **18** | (1) `@RestControllerAdvice` + `@ExceptionHandler` (2) `ProblemDetail` (RFC 9457) thay vì tự chế format lỗi (3) mã lỗi nghiệp vụ (`errorCode`) | SF docs → *Web → Exceptions*; Boot docs → **Web → Problem Details** | Mọi lỗi trả cùng một shape JSON | Không còn stack trace lọt ra response |
| **19** | (1) JPA: `@Entity`, `@Id`, `@GeneratedValue`, `@Column`, `JpaRepository` (2) derived query (`findByStatus`, `findByTitleContaining`) (3) chuyển in-memory → **Postgres thật** | Boot docs → **Data → SQL Databases**; SF docs → *Data Access → JPA* | `java-backend-lab` ghi/đọc Postgres; `schema` tự tạo | Tắt app, bật lại → dữ liệu còn |
| **20** | (1) **Viết lại CRUD từ trắng, không AI, hẹn giờ 120'** (2) nếu kẹt: mở tài liệu tối đa 3 lần, ghi lại chỗ kẹt (3) commit | — | Bản viết lại trong nhánh `rewrite-w3` | **Xong trong 120'** — đây là bài đo thật của tuần |
| **21** | Nghỉ | — | — | — |

### Tuần 4 — JPA sâu, transaction, testing 3 tầng, Docker, Security nhập môn

| Ngày | Việc chính (≤3) | Tài liệu | Bài tập phải nộp | Tự kiểm |
|---|---|---|---|---|
| **22** | (1) Quan hệ `@OneToMany`/`@ManyToOne`, `mappedBy`, cascade (2) **N+1**: tạo ra nó, thấy nó trong log, sửa bằng `JOIN FETCH`/`@EntityGraph` (3) phân trang `Pageable` | SF docs → *Data Access → JPA → Entity relationships*; `vladmihalcea.com` (bài N+1, miễn phí) | `java-backend-lab` có `TaskFlow..n Task`; log chứng minh N+1 rồi hết N+1 | Đếm được số câu SQL trước/sau khi sửa |
| **23** | (1) `@Transactional`: rollback mặc định theo `RuntimeException`, `readOnly`, propagation mức hay dùng (2) **self-invocation** làm mất transaction — tái hiện lỗi này (3) isolation mức khái niệm | SF docs → *Data Access → Transaction Management* | Test chứng minh rollback: lưu 2 bản ghi, bản 2 ném lỗi → DB trống | Tái hiện được lỗi self-invocation và giải thích cách sửa |
| **24** | (1) 3 tầng test: `@WebMvcTest` (controller + MockMvc), `@DataJpaTest`, `@SpringBootTest` (2) **Testcontainers** Postgres thay H2 (3) `@Transactional` trong test và bẫy của nó | `testcontainers.com` → *Java → PostgreSQL*; Boot docs → **Testing** | 3 file test, `mvn test` xanh, Testcontainers tự bật container | Test không phụ thuộc DB có sẵn trên máy |
| **25** | (1) `Dockerfile` **multi-stage** (build bằng Maven → runtime JRE) (2) `docker compose` app + Postgres + healthcheck (3) chạy cả hệ từ máy sạch | `docs.docker.com` → *Get started / Multi-stage builds* | `Dockerfile`, `compose.yaml`; `docker compose up` chạy được | `docker compose down -v && up` vẫn chạy, không cần thao tác tay |
| **26** | (1) `SecurityFilterChain`, `PasswordEncoder` (BCrypt), `UserDetailsService` (2) form login vs token (3) `@PreAuthorize` + role | Boot docs → **Security**; SF docs → *Security* (chương đầu) | Endpoint `/admin/**` chỉ role ADMIN vào được; mật khẩu lưu dạng hash | Gọi API không token → 401 (không phải 500) |
| **27** | (1) Gộp: auth + test + docker + README (2) viết `README.md` có: mục tiêu, kiến trúc, cách chạy, ảnh chụp API (3) tự bảo vệ 2' trước gương, ghi âm | — | Tag `v0.4` trên repo | Nghe lại bản ghi: có nói được "vì sao" của từng lựa chọn chưa? |
| **28** | Review 4 tuần: làm lại **T1** (đo tiến bộ so với S0) + đọc toàn bộ `LEARNING.md` + cập nhật `01_skills_matrix.md` | — | Bảng so sánh S0 vs W4 | Ít nhất **2 kỹ năng lên 1 bậc** — nếu không, xem lại khung ngày |

---

## 5. Tuần 5–10: Spring Boot thực chiến + TaskFlow

> Lịch và mốc: xem **§2** (bảng chuẩn). Tuần này chỉ mô tả nội dung, không định nghĩa lại lịch.
> Ghi chú cũ "TaskFlow rút về W5–W8, W9–W10 cho `nexus`" đã bỏ — xem changelog cuối file.

| Tuần | Việc | Tài liệu | Sản phẩm |
|---|---|---|---|
| **5** | JWT đầy đủ (filter, claim, hết hạn), role-based, khái niệm refresh token; API design (đặt tên resource, mã trạng thái, versioning) | Boot docs **Security**; SF docs *Security*; `roadmap.sh/java` để rà lỗ hổng kiến thức | Nhánh `feature/jwt` merge; `API_DESIGN.md` |
| **6** | TaskFlow (chọn đề ở `04_projects_spec.md`): domain model, ERD, migration (Flyway), repository + service có unit test | Flyway docs; Boot docs **Data** | ERD + 5 migration + service ≥ 8 unit test |
| **7** | TaskFlow: toàn bộ endpoint, validation, ProblemDetail, phân quyền theo owner (không cho xem dữ liệu người khác) | SF docs Web | Postman collection + 100% endpoint có test happy path |
| **8** | TaskFlow: test tích hợp (Testcontainers), coverage tầng service ≥ 70%; **bắt đầu nộp thử 5 đơn/tuần** | Boot docs **Testing** | CI chạy test; bảng theo dõi ứng tuyển bắt đầu có dữ liệu |
| **9** | TaskFlow: Docker, GitHub Actions (build + test), README + 1 ADR ("vì sao chọn Postgres/Flyway") | `docs.github.com` Actions | CI xanh trên PR; README đọc hiểu trong 3' |
| **10** | TaskFlow: hoàn thiện, video demo 3', tự bảo vệ 2'; **Readiness check #1** | `04_readiness_rubric.md` | Repo public + README + video (unlisted) |

## 6. Tuần 11–16: tính production + MiniWallet

> Tuần trong bảng dưới **phải khớp §2**. Nếu lệch, §2 đúng.

| Tuần | Việc | Sản phẩm |
|---|---|---|
| **11** | **Tết 04–10/02** — mục tiêu 50%: chỉ Anki + 1 bài DSA/ngày, không nội dung mới | Chuỗi Anki không đứt |
| **12** | Redis: cache-aside cho 1 endpoint đọc nhiều; TTL; invalidation khi ghi; **đo** độ trễ trước/sau | Số đo p50/p95 + giải thích khi nào cache là sai |
| **13** | Messaging: RabbitMQ **hoặc** Kafka (chọn 1) bằng Docker; producer/consumer; retry & dead-letter (khái niệm); đọc về **outbox pattern** | 1 luồng async chạy được + `NOTES_messaging.md` |
| **14** | Observability: log JSON có `traceId`, Actuator, Micrometer + Prometheus (local); **G6a** của `nexus` | `/actuator/health` + log JSON |
| **15** | Hiệu năng (index, `EXPLAIN ANALYZE`, HikariCP, pagination, load test nhẹ) + MiniWallet spec/domain | `PERF_REPORT.md` + ERD MiniWallet |
| **16** | MiniWallet hoàn thiện: API + test + docker + CI + demo; **G6b** của `nexus` | **Readiness check #2** |

## 7. Tuần 17–24: nộp đơn, phỏng vấn, vòng lặp

- **Nộp 10–15 đơn/tuần**, ghi vào bảng theo dõi (công ty, vị trí, ngày, kênh, phản hồi, lý do rớt nếu biết).
- **3 buổi mock/tuần**: 1 technical (tự nói khi code), 1 behavioral (STAR), 1 tiếng Anh (tự giới thiệu + 5 câu hỏi).
- **DSA**: 2 buổi/tuần theo pattern (đủ 40 bài tích luỹ từ tuần 1).
- **Cuối tuần**: đọc lại phản hồi → sửa **một** thứ (CV, câu trả lời, hoặc 1 lỗ hổng kỹ thuật). Không sửa 5 thứ cùng lúc.
- Nếu **có phỏng vấn**: hoãn nội dung mới, chỉ bù đúng lỗ hổng bị hỏi + ôn.
- Nếu **có offer**: chuyển sang `04_after_hire.md`.

---

## 8. Bản 3h/ngày (nếu 6h không giữ được)

| Hạng mục | Bản 6h | Bản 3h |
|---|---|---|
| DSA | 40' | 20' (1 bài mỗi 2 ngày) |
| Anki | 20' | 10' |
| Học + code | 3h30 | **2h** |
| Viết lại từ trí nhớ | 60' | **30'** (bắt buộc giữ — đây là phần không được cắt) |
| Ghi chép | 30' | 10' |
| **Thời gian tới "nộp được"** | **~16 tuần** (MiniWallet xong) | **~30–36 tuần** |

**Quy tắc cắt:** cắt **nội dung mới** (bỏ MiniWallet, bỏ Kafka, bỏ Redis) trước; **không cắt** DSA, viết lại từ trí nhớ, và test. Lý do: ba thứ đó là thứ được hỏi trong phỏng vấn.

---

## 9. Quy tắc nộp đơn (quan trọng — đừng nộp quá sớm, đừng chờ quá lâu)

| Mốc | Nộp ở đâu | Vì sao |
|---|---|---|
| **W8** | 5 đơn/tuần vào công ty **không phải mục tiêu** (outsourcing nhỏ, startup sớm) | Lấy dữ liệu thật về việc hồ sơ của mình bị đọc thế nào; được phép rớt |
| **W13** | 10–15 đơn/tuần, gồm công ty mục tiêu **nếu** Rubric mục A+B đạt | Không chờ "hoàn hảo" — thị trường là nguồn thông tin duy nhất về thị trường |
| **Sau 60 đơn Java / 8 tuần mà 0 phỏng vấn** | Kích hoạt ngưỡng ở Phase 3: thêm **.NET** + **internship có lương**, không bỏ Java. **Không dùng tester** (đã loại 20/11/2026) | Đây là ngưỡng đã định trước, không phải thất bại |

---

## 10. Đo tiến bộ — 3 chỉ số, không nhiều hơn

1. **Số kỹ năng lên bậc** trong `01_skills_matrix.md` (mục tiêu: +1 bậc/2 tuần cho 4 kỹ năng P0).
2. **Số bài "viết lại từ trắng trong thời gian giới hạn"** đạt (mục tiêu: 1 bài/tuần từ W3).
3. **Số đơn + số phản hồi** từ W8 (mục tiêu: ≥ 10% phản hồi từ W13; dưới 5% sau 40 đơn → vấn đề ở CV, không ở thị trường).

---

## Checkpoint Phase 4.1

- Lộ trình chia **24 tuần**, 4 tuần đầu có **28 ngày cụ thể**, mỗi ngày 2–3 việc + tài liệu chính xác + bài nộp + tiêu chí tự kiểm.
- Phiên bản đã chốt bằng nguồn chính thức: **Java 25 + Spring Boot 4.2.0**; sách *Learning Spring Boot 4* của Hoàn dùng được ngay.
- Nguyên tắc xuyên suốt: **code tay, viết lại từ trí nhớ, test** — vì `nexus` đã chứng minh "có repo" không bằng "hiểu".
- Nộp đơn bắt đầu **W8** (thử) và **W13** (thật) — không chờ đến W24.

**Quyết định đề xuất:** giữ 24 tuần, nhưng **dịch trọng tâm 4 tuần đầu sang viết code tay** (không đọc sách tuần tự), vì điểm xuất phát thật là L2 chứ không phải L2–L3.
**Vì sao:** 4/8 kỹ năng đã hạ 1 bậc sau khi loại `nexus`; đọc thêm không sửa được khoảng cách "đã học nhưng chưa tự làm" — chỉ có gõ code mới sửa được.
**Điều gì sẽ khiến tôi đổi ý:** nếu ở W4 làm lại T1 vẫn dưới 70% **và** bài viết lại từ trắng vẫn quá 120' → hạ mục tiêu xuống "vào bằng internship có lương" (Phase 3, nhánh dự bị) thay vì cố Java fresher trực tiếp. (Nhánh tester đã bị xoá — không phải phương án.)


---

## Changelog

| Ngày | Thay đổi | Lý do |
|---|---|---|
| 20/11/2026 | Bản gốc 24 tuần, 28 ngày đầu chi tiết | — |
| 20/11/2026 | ~~TaskFlow rút về W5–W8, W9–W10 cho cổng `nexus`~~ | **Đã bỏ 21/11/2026** — ghi chú vá này tạo ra lịch thứ ba mâu thuẫn với §2 và `09_executive_summary.md` |
| 21/11/2026 | **§2 thành bảng lịch chuẩn duy nhất W0–W24** (ngày, dự án, cổng G1–G6, Readiness, mốc nộp, KPI); mọi file khác chỉ trỏ link | Ba lịch mâu thuẫn cho W5–W16; một dự án ba tên (`task-api`/TaskFlow/"Project 1") |
| 21/11/2026 | Tết Nguyên đán 2027 chốt **04–10/02/2027** ở W11 (Thông báo 11483/TB-BNV) | Trước đó ghi "~06/02, cần xác nhận" |
| 21/11/2026 | Nhịp nộp: **0 đơn tới W7**, 5/tuần từ W8 vào công ty không mục tiêu, 10–15 từ W17 | Nộp 5 đơn trong 72h bằng CV chưa sửa là đốt cửa thật |
| 21/11/2026 | ~~Giữ Boot 4.1.x vì 4.2 chưa GA~~ → **nâng lên 4.2.0** (GA 19/11/2026), dùng `RestClient` thay `RestTemplate` | 4.2 đã GA, không còn lý do chờ; `RestTemplate` bị deprecate trong 4.2 |
