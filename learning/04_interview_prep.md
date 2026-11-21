# Phase 4.5 — Chuẩn bị phỏng vấn (thị trường TP.HCM, fresher Java)

**Cập nhật lần cuối:** 21/11/2026

**Căn cứ:** cấu trúc vòng tuyển ở `02_interview_formats.md` (Phase 2) + 25 tin thật trong `02d_linkedin_jobs_2026-11-20.csv`. **93,7% tin đòi tiếng Anh** → phần D là bắt buộc, không phải "nếu có thời gian".

---

## A. Bản đồ 5 vòng và thứ họ thật sự chấm

| Vòng | Hình thức thường gặp | Họ chấm gì | Tỉ lệ rớt cao nhất vì |
|---|---|---|---|
| 1. Sàng CV / HR | 10–15' điện thoại, có khi tiếng Anh | Có đúng stack không, lương kỳ vọng, thời gian onboard | CV không khớp JD; nói lương cao hơn khung fresher |
| 2. Test kỹ thuật | Bài 45–90' (trắc nghiệm + 1–2 bài code) hoặc take-home 2–3 ngày | Java core, SQL, đọc code | Không viết nổi vòng lặp + collection cơ bản dưới áp lực thời gian |
| 3. Phỏng vấn kỹ thuật 1-1 | 45–60', thường **viết code trên giấy/Notepad** | Tư duy, cách hỏi lại, kiến thức nền (Java, Spring, DB) | Im lặng khi không biết; không hỏi lại yêu cầu |
| 4. Phỏng vấn dự án / sâu | 30–45' bám vào CV | Có thật làm không, hiểu vì sao không | Không giải thích được lựa chọn của chính mình → mất uy tín toàn bộ |
| 5. Văn hóa / team / lãnh đạo | 30' nói chuyện | Thái độ, học hỏi, teamwork, tiếng Anh | Nói xấu trường/công ty cũ; không có câu hỏi ngược |

> **Sự thật cần nhớ:** ở bậc fresher, họ **không** kỳ vọng bạn biết nhiều. Họ kỳ vọng bạn **không bịa**, **hỏi lại được**, và **học được**. Người trả lời "em chưa biết, nhưng em đoán là ... vì ..." thường qua; người trả lời trôi chảy một thứ không hiểu thường rớt ở vòng 4.

---

## B. Ngân hàng câu hỏi theo chủ đề (kèm hướng trả lời, không phải đáp án học thuộc)

### B1. Java core (30 câu — mức hay gặp nhất)
| Câu | Điều họ muốn nghe |
|---|---|
`String` vs `StringBuilder` vs `StringBuffer` | Immutability; khi nào nối chuỗi trong vòng lặp là sai
`equals` và `hashCode` contract | Nếu `equals` bằng mà `hashCode` khác → mất phần tử trong `HashMap`
`HashMap` hoạt động thế nào | bucket, hash → index, collision (linked list / tree), resize
Interface vs abstract class | Khi nào chọn cái nào — **nêu ví dụ trong TaskFlow**
`final`, `static`, `immutable` | 3 khái niệm khác nhau; immutable class viết thế nào
Checked vs unchecked exception | Khi nào tạo custom exception; vì sao không nuốt exception
Generics + type erasure | Vì sao không `new T[]`; wildcard `? extends` vs `? super`
Stream vs vòng lặp | Khi nào stream làm code **khó** đọc hơn
`Optional` dùng đúng | Trả về, không dùng làm field/param
Thread vs `Runnable` vs `ExecutorService` | Vì sao không `new Thread()` trong web app
`synchronized` vs `Lock` vs `Atomic` | Deadlock là gì; ví dụ trong MiniWallet
`volatile` | Đảm bảo visibility, **không** đảm bảo atomic
Heap vs stack; GC | Cơ bản đủ: object ở heap, GC dọn object không reachable
`OOM` vs `StackOverflow` | Nguyên nhân khác nhau
Immutability và thread safety | Record, `final` field
`record` (Java 16+) | Dùng cho DTO; khác Lombok `@Data`
Virtual threads (Java 21+) | Biết là có, giải thích 1 câu; **không** cần dùng

