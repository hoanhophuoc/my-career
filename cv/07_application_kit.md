# Phase 7.2 — Bộ hồ sơ nộp đơn & hệ thống ứng tuyển

**Ngày:** 20/11/2026 · **Cập nhật lần cuối:** 21/11/2026 · **Mục tiêu:** mỗi đơn nộp ≤ **15 phút**, không viết lại CV từ đầu, không nộp tràn lan.

> **Cổng sự thật:** chỉ dùng **bản gửi đi** trong `07_cv_truth_checklist.md` (toàn dấu ✅). Mọi output của công cụ AI (`07_tools_evaluation.md`) phải qua cổng này trước khi gửi.

---

## 1. Nguyên tắc: 1 CV gốc + 3 slot may đo

Không có "CV riêng cho từng công ty" — đó là cách nộp 3 đơn rồi kiệt sức. Có **1 CV gốc** (`01_honest_cv_v1.md`) và chỉ đổi **3 chỗ**:

| Slot | Đổi gì | Thời gian |
|---|---|---|
| **S1 — MỤC TIÊU** (1 dòng) | Chèn đúng chức danh trong JD: "fresher backend Java" / "Java developer (fresher)" / "backend engineer intern" | 1 phút |
| **S2 — 3 dòng đầu KỸ NĂNG** | Đảo thứ tự để khớp 3 từ khoá đầu của JD (ví dụ JD nhấn SQL → SQL lên trước Java) | 2 phút |
| **S3 — thứ tự DỰ ÁN** | JD về Java → Chat-System (và nexus sau G6) lên trước; JD về .NET → IT-Tools lên trước | 2 phút |

Mọi thứ còn lại **giữ nguyên**. Nếu một JD đòi thứ bạn không có (Kafka, K8s, 2 năm KN) → **không sửa CV cho khớp**, chỉ nộp nếu ≥ 60% yêu cầu khớp.

## 2. Sáu kiểu JD và cách đổi 3 slot

| Kiểu JD | Dấu hiệu | S1 | S2 (3 từ đầu) | S3 |
|---|---|---|---|---|
| **Java backend sản phẩm** | Spring Boot, REST, PostgreSQL/MySQL, "fresher/junior" | Fresher Backend Developer (Java) | Java · SQL · REST APIs | nexus (sau G6) → Chat-System |
| **Outsourcing Nhật/Âu** | "tiếng Anh/Nhật", "theo dự án khách hàng", C#/Java/.NET | Software Engineer (Fresher) | Java · C# · SQL | IT-Tools → Chat-System |
| **Fintech / ngân hàng** | "transaction", "bảo mật", "tuân thủ", Java core nặng | Java Developer (Fresher) | Java · SQL · JWT/RBAC | Chat-System (transaction/history) → IT-Tools |
| **ERP / low-code / product nội bộ** | SQL nặng, báo cáo, "database" xuất hiện nhiều | Backend Developer (Fresher) | SQL · Java · PostgreSQL | Chat-System (schema) → IT-Tools |
| ~~QA / SDET~~ | **Đã bỏ (20/11/2026)** — Hoàn không làm tester; không có bộ CV cho kiểu JD này | — | — | — |
| **.NET (dự bị)** | ASP.NET Core, C#, EF Core | .NET Backend Developer (Fresher) | C# · SQL · ASP.NET Core | IT-Tools → Chat-System |

## 3. Xuất PDF — 8 quy tắc để ATS không nuốt CV

1. **1 trang**, 1 cột, không bảng, không icon, không ảnh.
2. Font 10–11pt (Calibri/Arial/Times), lề 1.5–2 cm.
3. Tên file: `HoPhuocHoan_BackendJava_Fresher.pdf` (có tên + vị trí; **không** `CV(1).pdf`).
4. Xuất **PDF có text** (từ Word/Google Docs), không scan, không ảnh chụp.
5. Tiêu đề mục bằng chữ thường in đậm: `HỌC VẤN`, `KỸ NĂNG` — không dùng text box, không header/footer chứa thông tin quan trọng.
6. Ngày tháng viết `09/2022 – 09/2026`, không "Present" mơ hồ.
7. **Không** ghi lương mong muốn, ngày sinh, CCCD, ảnh thẻ, tình trạng hôn nhân.
8. Tự mở PDF bằng trình đọc → bôi đen thử 1 dòng: nếu bôi đen được thì ATS đọc được.

## 4. Email / tin nhắn nộp đơn — 90 từ, 4 câu

