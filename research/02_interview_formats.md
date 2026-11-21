# 02.6 — QUY TRÌNH & DẠNG BÀI TEST KHI TUYỂN FRESHER/JUNIOR JAVA

**Cập nhật lần cuối:** 21/11/2026

**Ngày:** 20/11/2026 · Dựa trên: S12 (CMC Fresher Techie), S18 (CareerLink), S19 (review CMC), S20 (Voz: TMA/FPT/công ty Hàn), P07/P08 (JD thật).
**Cảnh báo phương pháp:** phần lớn là **người ứng tuyển tự kể lại** → có thiên lệch (người đậu thì kể dễ, người trượt thì kể khó). Dùng để **biết dạng bài**, không dùng để **đo độ khó**.

---

## 1. Bốn kiểu quy trình gặp nhiều nhất

### Kiểu A — Outsourcing lớn (FPT, TMA, CMC, NashTech, KMS)
```
CV + bảng điểm  →  Entry test (trắc nghiệm + tự luận + ngoại ngữ)  →  Test coding / live coding  →  Phỏng vấn tech (có thể bằng tiếng Anh)  →  HR
```
- **CMC Global**: entry test gồm **ngoại ngữ (Listening/Reading)** + **chuyên môn trắc nghiệm & tự luận** (Programming, Database, IQ, Logic). **Miễn phần ngoại ngữ nếu có TOEIC 650+ hoặc IELTS 6.0+** `[Sự thật — S12, Tin cậy: Cao]`
- **CMC Fresher Techie**: phỏng vấn **hoàn toàn bằng tiếng Anh**, kèm **một bài live coding** `[Sự thật — S19, tự khai, TB]`
- **FPT Software fresher**: HR gọi báo **"bài test Java gồm 3 bài coding"** `[Sự thật — S20, tự khai, TB]`
- **TMA fresher**: nộp **CV tiếng Anh + bảng điểm**, GPA theo yêu cầu, **TOEIC ~650** `[Sự thật — S20, tự khai, TB]`

### Kiểu B — Product/fintech (VNG, MoMo, ZaloPay, ngân hàng)
```
CV  →  Online assessment (coding + trắc nghiệm)  →  1–2 vòng tech (DS&A nhẹ + Java/Spring + SQL)  →  vòng domain/product  →  HR
```
Ít review công khai hơn Kiểu A. Kỳ vọng: **tiếng Anh tốt hơn**, hỏi **sâu hơn về dự án cá nhân**.

### Kiểu C — Công ty Nhật/Hàn quy mô vừa
```
CV  →  Test IQ / logic (có khi 12–15 phút, 13 câu)  →  Phỏng vấn thái độ + vài câu tech dễ (Cookie, Session, MVC)  →  OJT 2 tháng
```
`[Sự thật — S20, một case cụ thể, TB]` → Nhấn mạnh **thái độ và tiếng Nhật/Hàn** hơn chiều sâu kỹ thuật.

### Kiểu D — Khách hàng quyết (outsourcing 2 vòng tech)
```
Vòng tech với team  →  Vòng tech với client  →  vào dự án
```
`[Sự thật — S19, CMC]` → Vòng client có thể hỏi **bài toán theo domain của khách**.

---

## 2. Bảng: vòng nào hỏi gì (tổng hợp)

| Vòng | Nội dung thực tế | Chuẩn bị gì |
|---|---|---|
| **CV screening** | GPA, trường, có bảng điểm, tiếng Anh | Bảng điểm + GPA 8.74 là lợi thế; **đừng để bằng cấp mâu thuẫn** (xem `01_graduation_checklist.md`) |
| **Entry test (trắc nghiệm)** | Java core, OOP, SQL, logic/IQ | Bộ `learning/01_diagnostic_tests/01_java_core.md` + `02_sql.md` chính là dạng này |
| **Test coding** | 3 bài mức easy–medium (FPT), hoặc live coding (CMC) | `learning/01_diagnostic_tests/03_dsa.md`; luyện **viết trên giấy/editor trống** |
| **Phỏng vấn tech** | Bám **theo CV và dự án gần nhất** (S19 ghi rõ: "câu hỏi thường bám theo dự án cũ") | Đây là lý do bài **T6 project defense** quan trọng nhất |
| **Phỏng vấn tiếng Anh** | Giới thiệu bản thân, mô tả dự án, giải thích lựa chọn kỹ thuật | Chuẩn bị **3 câu chuyện 90 giây** bằng tiếng Anh (xem `06_english_plan.md` ở Phase 6) |
| **HR** | Lương, thời gian, cam kết | Ba câu hỏi ở `02_entry_programs_2026_2027.md` mục 4 |

