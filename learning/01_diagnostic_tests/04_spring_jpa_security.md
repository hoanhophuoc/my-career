# T4 — SPRING BOOT / JPA / SECURITY (60 phút)

**Quy tắc:** 20 câu khái niệm **không** tra cứu. 3 tình huống **được** xem docs.spring.io (đúng như khi đi làm). Không AI.

---

## PHẦN A — 20 câu khái niệm (mỗi câu 1 điểm)

**A1.** IoC (Inversion of Control) là gì? DI (Dependency Injection) quan hệ với IoC thế nào?
**A2.** `@Component` khác `@Bean` ở đâu? Khi nào buộc phải dùng `@Bean`?
**A3.** `@SpringBootApplication` gồm những annotation nào?
**A4.** Vì sao constructor injection được khuyến nghị hơn field injection? (nêu ≥ 2 lý do)
**A5.** Bean scope mặc định là gì? Kể 3 scope khác và khi nào dùng.
**A6.** `@Transactional` mặc định có propagation gì? Nó rollback với exception loại nào, **không** rollback với loại nào?
**A7.** N+1 query là gì? Nêu 3 cách xử lý.
**A8.** `LazyInitializationException` xảy ra khi nào và vì sao?
**A9.** `@RestController` khác `@Controller` ở đâu?
**A10.** Phân biệt `@PathVariable`, `@RequestParam`, `@RequestBody`.
**A11.** Muốn xử lý lỗi tập trung cho toàn bộ API, em dùng gì? Nêu 2 annotation.
**A12.** Làm sao validate input (`@NotNull`, `@Email`...) và trả về lỗi có cấu trúc?
**A13.** Trong Spring Security, `SecurityFilterChain` là gì? Tại sao từ Spring Security 5.7+ người ta bỏ `WebSecurityConfigurerAdapter`?
**A14.** Mô tả luồng xác thực bằng JWT từ lúc login đến lúc gọi API được bảo vệ (5 bước).
**A15.** Vì sao phải dùng `BCryptPasswordEncoder` thay vì lưu mật khẩu thô? Vì sao không dùng MD5/SHA-256 trần?
**A16.** CORS là gì? Khi nào lỗi CORS xuất hiện và cấu hình ở đâu trong Spring?
**A17.** `@Profile` dùng để làm gì? Liên quan gì tới `application.yml` / `application-prod.yml`?
**A18.** Spring Boot Actuator cho gì? Kể 3 endpoint và cảnh báo bảo mật khi bật ở production.
**A19.** Khác nhau giữa `@SpringBootTest`, `@WebMvcTest`, `@DataJpaTest`. Testcontainers giải quyết vấn đề gì?
**A20.** Spring Boot 3 khác Spring Boot 2 ở 2 điểm lớn nào về **phiên bản Java tối thiểu** và **namespace**?

## PHẦN B — 3 tình huống (mỗi tình huống 6–7 điểm, được xem docs)

### S1 — N+1
API `GET /orders` trả 50 đơn, mỗi đơn có danh sách `items`. Code:
```java
List<Order> orders = orderRepository.findAll();   // 50 đơn
return orders.stream().map(o -> new OrderDto(o.getId(), o.getItems().size())).toList();
```
Với `@OneToMany(fetch = LAZY)`, Hibernate chạy **51 query**.
**Hỏi:** (a) giải thích vì sao 51; (b) sửa bằng `JOIN FETCH` — viết JPQL; (c) sửa bằng `@EntityGraph`; (d) nêu nhược điểm của `JOIN FETCH` khi phân trang (`Pageable`); (e) cách khác nếu không muốn fetch hết items (gợi ý: `@BatchSize` / projection / count query).

### S2 — @Transactional không rollback
```java
@Service
public class TransferService {
    public void transfer(Long from, Long to, BigDecimal amount) {
        doTransfer(from, to, amount);   // gọi nội bộ
    }
    @Transactional
    public void doTransfer(...) { /* trừ tiền, cộng tiền, có thể ném Exception */ }
}
```
**Hỏi:** (a) Vì sao `@Transactional` ở `doTransfer` **không có tác dụng**? (b) Cơ chế nào của Spring gây ra (proxy, self-invocation)? (c) Sửa bằng 2 cách. (d) Nếu `doTransfer` ném một **checked exception** thì transaction có rollback không? Vì sao? Làm sao để rollback?

### S3 — Security / JWT
Bạn có `POST /auth/login` (công khai) và `GET /api/me` (cần JWT).
**Hỏi:** (a) Viết `SecurityFilterChain` bean ở mức khái niệm: endpoint nào permitAll, endpoint nào authenticated, session policy là gì. (b) Filter kiểm tra JWT đặt ở đâu trong chuỗi filter, trước hay sau `UsernamePasswordAuthenticationFilter`? (c) Phân biệt 401 và 403 trong ngữ cảnh này — khi nào trả cái nào? (d) JWT lưu ở đâu phía client, và rủi ro của `localStorage` là gì? (e) Làm sao thu hồi (revoke) một JWT trước khi hết hạn?

### S4 — Đọc code cũ: Spring Boot 3 → 4 (4 câu ngắn)

Mục tiêu: phân biệt **"code cũ"** với **"code sai"**. Rất nhiều công ty VN còn chạy Boot 2.x/3.x, nên đọc được code cũ là kỹ năng bắt buộc — nhưng phải biết cái gì đã đổi.

**Hỏi:**
(a) Một class cũ khai `@Entity` với `import javax.persistence.*` **không compile** trên Spring Boot 4. Vì sao, và sửa thế nào?
(b) Code Boot 2.x cấu hình bảo mật bằng `extends WebSecurityConfigurerAdapter` + `configure(HttpSecurity)`. Trên Boot 3/4 cách viết đó **không còn** — viết lại bằng bean gì?
(c) Boot 4 dùng **Jackson 3**, đổi package gốc từ `com.fasterxml.jackson.*` sang gì? Điều đó ảnh hưởng gì tới một custom `JsonSerializer` bạn tự viết?
(d) Từ Boot 4.2, `RestTemplate` bị **deprecate**. Thay bằng client nào, và vì sao Spring khuyến nghị nó?

> **Ghi chú phiên bản (21/11/2026):** Boot **4.2.0 đã GA ngày 19/11/2026** (`[S23]`), nên dự án học dùng **4.2.0**. `RestTemplate` bị deprecate ngay trong 4.2 — đây là lý do câu (d) đáng hỏi. 4.1.x vẫn còn OSS tới 31/07/2027 nên hạ xuống 4.1 cũng an toàn; **4.0 hết OSS 31/12/2026**.

---

## Tự kiểm tra
- [ ] Trả lời A1–A20 **không** mở docs?
- [ ] S2 giải thích được "self-invocation không đi qua proxy" bằng lời của mình?
- [ ] Đã chấm bằng `09_answer_key.md` và ghi L vào `01_skills_matrix.csv`?