**Tiêu đề:** `Ứng tuyển Fresher Backend Developer (Java) — Hồ Phước Hoan`

**Bản tiếng Việt (dán, chỉ đổi 2 chỗ trong ngoặc):**
```
Kính gửi anh/chị [Tên hoặc "Bộ phận Tuyển dụng"],

Tôi xin ứng tuyển vị trí [tên vị trí] tại [tên công ty]. Tôi tốt nghiệp loại Giỏi
ngành Kỹ thuật phần mềm (GPA 8.74/10), điểm CSDL 9.0 và Hệ điều hành 9.4.
Tôi đã xây dựng một REST API cá nhân bằng ASP.NET Core + EF Core + PostgreSQL
(xác thực JWT, phân quyền, unit test) và đang làm dự án Spring Boot viết tay.

Tôi quan tâm đến [1 câu cụ thể về công ty/sản phẩm — đọc website 2 phút] và muốn
học Spring Boot trong môi trường có code review.

CV đính kèm. Tôi sẵn sàng trao đổi bất kỳ lúc nào.

Trân trọng,
Hồ Phước Hoan · [điện thoại] · github.com/hoanhophuoc
```

**Bản tiếng Anh:**
```
Dear [Name / Hiring Team],

I would like to apply for the [position] at [company]. I graduated with a Very Good
degree in Software Engineering (GPA 8.74/10), with 9.0/10 in Database Systems and
9.4/10 in Operating Systems. I built a solo REST API in ASP.NET Core + EF Core +
PostgreSQL (JWT authentication, role-based access, unit tests) and am now writing
a Spring Boot project by hand.

I am particularly interested in [one specific sentence about the company], and I want
to grow my Spring Boot skills in a team that reviews code.

My CV is attached. I am available for an interview at your convenience.

Best regards,
Ho Phuoc Hoan · [phone] · github.com/hoanhophuoc
```

**Không** viết: "Dear Sir/Madam", "I am writing to express my keen interest", "I am a passionate developer", "I am the perfect candidate".

## 5. GitHub profile — 25 phút

| Việc | Chi tiết |
|---|---|
| **Bio** | `Backend developer (Java) · SQL · REST APIs — fresher, HCM` + link LinkedIn |
| **Ghim 3 repo** | Chat-System · IT-Tools · (nexus sau G6) — **chỉ sau khi dòng tương ứng đạt ✅** trong `07_cv_truth_checklist.md`. Chi tiết: `07_github_cleanup_plan.md` |
| **Profile README** (repo tên = username) | 5 dòng: giới thiệu, 3 kỹ năng, 2 repo nổi bật, email liên hệ |
| **README cho từng repo ghim** | Chạy thế nào · test thế nào · kiến trúc 3 dòng · ảnh nếu có UI |
| **Dọn** | Ẩn fork, archive repo bài tập rỗng, xoá `.env`/`target/`/`node_modules` khỏi history nếu lộ |
| **Không** | Không để repo `test`, `demo`, `untitled` công khai |

## 6. Bốn kênh + bộ lọc cụ thể

| Kênh | Bộ lọc | Tần suất |
|---|---|---|
| **ITviec** | Keyword `Java` `Spring Boot`; Level `Fresher/Junior`; Location `HCM`; tạo **job alert email** | Hằng ngày, 5 phút |
| **LinkedIn Jobs** | `Java fresher`, `Spring Boot junior`, `backend intern`; Location HCM; **Date posted: Past week**; bật alert | 2 lần/tuần |
| **TopCV / VietnamWorks** | `Java`, `Fresher`; lọc "Mới đăng" | 2 lần/tuần |
| **Portal công ty + referral** | 10 công ty mục tiêu (danh sách ở `02_entry_programs_2026_2027.md`) — theo dõi trang tuyển dụng | 1 lần/tuần |

Chi tiết chuỗi tìm kiếm, alert và quy trình 45 phút/ngày: `07_job_alerts_and_routine.md`.

**Quy tắc vàng:** chỉ nộp tin **đăng ≤ 7 ngày** (tin cũ thường đã có ứng viên). Ưu tiên tin có **tên người/HR liên hệ** — tỉ lệ phản hồi cao hơn nộp form.

## 7. Nhịp nộp (theo `04_master_roadmap.md`)

