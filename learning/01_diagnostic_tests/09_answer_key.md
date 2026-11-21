# 09 — ĐÁP ÁN & GIẢI THÍCH

> **Chỉ mở sau khi đã làm bài và ghi đáp án ra giấy.** Đáp án ở đây đã đối chiếu với hành vi chuẩn của Java (JLS/Javadoc), PostgreSQL 16 và Spring Boot 3.x/4.x. Chỗ nào là *thực hành tốt* (không phải "đúng/sai tuyệt đối") tôi ghi rõ.

---

## PHẦN A — JAVA: 30 câu trắc nghiệm

| Câu | Đáp án | Vì sao (1 dòng) |
|---|---|---|
| A1 | **B** | `String` immutable; `trim()` trả về chuỗi mới, không gán lại thì `s` không đổi |
| A2 | **B** | Literal được intern → `a == b` true; `new String` là object mới → `==` false; `equals` so nội dung → true |
| A3 | **B** | ArrayList truy cập theo index O(1); LinkedList phải duyệt O(n) |
| A4 | **B** | HashMap cho **1** key null (Hashtable không cho) |
| A5 | **B** | `final` khoá **tham chiếu**, không khoá nội dung object |
| A6 | **B** | Từ Java 8: `default` + `static` method có thân hàm |
| A7 | **B** | NPE là `RuntimeException` → unchecked |
| A8 | **A** | Phải implement `AutoCloseable` (hoặc `Closeable`) |
| A9 | **C** | `StringBuilder.append` tránh tạo object mới mỗi vòng |
| A10 | **B** | Integer cache −128..127 → 127 bằng nhau; 128 là object mới → `==` false |
| A11 | **B** | `flatMap` trải phẳng `Stream<Stream<T>>` |
| A12 | **C** | `toMap` ném `IllegalStateException` khi trùng key (trừ khi truyền merge function) |
| A13 | **B** | Optional = tín hiệu "có thể vắng" ở kiểu trả về; **không** dùng cho field/param bừa bãi |
| A14 | **B** | static bị **hide**, không override (không đa hình) |
| A15 | **B** | Overload chọn lúc biên dịch theo kiểu khai báo |
| A16 | **B** | Constructor không được kế thừa |
| A17 | **B** | `super()`/`this()` phải là câu lệnh đầu tiên |
| A18 | **B** | Interface (trước Java 8) chỉ có hằng `static final`; không có field non-static |
| A19 | **B** | equals bằng ⇒ hashCode **phải** bằng (chiều ngược lại không bắt buộc) |
| A20 | **A** | Erasure: thông tin generic bị xoá khi chạy (vì tương thích ngược) |
| A21 | **B** | `? extends` là producer → không `add` được (trừ `null`) |
| A22 | **B** | `synchronized` instance method khoá `this` |
| A23 | **B** | volatile = visibility + cấm reorder, **không** đảm bảo `count++` nguyên tử |
| A24 | **A** | `submit` trả `Future`, exception bị "nuốt" vào Future; `execute` ném ra |
| A25 | **B** | Thứ tự acquire lock cố định là cách phòng deadlock phổ biến nhất |
| A26 | **B** | `return` trong `finally` **ghi đè** giá trị trả về (và nuốt exception — code smell) |
| A27 | **B** | Mảng có kiểm tra kiểu lúc chạy → `ArrayStoreException` |
| A28 | **B** | Java 7 |
| A29 | **C** | `var` chỉ cho biến local có khởi tạo, không dùng cho field/param/return |
| A30 | **B** | Record: field `private final`, accessor `x()`, có `equals/hashCode/toString` tự sinh |

**Điểm:** đếm số đúng/30. Dưới 20 → Java core đang ở **L2**, phải viết code lại từ đầu (không đọc thêm sách).

---

## PHẦN B — 10 câu đọc code

