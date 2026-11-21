# 02 — BÁO CÁO THỊ TRƯỜNG VIỆC LÀM IT TP.HCM CHO NGƯỜI MỚI (2026–2027)

**Ngày:** 20/11/2026 · **Cập nhật lần cuối:** 21/11/2026 · **Nguồn chính:** S1–S20 trong `09_decision_log_and_sources.md`
**Nhắc lại giới hạn:** cơ cấu level/kỹ năng dưới đây là **census trên ITviec** (743 tin, kỳ edition 10 — **số của bên thứ ba, không phải pack tự thu**), **không phải toàn thị trường**.

---

## 0. Bảng số liệu gốc (một nguồn sự thật)

Mọi con số tiêu đề của pack được tính từ **một** file: `02_postings_master.csv`, bằng `python3 tools/02_stats.py`.
Bảng dưới đây là output của script đó (chạy lại để kiểm chứng). File nào trích số khác thì file đó sai.

| Con số | Giá trị | Định nghĩa | Bộ dữ liệu | Ngày | File tính ra |
|---|---|---|---|---|---|
| Tổng tin sau lọc nhóm vai trò | **602** | dòng không có `excluded_reason` | `02_postings_master.csv` | 20/11/2026 | `tools/02_stats.py` |
| Trong đó | LinkedIn **392** · Glints **86** · ITviec **75** · VietnamWorks **41** · TopDev **8** | đếm theo `source` | `02_postings_master.csv` | 20/11/2026 | `tools/02_stats.py` |
| Dòng bị loại (nhóm vai trò) | **69** | có `excluded_reason` | `02_postings_master.csv` | 20/11/2026 | `tools/02_stats.py` |
| `true_entry_level` | **42 (7,0%)** | `years_exp_min = 0` đọc được từ JD | `02_postings_master.csv` | 20/11/2026 | `tools/02_stats.py` |
| `true_entry_level` + Java/Spring | **4** | true entry ∩ kỹ năng Java | `02_postings_master.csv` | 20/11/2026 | `tools/02_stats.py` |
| Reachable | **265** | `level_label` ∈ Entry/Internship/Associate/Not Applicable, tiêu đề không có senior | `02_postings_master.csv` | 20/11/2026 | `tools/02_stats.py` |
| Reachable + Java/Spring | **113** | reachable ∩ Java/Spring | `02_postings_master.csv` | 20/11/2026 | `tools/02_stats.py` |
| LinkedIn reachable | **153 (39,0% của 392)** | reachable ∩ source=linkedin | `02_postings_master.csv` | 20/11/2026 | `tools/02_stats.py` |
| Có lương công khai | **60 (10,0%)** | `salary_min` không rỗng | `02_postings_master.csv` | 20/11/2026 | `tools/02_stats.py` |
| Lương trung vị | **12,5 triệu** | trung vị `salary_min`, mọi level | `02_postings_master.csv` | 20/11/2026 | `tools/02_stats.py` |
| `title_inflation` | **17** | tiêu đề ghi junior/fresher nhưng đòi ≥1 năm | `02_postings_master.csv` | 20/11/2026 | `tools/02_stats.py` |
| Census ITviec (bên thứ ba) | **743 tin / 629 tin** | vitX đếm toàn bộ tin ITviec | nguồn S1 (vitX) | 31/10/2026 | không do pack tính |
| Cấu trúc level theo tiêu đề | senior+ **244** · không ghi **276** · junior/fresher **82** | từ khoá trong tiêu đề | `02_postings_master.csv` | 20/11/2026 | `tools/02_stats.py` |

> **Vì sao con số “LinkedIn chạm tới được” đổi từ 111 thành 153:** con số cũ dùng điểm số có đọc mô tả JD (`desc`) — dữ liệu đó đã bị đưa ra khỏi repo vì là nội dung có bản quyền của bên thứ ba (P0-1), nên **không tái lập được nữa**. Con số 153 chỉ dùng metadata công khai và **tái lập được bằng một lệnh**. Khi đọc tài liệu cũ, đừng trộn hai định nghĩa.

