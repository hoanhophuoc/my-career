# Phase 9 — Bản điều hành (executive summary)

**Cập nhật lần cuối:** 21/11/2026

**Viết ngày:** 20/11/2026 · **Người:** Hồ Phước Hoàn · **Đọc hết file này: 6 phút.**
**Đây là file duy nhất cần mở mỗi sáng.** Mọi chi tiết nằm ở 8 Phase phía sau, đã đánh số.

> Ghi chú R7: kế hoạch ban đầu là 8 file cho Phase 9. Tôi gộp còn **3 file** vì 5 file còn lại sẽ là bản sao rút gọn của các Phase đã có (bài học từ Phase 7: gộp 8 → 3 thì dùng được, tách 8 thì không ai mở). Ba file: bản điều hành (file này), `09_kpi_tracker.csv`, `09_refresh_prompts.md`.

---

## 1. Tôi đang ở đâu (một bảng)

| Hạng mục | Trạng thái thật (20/11/2026) | Nguồn |
|---|---|---|
| Học vấn | **Tốt nghiệp loại Giỏi**, CNTT; **IELTS 6.5 đã được Trường công nhận** | `01_graduation_checklist.md` |
| Năng lực đo được | Java core **L2**, SQL **L2**, testing **L1–L2**, Spring Boot **L1**; **0 dòng Spring Boot trên CV** | `01_skills_matrix.md` |
| Hướng đã chốt | **Java / Spring Boot backend** — điểm 3,80, hạng 1; .NET 3,25 (dự bị duy nhất); **tester/QA đã bị loại hoàn toàn** (20/11/2026) | `03_strategy.md` |
| Phiên bản học | **Java 25 LTS + Spring Boot 4.2.0** (GA 19/11/2026; Boot 4.0 hết OSS support 31/12/2026) | `04_master_roadmap.md` |
| Tài sản code | **36 repo, 261 MB** đã clone; TaskFlow chưa tồn tại; `nexus` bị loại khỏi CV cho tới khi qua cổng G6 | `02c_repo_inventory.md`, `05_how_to_learn.md` |
| Hồ sơ | 1 CV gốc + 3 slot may đo; tracker 14 cột; headline LinkedIn 118/220 ký tự | `07_application_kit.md` |
| Tài nguyên | **12 cuốn = 49 giờ, 12/12 đã có trong tủ** (`books.txt` 212 file, audit lại 20/11), 24 tài nguyên free đã trả HTTP 200, 1.861 bookmark đã phân loại | `05_shelf_and_books.md` |
| Thời gian | 6h/ngày × 6 ngày/tuần = **36h/tuần**, 24 tuần (W1 = 24/11/2026 → W24 = 04/05/2027; Tết 04–10/02/2027 ở W11) | `04_master_roadmap.md` §2 |
| Ngân sách | **0 đồng** — đúng R6, kể cả chứng chỉ (Phase 8) | `08_education_competitions_community.md` |

**Thị trường, đo bằng dữ liệu thật (không phải cảm nhận):**

| Nguồn | Cỡ mẫu | Kết luận dùng được |
|---|---|---|
| Census 743 tin (Phase 2) | 743 | Junior chỉ **5%** tin; backend <1 năm trung vị **12,4 triệu**; Java junior 0,5–1 năm **19–20 triệu gross** |
| ITviec (crawl 20/11, chưa đăng nhập) | 109 tin | fresher/junior/intern **7,5%**; senior+ **68%**; lương ẩn **96,3%** |
| ITviec TP.HCM (crawl lại sau đăng nhập) | **75 tin / 55 công ty** | entry-level **6,7%**; lương hiện số **17/75 (22,7%)**, trần trung vị **~2.115 USD**; 64 tin còn ẩn vì NTD tự chọn ẩn |
| **Glints TP.HCM** (crawl 20/11) | **86 tin / 56 công ty** | **47 tin có lương (54,7%)**; **24 tin IT yêu cầu 0–1 năm**; trung vị ~**25 triệu** → khớp benchmark; đây là sàn phải quét **hàng tuần** |
| TopDev · VietnamWorks · NodeFlair · JobStreet | 8 · **42** · **0** · 6 | VietnamWorks (sau đăng nhập) có **10 tin TP.HCM**, 6 tin backend Java — đáng nộp thêm nhưng **0 tin fresher**; **JobStreet đã ngừng site VN** (redirect Jora), tin còn lại toàn remote |
| **Glints phân bố theo quận** | **86 tin, 86 tin có quận** | **Quận 7: 26 · Quận 1: 18 · Quận 3: 13 · Phú Nhuận: 11 · Quận 2: 11**. Bộ lọc khoảng cách dùng cấu hình cục bộ (`config.local.json`, không commit). Xem `10_commute_and_platform_guide_2026-11-20.md` |
| LinkedIn (crawl 20/11) | 392 tin / 163 công ty | reachable **153 (39,0%)**; trong đó Java/Spring **63 tin**; **0/392** tin có số lương trong metadata (7 tin nêu lương trong JD, chỉ đọc được từ bản thô cục bộ); hai nguồn chỉ trùng **11 công ty** |