| Câu | Đáp án | Giải thích |
|---|---|---|
| B1 | `UnsupportedOperationException` | `Arrays.asList` trả list **fixed-size**, `add` không hỗ trợ (biên dịch vẫn OK) |
| B2 | `A` | static bị hide; chọn theo kiểu khai báo (`A`) |
| B3 | `1 2` | Cùng key "a" bị ghi đè → size 1, value 2 |
| B4 | `0` / `0.5` / `0.0` | Phép chia nguyên `1/2 = 0`; ép `double` **sau** khi đã chia → 0.0 |
| B5 | **Không** đảm bảo bằng 2000 | `count++` là read-modify-write 3 bước, không nguyên tử → race condition. Sửa: `synchronized`, `AtomicInteger`, hoặc `LongAdder` |
| B6 | `[20, 40]` | filter số chẵn (2,4) → ×10 |
| B7 | `caught finally` | catch chạy trước, finally luôn chạy, không có return nên in trên 1 dòng |
| B8 | `false` | `instanceof` với `null` trả **false**, không NPE |
| B9 | `[c, b, a]` | `reverseOrder()` → giảm dần |
| B10 | **Lỗi biên dịch** | `Box<?>` là wildcard capture → không gọi được `set(T)` (chỉ đọc được) |

---

## PHẦN C — 3 bài viết code: điểm mấu chốt để tự chấm

### C1 — Shape
Phải có: `interface Shape` với 2 method; 2 class implement; method `sortedByArea` **trả list mới** (không sort in-place list gốc) dùng `Comparator.comparingDouble(Shape::area)`; `main` in đúng thứ tự (circle 2 → 12.566…, rectangle 12 → 12.0).
**Điểm quyết định:** `Circle` trước `Rectangle` vì 12.566 > 12.
**Trả lời "vì sao interface":** hai class không chia sẻ *trạng thái* hay *hành vi chung* nào ngoài hợp đồng `area/name`; interface cho phép đa kế thừa kiểu và không ràng buộc cây phân cấp. Abstract class chỉ hợp lý nếu có code dùng chung hoặc field chung.

### C2 — Employee streams
```java
Map<String, Double> avg = es.stream()
    .collect(Collectors.groupingBy(Employee::dept,
             Collectors.averagingDouble(Employee::salary)));

Map<String, Employee> top = es.stream()
    .collect(Collectors.groupingBy(Employee::dept,
             Collectors.collectingAndThen(
                Collectors.maxBy(Comparator.comparingDouble(Employee::salary)),
                Optional::orElseThrow)));   // hoặc dùng toMap + BinaryOperator.maxBy

List<String> names = es.stream()
    .sorted(Comparator.comparingDouble(Employee::salary).reversed())
    .map(Employee::name).toList();
```
**Câu hỏi "2 người cùng lương cao nhất thì sao":** `maxBy` trả **một** phần tử (phần tử đầu gặp theo thứ tự stream) → kết quả *không xác định* nếu list chưa sắp; muốn tất định phải thêm tie-breaker (ví dụ theo `name`). Đây chính là loại câu hỏi interviewer hay hỏi để kiểm tra em có nghĩ tới tính xác định không.

### C3 — WordCount + SafeCounter
Điểm mấu chốt:
- `EmptyFileException extends Exception` (checked) → phải khai báo `throws`.
- try-with-resources: `try (var reader = Files.newBufferedReader(p, StandardCharsets.UTF_8))`.
- Đếm: `Pattern.compile("[^a-zA-Z0-9]+")` để tách, `toLowerCase(Locale.ROOT)`, bỏ token rỗng, `map.merge(w, 1, Integer::sum)`.
- `SafeCounter`: `AtomicLong` + `incrementAndGet()`; **hoặc** `synchronized` + `long`. Giải thích: `count++` không nguyên tử; `AtomicLong` dùng CAS nên nhanh hơn lock khi tranh chấp thấp; `LongAdder` tốt hơn khi tranh chấp cao và chỉ cần đọc cuối.