### 0.1 Nhóm vai trò đã loại — đọc song song để không đọc nhầm độ khó thị trường

Hoàn đã quyết định **không làm tester/QA/support/BrSE** — quyết định đó giữ nguyên. Nhưng các số "chạm tới được 39%" hay "true entry 7,0%" là **đã tính sau khi loại** các nhóm này, mà đây lại thường là **cửa vào thật của fresher**.

| Cách đọc | Số liệu | Ý nghĩa |
|---|---|---|
| **Không có nhóm đã loại** (cách pack đang dùng) | 602 tin / 42 true-entry (7,0%) | Thị trường cho đúng hướng Java backend |
| **Có nhóm đã loại** | 671 dòng trong master; 69 dòng còn nhãn `excluded_reason` | Nếu mở lại tester/QA/support, số "cửa" tăng đáng kể — nhưng đó là hướng Hoàn đã từ chối |
| Riêng tester/QA ở LinkedIn | ~143/550 tin trước lần lọc đầu (ước lượng từ nhật ký purge đợt 1) | Nhóm lớn nhất bị loại; **không** phải nhóm dễ xin nhất |

**Cảnh báo trung thực:** nhật ký purge từng dòng (`tools/purge_log_2026-11-20.csv`) chỉ ghi **69 dòng của đợt lọc thứ hai**. Đợt lọc tester/QA đầu tiên (212 tin) thực hiện trước khi có nhật ký, nên **chỉ còn con số tổng, không còn từng dòng**. Đó là lý do master không thể dựng lại đầy đủ nhóm tester.

---

## 1. Ba con số tóm tắt toàn bộ thị trường

| Con số | Nguồn | Ý nghĩa |
|---|---|---|
| **5%** tin tuyển là **Junior**; **0 khe riêng cho Fresher/Intern** trên ITviec | S1 (40/743 junior) | Người mới cạnh tranh trong 5% thị trường, không phải 30% |
| **8,3%** tin nhắc **Java** — stack đứng đầu (62/743) | S1 | Chọn Java là đúng |
| **93,7%** tin yêu cầu **tiếng Anh** | S1 (2.542 tin đọc toàn văn) | Tiếng Anh không phải "điểm cộng", là **vé vào cửa** |

---

## 1. Cơ cấu thị trường: người mới đang ở đâu

| Level | Số tin | % |
|---|---|---|
| Junior | 40 | **5%** |
| Mid | 341 | **46%** |
| Senior | 211 | 28% |
| Lead | 87 | 12% |
| Manager | 64 | 9% |
| *(Fresher / Intern)* | **không có mục riêng** | — |

`[Sự thật — S1, census 30/10/2026 — Tin cậy: Cao cho ITviec]`

**Diễn giải:** thị trường IT Việt Nam **không thiếu việc** — nó thiếu việc **cho người chưa có kinh nghiệm**. Đây không phải cảm giác của Hoàn; đây là cơ cấu đo được.

**Nhưng đọc kỹ hơn:** "Junior" trên ITviec là **một nhãn do nhà tuyển dụng tự chọn**, và nhiều công ty đăng tin fresher ở mục "Junior" hoặc không chọn level nào. 40 tin junior **không** có nghĩa cả TP.HCM chỉ có 40 việc cho người mới — nghĩa là **trên ITviec** chỉ có 40 tin được gắn nhãn đó.

**So với 3 tháng trước (S1):**
- 24/08/2026: **804** tin mở (đỉnh)
- 03/09: 743 · 01/10: 655 · 15/10: 644 · 30/10: **629**
- **−21,8% so với đỉnh 24/08** (804 → 629). Nếu tính từ mốc 03/09 (743) thì mức giảm là **−15,3%** — hai con số đúng với hai mốc khác nhau, đừng dùng lẫn.
- Tỷ lệ senior+ tăng từ 43,7% → **49%** (S1, census 30/10/2026). Con số **68%** xuất hiện ở bản trước là của **một lần crawl ITviec 109 tin ngày 20/11/2026** (mẫu nhỏ, lệch vì truy vấn Java/backend), **không** phải census — đừng dùng 68% cho toàn thị trường.