→ Hệ quả chiến lược, không đổi: **thị trường không dành cho fresher**, nên đường đi là *chương trình đầu vào (fresher academy, internship có lương) + .NET dự bị*, không phải "nộp 200 đơn rồi chờ".

---

## 2. Bảy quyết định đã chốt (không mở lại trừ khi có dữ kiện mới)

1. **Java/Spring Boot 12 tháng đầu**, .NET là dự bị duy nhất. **Không làm tester/QA** — đã loại khỏi mọi bảng, shortlist và ngưỡng đổi hướng.
2. **Java 25 + Spring Boot 4.2.0** — không học Boot 1.x/2.x trong sách cũ.
3. **`nexus` không vào CV** cho tới khi qua **G6a + G6b**; trong 8 tuần đầu, TaskFlow (code tay) là dự án chính.
4. **Không học thạc sĩ** trong 12 tháng (90–159 triệu; đợt 2026 đã đóng) — xem lại 10/2029.
5. **Không mua chứng chỉ** trong 12 tháng (0 đồng); Oracle 1Z0-831 (245 USD) chỉ sau khi có lương.
6. **Không thi lại IELTS** — chỉ luyện **nói** 15'/ngày cho phỏng vấn.
7. **Nộp đơn là một kỹ năng phải đo**: **0 đơn tới W7**, 5 đơn/tuần W8–W12 (chỉ công ty không mục tiêu), 10/tuần W13–W16, 10–15/tuần từ W17; mọi đơn vào tracker.

---

## 3. 72 giờ tới (21–23/11/2026) — làm đúng thứ tự này

| # | Việc | Thời lượng | Xong khi |
|---|---|---|---|
| 1 | **RSVP DevFest Cloud HCM 05/12** (đã xác nhận miễn phí); kiểm tra phí Road to DevFest **sáng 21/11 (07:30)** | 15' | Có email/QR xác nhận |
| 2 | **Sửa 8 dòng CV** theo `01_cv_linkedin_audit.md` mục 3 | 45' | Xuất PDF, mở lại thấy đúng |
| 3 | **Không nộp đơn nào.** Chốt danh sách 10 công ty mục tiêu + 10 công ty "không phải mục tiêu" để nộp từ W8 | 30' | Danh sách trong `07_application_kit.md` |
| 4 | Cài **JDK 25 + Spring Boot 4.2.0 + PostgreSQL**, tạo repo `java-backend-lab`, commit đầu tiên | 2h | `./mvnw test` xanh, 1 commit |
| 5 | Làm **T1 (Java)** và **T6 (Chat-System)** | 4h | Có điểm; quyết định nội dung 4 tuần đầu |

> **Vì sao KHÔNG nộp đơn trong 3 ngày đầu (chốt 21/11/2026):** CV hiện chưa qua bài T1/T6 và chưa có bản "gửi đi" chỉ chứa dòng đã kiểm chứng. Nộp vào Netcompany/EPAM/Amaris/CEVA/DXC lúc này là dùng mất **cửa thật** bằng một hồ sơ chưa sửa. Nhịp nộp bắt đầu **W8** với công ty không phải mục tiêu; các cửa thật giữ tới **sau Readiness #1 (W10)**. Xem `04_master_roadmap.md` §2.

---

## 4. 7 ngày (21–27/11) — tuần S0 + W1