---

## PHẦN D — SQL

```sql
-- Q1
SELECT c.id, c.name, COUNT(o.id) AS order_count
FROM customers c LEFT JOIN orders o ON o.customer_id = c.id
WHERE c.city = 'Hồ Chí Minh'
GROUP BY c.id, c.name
ORDER BY order_count DESC;

-- Q2
SELECT cat.name AS category_name, SUM(oi.quantity * oi.unit_price) AS revenue
FROM order_items oi
JOIN orders o   ON o.id = oi.order_id AND o.status = 'paid'
JOIN products p ON p.id = oi.product_id
JOIN categories cat ON cat.id = p.category_id
GROUP BY cat.name ORDER BY revenue DESC;

-- Q3
SELECT p.name AS product_name, SUM(oi.quantity) AS total_quantity
FROM order_items oi
JOIN orders o   ON o.id = oi.order_id AND o.status = 'paid'
JOIN products p ON p.id = oi.product_id
GROUP BY p.id, p.name ORDER BY total_quantity DESC LIMIT 5;

-- Q4 (hai cách)
SELECT c.* FROM customers c
WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);
SELECT c.* FROM customers c LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL;

-- Q5 (doanh thu theo tháng; nếu muốn "trung bình", bọc thêm AVG bên ngoài)
SELECT to_char(date_trunc('month', o.created_at), 'YYYY-MM') AS month,
       SUM(oi.quantity * oi.unit_price) AS revenue
FROM orders o JOIN order_items oi ON oi.order_id = o.id
WHERE o.status = 'paid' AND o.created_at >= '2026-01-01' AND o.created_at < '2027-01-01'
GROUP BY 1 ORDER BY 1;

-- Q6
SELECT p.id, p.name FROM products p
WHERE NOT EXISTS (SELECT 1 FROM order_items oi WHERE oi.product_id = p.id);

-- Q7 (window function)
SELECT DISTINCT c.id, c.name,
       MAX(o.created_at) OVER (PARTITION BY c.id) AS last_order_at,
       COUNT(o.id)       OVER (PARTITION BY c.id) AS order_count
FROM customers c LEFT JOIN orders o ON o.customer_id = c.id;

-- Q8
SELECT d.day, d.daily_revenue,
       SUM(d.daily_revenue) OVER (ORDER BY d.day) AS running_total
FROM (
  SELECT date_trunc('day', o.created_at)::date AS day,
         SUM(oi.quantity * oi.unit_price) AS daily_revenue
  FROM orders o JOIN order_items oi ON oi.order_id = o.id
  WHERE o.status = 'paid' AND o.created_at >= '2026-10-01' AND o.created_at < '2026-11-01'
  GROUP BY 1
) d ORDER BY d.day;

-- Q9
WITH spend AS (
  SELECT o.customer_id, SUM(oi.quantity * oi.unit_price) AS total_spent
  FROM orders o JOIN order_items oi ON oi.order_id = o.id
  WHERE o.status = 'paid' GROUP BY o.customer_id
)
SELECT c.name, s.total_spent FROM spend s JOIN customers c ON c.id = s.customer_id
WHERE s.total_spent > 2 * (SELECT AVG(total_spent) FROM spend);
```

**Q10:**
a) `CREATE INDEX idx_orders_status_created ON orders (status, created_at DESC);`
Lý do: `status` là điều kiện **bằng**, `created_at` là điều kiện **sắp xếp** → index nhiều cột cho phép lấy dữ liệu **đã đúng thứ tự**, `LIMIT 20` dừng sớm, không cần sort.
b) Trước: `Seq Scan on orders` + `Sort` (+ `Limit`). Sau: `Index Scan using idx_orders_status_created` (hoặc `Bitmap Heap Scan` nếu planner thấy đọc nhiều dòng hơn) và **mất bước Sort**.
c) `SELECT *` kéo 40 cột → nhiều I/O hơn, không dùng được index-only scan, tốn băng thông; chỉ chọn cột cần.
d) **Không hiệu quả** với index chỉ trên `status`: 3 giá trị → mỗi giá trị ~1/3 bảng, đọc 1/3 bảng thì planner thích `Seq Scan` hơn. Nhưng index ghép `(status, created_at DESC)` vẫn hữu ích vì nó giải quyết cả **lọc** và **sắp xếp** + `LIMIT` nhỏ.

