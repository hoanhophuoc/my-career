# T5 — HTTP / REST / GIT / LINUX / DOCKER (30 phút · KHÔNG tra cứu)

15 câu. Viết câu trả lời ngắn (1–3 dòng/câu). Đây là nhóm kiến thức mà **ai cũng phải biết** — sai ở đây là mất điểm rẻ.

## HTTP & REST (1–6)

**1.** Kể 6 method HTTP và nói method nào **idempotent**, method nào **an toàn (safe)**.
**2.** Phân biệt 401 và 403. Phân biệt 404 và 410. Khi nào trả 422 thay vì 400?
**3.** `PUT` khác `PATCH` thế nào? Cho ví dụ body của mỗi loại cho resource `user`.
**4.** Đặt tên endpoint đúng chuẩn REST cho: lấy danh sách đơn của 1 user, lấy 1 đơn, huỷ 1 đơn, lấy 3 sản phẩm bán chạy.
**5.** Phân biệt `POST` tạo resource và `PUT` tạo resource (idempotency + ai sinh id).
**6.** Kể 4 header quan trọng khi thiết kế API (gợi ý: content type, auth, cache, request id) và tác dụng.

## Git (7–10)

**7.** `git merge` khác `git rebase` ở đâu về **lịch sử commit**? Khi nào **không nên** rebase?
**8.** `git revert` khác `git reset --hard` thế nào? Vì sao trên branch chung (main/shared) phải dùng `revert`?
**9.** `git fetch` khác `git pull` ở đâu? `git pull --rebase` làm gì?
**10.** Em có 2 commit đã push lên branch riêng của mình và muốn gộp thành 1. Làm thế nào, và điều kiện an toàn là gì?

## Linux (11–13)

**11.** Viết lệnh: (a) tìm file `.log` trong `/var` sửa trong 24h qua; (b) tìm trong tất cả file `.java` dòng chứa `TODO`; (c) xem 50 dòng cuối file và theo dõi file đó liên tục.
**12.** `chmod 644` và `755` nghĩa là gì (đọc theo owner/group/other)? Vì sao script phải có `+x`?
**13.** Process `java` đang chiếm 100% CPU. Viết chuỗi lệnh để: xem process, xem nó đang mở port nào, xem 20 dòng log cuối của nó.

## Docker (14–15)

**14.** Phân biệt image và container; Dockerfile và docker-compose. Khi nào dùng compose thay vì `docker run`?
**15.** Viết (ở mức khái niệm) một `Dockerfile` multi-stage cho Spring Boot: stage build dùng Maven/Gradle, stage runtime dùng JRE. Giải thích tại sao multi-stage làm image nhỏ hơn. Nêu cách map port và mount volume trong compose.

---
**Tự chấm:** đối chiếu `09_answer_key.md` phần E. Nhóm này nếu dưới 10/15 thì phải sửa **ngay trong tuần 1** — đây là loại câu hỏi "loại thẳng" ở vòng screening.
