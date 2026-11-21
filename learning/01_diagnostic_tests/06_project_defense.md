# T6 — "GIẢI THÍCH DỰ ÁN" (60 phút · nói thành tiếng · ghi âm)

**Đây là bài quan trọng nhất trong cả bộ test.** Không phải vì khó, mà vì nó phơi ra chính xác chỗ CV đang nói dối.
**Cách làm:** chọn 1 dự án → **không mở code** → bật ghi âm → trả lời 10 câu → nghe lại. Nếu câu nào phải "ờ... để em mở code xem" thì dự án đó **chưa bảo vệ được**.

**Quy tắc:** mỗi câu trả lời 60–90 giây. Không đọc CV. Không dùng từ mà mình không giải thích được.

---

## Bộ câu hỏi chung (áp cho mọi dự án)

1. Dự án làm gì, cho ai, giải quyết vấn đề gì? (60 giây, không dùng từ "platform", "scalable", "robust")
2. Kiến trúc tổng thể: có những thành phần nào, chúng nói chuyện với nhau thế nào?
3. Vì sao chọn stack đó? Nếu làm lại, em chọn gì khác và vì sao?
4. Mô tả **một luồng request cụ thể** từ đầu đến cuối (từ client → API → DB → trả về). Kể cả tên bảng/cột nếu nhớ.
5. Dữ liệu được mô hình hoá thế nào? Quan hệ khó nhất giữa các bảng là gì?
6. Xác thực/phân quyền hoạt động ra sao? Token đi qua những đâu?
7. Xử lý lỗi thế nào? Kể **một lỗi thật** đã gặp và cách sửa.
8. Test gì? Test nào **không** viết và vì sao? Nếu phải test phần khó nhất thì làm sao?
9. Deploy thế nào? Chạy ở đâu? Nếu traffic tăng 10× thì hỏng ở đâu trước?
10. **Em làm phần nào?** (câu này phải trả lời được **cụ thể đến mức file/class**, và nói được phần nào AI viết giúp.)

---

## 1. Nexus (Java — repo `hoanhophuoc/nexus`, push 17–18/11/2026) — ⛔ ĐÃ CÓ KẾT LUẬN

**Cập nhật 20/11/2026:** Hoàn xác nhận **AI viết 100%, bản thân không hiểu code**. → **Không đưa vào CV. Không cần làm phần này.**

Giữ lại phần câu hỏi dưới đây chỉ cho **một trường hợp duy nhất**: nếu Hoàn muốn "cứu" (`nexus` bằng cách **viết lại một lát cắt từ đầu bằng tay** — xem Phase 4.4). Khi đó, đây chính là 5 câu phải tự trả lời được *sau khi* viết lại:

- N1. "Outbox pattern" là gì, vì sao dùng nó thay vì ghi DB rồi gửi WebSocket luôn?
- N2. "Poison message" và "outage path" là gì?
- N3. "Per-class coverage floor" là gì? Vì sao đặt ngưỡng theo từng class?
- N4. WebSocket reconnect: client mất mạng rồi vào lại, đảm bảo không mất tin nhắn bằng cách nào?
- N5. `PLpgSQL` trong repo dùng để làm gì? Vì sao đặt logic ở DB?

**Không trả lời được N1 và N4 sau khi tự viết lại → xoá repo hoặc để private và bỏ hẳn khỏi hồ sơ.**

## 2. Chat-System (Java — 11–12/2024, nhóm 3, có commit của Hoàn + `NgocAnhDo26`)

10 câu chung + 3 câu riêng:
- C1. Hibernate mapping giữa User–Conversation–Message thế nào? Quan hệ nhiều-nhiều xử lý ra sao?
- C2. Socket ở đây là gì (TCP socket thô hay gì)? Làm sao server biết gửi tin cho đúng client?
- C3. Em làm phần nào trong nhóm này? (có commit `phuochoan` ngày 19/12/2024: "update online, offline")

## 3. IT-Tools (ASP.NET Core — dự án **mạnh nhất hiện có**)

10 câu chung + 3 câu riêng:
- I1. Vì sao JWT phù hợp ở đây hơn session? Token chứa gì, hết hạn bao lâu?
- I2. Ba vai trò User/Premium/Admin được kiểm tra ở đâu — controller, service, hay filter? Vì sao?
- I3. `EF Core LINQ projections` em dùng để làm gì (tránh load cột nào)?

## 4. Helios Platform (đồ án tốt nghiệp — **bài test khắc nghiệt nhất**)

Làm bài này **chỉ để biết mình có nên giữ nó trên CV hay không**. 10 câu chung + 3 câu riêng:
- H1. Kubernetes Operator là gì? "Reconcile loop" hoạt động thế nào?
- H2. CRD `HeliosApp` có những field nào, và Operator làm gì với chúng?
- H3. Vì sao GitOps (Argo CD) lại khác CI/CD truyền thống (Tekton)?

**Quy tắc quyết định:** trả lời được **≥ 6/13** → có thể giữ 1–2 bullet. Dưới 6 → **xoá khỏi CV** (đúng như khuyến nghị ở `01_cv_linkedin_audit.md`).

## 5. Learnix (NestJS)

10 câu chung. Nếu trả lời được ≥ 8/10 và mô tả rõ phần mình làm → có thể giữ 1 bullet "full-stack" (nhưng **không** dùng để ứng tuyển Java).

---

## Bảng ghi kết quả

| Dự án | Số câu trả lời được (không mở code) | Kết luận | Hành động |
|---|---|---|---|
| Nexus | — | **⛔ Xoá** (AI 100%, đã xác nhận) | Không làm T6 cho dự án này |
| Chat-System | __/13 | ☐ Giữ ☐ Sửa ☐ Xoá | **Ưu tiên làm trước** — đây là dự án Java duy nhất còn cứu được |
| IT-Tools | __/13 | ☐ Giữ ☐ Sửa ☐ Xoá | |
| Helios | __/13 | ☐ Giữ 1–2 bullet ☐ Xoá | |
| Learnix | __/10 | ☐ Giữ ☐ Xoá | |

**Sau khi làm xong:** cập nhật `01_honest_cv_v1.md` — điền các chỗ `[...]` hoặc xoá dự án tương ứng. Đây là lần duy nhất trong pack này tôi yêu cầu sửa CV dựa trên kết quả bài test, không dựa trên cảm giác.

**Thứ tự ưu tiên đã đổi:** Chat-System → IT-Tools → Learnix → (Helios: chỉ để biết có xoá hay không). `nexus` đã bị loại từ trước khi làm bài.