---

## 3. Câu hỏi kỹ thuật thực tế hay gặp ở fresher (tổng hợp từ S18, S19, S20)

**Java core / OOP** — xuất hiện ở **cả ba cấp** (S18):
- Abstract class khác interface thế nào?
- 4 tính chất OOP, cho ví dụ **trong code của em**
- Vì sao `String` immutable? (câu này hay bị hỏi tiếp "vì sao", không chỉ định nghĩa)
- `ArrayList` vs `HashMap` — khi nào dùng cái nào
- Override `equals` thì phải override `hashCode` — vì sao?
- `static` vs instance; `final`

**SQL** (S20 — interviewer thường hỏi fresher có ghi SQL trong CV):
- JOIN có mấy loại, khác nhau ở đâu (INNER/LEFT/RIGHT/FULL)
- `GROUP BY` dùng khi nào, `HAVING` khác `WHERE` ở đâu

**Spring / JPA** (S18: "xuất hiện nhiều từ cấp junior"):
- IoC/DI là gì, vì sao dùng
- `@Component` vs `@Bean`
- `@Transactional` rollback khi nào
- N+1 là gì

**Design pattern / SOLID** (S19: CMC hay hỏi)
- SOLID — giải thích 1 nguyên tắc em **đã dùng thật**

**Câu hành vi quan trọng nhất** (S18: "một lỗi production kể rõ ràng phân biệt junior với middle"):
- "Kể một lỗi em từng gặp và cách em sửa."

---

## 4. Dạng bài test theo công ty (những gì biết chắc)

| Công ty | Bài test | Nguồn | Độ tin cậy |
|---|---|---|---|
| CMC Global | Ngoại ngữ (L/R) + trắc nghiệm/tự luận (Programming, Database, IQ, Logic); live coding; phỏng vấn English | S12, S19 | Cao (trang chính thức) / TB (review) |
| FPT Software | 3 bài coding Java | S20 | TB (tự khai) |
| TMA Solutions | CV English + bảng điểm + TOEIC ~650 | S20 | TB |
| Công ty Hàn quy mô vừa | IQ 13 câu / 12 phút + vài câu tech dễ | S20 | Thấp (1 case) |
| Các công ty khác | **Chưa xác minh** | — | — |

---

## 5. "So what" cho Hoàn

1. **IELTS 6.5 của Hoàn đã đủ ngưỡng miễn test ngoại ngữ ở CMC (yêu cầu IELTS 6.0+/TOEIC 650+)** → đây là lợi thế **cụ thể, đo được**, nên ghi rõ trong CV và nêu ra khi HR hỏi.
2. **Bài test entry của CMC đúng dạng bộ test chẩn đoán của tôi** (Programming + Database + IQ/Logic) → làm tốt `learning/01_diagnostic_tests/` là chuẩn bị trực tiếp cho vòng này.
3. **Câu hỏi tech bám CV** → mọi dòng trên CV phải bảo vệ được. Đây là lý do phải sửa CV **trước** khi nộp.
4. **Phỏng vấn bằng tiếng Anh là chuyện thường** → Speaking 6.0 là **điểm chặn thật**, không phải điểm phụ. Phase 6 sẽ đặt speaking lên đầu.
5. **Không cần LeetCode hard.** Cần **viết code cơ bản trôi chảy dưới áp lực thời gian** (3 bài/90 phút).

---

## 6. Chưa biết

- Tỷ lệ công ty dùng take-home assignment (không có số liệu).
- Có bao nhiêu công ty yêu cầu **system design** ở cấp junior (review fresher không nhắc tới → nhiều khả năng rất ít).
- Nội dung chính xác bài test của VNG/MoMo/ZaloPay/ngân hàng (không có review đủ tin cậy trong phiên này).