---

## PHẦN DSA — hướng giải & độ phức tạp

| Bài | Pattern | Cách làm | Thời gian / bộ nhớ |
|---|---|---|---|
| 1 Two Sum | Hash map | Lưu `value → index`, mỗi bước tìm `target - nums[i]` | O(n) / O(n) |
| 2 Valid Parentheses | Stack | Gặp mở → push; gặp đóng → pop và so cặp; cuối cùng stack phải rỗng | O(n) / O(n) |
| 3 Group Anagrams | Hash theo key chuẩn hoá | key = mảng 26 tần số (hoặc chuỗi đã sort) | O(n·k) / O(n·k) |
| 4 Buy/Sell Stock | Greedy 1 lượt | giữ `minPrice`, cập nhật `maxProfit` | O(n) / O(1) |
| 5 Longest Substring | Sliding window + map vị trí | mở rộng `right`, khi trùng thì nhảy `left` | O(n) / O(k) |
| 6 Reverse List | Con trỏ 3 biến | `prev/curr/next`; đệ quy thì dùng call stack | O(n) / O(1) (lặp) |
| 7 Level Order | BFS + Queue | mỗi vòng lặp theo `size = queue.size()` để tách tầng | O(n) / O(n) |
| 8 Islands | DFS/BFS + đánh dấu | duyệt lưới, gặp `'1'` → flood fill, tăng đếm | O(m·n) / O(m·n) (DFS đệ quy có thể tràn stack với lưới lớn) |
| 9 Climbing Stairs | DP / Fibonacci | `dp[i] = dp[i-1] + dp[i-2]`, tối ưu còn 2 biến | O(n) / O(1) |
| 10 Top K Frequent | Heap hoặc bucket | đếm tần số → min-heap size k (O(n log k)) hoặc bucket theo tần số (O(n)) | O(n log k) / O(n) |

**Tự đánh giá thật lòng:** nếu bài 5 và 8 phải "mò" > 10 phút → đó là 2 pattern cần luyện trước (sliding window, grid traversal).

---

## PHẦN E — SPRING / JPA / SECURITY