`[Sự thật — S1 — Tin cậy: Cao]` → Thị trường **co lại và dịch lên trên** đúng vào lúc Hoàn đang tìm việc. Đây là tin xấu, và cần nói thẳng.

---

## 2. Stack nào có việc thật? (trả lời H1, H2)

| Stack | Số tin (theo tiêu đề) | % | So sánh |
|---|---|---|---|
| **Java** | **62** | **8,3%** | **#1** |
| Python | 49 | 6,6% | #2 |
| .NET / C# | 26 | 3,5% | #3 |
| AWS | 25 | 3,4% | hạ tầng |
| Node.js | 23 | 3,1% | |
| React | 22 | 3,0% | frontend #1 |
| **Go** | **18** | **2,4%** | **1/3 của Java** |
| PHP | 14 | 1,9% | |
| Azure | 13 | 1,7% | |
| Angular | 9 | 1,2% | |

`[Sự thật — S1, đếm theo tiêu đề, 30/10/2026 — Tin cậy: TB-Cao]` *(S1 tự ghi: "nhu cầu thật cho mỗi stack cao hơn vì chỉ đếm tiêu đề")*

### H1 — "Java tuyển nhiều nhưng chủ yếu mid trở lên; fresher rất ít"
**Kết luận: ĐÚNG, và đúng hơn Hoàn nghĩ.** Java là stack **lớn nhất** (62 tin) nhưng **47% toàn bộ tin là senior+** và **junior chỉ 5%**. Không có mục fresher.
**Tin cậy: Cao** (census + tỷ lệ level cùng một nguồn).

### H2 — "Golang ít việc, khó cho người mới"
**Kết luận: ĐÚNG.** Go = **18 tin** (2,4%), bằng **29%** số tin Java. Trong số tin Go quan sát được, 1 tin là **Senior Backend (Golang)** yêu cầu senior.
**Tin cậy: TB-Cao.** Vector quyết định: **ở lại Java**. Việc Hoàn chuyển từ Go sang Java là quyết định đúng — dữ liệu ủng hộ, không phải cảm tính.

---

## 3. Vị trí công việc: backend là nhóm lớn nhất

| Nhóm | Số tin | % |
|---|---|---|
| **Backend** | **144** | **19%** |
| Data & AI | 87 | 12% |
| Cloud & DevOps | 80 | 11% |
| QA & Testing | 72 | 10% |
| Embedded & IoT | 21 | 3% |
| ERP & enterprise | 19 | 3% |
| Mobile | 18 | 2% |
| Frontend | 17 | 2% |
| Design & UX | 11 | 1% |
| *(khác: management, BA, ops)* | 273 | 37% |

`[Sự thật — S1 — Tin cậy: Cao]`
**So what:** backend (19%) > frontend (2%) **gần 10 lần** trên board này. Hướng đi của Hoàn trùng với nhóm lớn nhất thị trường. `S3` cũng xác nhận: Back-end là nhóm kỹ năng được nhắc nhiều nhất trong tin tuyển (**33,2%**, +8,7% YoY).

---

## 4. Kỹ năng thực tế trong tin fresher/junior Java (mẫu 21 tin)

Từ các JD đọc được (`02d_linkedin_jobs_2026-11-20.csv`, P07–P21), bộ kỹ năng lặp lại nhiều nhất:

| Kỹ năng | Số tin nhắc | Ghi chú |
|---|---|---|
| **Java** | 12/21 | luôn là must-have |
| **Spring Boot** | 6/21 | xuất hiện cả ở tin junior 0,5 năm (P07) |
| **SQL** | 5/21 | hay đi kèm "Java + SQL" trong bài test trắc nghiệm |
| **REST API / JSON / XML** | 5/21 | |
| **Tiếng Anh** | 14/21 | 4 tin ghi rõ "Good English" hoặc "tiếng Anh tốt" |
| Git / Docker / K8s / Kafka | 3/21 | **chỉ ở tin senior**, không ở tin fresher |
| OOP | 3/21 | hay hỏi miệng hơn là ghi trong JD |
| Automation test (Selenium/Playwright) | 4/21 | toàn bộ là tin **tester**, không phải backend |

