# Phase 4.3 — Thang đo "đã đủ để nộp chưa"

**Cập nhật lần cuối:** 21/11/2026

**Mục đích:** thay cảm giác "chắc mình ổn rồi" bằng **9 điều kiện đo được**. Mỗi điều kiện có cách kiểm tra cụ thể, không phải tự đánh giá.

**Cách dùng:** kiểm tra ở W4, W10 (**check #1**), W16 (**check #2**), W24. Ghi kết quả vào bảng cuối file. Không tự nâng điểm cho mình.

---

## A. Bốn điều kiện **bắt buộc** để nộp bất kỳ đâu

| # | Điều kiện | Cách kiểm tra (không tự đánh giá) | Đạt khi |
|---|---|---|---|
| **A1** | **Java core đủ để viết, không chỉ đọc** | Làm lại **T1** trong 90', không tài liệu, không AI; cộng thêm: viết từ trắng 1 lớp có OOP + generic method + stream `groupingBy` + `try-with-resources` trong 45' | T1 **≥ 80%** và bài code chạy đúng, biên dịch được |
| **A2** | **SQL làm được việc thật** | **T2 ≥ 8/10**; và đưa ra 1 truy vấn chậm, chạy `EXPLAIN ANALYZE`, thêm index, **đo** nhanh hơn bao nhiêu | Điểm ≥ 8 **và** giải thích được vì sao index đó giúp |
| **A3** | **Spring Boot dựng được từ trắng** | Trong **3 giờ, không AI, không copy project cũ**: tạo project mới có 1 entity + CRUD + validation + xử lý lỗi + 2 test (1 unit, 1 `@WebMvcTest`) | Chạy được `mvn test` xanh và gọi API bằng `curl` thành công |
| **A4** | **Có 1 dự án bảo vệ được 2 phút** | Tự bảo vệ **TaskFlow** (không mở code): vì sao chọn thiết kế đó, chỗ khó nhất, đã sửa thế nào, nếu làm lại sẽ đổi gì. Ghi âm, nghe lại | Trả lời được **8/10** câu trong `learning/01_diagnostic_tests/06_project_defense.md` cho dự án đó |

> **Nếu thiếu 1 trong A1–A4:** chưa nộp công ty mục tiêu. Vẫn được nộp "đơn luyện tập" (W8) — nhưng biết rõ mình đang lấy dữ liệu, không phải đang kỳ vọng đậu.

---

## B. Ba điều kiện để nộp **công ty mục tiêu**

| # | Điều kiện | Cách kiểm tra | Đạt khi |
|---|---|---|---|
| **B1** | **Testing thật, không phải test cho có** | Trong TaskFlow: coverage tầng service **≥ 70%**; có ít nhất 1 test tích hợp dùng **Testcontainers**; có 1 test chứng minh **rollback transaction** | `mvn test` xanh từ máy sạch (chỉ cần Docker), không cần DB cài sẵn |
| **B2** | **Chạy được như một hệ thống** | `docker compose down -v && docker compose up` trên máy khác/máy sạch → app + DB lên, API trả lời, health check OK | Không thao tác tay nào; README đọc 3' là chạy được |
| **B3** | **Tiếng Anh trả lời được, không cần dịch** | Tự giới thiệu 2' + trả lời 5 câu hành vi bằng tiếng Anh, ghi âm, không đọc giấy | Nghe lại: hiểu được, không dừng quá 3 giây/câu; **không cần hoàn hảo ngữ pháp**. *(Đã có IELTS 6.5 được Trường công nhận → không phải học lại chứng chỉ; chỉ luyện **nói** 15'/ngày từ W13)* |

## C. Hai điều kiện "nộp tốt" (không bắt buộc, nhưng tăng tỉ lệ gọi)

| # | Điều kiện | Đạt khi |
|---|---|---|
| **C1** | **DSA đủ cho vòng screening** | 40 bài tích luỹ; làm 1 bài **medium lạ** trong 25' có giải thích miệng |
| **C2** | **CV "may đo"** | Có 3 bản CV sửa theo 3 JD thật (đổi thứ tự bullet, đổi từ khoá khớp JD — **không** bịa) |

---

## Bảng ghi kết quả (điền tay)

| Điều kiện | W4 | W10 (#1) | W16 (#2) | W24 |
|---|---|---|---|---|
| A1 — T1 (%) | | | | |
| A2 — T2 (/10) | | | | |
| A3 — dựng CRUD 3h (đạt/không) | | | | |
| A4 — bảo vệ 2' (/10 câu) | | | | |
| B1 — coverage + Testcontainers | | | | |
| B2 — `compose up` máy sạch | | | | |
| B3 — English 2' + 5 câu | | | | |
| C1 — 40 bài DSA | | | | |
| C2 — 3 CV may đo | | | | |
| **Kết luận** | | | | |

---

## Cách đọc kết quả

| Tình trạng | Nghĩa là | Làm gì |
|---|---|---|
| **A đủ + B đủ** | Nộp công ty mục tiêu được | Nộp 10–15/tuần; tiếp tục C1/C2 |
| **A đủ, B thiếu 1** | Nộp được nhóm vừa, chưa nộp nhóm mục tiêu | Dồn 2 tuần vào đúng điều kiện B còn thiếu |
| **A thiếu A1 hoặc A3** | Vấn đề gốc là **Java/Spring**, không phải CV | Quay lại lộ trình tuần 1–5; **không** sửa CV tiếp (sửa CV không tạo ra kỹ năng) |
| **A đủ nhưng nộp 40 đơn < 5% phản hồi** | Vấn đề ở **CV/kênh nộp**, không ở kỹ năng | Viết lại CV theo `01_cv_linkedin_audit.md`; nhờ 2 người đọc; đổi kênh (referral, group, career page) |
| **Có phỏng vấn, rớt ở vòng kỹ thuật** | Vấn đề ở **độ sâu**, không ở bề rộng | Ghi lại câu bị hỏi, bù đúng chủ đề đó trong 3 ngày, rồi nộp tiếp |

---

## Checkpoint Phase 4.3

- 9 điều kiện, mỗi điều kiện có **bài kiểm tra cụ thể** — không có chỗ nào ghi "tự tin là được".
- **A3 (dựng CRUD 3 giờ không AI)** là điều kiện quan trọng nhất: nó là thứ phân biệt "đã học Spring" với "làm được Spring" — đúng vấn đề mà `nexus` đã che mất.
- B3 (tiếng Anh) là điều kiện **bắt buộc** vì 93,7% tin IT ở VN đòi tiếng Anh (S1, Phase 2).

**Quyết định đề xuất:** đặt **A3 là cổng chính** — không đạt A3 thì không nộp công ty mục tiêu, dù CV đẹp.
**Vì sao:** mọi vòng phỏng vấn Java fresher đều yêu cầu viết code nhỏ tại chỗ hoặc giải thích code; CV chỉ mua được buổi đầu.
**Điều gì sẽ khiến tôi đổi ý:** nếu 10 buổi phỏng vấn thật cho thấy họ **không** hỏi code tại chỗ mà chỉ hỏi khái niệm + dự án → hạ A3 xuống mức "giải thích được" và dồn giờ sang A4/B1.
