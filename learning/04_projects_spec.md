# Phase 4.4 — Hai dự án phải tự viết (thay chỗ `nexus` để lại)

**Vì sao có file này:** CV hiện **0 dòng Spring Boot**. Vậy phải có **dự án do Hoàn tự viết** — không phải để "cho đẹp CV", mà để có thứ **bảo vệ được 2 phút** và trả lời được câu hỏi xoáy.

> **Cập nhật 20/11/2026 (Hoàn đổi quyết định):** `nexus` sẽ trở thành **dự án chính trên CV** sau khi hoàn thành và học qua 6 cổng — xem `05_how_to_learn.md`. Hệ quả cho file này:
> - **TaskFlow** rút xuống **W5–W8** (thay vì W5–W10), mục tiêu là **có code tự viết** và học N+1/transaction/security — không cần đẹp hơn nữa.
> - **MiniWallet** giữ nguyên W15–W16 nhưng **hạ ưu tiên**: nếu G6 của `nexus` đang dở thì làm MiniWallet sau.
> - `nexus` **không** thay thế được yêu cầu "tự viết": nếu không qua G6, CV vẫn dùng TaskFlow.

**Luật chung cho cả hai dự án (không thương lượng):**
1. **Không AI viết code.** Được dùng AI để *hỏi khái niệm* ("transaction propagation là gì"), **không** để sinh code dán vào.
2. **Commit nhỏ, hằng ngày**, message nói **mình hiểu gì** (không phải "update code").
3. **Mỗi dự án phải có:** README chạy được trong 3', `docker compose up`, test xanh từ máy sạch, và **1 video 3' tự demo**.
4. **Không làm frontend** (trừ 1 trang HTML tĩnh để chụp ảnh nếu muốn). Đây là dự án backend.
5. **Cấm** copy nguyên project mẫu trên mạng rồi đổi tên. Người phỏng vấn đã thấy hàng trăm bản "clone todo list + JWT".

---

## **TaskFlow** — dự án 1: hệ thống quản lý công việc nhóm (W5–W10)

### Vì sao chọn đề này
Nó chạm đúng 6 thứ mà tin tuyển Java fresher hay ghi: **CRUD + quan hệ dữ liệu + phân quyền theo chủ sở hữu + tìm kiếm/lọc + phân trang + test**. Không cần hạ tầng phức tạp, nhưng đủ chỗ để thể hiện chiều sâu (N+1, authorization, transaction).

### Phạm vi (giữ nhỏ — đây là điểm hay bị làm hỏng)
| Có | Không |
|---|---|
| Đăng ký/đăng nhập JWT, 2 role: `ADMIN`, `MEMBER` | Refresh token xoay vòng phức tạp, OAuth2 |
| Workspace → Project → Task (3 tầng quan hệ) | Chat realtime, notification push |
| Task: title, description, status (TODO/DOING/DONE), priority, dueDate, assignee | Kanban kéo thả, file đính kèm, upload ảnh |
| Comment trên task | Mention, emoji reaction |
| Lọc + tìm kiếm + phân trang + sắp xếp | Full-text search (Elasticsearch) |
| Audit log đơn giản (ai đổi gì, khi nào) | Event sourcing |
| Test: unit + `@WebMvcTest` + `@DataJpaTest` + integration Testcontainers | Coverage 100% (mục tiêu 70% tầng service) |

### Mô hình dữ liệu (tối thiểu)
```
users(id, email UNIQUE, password_hash, display_name, role, created_at)
workspaces(id, name, owner_id → users.id, created_at)
workspace_members(workspace_id, user_id, role_in_ws)      -- PK ghép
projects(id, workspace_id → workspaces.id, name, description, created_at)
tasks(id, project_id → projects.id, title, description, status, priority,
      due_date, assignee_id → users.id NULL, created_by, created_at, updated_at,
      version)                                             -- version: @Version (optimistic lock)
comments(id, task_id → tasks.id, author_id → users.id, body, created_at)
audit_logs(id, actor_id, entity_type, entity_id, action, payload_json, created_at)
```
> **Ghi chú thiết kế phải giải thích được:** vì sao `workspace_members` là bảng nối có PK ghép; vì sao `tasks.version` tồn tại (2 người sửa cùng lúc); vì sao `audit_logs` không có FK chặt (log phải sống kể cả khi entity bị xoá).