`[Sự thật — 21 tin, Tin cậy: TB (mẫu nhỏ, không đại diện)]`

**Phát hiện quan trọng:** **Kafka/Kubernetes/Redis không xuất hiện trong tin fresher/junior Java** nào tôi đọc được. Chúng chỉ có trong tin senior/principal (P03, P04). → Việc CV Hoàn liệt kê Kubernetes/Tekton/Argo CD/CUE **không giúp gì cho vị trí fresher, chỉ tạo bẫy câu hỏi**. Xác nhận khuyến nghị ở `01_cv_linkedin_audit.md`.

**Ngược lại:** `Spring Boot` xuất hiện ngay ở tin **junior 6 tháng–1 năm** (P07). Nghĩa là Spring Boot **không phải "học sau"**, nó là điều kiện vào cửa. Đây là lý do Phase 4 phải đặt Spring Boot lên đầu.

---

## 5. Lương: con số thật, không phải lời đồn

| Nguồn | Vị trí | Mức | Ngày |
|---|---|---|---|
| S2 (ITviec, 1.839 người) | **Back-end Developer, dưới 1 năm** | **trung vị 12,4 triệu/tháng** | 11/11/2025 |
| S2 | Back-end Developer, thâm niên cao | 54,9 triệu/tháng | 11/11/2025 |
| S2 | Tech Lead | 51,8 triệu · CTO/CIO 101,25 triệu | 11/11/2025 |
| P07 (tin thật) | Java Software Engineer **Junior** (0,5–1 năm), Spring Boot | **19–20 triệu gross** | 18/11/2026 |
| P19 (tin thật) | Back-End **Intern** (FPT Life) | **7–10 triệu** | 20/11/2026 |
| P20 (tin thật) | **Fresher** Java, 2 tháng đào tạo (Hybrid) | **trợ cấp 3 triệu** | 01/2026 |
| P18 (tin thật) | Back-End **Intern** (FPT Telecom) | **không lương** | 20/11/2026 |
| `02e` (ITviec, 75 tin TP.HCM, **đã đăng nhập**) | Backend Java **middle/senior** (19 tin hiện số) | trần **1.000–5.000 USD**, trung vị trần **~2.115 USD (~55 triệu)** | 20/11/2026 |
| `02e` | **Entry-level** trong cùng 75 tin | chỉ **5 tin**; intern có trợ cấp thấp nhất ghi nhận **400–1.000 USD** (DMSpro) | 20/11/2026 |

`[Sự thật — Tin cậy: Cao cho S2, TB cho tin lẻ]`

**Dải thực tế cho Hoàn (0 năm kinh nghiệm, TP.HCM):**
- **Thực tập có trợ cấp:** 3–10 triệu (có nơi 0 đồng — P18)
- **Fresher chính thức:** **10–15 triệu** (trung vị báo cáo 12,4)
- **Junior có 6–12 tháng KN + tiếng Anh tốt + Spring Boot:** **15–20 triệu**
- **Trần của "fresher" thuần:** ~15 triệu. Muốn 19–20 triệu ngay (như P07) thì phải có **dự án Spring Boot thật + tiếng Anh giao tiếp**.

**So what:** con số 19–20 triệu trong P07 là **đích đến sau 6–12 tháng**, không phải mức khởi điểm. Đừng đặt kỳ vọng 20 triệu cho offer đầu tiên — nhưng cũng đừng nhận 5 triệu "học việc" không hợp đồng.

**Kiểm chứng chéo (20/11/2026, sau khi Hoàn đăng nhập ITviec):** trong 75 tin TP.HCM crawl lại, trung vị **trần** lương của nhóm middle/senior là ~55 triệu — gần như trùng con số 54,9 triệu "back-end thâm niên" của báo cáo khảo sát S2. Hai nguồn độc lập khớp nhau ở **cùng một mốc**, nên dải lương trong mục này đáng tin hơn trước. Chi tiết: `02e_itviec_market_snapshot_2026-11-20.md`.

---

## 6. Kênh nào có việc thật? (H9)