- [ ] Danh sách 20 công ty (10 mục tiêu + 10 luyện tập) đã chốt; **0 đơn đã nộp**
- [ ] Môi trường chạy được: JDK 25, Boot 4.2.0, Postgres, `java-backend-lab`
- [ ] T1 ≥ 80% · T6 hoàn thành
- [ ] **6 bài DSA** có hẹn giờ (1/ngày)
- [ ] Import bộ **60 thẻ Anki** có sẵn; ôn đủ 6/7 ngày
- [ ] Cuốn #1 của MVS: đọc đúng chương đã ghi, không đọc thêm
- [ ] 1 buổi nói tiếng Anh 15' (tự ghi âm, nghe lại)
- [ ] `LEARNING.md` có 6 dòng (mỗi ngày 3 dòng)

**Chỉ số tuần này chỉ có một con số quan trọng: số giờ code tay (không AI). Mục tiêu ≥20h.**

---

## 5. 30 ngày (21/11 → 20/12) — W1–W4

| Mục tiêu | Ngưỡng đạt | Cách đo |
|---|---|---|
| Java core từ L2 lên **L3** | T1 ≥ 80% **làm lại lần 2 sau 2 tuần** | Điểm test |
| SQL từ L2 lên **L2+** | T2 ≥ 8/10 | Điểm test |
| Testing từ L1–L2 lên **L2** | Viết được 10 unit test cho code của mình, không copy | Commit |
| Code tay | ≥ 80h trong 30 ngày | `09_kpi_tracker.csv` |
| Đơn nộp | **0** (nhịp nộp bắt đầu W8) | tracker |
| Sự kiện | 2 (05/12 DevFest Cloud + 13/12 DevFest HCMC nếu phí 0) | 3 thứ/sự kiện |
| Tiếng Anh | 15'/ngày × 25 ngày + 2 buổi 30' | file ghi âm |

**Nếu 30 ngày chỉ đạt 1 thứ:** phải là **T1 ≥ 80%**. Đó là cổng chặn mọi thứ phía sau.

---

## 6. KPI — 8 chỉ số, không hơn

| KPI | Nhịp đo | Ngưỡng đạt | Nếu trượt 2 tuần liền |
|---|---|---|---|
| Giờ code tay (không AI) | tuần | ≥20h (W1–W12), ≥15h sau W13 | Cắt sách xuống 50% giờ đọc |
| Bài DSA có hẹn giờ | tuần | 6/tuần | Giảm còn 4, giữ đều |
| Thẻ Anki ôn đủ | ngày | 100% thẻ đến hạn | Bỏ thẻ mới 1 tuần, chỉ ôn |
| Đơn nộp | tuần | 0 → 5 (W13) → 10–15 (W17) | Xem lại CV, không tăng số |
| Tỉ lệ phản hồi | 20 đơn | ≥10% từ W15 | Viết lại 2 dòng đầu CV + headline |
| Phỏng vấn | tháng | ≥1 trước W20 | Hạ xuống **internship có lương / fresher .NET** (không dùng tester) |
| Giờ đọc sách | tuần | ≤3h (≤8% tổng giờ) | Cắt ngay, đây là chỉ số dễ lạm phát nhất |
| Sự kiện cộng đồng | tháng | 1, mang về 3 thứ | Không bù — bỏ tháng đó |

File ghi: **`09_kpi_tracker.csv`** (24 tuần, điền 5 phút mỗi Chủ nhật).

---

## 7. Rủi ro — 8 cái, kèm dấu hiệu và cách xử lý

| # | Rủi ro | Dấu hiệu sớm | Xử lý |
|---|---|---|---|
| 1 | **AI viết hộ tái diễn** (nguyên nhân `nexus` bị loại) | Không giải thích được 1 dòng code mình vừa commit | NO-AI 8h/tuần là bắt buộc; mỗi commit phải viết lại được từ trí nhớ |
| 2 | **Chỉ 7,5% tin là entry** → bị từ chối hàng loạt | 20 đơn, 0 phản hồi | Đổi kênh (giới thiệu, sự kiện, chương trình đầu vào), không tăng số đơn |
| 3 | **CV phụ thuộc TaskFlow** chưa tồn tại | W8 vẫn chưa có TaskFlow chạy | Dùng Chat-System + CoolWear làm 2 dự án CV; TaskFlow dời W9–W12 |
| 4 | **Kiệt sức vì 6h/ngày** | 3 ngày liên tiếp <4h, hoặc bỏ DSA 1 tuần | Chuyển bản 3h/ngày (mục 8 roadmap) — giãn 24 → 48 tuần, không bỏ |
| 5 | **Tết Nguyên Đán 2027** (~06/02, cần xác nhận lịch nghỉ) rơi vào W11 | — | W11 đặt mục tiêu 50%, chỉ giữ Anki + 1 bài DSA/ngày |
| 6 | **Nói tiếng Anh vẫn là điểm yếu** (IELTS S 6.0) | Trả lời phỏng vấn thử < 2 phút/lượt | Tăng lên 2×30'/tuần; ghi âm và nghe lại, không học thêm ngữ pháp |
| 7 | **Mạng lưới yếu** (0 người trong ngành) | 3 tháng không có ai giới thiệu | 1 sự kiện/tháng, bắt buộc mang về 1 người + kênh liên lạc |
| 8 | **Dữ liệu thị trường cũ đi** (số 20/11/2026) | Quá 8 tuần không crawl lại | Chạy `tools/crawl_linkedin_jobs.py` (15 phút) — prompt ở file số 3 |