### API (14 endpoint — đủ, không tham)
| Method | Path | Ghi chú điều kiện |
|---|---|---|
| POST | `/api/auth/register` | hash BCrypt; email trùng → 409 |
| POST | `/api/auth/login` | trả JWT (HS256), hết hạn 60' |
| GET | `/api/me` | từ token, **không** nhận userId từ client |
| POST | `/api/workspaces` | người tạo thành OWNER |
| GET | `/api/workspaces` | chỉ workspace mình là member |
| POST | `/api/workspaces/{id}/members` | chỉ OWNER; thêm member theo email |
| POST | `/api/workspaces/{id}/projects` | phải là member |
| GET | `/api/projects/{id}/tasks` | **lọc** `status`, `assigneeId`, `q`; **phân trang** `page,size,sort` |
| POST | `/api/projects/{id}/tasks` | validate title 3–100, dueDate không ở quá khứ |
| PATCH | `/api/tasks/{id}` | chỉ assignee/creator/OWNER; có `If-Match` hoặc `version` |
| DELETE | `/api/tasks/{id}` | chỉ creator hoặc ADMIN |
| POST | `/api/tasks/{id}/comments` | phải là member của workspace chứa task |
| GET | `/api/tasks/{id}/comments` | sắp xếp theo thời gian |
| GET | `/api/tasks/{id}/audit` | chỉ ADMIN |

**Điều kiện bảo mật bắt buộc (đây là chỗ phân biệt người hiểu và người copy code):**
- Mọi query phải lọc theo `user.sub` từ token — **không bao giờ** tin `userId` trong body/param.
- Truy cập task của workspace khác → **404** (không phải 403 — không tiết lộ sự tồn tại).
- Test phải có 1 case: user A gọi API của user B → 404.

### Tiêu chí nghiệm thu (đo được)
| # | Tiêu chí | Cách kiểm |
|---|---|---|
| P1.1 | `docker compose up` từ máy sạch → app + Postgres chạy, `/actuator/health` = UP | Máy khác hoặc `down -v` rồi `up` |
| P1.2 | `mvn test` xanh, không cần DB cài sẵn | Testcontainers tự bật Postgres |
| P1.3 | Coverage tầng service ≥ 70% | JaCoCo report trong CI |
| P1.4 | Không có N+1 ở `GET /tasks` | Bật `spring.jpa.show-sql`, đếm số câu SQL (mục tiêu ≤ 3 cho 1 trang 20 task) |
| P1.5 | Cross-user access trả 404 | Test tích hợp |
| P1.6 | README: mục tiêu, sơ đồ, cách chạy, 3 quyết định thiết kế + lý do | Đọc 3' là chạy được |
| P1.7 | Video 3' tự demo + tự giải thích | Không đọc script |

### Bài nói 2 phút (thuộc lòng ý, không thuộc lòng chữ)
> "TaskFlow là hệ thống quản lý công việc nhóm em tự viết bằng Spring Boot 4.2 và PostgreSQL. Có 3 tầng dữ liệu workspace–project–task nên em phải xử lý phân quyền theo quan hệ: một người chỉ thấy task thuộc workspace mình là thành viên — em làm việc đó ở tầng service, không ở controller, và trả 404 thay vì 403 để không lộ dữ liệu.
> Chỗ khó nhất là **N+1**: khi lấy danh sách task kèm assignee, Hibernate bắn một câu cho mỗi task. Em phát hiện bằng cách bật log SQL, sửa bằng `JOIN FETCH` trong repository, số câu giảm từ 21 xuống 1 sau khi phân trang.
> Phần thứ hai là **concurrency**: hai người sửa cùng task. Em dùng `@Version` optimistic lock để bản ghi cũ bị từ chối bằng 409 thay vì ghi đè.
> Em viết test ba tầng: unit cho service, `@WebMvcTest` cho controller, và integration với Testcontainers cho repository — nên `mvn test` chạy được trên máy sạch chỉ cần Docker."

---

## **MiniWallet** — dự án 2: ví + sổ cái giao dịch (W15–W16, có thể kéo tới W18)

### Vì sao chọn đề này (và vì sao **không** chọn "clone Shopee/Tiki")
Đề thương mại điện tử dễ trôi thành 50 bảng CRUD không có chiều sâu. Ví + sổ cái buộc phải đối mặt với **đúng những câu hỏi khó nhất của backend**: tính nhất quán, khoá, idempotency, giao dịch. Đây là thứ khiến người phỏng vấn ngồi lại.

### Phạm vi
| Có | Không |
|---|---|
| User có 1 ví, số dư suy ra từ **sổ cái** (không lưu cứng `balance`) | Tích hợp cổng thanh toán thật |
| Nạp / rút / chuyển nội bộ | Ngoại tệ, tỷ giá |
| **Idempotency-Key** cho mọi giao dịch ghi tiền | Retry tự động phức tạp |
| Double-entry: mỗi giao dịch 2 dòng (nợ/có) | Kế toán đầy đủ |
| Khoá lạc quan + kiểm tra số dư trong cùng transaction | Distributed lock / Redis lock (chỉ **nói** là biết, không làm) |
| Sao kê có lọc theo thời gian + phân trang | Biểu đồ, export PDF |
| 1 endpoint thống kê tháng có **cache Redis** + đo trước/sau | Cache toàn hệ thống |