| Kênh | Đo được gì | Kết luận |
|---|---|---|
| **ITviec** | **56** tin Java ở TP.HCM (mọi level); 629 tin IT toàn quốc; có cấu trúc level rõ nhất | **Bắt buộc** — nhưng **không đủ** |
| **TopCV** | 40 fresher backend HCM · 43 backend dev HCM · 90 developer HCM (19/11/2026) | Có tin fresher **nhiều hơn** ITviec về mặt nhãn |
| **CareerViet** | 22 backend fresher (18/11/2026) | Bổ trợ, mạnh về ngân hàng/nhà nước |
| **Indeed VN** | 50+ fresher java · 100+ fresher software engineer HCM | Nhiều tin lặp lại từ nguồn khác, nhưng có lương công khai |
| **LinkedIn** | **Đã đo**: 392 tin / 163 công ty (20/11/2026, API khách, đã bỏ 143 tin tester) — nhưng chỉ 1,7% tin có lương | Nguồn **bắt buộc thứ hai**: chỉ trùng 11 công ty với ITviec |
| **Glints** | **86 tin TP.HCM / 56 công ty**; **47 tin (54,7%) có lương**; **24 tin IT yêu cầu 0–1 năm** | **Nguồn tốt nhất cho người mới** — mỗi tuần nên quét lại (chi tiết `02f_multi_platform_snapshot_2026-11-20.md`) |
| **TopDev** (nay là Saramin) | 9 tin toàn quốc, 8/9 khoá lương sau đăng nhập | **Không ưu tiên** cho fresher backend |
| **VietnamWorks** | Đăng nhập rồi mới đủ: **42 tin**, trong đó **10 tin TP.HCM**, 11 tin có lương (26,2%); nặng Hà Nội và bank/chứng khoán | Không phải kênh chính, nhưng có **6 tin backend Java TP.HCM** để nộp thêm |
| **NodeFlair** | Tìm `java` + Việt Nam → **0 kết quả**; `/vn/jobs` 404 | **Bỏ** — không có dữ liệu VN |
| **JobStreet VN** | `jobstreet.vn` **redirect sang Jora Australia**; DNS `vn.jobstreet.com` không tồn tại; chỉ còn 7 tin **remote** xuyên biên giới trên `ph.jobstreet.com` | **Bỏ** — sàn VN đã ngừng, không có tin onsite TP.HCM |
| **Trang công ty / referral / Facebook group** | Không đo được bằng công cụ | **Nơi có nhiều tin fresher thật nhất — theo suy luận, chưa kiểm chứng** |

### H9 — "LinkedIn là kênh có nhiều tin nhất ở TP.HCM"
**Kết luận: KHÔNG CHỨNG MINH ĐƯỢC, và nhiều khả năng SAI.**
- `[Chưa biết]` không có số đo LinkedIn → tôi không được phép khẳng định.
- `[Suy luận — TB]` LinkedIn là mạng xã hội nghề nghiệp **tổng hợp toàn cầu**, không có census IT theo level. Các board IT chuyên biệt (ITviec) đếm được **629 tin IT toàn quốc** và **56 tin Java ở TP.HCM** — những con số này **không thể quan sát được trên LinkedIn**.
- `[Suy luận — Cao]` Với người mới, tin fresher thật thường nằm ở: **trang tuyển dụng của công ty** (FPT, KMS, TMA đều có mục riêng), **chương trình fresher theo đợt** (CMC Techie, FPT Fresher/Talent), **TopCV/CareerViet**, và **referral**. Đăng trên LinkedIn tốn phí → công ty nhỏ ít đăng.
- **Kết luận thực dụng:** giữ LinkedIn (vì recruiter tìm ứng viên ở đó, và Hoàn có 4 alert sẵn), **nhưng không được coi là kênh chính**. Kênh chính phải là **10–15 trang công ty + 3 board + referral**.

---

## 7. Xu hướng AI (trả lời một phần H4)