**A1.** IoC = container tạo và nối object thay vì code tự `new`; DI = cách cung cấp dependency từ ngoài (constructor/setter/field) — DI là **cơ chế**, IoC là **nguyên lý**.
**A2.** `@Component` trên class, được component-scan tìm thấy. `@Bean` trên method trong `@Configuration`, dùng khi class **không sửa được** (thư viện ngoài) hoặc cần cấu hình động/nhiều biến thể.
**A3.** `@SpringBootConfiguration` (=`@Configuration`), `@EnableAutoConfiguration`, `@ComponentScan`.
**A4.** Dependency hiện rõ ở chữ ký; field `final` → bất biến; test không cần reflection; thiếu bean thì **fail lúc khởi động** thay vì NPE lúc chạy; không che giấu vòng phụ thuộc.
**A5.** `singleton` (mặc định). Khác: `prototype` (mỗi lần lấy 1 instance), `request`, `session` (web), `application`, `websocket`.
**A6.** `REQUIRED`. Mặc định rollback với `RuntimeException` và `Error`; **không** rollback với checked exception (trừ khi `rollbackFor`). Cũng không rollback nếu exception bị catch bên trong.
**A7.** 1 query lấy N parent + N query cho association → N+1. Sửa: `JOIN FETCH`, `@EntityGraph`, `@BatchSize`/`hibernate.default_batch_fetch_size`, DTO projection, hoặc fetch 2 bước theo danh sách id.
**A8.** Truy cập proxy lazy sau khi `EntityManager`/session đã đóng (ngoài transaction, thường ở tầng view/serialization).
**A9.** `@RestController` = `@Controller` + `@ResponseBody`: giá trị trả về được serialize (JSON) thay vì resolve view.
**A10.** `@PathVariable` = đoạn trong URL (`/users/{id}`); `@RequestParam` = query string/form (`?page=2`); `@RequestBody` = deserialize body (JSON → object).
**A11.** `@RestControllerAdvice` (hoặc `@ControllerAdvice`) + `@ExceptionHandler`.
**A12.** `@Valid` trên `@RequestBody` + annotation `jakarta.validation` (`@NotNull`, `@Email`, `@Size`); bắt `MethodArgumentNotValidException` trong advice, trả `{field, message}` có cấu trúc + 400.
**A13.** `SecurityFilterChain` là bean mô tả chuỗi filter + rule phân quyền. `WebSecurityConfigurerAdapter` bị bỏ vì kế thừa cứng nhắc, khó có nhiều chain; cấu hình theo component rõ ràng hơn.
**A14.** (1) `POST /auth/login` với username/password → (2) `AuthenticationManager` + `UserDetailsService` + `PasswordEncoder` kiểm tra → (3) sinh JWT đã ký (claims: `sub`, roles, `exp`) → (4) client gửi `Authorization: Bearer <token>` → (5) filter kiểm tra chữ ký + hạn, đặt `Authentication` vào `SecurityContext`; phân quyền theo role.
**A15.** BCrypt là hash **chậm, có salt, adaptive** (cost factor) → chống brute-force/rainbow table. MD5/SHA-256 trần quá nhanh và không salt → hash trùng nhau, dễ tra bảng.
**A16.** CORS = cơ chế trình duyệt chặn request cross-origin (khác scheme/host/port) trừ khi server cho phép qua header; preflight `OPTIONS`. Cấu hình: `CorsConfigurationSource` bean + `http.cors()` (hoặc `WebMvcConfigurer.addCorsMappings`).
**A17.** `@Profile("dev")` chỉ tạo bean khi profile active; `application-dev.yml` được nạp chồng lên `application.yml`.
**A18.** Actuator: health, metrics, info, mappings, env, beans, heapdump. Cảnh báo: `env`/`heapdump`/`beans` lộ thông tin và bí mật → chỉ `expose` `health,info`, đặt sau auth, hoặc dùng port quản trị riêng.
**A19.** `@SpringBootTest` = full context (chậm); `@WebMvcTest` = slice controller (MockMvc, không DB); `@DataJpaTest` = slice repository, transaction rollback, DB nhúng. Testcontainers = chạy **DB thật** (Postgres) trong Docker cho integration test thực tế hơn H2.
**A20.** Java **17** tối thiểu; chuyển sang namespace **`jakarta.*`** (thay `javax.*`).

**S1.** (a) 1 query `findAll()` + mỗi lần `o.getItems().size()` khởi tạo lazy collection → 50 query nữa = 51.
(b) `@Query("select distinct o from Order o join fetch o.items")`.
(c) `@EntityGraph(attributePaths = "items")` trên method repository.
(d) `JOIN FETCH` + `Pageable` → Hibernate cảnh báo `HHH000104: firstResult/maxResults specified with collection fetch; applying in memory` (phân trang trong bộ nhớ) và có thể nhân bản dòng.
(e) Dùng `@BatchSize(size = 50)` (hoặc `hibernate.default_batch_fetch_size`) để gom theo lô; hoặc query 2 bước: lấy id theo trang rồi lấy items theo `IN (...)`.