### Câu hỏi mà dự án này phải trả lời được
1. Vì sao **không** lưu `balance` mà tính từ ledger? (đối soát được, không lệch do bug)
2. Hai request chuyển tiền cùng lúc với cùng `Idempotency-Key` → chuyện gì xảy ra? (khoá UNIQUE trên key + trả lại kết quả cũ)
3. Chuyển 100k từ A sang B: nếu trừ A xong mà cộng B lỗi thì sao? (`@Transactional`, và vì sao phải cùng datasource)
4. Vì sao `SELECT ... FOR UPDATE`/optimistic lock ở đây, và đánh đổi là gì?
5. Vì sao cache số dư là **sai** nhưng cache thống kê tháng là **đúng**? (dữ liệu phải chính xác tức thời vs dữ liệu chấp nhận trễ)

### Tiêu chí nghiệm thu
| # | Tiêu chí | Cách kiểm |
|---|---|---|
| P2.1 | Test: 2 luồng chuyển tiền đồng thời không làm âm số dư | Test đa luồng, chạy 20 lần |
| P2.2 | Cùng `Idempotency-Key` gửi 2 lần → chỉ 1 giao dịch | Test tích hợp |
| P2.3 | Tổng nợ = tổng có sau 1.000 giao dịch ngẫu nhiên | Script sinh dữ liệu + truy vấn đối soát |
| P2.4 | `EXPLAIN ANALYZE` sao kê có index, có số trước/sau | `PERF_REPORT.md` |
| P2.5 | Cache thống kê: đo p95 trước/sau, nêu TTL và lúc invalidate | Số thật, không ước lượng |
| P2.6 | README + video 3' | Như P1.6/P1.7 |

---

## Thứ tự làm & mốc thời gian

| Tuần | Việc | Mốc |
|---|---|---|
| W5 | Viết spec 1 trang cho TaskFlow (đúng 14 endpoint ở trên, không thêm) | Spec xong trước khi code |
| W6–W10 | TaskFlow theo lộ trình `04_master_roadmap.md` | **Readiness #1** |
| W11–W14 | Học Redis/Kafka/observability **trên chính TaskFlow** (thêm, không làm lại) | Có số đo |
| W15–W16 | MiniWallet | **Readiness #2** |
| W21 | Nếu chưa có việc: thêm 1 tính năng **có test + đo** vào MiniWallet (ví dụ rate limit, hoặc outbox cho thông báo) | Không thêm dự án thứ 3 |

> **Cấm:** làm dự án thứ 3 trước khi có offer. Hai dự án sâu > năm dự án nông. Người phỏng vấn hỏi 15 phút về **một** dự án, không hỏi 3 phút về năm dự án.

---

## Cách "cứu" một phần `nexus` (tùy chọn, không bắt buộc)

Nếu muốn giữ kỹ năng đọc code lớn: chọn **đúng một lát cắt** của `nexus` (ví dụ: luồng gửi tin nhắn + hàng đợi), **đóng repo, không nhìn**, viết lại từ đầu bằng tay trong 3–4 giờ. Xong thì so sánh với bản AI. Được phép **nói** về những gì mình hiểu sau khi làm lại — **không** được nói "em viết dự án này".

Giá trị thật của việc này: nó dạy bạn **đọc code người khác/AI** — kỹ năng mà công việc thật cần hơn là tự viết từ số 0.

---

## Checkpoint Phase 4.4

- 2 dự án, phạm vi **cắt rõ ràng** (14 endpoint; 6 nhóm chức năng), mỗi dự án có tiêu chí nghiệm thu đo được và bài nói 2 phút.
- TaskFlow (rút gọn W5–W8) **vẫn cần**: nó là "code tay" chứng minh bạn tự viết được, và là lưới an toàn nếu `nexus` không qua G6.
- MiniWallet tạo chiều sâu về tính nhất quán — nhưng **sau** G6 của `nexus`.
- Cấm dự án thứ 3 trước khi có offer.

**Quyết định đề xuất:** TaskFlow là dự án **đưa vào CV**, MiniWallet là dự án **để nói trong phỏng vấn** (đưa vào CV dưới dạng 2 bullet ngắn).
**Vì sao:** CV 1 trang chỉ chứa được 2 dự án; TaskFlow khớp từ khoá tin tuyển (CRUD/Spring/JWT/test), MiniWallet tạo khác biệt khi hỏi sâu.
**Điều gì sẽ khiến tôi đổi ý:** nếu 10 JD mục tiêu đều nhắc "microservices/Kafka" → đổi MiniWallet thành dự án chính và thêm 1 service nhỏ tách riêng, thay vì làm dự án thứ ba.