| Số liệu | Giá trị | Nguồn |
|---|---|---|
| % tin IT có AI/ML/LLM/CV/NLP **trong tiêu đề** | **12,7%** (từ 11,3% đầu 8/2026) | S1 |
| Tăng trưởng tin AI/Data/ML YoY | **+96,6%** (Q1-2026) | S3 |
| Python trong tin tuyển | 18,6% (+6,2% YoY) | S3 |
| Q3-2025: tin AI/Data/ML | +42,1% YoY, trong khi **non-AI giảm −3,1%** | S4 |

`[Sự thật — S1/S3/S4 — Tin cậy: Cao]`

**Nhưng đọc kỹ S1:** tỷ lệ tin có AI trong tiêu đề **giảm** từ 14,1% → 12,7% trong khi tổng tin giảm mạnh hơn. S1 kết luận: *"AI work is going into backend, data and cloud roles rather than new AI titles"* — tức AI **không tạo ra nghề mới cho fresher**, nó trở thành **kỹ năng kỳ vọng trong nghề cũ**.

**So what cho Hoàn:** đừng chuyển sang "AI engineering" vì thấy tăng trưởng 96,6% — đó là **tăng trưởng của tin senior/Data**, không phải fresher. Học AI ở mức **dùng được trong backend** (prompt, đọc/review code AI, test) là đủ; xem Phase 3.

---

## 8. Thời gian tuyển & mùa vụ

| Dữ liệu | Giá trị | Nguồn |
|---|---|---|
| Median số ngày một tin backend còn sống | **29 ngày** (lâu nhất trong các nhóm) | S1 |
| Số công ty đang tuyển | **321**; **202** công ty chỉ đăng **1** tin | S1 |
| Ngân hàng/fintech/chứng khoán | **19%** tổng tin — **nhóm mua kỹ sư lớn nhất** | S1 |
| Tin IT tại TP.HCM | **61%** tổng tin IT cả nước (10/2026) | S1 |

`[Sự thật — S1 — Tin cậy: Cao]`

**So what:**
- Backend mất ~1 tháng để tuyển → nhà tuyển dụng **không vội**, và họ nhận nhiều hồ sơ. Hệ quả: nộp sớm trong đợt đăng tin có lợi thế.
- 202 công ty chỉ đăng 1 tin → **không có "ông lớn" nào thống trị**; phải nộp rải, không dồn vào 5 công ty.
- **Toàn bộ pack này chỉ dùng tin tại TP.HCM** (yêu cầu của Hoàn, 20/11/2026). Không có phương án địa lý khác, không có "lựa chọn thứ hai" ở tỉnh/thành khác.
- Ngân hàng = 19% → **phải có ngân hàng trong danh sách mục tiêu**, dù vòng tuyển của họ chậm hơn.

---

## 9. Trả lời H3 — "phỏng vấn gồm LeetCode + system design + bài toán doanh nghiệp + tiếng Anh"

**Kết luận: ĐÚNG MỘT PHẦN, và phần đúng quan trọng hơn phần sai.**

| Thành phần | Với fresher/junior thực tế | Bằng chứng |
|---|---|---|
| **Tiếng Anh** | ✅ **Có, gần như luôn** — kể cả phỏng vấn bằng tiếng Anh | 93,7% tin đòi English (S1); CMC Fresher Techie phỏng vấn **hoàn toàn bằng tiếng Anh** + live coding (S12, S19); FPT/CMC miễn test ngoại ngữ nếu TOEIC 650+/IELTS 6.0+ |
| **Bài test đầu vào (trắc nghiệm + tự luận)** | ✅ **Có, phổ biến** — Programming, Database, IQ, Logic | S12 (CMC) |
| **Coding test** | ✅ **Có, nhưng nhẹ** — 3 bài coding (FPT), live coding (CMC) | S20 (Voz: "test Java gồm 3 bài coding"), S19 |
| **LeetCode khó / thuật toán nâng cao** | ⚠️ **Ít** — chủ yếu easy, đôi khi 1 medium | S18 ("Core Java và Collections được hỏi ở cả ba cấp độ"; "Fresher Java có cần biết Spring Boot? Nên biết ở mức tạo REST API đơn giản, nhưng Core Java vẫn được hỏi kỹ hơn") |
| **System design** | ❌ **Hiếm ở fresher** | Không có trong bất kỳ review fresher nào đọc được; chỉ xuất hiện ở mid+ |
| **Bài toán doanh nghiệp / domain** | ⚠️ **Có ở vòng khách hàng** (outsourcing) | S19: "Nội dung vòng khách hàng có thể phụ thuộc domain của client" |
| **IQ test** | ⚠️ Có ở một số công ty (Hàn, Nhật) | S20: 13 câu/12 phút |