### B2. Spring Boot (25 câu)
| Câu | Điều họ muốn nghe |
|---|---|
| DI là gì, vì sao constructor injection | Test được, không null, không vòng phụ thuộc ẩn |
| `@Component` vs `@Service` vs `@Repository` | Khác nhau về ngữ nghĩa + `@Repository` có exception translation |
| `@Bean` vs `@Component` | Khi nào cần `@Bean` (thư viện bên thứ ba) |
| Auto-configuration hoạt động thế nào | `@ConditionalOnClass`, `spring.factories`/imports — giải thích ý, không cần chi tiết |
| Bean scope | singleton mặc định; prototype; **singleton phải stateless** |
| `@Transactional` rollback khi nào | Mặc định `RuntimeException`; self-invocation làm mất proxy |
| Propagation mức hay dùng | `REQUIRED` mặc định; `REQUIRES_NEW` khi nào |
| N+1 là gì, sửa thế nào | `JOIN FETCH`/`@EntityGraph`; đo bằng log SQL |
| Lazy vs eager | Vì sao eager là bẫy; `LazyInitializationException` |
| `@RestController` vs `@Controller` | `@ResponseBody` |
| Xử lý lỗi tập trung | `@RestControllerAdvice` + `ProblemDetail` |
| Validation | `@Valid` ở đâu, nhóm validation (nhóm Create/Update) |
| Security: filter chain chạy thế nào | Request → filter → controller; JWT filter đặt ở đâu |
| JWT gồm gì, có bảo mật không | 3 phần; **không** mã hoá payload; phải HTTPS; hết hạn |
| Vì sao không lưu mật khẩu thường/BCrypt là gì | Salt + hash chậm |
| Test 3 tầng trong Spring | `@WebMvcTest` / `@DataJpaTest` / `@SpringBootTest` khác gì |
| Testcontainers để làm gì | Test với DB thật, không lệ thuộc H2 |
| Actuator | health/metrics; không mở public |
| Cấu hình theo môi trường | profile, biến môi trường, **không** commit secret |
| Vì sao Boot 4 / khác Boot 3 điều gì | Java 17+, Framework 7, Jakarta EE 11, JUnit 6 — biết mức này đủ |

### B3. SQL & DB (15 câu)
JOIN các loại; `WHERE` vs `HAVING`; index là gì và khi nào **không** dùng; vì sao index làm chậm ghi; `EXPLAIN` đọc gì; transaction ACID; isolation level (biết 4 mức + ví dụ dirty read); khoá lạc quan vs bi quan; deadlock trong DB; chuẩn hoá 1NF-3NF; khi nào phi chuẩn hoá; `UNION` vs `UNION ALL`; `COUNT(*)` vs `COUNT(col)`; pagination lớn dùng offset có vấn đề gì (keyset pagination).

### B4. Câu hỏi bẫy — cách xử lý
| Câu bẫy | Cách trả lời đúng |
|---|---|
| "Em biết Kafka không?" (thật ra mới đọc) | "Em mới đọc và làm 1 producer/consumer nhỏ, chưa vận hành thật. Em hiểu nó giải bài toán gì và đánh đổi ra sao." |
| "Dự án này em làm một mình à?" | Nói thật: "Vâng, em tự làm, có dùng tài liệu chính thức. Phần khó nhất là X, em làm sai lần đầu vì Y." |
| "Vì sao GPA 8.74 mà không đi làm sớm hơn?" | Trả lời thật + hướng về hiện tại: "Em tập trung học; giờ em đang bù phần thực chiến — 6 tuần vừa rồi em viết TaskFlow." |
| "Em có dùng AI không?" | "Có, để tra khái niệm và review. Nhưng code trong dự án này em tự viết; em có thể giải thích từng dòng nếu anh/chị muốn." — **đây là câu trả lời mạnh**, đừng giấu |
| "Điểm yếu lớn nhất?" | Cụ thể + đang sửa: "Em hay code xong mới viết test. Em đang sửa bằng cách viết test trước cho phần service." |
| Không biết câu gì | "Em chưa gặp vấn đề này. Cách em sẽ tìm là [đọc docs / viết thử nhỏ]. Anh/chị có thể gợi ý hướng không?" — **không đoán bừa** |

### B5. Viết code tại chỗ (vòng 3) — quy trình 5 bước phải thuộc
1. **Nhắc lại đề bằng lời mình** + hỏi 2 câu (input rỗng? trùng? kích thước?).
2. **Nêu ví dụ** (1 nhỏ, 1 biên).
3. **Nói hướng** trước khi gõ ("em dùng HashMap đếm, O(n)").
4. **Viết** — tên biến rõ, hàm nhỏ; nói ra suy nghĩ.
5. **Chạy tay 1 ví dụ** + nêu độ phức tạp + nêu trường hợp chưa xử lý.

Bài hay gặp: đếm/ký tự, đảo chuỗi, two-sum, kiểm tra palindrome, Fibonacci (đệ quy + quy hoạch động), sắp xếp mảng theo điều kiện, đọc/ghi file CSV, đếm từ, tìm phần tử trùng.

---

## C. Phần dự án (vòng 4) — nơi `nexus` sẽ giết bạn nếu còn trên CV

**Luật:** mỗi dòng trên CV phải qua được bài 60 giây: *"Nếu họ hỏi xoáy vào dòng này, mình có 60 giây trả lời thật không?"* Không → xoá dòng đó (xem `01_honest_cv_v1.md` Part D).