---

## 8. Cổng kiểm tra (không đạt thì không đi tiếp)

| Cổng | Khi nào | Điều kiện qua | Nếu không qua |
|---|---|---|---|
| **G1** Môi trường | S0 | JDK 25 + Boot 4.2.0 + Postgres chạy, 1 commit | Dừng, sửa môi trường — không học tiếp |
| **G2** Java core | W4 | T1 ≥ 80% (làm lại lần 2) | Lặp W3–W4, lùi lịch 2 tuần |
| **G3** SQL | W4 | T2 ≥ 8/10 | Lặp phần SQL, không sang Spring |
| **G4** TaskFlow chạy | W8 | 14 endpoint + test xanh + README | Dời W9–W12, CV dùng Chat-System |
| **G5** Readiness #1 | W10 | Rubric `04_readiness_rubric.md` đạt ngưỡng "nộp được" | Chưa mở cửa thật; giữ 5 đơn/tuần vào công ty không mục tiêu |
| **G6** `nexus` | G6a ở W14 · G6b ở W16 | G6a (giải thích được 6 cổng) + G6b (tự thêm 1 tính năng) | `nexus` không vào CV |

---

## 9. Bản đồ 24 tuần

**Không chép lại ở đây.** Bảng W0–W24 chuẩn (ngày bắt đầu, dự án từng tuần, cổng G1–G6, Readiness #1/#2, mốc nộp đơn, KPI tuần) nằm ở **`04_master_roadmap.md` §2** — đó là nguồn sự thật duy nhất.

---

## 10. Checkpoint

- Pack đã đủ 9 Phase; file này là **điểm vào duy nhất**, mọi số liệu đều truy được về file gốc.
- Trạng thái thật: Java core L2, SQL L2, Spring Boot L1, **0 dòng Spring Boot trên CV** — không tô hồng.
- Thị trường: 6,7% (ITviec) và 28,3% (LinkedIn) tin là chạm tới được → chiến lược bậc thang là bắt buộc, không phải lựa chọn.
- Ngân sách 0 đồng được giữ ở cả 9 Phase, kể cả chứng chỉ và học lên.
- 72 giờ tới chỉ có 5 việc; việc quan trọng nhất là **môi trường chạy được + T1 + T6 + sửa CV**, không phải nộp đơn hay đọc thêm tài liệu.
- KPI có 8 chỉ số và một file điền 5 phút/tuần — nếu phải nhớ nhiều hơn 8 thì hệ thống đã hỏng.

**Quyết định đề xuất:** chạy S0 đúng 3 ngày (21–23/11), rồi vào W1 ngày 24/11; **không** thêm tài liệu, sách hay khóa học nào mới trong 4 tuần đầu.

**Vì sao:** 4 tuần đầu quyết định toàn bộ 20 tuần còn lại (G2/G3 là cổng chặn), và mọi thứ thêm vào lúc này chỉ làm giảm giờ code tay — biến số duy nhất đã chứng minh là có tác dụng.

**Điều gì khiến tôi đổi ý:** nếu đến 23/11 mà môi trường vẫn chưa chạy (G1 trượt) → dừng mọi việc khác 1 ngày để sửa, vì mọi Phase sau đều giả định có repo chạy được; nếu 5 đơn nhóm A có ≥2 phản hồi trong 14 ngày → đẩy nhịp nộp lên 10 đơn/tuần ngay từ W5 thay vì W13.