**Kết luận cho Hoàn:** ưu tiên ôn **Core Java + OOP + SQL + Spring Boot cơ bản + tiếng Anh nói**. **Không** cần luyện LeetCode hard hay system design ở giai đoạn này — điều đó sẽ đánh đổi bằng thời gian ôn Spring Boot, thứ được hỏi trực tiếp.

---

## 10. Năm kết luận và "so what"

| # | Kết luận | Độ tin cậy | **Hoàn nên làm gì** |
|---|---|---|---|
| 1 | Java là stack lớn nhất nhưng junior chỉ 5%, fresher không có mục riêng | Cao | **Ở lại Java** (đúng), nhưng **không** chỉ nộp qua job board |
| 2 | Go = 18 tin, 29% của Java | TB-Cao | **Không quay lại Go** trong 12 tháng tới |
| 3 | 93,7% tin đòi tiếng Anh; IELTS 6.5 đủ để **miễn test ngoại ngữ** ở nhiều chương trình fresher | Cao | Dùng IELTS 6.5 làm **vũ khí hồ sơ**, và luyện **nói** (điểm yếu thật: S 6.0) |
| 4 | Fresher thật: 10–15 triệu; 19–20 triệu là mức của junior có 6–12 tháng KN + Spring | Cao | Đặt kỳ vọng 10–15 triệu cho offer đầu; **không** nhận 3–5 triệu không hợp đồng |
| 5 | Ngân hàng/fintech = 19% tin, backend lâu nhất 29 ngày, 202 công ty chỉ 1 tin | Cao | Nộp **rải 10–15 công ty/tuần**, có ngân hàng trong danh sách |

---

## 11. Quyết định đề xuất (Phase 2)

**Đề xuất:** giữ **Java/Spring Boot** làm hướng duy nhất; định vị bản thân là **"fresher backend Java có tiếng Anh B2 và GPA 8.74"**; nộp **rải qua trang công ty + chương trình fresher** thay vì chờ job alert.

**Vì sao:** Java = 8,3% tin (lớn nhất), backend = 19% (lớn nhất), Go chỉ 2,4% và toàn senior, và tiếng Anh + GPA là hai tài sản Hoàn có thật mà phần lớn fresher khác không có.

**Điều gì sẽ khiến tôi đổi ý:**
- Nếu sau **60 đơn Java** (khoảng 6–8 tuần) mà **0 phỏng vấn** → chuyển sang **.NET** (26 tin, 3,5%, và Hoàn đã có IT-Tools). **QA/tester không còn là phương án** (Hoàn chốt 20/11/2026 là không làm tester).
- Nếu **sau 8 tuần không có tin Java fresher nào mới tại TP.HCM** → mở rộng *loại công việc* (intern có lương/support/implementation tại TP.HCM), **không** mở rộng địa lý và **không** nhận tester.

---

## 12. Điều báo cáo này **không** nói được

1. **Không** biết có bao nhiêu tin fresher Java thật ở TP.HCM ngoài ITviec (TopCV/CareerViet/trang công ty chưa đếm hết).
2. **Không** biết LinkedIn có bao nhiêu tin (bị chặn) → H9 chỉ trả lời được bằng suy luận.
3. **Không** có tỷ lệ đậu phỏng vấn của fresher (không nguồn nào công bố).
4. **Không** đo được "tin ma" (đăng cho có) — chỉ suy ra từ median 29 ngày.
5. **VietnamWorks chỉ đủ 42 tin khi đã đăng nhập** (khách: 9 thẻ); **TopDev** vẫn mỏng (9 tin, 8/9 khoá lương) → không dùng hai sàn này để suy ra mặt bằng lương.
