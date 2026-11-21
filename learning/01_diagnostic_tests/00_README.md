# BỘ BÀI TEST CHẨN ĐOÁN — HƯỚNG DẪN

**Mục đích:** biết chính xác Hoàn đang ở L nào, để lộ trình không dạy lại thứ đã biết và không bỏ qua lỗ hổng thật.
**Điều kiện làm bài (bắt buộc):** **closed-book · KHÔNG AI · KHÔNG Google · KHÔNG IDE gợi ý (tắt Copilot)**. Chỉ được dùng: giấy, bút, và với bài code thì một editor trống + docs đã in sẵn nếu ghi rõ "được dùng docs".

> Nếu làm bài trong điều kiện "mở", kết quả sẽ **cao hơn thực tế 1–2 bậc** và toàn bộ lộ trình Phase 4 sẽ sai. Đây là bài tự đánh giá, không ai chấm điểm hộ.

---

## 1. Cấu trúc & thời gian

| File | Nội dung | Số câu | Thời gian | Được dùng docs? |
|---|---|---|---|---|
| `01_java_core.md` | 30 trắc nghiệm + 10 đọc code + 3 bài viết code | 43 | **90 phút** | Không (phần code: chỉ Java API docs) |
| `02_sql.md` | 10 truy vấn trên 1 schema cho sẵn | 10 | **60 phút** | Không (được xem schema) |
| `03_dsa.md` | 10 bài easy–medium | 10 | **120 phút** (12 phút/bài) | Không |
| `04_spring_jpa_security.md` | 20 câu khái niệm + 3 tình huống | 23 | **60 phút** | Được docs.spring.io |
| `05_practical.md` | HTTP/REST/Git/Linux/Docker | 15 | **30 phút** | Không |
| `06_project_defense.md` | 10 câu/dự án, nói thành tiếng, ghi âm | 40 | **60 phút** | Không |

**Tổng: ~7 giờ.** Chia làm 3 buổi (không làm liền một hơi — kết quả sẽ tệ hơn thực lực).

Đáp án: `09_answer_key.md` — **chỉ mở sau khi đã nộp bài.** Tự chấm theo rubric dưới đây, rồi ghi vào `01_skills_matrix.csv` cột `level_now_estimate`.

---

## 2. Rubric chấm & bảng quy đổi sang L

Chấm theo **từng nhóm kỹ năng**, không chấm tổng. Mỗi nhóm ra một mức L.

| Nhóm | Bài tương ứng | Công thức |
|---|---|---|
| Java core | T1 phần A+B (40 câu) | ≥ 34/40 → L4 · 28–33 → L3 · 20–27 → L2 · 12–19 → L1 · < 12 → L0 |
| Java viết code | T1 phần C (3 bài) | cả 3 chạy đúng + giải thích được → L3+ · 2/3 → L2–L3 · 1/3 → L2 · 0/3 → L1 |
| SQL | T2 (10 câu) | 9–10 → L4 · 7–8 → L3 · 5–6 → L2 · 3–4 → L1 · ≤2 → L0 |
| DSA | T3 (10 bài) | 9–10 → L4 · 7–8 → L3 · 5–6 → L2 · 3–4 → L1 · ≤2 → L0 |
| Spring/JPA/Security | T4 (23 câu) | ≥ 19 → L4 · 16–18 → L3 · 11–15 → L2 · 6–10 → L1 · < 6 → L0 |
| Thực hành (HTTP/Git/Linux/Docker) | T5 (15 câu) | 13–15 → L4 · 10–12 → L3 · 7–9 → L2 · 4–6 → L1 |
| Bảo vệ dự án | T6 (40 câu, nói) | tự chấm: trả lời được ≥ 8/10 câu của 1 dự án mà không mở code → dự án đó "bảo vệ được" |

**Quy tắc cộng thêm:** bài nào làm **quá thời gian** thì hạ **1 bậc** (vì trong phỏng vấn có đồng hồ). Bài nào **đúng nhưng phải tra docs** ở phần "không được dùng docs" → tính là **sai**.

---

## 3. Lịch làm lại (đo tiến bộ)

| Lần | Khi nào | Ghi chú |
|---|---|---|
| #1 | **Tuần này** (Stage 0) | Baseline. Đừng sửa đáp án, đừng học trước. |
| #2 | **Sau 5–6 tuần** | Làm lại **cùng đề** để đo tiến bộ thật. |
| #3 | **Trước khi apply mạnh** (tuần 10–12) | Kỳ vọng: Java core L3+, SQL L3, Spring L2–L3 |
| #4 | **Trước mỗi đợt phỏng vấn** | Chỉ làm nhóm yếu |

Ghi kết quả vào `01_skills_matrix.csv` (cột `level_now_estimate`) + một dòng ngày để thấy đường đi lên.

---

## 4. Cách dùng kết quả (đừng bỏ qua bước này)

1. Nhóm nào **L0–L1** mà nằm trong 8 dòng ưu tiên của `01_skills_matrix.md` → phải học lại từ gốc, không nhảy cóc.
2. Nhóm nào **L2** → không cần học lý thuyết lại; cần **viết code** cho đến khi thành L3.
3. Nhóm nào **L3** → chỉ cần ôn theo chu kỳ (Phase 4.8), đừng tốn thời gian.
4. Nhóm nào **L4** → bỏ khỏi lộ trình, dùng làm "điểm tựa" khi phỏng vấn.

---

## 5. Mini-diagnostic 25 phút (nếu muốn nhanh hơn)

Nếu 7 giờ là quá nhiều cho tuần này, làm **bản rút gọn** này trước, rồi làm đủ sau:
- T1: câu 1–10 (trắc nghiệm) + 1 bài code (C2)
- T2: câu 1, 4, 7
- T3: bài 1, 5, 8
- T4: câu 1–8
- T6: 5 câu đầu của **Nexus**

Kết quả mini **không** thay được bản đầy đủ, nhưng đủ để tôi chỉnh Stage 1 của Phase 4 nếu cần.

---

## 6. Lưu ý về tính trung thực của bài test

Bài test này **không phải kỳ thi** — không ai thưởng điểm cao. Nếu Hoàn làm được 90% thì lộ trình là 4 tuần; nếu 30% thì là 16 tuần. Cả hai đều ổn. Con số **sai** mới là thứ gây hại: nó khiến Hoàn apply quá sớm (bị từ chối liên tục, mất tự tin) hoặc học lại quá lâu (chậm 3 tháng vô ích).