**S2.** (a) Vì lời gọi `doTransfer(...)` là **gọi nội bộ** (`this.doTransfer`), không đi qua proxy nên không có transaction advice.
(b) Spring AOP dùng **proxy**: chỉ lời gọi từ bên ngoài vào bean mới qua proxy.
(c) Cách 1: tách `doTransfer` sang bean khác và inject. Cách 2: dùng `TransactionTemplate`. (Cách 3: `AopContext.currentProxy()` — hoạt động nhưng xấu.)
(d) **Không** rollback với checked exception mặc định → phải `@Transactional(rollbackFor = Exception.class)`.

**S3.** (a)
```java
@Bean
SecurityFilterChain chain(HttpSecurity http, JwtAuthFilter jwtFilter) throws Exception {
    http.csrf(c -> c.disable())
        .sessionManagement(s -> s.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
        .authorizeHttpRequests(a -> a
            .requestMatchers("/auth/login").permitAll()
            .anyRequest().authenticated())
        .addFilterBefore(jwtFilter, UsernamePasswordAuthenticationFilter.class);
    return http.build();
}
```
(b) **Trước** `UsernamePasswordAuthenticationFilter` (vì ta tự xác thực bằng token, không dùng form login).
(c) **401** = chưa xác thực / token thiếu-hoặc-sai; **403** = đã xác thực nhưng thiếu quyền.
(d) `localStorage` tiện nhưng **XSS đọc được**; an toàn hơn: httpOnly + Secure + SameSite cookie, hoặc giữ trong memory.
(e) JWT stateless nên **không thu hồi trực tiếp** được: dùng TTL ngắn + refresh token, hoặc denylist theo `jti` trong Redis, hoặc `tokenVersion` lưu ở user.

---

## PHẦN F — THỰC HÀNH

1. GET/HEAD/OPTIONS = safe + idempotent; PUT/DELETE = idempotent (không safe); POST = không idempotent; PATCH = thường không idempotent.
2. 401 chưa xác thực; 403 đã xác thực nhưng bị cấm; 404 không tồn tại; 410 đã từng tồn tại và bị xoá vĩnh viễn; 422 body đúng cú pháp nhưng sai ngữ nghĩa (thiếu field bắt buộc) — 400 dùng khi request malformed.
3. `PUT /users/1` body đầy đủ (thay toàn bộ); `PATCH /users/1` body chỉ field thay đổi.
4. `GET /users/{id}/orders` · `GET /orders/{id}` · `POST /orders/{id}/cancel` · `GET /products?sort=best_selling&limit=3`.
5. `PUT` client biết id, gọi lại nhiều lần cho cùng kết quả; `POST` server sinh id, gọi lại tạo bản ghi mới (trừ khi có idempotency key).
6. `Content-Type`, `Authorization`, `Cache-Control`/`ETag`, `X-Request-Id`.
7. merge giữ lịch sử + tạo merge commit; rebase **viết lại** commit lên base mới → tuyến tính. Không rebase branch **đã chia sẻ/đã push** cho người khác.
8. revert tạo commit mới đảo ngược (an toàn, giữ lịch sử); `reset --hard` dời con trỏ và **xoá** thay đổi → chỉ dùng trên branch riêng/chưa push.
9. fetch tải về không merge; pull = fetch + merge; `pull --rebase` = fetch + rebase.
10. `git rebase -i HEAD~2` → `squash`; an toàn khi branch là của em và chưa có người khác dựa vào; sau đó `push --force-with-lease`.
11. (a) `find /var -name "*.log" -mtime -1`　(b) `grep -rn "TODO" --include="*.java" .`　(c) `tail -n 50 app.log` rồi `tail -f app.log`.
12. `644` = owner `rw-`, group `r--`, other `r--`; `755` = `rwx r-x r-x`. Script cần bit `x` để chạy trực tiếp.
13. `ps aux | grep java` (hoặc `jps -l`) → `ss -lntp | grep <pid>` (hoặc `lsof -p <pid>`) → `tail -n 20 <logfile>` (hoặc `journalctl -u <service> -n 20`).
14. Image = khuôn mẫu bất biến; container = instance đang chạy. Dockerfile build **một** image; compose mô tả **nhiều** service + network + volume. Dùng compose khi có ≥ 2 service (app + DB) hoặc cần cấu hình lặp lại.
15.
```dockerfile
FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn -q dependency:go-offline
COPY src ./src
RUN mvn -q package -DskipTests

FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
ENTRYPOINT ["java","-jar","app.jar"]
```
Nhỏ hơn vì image cuối **không chứa Maven, JDK, source, ~/.m2**. Compose: `ports: ["8080:8080"]`, `volumes: ["./data:/app/data"]`, `depends_on: [db]`.