| Tuần | Số đơn | Ghi chú |
|---|---|---|
| **W1–W7** | **0** | Chưa có gì để nộp; chỉ chuẩn bị CV gửi đi + danh sách công ty |
| **W8–W12** | 5/tuần | **Chỉ công ty không phải mục tiêu** — mục đích là thử CV + đo phản hồi |
| **W13–W16** | 10/tuần | Mở dần công ty mục tiêu sau Readiness #1 |
| **W17–W24** | 10–15/tuần | 2 buổi/tuần × 60 phút; có phỏng vấn thì giảm còn 5, dồn giờ bù lỗ hổng |

Nguồn: `04_master_roadmap.md` §2.

**Kỳ vọng thực tế (ước lượng, không phải số liệu đo):** 10 đơn chất lượng → 1–2 phản hồi → 0,5–1 lần phỏng vấn. Nếu sau **30 đơn không có phản hồi nào**, vấn đề nằm ở **CV** (mục 3) chứ không phải ở số lượng — đừng nộp thêm, hãy sửa.

## 8. Bảng theo dõi — dùng thế nào

File: `07_application_tracker.csv` (14 cột).

- **Ghi ngay khi nộp** (30 giây): ngày, công ty, vị trí, nguồn, link JD, CV đã dùng.
- **Cập nhật mỗi thứ Sáu, 20 phút:** trạng thái, câu hỏi bị hỏi, lỗ hổng phát hiện.
- **Cột `lo_hong_phat_hien` là cột giá trị nhất** — sau 5 buổi phỏng vấn, đọc lại sẽ thấy đúng 2–3 lỗ hổng lặp lại, và đó là nội dung để học tuần sau.
- **Follow-up 1 lần duy nhất**, sau 5–7 ngày, 2 câu:

```
Chào anh/chị, tôi đã nộp vị trí [X] ngày [dd/mm]. Tôi muốn hỏi hồ sơ đã được
xem xét chưa, và có thông tin gì thêm tôi cần bổ sung không? Cảm ơn anh/chị.
```

- **Khi bị từ chối**, hỏi feedback **một lần**, 60 từ: *"Cảm ơn anh/chị đã phản hồi. Nếu không phiền, anh/chị có thể cho tôi biết điểm nào trong hồ sơ chưa phù hợp để tôi cải thiện không?"* — 20–30% trường hợp có trả lời, và đó là dữ liệu miễn phí.

## 9. Tám điều **không** làm

1. Nộp cùng một CV cho 50 công ty rồi tự hỏi vì sao im lặng.
2. Ghi lương mong muốn trong CV (để dành cho buổi nói chuyện, và bạn chưa có ngưỡng — B11).
3. Gửi CV dạng `.doc`, `.docx` scan, hoặc file 5 MB.
4. Đính kèm bảng điểm/CCCD/ảnh thẻ khi chưa được yêu cầu (R10 — và không cần thiết ở vòng 1).
5. Nhắn recruiter 3 lần trong 1 tuần.
6. Nhận xét công ty trên mạng xã hội trong lúc đang ứng tuyển.
7. Nhờ AI viết cover letter "thật hay" — JD fresher đọc 90 từ là đủ; thư 400 từ bị bỏ qua.
8. Nộp vào vị trí đòi 2+ năm KN "cho biết" — chỉ tốn thời gian và làm hỏng tâm lý.

---

## Checkpoint Phase 7.2

- **1 CV gốc + 3 slot may đo** (S1 mục tiêu, S2 ba từ khoá đầu, S3 thứ tự dự án) → mỗi đơn ≤ 15 phút.
- 6 kiểu JD × cách đổi slot; 8 quy tắc xuất PDF để ATS đọc được; email 90 từ (VI/EN).
- 4 kênh + bộ lọc cụ thể; nhịp nộp W13 (thử) → W17–W24 (10–15/tuần); tracker 14 cột + follow-up 1 lần + mẫu xin feedback.
- Nếu 30 đơn không phản hồi → sửa CV, không nộp thêm.

**Quyết định đề xuất:** **0 đơn tới hết W7**, nộp **5 đơn/tuần từ W8** chỉ vào công ty không phải mục tiêu, giữ các cửa thật cho sau Readiness #1 (W10).
**Vì sao:** nộp bằng CV chưa qua T1/T6 vào cửa tốt nhất là đốt mất cơ hội đo phản hồi đúng lúc. Nộp sớm vào công ty luyện tập vẫn cho **dữ liệu thật về CV** mà không tốn cửa.
**Điều gì sẽ khiến tôi đổi ý:** nếu W8–W12 có ≥ 3 phản hồi từ 20 đơn (tỉ lệ > 15%) → CV đã ổn, tăng thẳng lên 15 đơn/tuần ở W17 thay vì 10.