**Cấu trúc trả lời 1 dự án (90 giây), học thuộc ý:**
1. **Bài toán** (1 câu): "Hệ thống quản lý công việc nhóm, có phân quyền theo workspace."
2. **Công nghệ + vì sao** (1 câu): "Spring Boot 4.2 + Postgres vì cần transaction và quan hệ."
3. **2 chỗ khó + cách sửa** (2 câu): N+1 → `JOIN FETCH`, đo 21→1 câu SQL; concurrency → `@Version`, 409.
4. **Điều học được** (1 câu): "Em hiểu ra là phải đo trước khi tối ưu."
5. **Nếu làm lại** (1 câu): "Em sẽ viết test trước cho service, vì sửa sau tốn gấp ba."

**Chuẩn bị sẵn 8 câu STAR** (Viết + nói thành tiếng, mỗi câu ≤ 90 giây):
1. Lần em học công nghệ mới nhanh nhất.
2. Lần em làm sai và tự sửa.
3. Lần em bị chê/phản hồi tiêu cực.
4. Lần em phải làm việc nhóm (đồ án) và xung đột ý kiến.
5. Lần em trễ deadline và xử lý.
6. Lần em phải giải thích kỹ thuật cho người không biết kỹ thuật.
7. Việc em tự học ngoài trường gần nhất (dùng **TaskFlow**).
8. Vì sao chọn backend Java (trả lời thật: "em thích phần logic và dữ liệu hơn giao diện" — **không** nói "vì lương").

---

## D. Phần tiếng Anh (bắt buộc — 93,7% tin đòi)

**Mẫu 1 phút tự giới thiệu (viết ra, sửa 3 lần, thuộc ý):**
> "Hi, I'm Hoan. I graduated in Information Technology from [trường] and I'm focusing on Java backend development. In the last few weeks I built a task management system with Spring Boot and PostgreSQL — it has JWT authentication, role-based access, and integration tests with Testcontainers. The hardest part was fixing an N+1 query problem, which I solved with a fetch join and measured the result. I'm looking for a junior backend role where I can keep learning from senior engineers."

**10 câu tiếng Anh phải trả lời trôi (luyện 2 tuần):**
Tell me about yourself · Why Java? · Walk me through your project · What was the hardest bug? · How do you learn new things? · What's your weakness? · How do you handle deadlines? · Why our company? · Where do you see yourself in 2 years? · Do you have any questions for us?

**Cách luyện (miễn phí):** ghi âm bằng điện thoại → nghe lại → sửa **một** lỗi/lần. 15'/ngày từ W13. Không cần app trả phí.
Nếu cần người sửa: các câu lạc bộ tiếng Anh miễn phí ở TP.HCM, hoặc trao đổi với bạn cùng học.

## E. Câu hỏi **bạn** nên hỏi (vòng 5) — chọn 2–3
1. "Team đang dùng Spring Boot phiên bản nào, có kế hoạch lên 4.x chưa?" *(cho thấy bạn biết version — và trả lời được nếu họ hỏi lại)*
2. "Một bạn fresher trong 3 tháng đầu được giao việc gì?"
3. "Code review ở đây diễn ra thế nào?"
4. "Điều gì khiến người mới ở đây thành công và điều gì khiến họ chật vật?"
5. "Em có thể chuẩn bị gì trước ngày bắt đầu?"

## F. 6 lỗi làm rớt fresher (theo thứ tự tần suất)
1. **Bịa** một công nghệ trong CV → sập ở vòng 4. (`nexus` là ví dụ bạn đã tự tránh được.)
2. **Im lặng** khi làm bài code — người phỏng vấn không đánh giá được tư duy.
3. Không hỏi lại yêu cầu, làm sai đề rồi làm lại từ đầu.
4. Nói "em không biết" rồi **dừng** — phải nói tiếp hướng tìm.
5. Nói xấu trường/giảng viên/công ty cũ.
6. Không có câu hỏi ngược → bị đọc là "không quan tâm".

---

## Checkpoint Phase 4.5

- 5 vòng, mỗi vòng có **thứ họ chấm** và **lý do rớt** — để chuẩn bị đúng chỗ.
- ~70 câu hỏi theo 3 chủ đề (Java/Spring/SQL) + 8 câu STAR + 10 câu tiếng Anh + quy trình 5 bước khi code tại chỗ.
- Điểm mạnh của bộ này: nó dạy **cách trả lời khi không biết** — thứ quyết định kết quả ở bậc fresher nhiều hơn kiến thức.

**Quyết định đề xuất:** dồn luyện phỏng vấn vào **W13–W24** (sau khi có dự án), không luyện trước — vì trả lời về dự án thật tốt hơn trả lời thuộc lòng.
**Vì sao:** vòng 3–4 chiếm phần lớn quyết định, và cả hai đều bám vào dự án.
**Điều gì sẽ khiến tôi đổi ý:** nếu W8 (nộp thử) nhận được test kỹ thuật ngay → luyện B5 (code tại chỗ) sớm hơn 4 tuần.