## PHẦN S4 — Spring Boot 3 → 4 (đọc code cũ)

**(a) `javax.persistence` → `jakarta.persistence`.** Từ Spring Boot 3.0, Spring chuyển sang **Jakarta EE 9+**: toàn bộ namespace `javax.*` của Java EE đổi thành `jakarta.*`. Boot 4 dùng **Jakarta EE 11** (JPA 3.2, Servlet 6.1, Validation 3.1). Sửa: đổi import, và đổi dependency (`jakarta.persistence-api`). Lưu ý: `javax.sql`, `javax.crypto`, `javax.net` là của **JDK**, **không** đổi — đây là chỗ hay sửa nhầm.

**(b) `SecurityFilterChain` bean.** `WebSecurityConfigurerAdapter` bị bỏ từ Boot 3.0. Viết:
```java
@Bean
SecurityFilterChain chain(HttpSecurity http) throws Exception {
    return http
        .csrf(csrf -> csrf.disable())
        .authorizeHttpRequests(a -> a
            .requestMatchers("/auth/**").permitAll()
            .anyRequest().authenticated())
        .sessionManagement(s -> s.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
        .addFilterBefore(jwtFilter, UsernamePasswordAuthenticationFilter.class)
        .build();
}
```
Điểm cần nói được: cấu hình bằng **bean** (không kế thừa), và API dùng **lambda DSL** (method chaining kiểu cũ đã deprecate).

**(c) Jackson 3: `tools.jackson.*`.** Package gốc đổi từ `com.fasterxml.jackson` sang `tools.jackson`; `ObjectMapper` chuyển sang builder (`JsonMapper.builder()`). Custom serializer phải **đổi import** và đổi kiểu generic (`JsonSerializer<T>` cùng tên nhưng khác package) — nếu chỉ copy code cũ, lỗi biên dịch sẽ chỉ ra ngay.

**(d) `RestClient`.** Từ 4.2, `RestTemplate` bị deprecate để chuyển sang **`RestClient`** (API fluent, đồng bộ, dùng chung hạ tầng message converter với `WebClient`). Câu trả lời đủ tốt: "`RestTemplate` vẫn chạy nhưng không còn được khuyến nghị; dự án mới nên dùng `RestClient`, còn reactive thì `WebClient`."

**Chấm:** 1 điểm/câu, cần ≥ 3/4 để coi là "đọc được code cũ". Sai (a) hoặc (b) là lỗi nặng vì sẽ gặp ở mọi dự án cũ.

---

## Cách dùng điểm số

| Nhóm | Điểm của em | L | Việc tiếp theo |
|---|---|---|---|
| Java A+B | __/50 | | |
| Java C | __/3 bài | | |
| SQL | __/10 | | |
| DSA | __/10 | | |
| Spring | __/23 | | |
| Thực hành | __/15 | | |
| Bảo vệ dự án | __/15, __/13, __/13, __/13 | | |

Ghi vào `01_skills_matrix.csv` rồi quay lại Phase 1.1 để cập nhật ma trận — **đây là lần cập nhật duy nhất có giá trị**, phần còn lại chỉ là ước lượng.
