# Ảnh chụp thị trường — LinkedIn Jobs (20/11/2026)

**Mục đích:** trả lời một câu duy nhất — *trong 90 ngày gần nhất, ở TP.HCM, có bao nhiêu việc Java/Spring Boot mà một fresher thật sự nộp được, và đó là những tin nào?*

**Phạm vi:** 392 tin unique · 163 công ty · 10 từ khoá · 20/11/2026.
*Đã lọc bỏ **143 tin tester/QA/QC** khỏi dữ liệu thô theo yêu cầu "không làm tester" (550 → 407); mọi tỉ lệ dưới đây tính lại trên mẫu 407 tin.*

---

## 0. TL;DR — 5 dòng

1. **392 tin** unique (**đã bỏ 143 tester + 15 role khác**), nhưng chỉ **111 (28,3%)** là "chạm tới được" (không phải senior + đòi ≤2 năm kinh nghiệm); riêng Java/Spring còn **46 tin**.
2. **45,7% (179/392)** tiêu đề đã là senior/lead/principal/manager → nửa thị trường hiển thị là không dành cho fresher.
3. **LinkedIn không phải nguồn lương**: chỉ **7/392 (1,8%)** tin có con số lương dùng được; phần lớn ghi "Base pay range" mà không có số.
4. Cửa thật cho fresher là **chương trình đầu vào** (Netcompany *Talented IT Graduates*, EPAM *Hire-to-Train*, KMS *Fresher Test Engineer*, MoMo *Talent 2027*), không phải tin "Junior Java Developer" đăng lẻ.
5. **DXC** đăng nhiều nhất (16 tin chạm tới được) nhưng **7/16 đòi tiếng Trung/Nhật** — nếu không có ngoại ngữ 3, DXC co lại còn ~9 tin. Toàn thị trường có **41 tin** đòi ngoại ngữ thứ ba như điều kiện.

---

## 1. Cách lấy dữ liệu (và vì sao hợp lệ)

- Dùng **API công khai dành cho khách** của LinkedIn: `linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search` và `.../jobPosting/{id}` (chính là endpoint trang job công khai gọi, không cần đăng nhập).
- **Không dùng cookie, không dùng mật khẩu, không đăng nhập thay Hoàn.** Phiên đăng nhập của Hoàn chỉ dùng để mở trang; dữ liệu lấy qua endpoint công khai.
- 10 từ khoá × vị trí `Ho Chi Minh City, Vietnam` × lọc `f_TPR=r7776000` (= **90 ngày**), phân trang 10 tin/trang.
- Giãn cách **0,6–0,7 giây/request**, tự lùi khi bị 429 → không đập vào server.
- Script: `tools/crawl_linkedin_jobs.py` (crawl) và `tools/analyze_linkedin_jobs.py` (chấm điểm). Chạy lại được bất cứ lúc nào.

**Từ khoá:** java · spring boot · backend developer · java fresher · java intern · software engineer · .net developer · qa automation · tester · backend engineer · java developer.

---

## 2. Con số

| Chỉ số | Giá trị | Tỷ lệ |
|---|---|---|
| Tin unique | **392** | 100% |
| Công ty khác nhau | **168** | — |
| Ở TP.HCM | 404 | 99,3% |
| Tiêu đề senior/lead/principal/manager/architect | 185 | **45,5%** |
| Có tín hiệu intern/fresher/junior (tiêu đề hoặc mô tả) | 116 | 28,5% |
| Nhãn "Entry level" của LinkedIn | 29 | 7,1% |
| Nhãn "Internship" | 7 | 1,7% |
| Nhãn "Associate" | 28 | 6,9% |
| **Chạm tới được** (không senior + ≤2 năm KN) | **111** | **28,3%** |
| → trong đó Java/Spring | **46** | 11,3% (20,8% của nhóm tin Java) |
| → trong đó QA/SDET | **0** | **Đã xoá toàn bộ 143 tin tester/QA/QC khỏi dữ liệu thô (20/11/2026)** |
| Nhắc Java | 221 | 54,3% |
| Nhắc Spring (bất kỳ) / Spring Boot | 87 / **75** | 21,4% / 18,4% |
| Nhắc SQL | 134 | 32,9% |
| Nhắc English | 256 | 62,9% |
| Nhắc Docker / Kubernetes | 114 / 97 | 28,0% / 23,8% |
| Có số lương dùng được | **7** | **1,7%** |
| Đòi ≥3 năm kinh nghiệm (đọc trong JD) | 255 | 62,7% |
| Không ghi số năm nào | 99 | 24,3% |

**Top công ty theo số tin chạm tới được:** DXC 11 · EPAM 7 · Astek 4 · OPSWAT 4 · Alignerr 4 · MoMo 3 · Deloitte 3 · Hitachi Digital Services 3 · Ampere 3 · Qualcomm 3.

**7 tin có lương thật (dùng được):**

| Lương ghi trong JD | Vị trí | Công ty |
|---|---|---|
| 15.000.000–25.000.000 VND | Lập trình viên ERP (Odoo) | Majorbird Group |
| 15.000.000–25.000.000 VND | Confirmed ERP Developer | Majorbird Group |
| $1.000 | JavaEE Developer (EJB, English) | CEVA Logistics |
| USD 5.000 | Mid–Senior Python Backend Developer | CJ OliveNetworks Vina |
| USD 2.000 | Senior/Staff/Principal Engineer | Canonical |
| (2 tin còn lại là bản sao của Majorbird) | | |

---

## 3. Bốn phát hiện

**F1 — "Junior" trên LinkedIn thường không phải junior.** Ví dụ thật trong dữ liệu: *"Java Software Engineer (**4+ YOE**)"* và *"Lập trình viên Java (**Từ 4-5 năm KN**)"* đều bị LinkedIn gắn nhãn **Entry level**; *"Backend Engineer"* của LINE Vietnam gắn Entry level nhưng JD đòi 5 năm. → **Không bao giờ lọc theo nhãn cấp bậc của LinkedIn**; phải đọc số năm trong JD. Đây là lý do tôi lọc lại bằng regex số năm (bỏ 341 tin đòi ≥3 năm).

**F2 — Kênh fresher thật là "chương trình", không phải tin lẻ.** 4 cửa rõ ràng, tất cả đều **không đòi kinh nghiệm**: Netcompany *Talented IT Graduates* (Entry level, JD Java/.NET/SQL/Oracle), EPAM *Java Engineer (Hire-to-Train Program)*, KMS *Fresher Test Engineer* + *Fresher Full-stack Test Engineer*, MoMo *Talent 2027*. Đăng lẻ "Junior Java Developer" phần lớn là 1–2 năm.

**F3 — Khoảng cách Java vs Spring Boot rộng hơn tưởng tượng.** 221 tin nhắc Java nhưng chỉ **75** nhắc Spring Boot (34%), và trong nhóm chạm tới được chỉ **13/60** tin Java có Spring Boot. Nghĩa là: *Java core + SQL + English* mở được 60 cửa; *Spring Boot* chỉ là điều kiện cộng thêm ở ~1/5 số đó. Điều này khớp với kết luận "Java core trước, framework sau" của Phase 4.

**F4 — Ngoại ngữ thứ ba là bộ lọc thật.** DXC (công ty đăng nhiều nhất) có 7 tin đòi **tiếng Trung (Mandarin)** hoặc **tiếng Nhật N2/N3**; ILA tuyển *Junior ERP Developer (AX2012)* — Dynamics, không phải Java. Với IELTS 6.5, nhóm tin "English" (363 tin) là nơi Hoàn có lợi thế, nhóm đòi Trung/Nhật nên bỏ qua hoàn toàn trong 12 tháng tới.

---

## 4. Mười hai tin đáng nộp — 48 giờ tới

Đã lọc: không senior + ≤2 năm + Java/Spring/.NET + TP.HCM + đăng trong 60 ngày. **Không có tin tester/QA nào** (đã xoá khỏi dữ liệu thô ngày 20/11/2026). Bảng dưới lấy đúng thứ tự `02d_linkedin_shortlist_2026-11-20.csv` (30 dòng) — nếu muốn xem đủ 30 thì mở file đó.

| # | Ưu tiên | Công ty | Vị trí | KN yêu cầu | Đăng | Vì sao nộp | Link |
|---|---|---|---|---|---|---|---|
| 1 | **A** | Amaris Consulting | Fullstack Java Developer (Junior/Middle) | 2 năm | 14/11 | Java + Spring + Spring Boot + MySQL/MongoDB + unit test + English; "2 năm" là mức xin vượt bằng dự án thật | [4466070381](https://www.linkedin.com/jobs/view/4466070381/) |
| 2 | **A** | DXC Technology | Junior Java Developer | không ghi | 09/11 | Spring Boot + Spring MVC + Hibernate + Oracle; **không** đòi Trung/Nhật (khác 7 tin DXC cần tiếng Trung/Nhật) | [4488831588](https://www.linkedin.com/jobs/view/4488831588/) |
| 3 | **A** | Netcompany | Software Developers | 1 năm | 30/10 | Java/.NET/SQL/Oracle/English — trùng đúng 4 thứ Hoàn có; công ty Đan Mạch, phỏng vấn bằng tiếng Anh | [4437682590](https://www.linkedin.com/jobs/view/4437682590/) |
| 4 | **A** | Amaris Consulting | Java Backend Developer (SAP Integration) | 1 năm | 19/11 | JD ngắn, đúng Java + Spring + Spring Boot + REST; "1 năm" xin được bằng dự án | [4491380828](https://www.linkedin.com/jobs/view/4491380828/) |
| 5 | **A** | Netcompany | Talented IT Graduates | không ghi | 16/11 | Chương trình đầu vào fresher, cùng bộ kỹ năng với #3 — nộp được ngay, không cần kinh nghiệm | [4490136970](https://www.linkedin.com/jobs/view/4490136970/) |
| 6 | **A** | DXC Technology | Java Software Engineer | 1 năm | 09/11 | Java + Spring + Spring Boot + unit test, tiếng Anh — bản "không cần tiếng Trung" của DXC | [4488828491](https://www.linkedin.com/jobs/view/4488828491/) |
| 7 | B | Wilmar CLV Careers | IT Associate (PMO / Dev) | 1 năm | 19/11 | Vừa PMO vừa dev — chỉ nộp nếu chấp nhận 30–50% thời gian làm tài liệu; công ty đa quốc gia, tiếng Anh | [4492297633](https://www.linkedin.com/jobs/view/4492297633/) |
| 8 | B | MoMo (M_Service) | MoMo Talent 2027 | 2 năm | 19/11 | Chương trình talent tuyển sớm cho 2027; Java + Docker + REST; 2 năm là **xin vượt** | [4491385564](https://www.linkedin.com/jobs/view/4491385564/) |
| 9 | B | Endava | Junior Cloud Native Developer | không ghi | 17/11 | Java + Kafka + Kubernetes + Docker; "Junior" thật nhưng là cloud-native nên cần thêm Docker/K8s | [4491128162](https://www.linkedin.com/jobs/view/4491128162/) |
| 10 | C | ILA Vietnam | Junior ERP Developer (AX2012) | 1 năm | 18/11 | .NET/C# + SQL — dự bị .NET; là Dynamics AX nên **không** dùng để học Java | [4490840936](https://www.linkedin.com/jobs/view/4490840936/) |
| 11 | C | CEVA Logistics | Dotnet Developer (Azure, English) | 1 năm | 19/11 | .NET + Azure + Docker + CI/CD — dự bị .NET có cloud, đúng hướng "chân thứ hai" | [4491383484](https://www.linkedin.com/jobs/view/4491383484/) |
| 12 | C | Nexlab Technology | Intern AI Software Engineer | không ghi | 03/11 | Intern có Java + AWS + Docker + CI/CD; tên có "AI" nhưng JD là software engineer — chỉ nộp nếu chấp nhận mảng AI | [4486867230](https://www.linkedin.com/jobs/view/4486867230/) |

**Bỏ qua có chủ ý:** (a) **toàn bộ tin tester/QA/QC** — 143 tin đã xoá khỏi dữ liệu thô (KMS Test Engineer, Eurofins Test Automation…) vì Hoàn không làm tester; (b) tin DXC "Mandarin Speaking"/"Junior Java Developer (Mandarin)"/"Kỹ Sư Phần Mềm (N3/N2)" (7 tin) — cần tiếng Trung/Nhật, Hoàn chỉ có Anh/Việt; (c) *Junior Product Engineer* GoTymeX — đăng từ 18/9, có thể đã đóng.

---

## 5. So với ITviec (crawl cùng ngày 20/11/2026)

| | ITviec | LinkedIn |
|---|---|---|
| Tin | 109 | **392** |
| Công ty | 71 | **168** |
| Fresher/junior/intern | 7 (7,5%) | 116 tín hiệu (28,5%) · 64 theo nhãn |
| Senior+ | 63 (68%) | 185 (45,5%) |
| Có lương | 4 (3,7%) | 7 (1,7%) |
| Trùng công ty | **11/168** (Katalon, VinSmart Future, VNG Games, Smilegate, Money Forward, HRS Group, Hitachi Digital Services, GoTymeX…) | |

→ Hai nguồn **bổ sung nhau, gần như không trùng** (chỉ 11 công ty chung). Kết luận: phải crawl cả hai; một mình ITviec bỏ sót 90%+ công ty đang tuyển. Cả hai đều **không có dữ liệu lương đủ để kết luận** — con số lương vẫn phải lấy từ báo cáo thị trường Phase 2 (trung vị backend <1 năm: **12,4 triệu**; Java junior 0,5–1 năm: **19–20 triệu gross**).

---

## 6. Giới hạn — điều tôi KHÔNG kết luận được

- **Không phải toàn bộ thị trường.** API khách trả 10 tin/trang và có trần phân trang; tin quá 90 ngày bị loại. Con số thật ngoài LinkedIn lớn hơn 550.
- **Không biết tin còn mở hay đã đóng.** Không mở từng tin để kiểm; dấu hiệu "Be among the first 25 applicants" chỉ là ước lượng.
- **Số năm kinh nghiệm đọc bằng regex** trên JD → có thể sai ở câu kiểu "team of 5 engineers, 3 years old product". Tôi đã chặn giá trị vô lý (>15) nhưng không đọc tay 550 JD.
- **Lương gần như không có.** 1,3% có số; 5 con số dùng được, 2 trong đó là bản sao. Không dùng để tính trung vị.
- **Không kiểm chứng được tin nào sẽ trả lời.** Tỷ lệ phản hồi của fresher trên LinkedIn ở VN không có nguồn công khai — tôi không đưa ra con số.
- **Chưa nộp tin nào.** Toàn bộ 12 tin trên là *đề xuất* (lấy từ shortlist 30 dòng), chưa có đơn nào được gửi.

---

## 7. Checkpoint

- Đã có 392 tin + 163 công ty. Theo cách tính **tái lập được** trong `tools/02_stats.py` (`reachable` = level không phải mid-senior và tiêu đề không có senior): **153 tin reachable, trong đó 63 tin Java/Spring**. Con số cũ "45 tin" dùng thêm điểm số từ mô tả JD — mô tả đã bị đưa ra khỏi repo (P0-1) nên không tái lập được.
- 45,5% tin là senior → nửa thị trường hiển thị không dành cho fresher; đây là số đo, không phải cảm nhận.
- Nhãn "Entry level" của LinkedIn sai thường xuyên → mọi lần lọc sau này phải đọc số năm trong JD.
- Cửa thật: 4 chương trình đầu vào (Netcompany, EPAM, KMS, MoMo) + 3 tin Java "1 năm".
- Spring Boot chỉ xuất hiện ở một phần nhỏ tin Java reachable → Java core + SQL vẫn là ưu tiên học.
- Lương trên LinkedIn vô dụng (1,7%) → giữ số của Phase 2, đừng trích LinkedIn.
- Hai nguồn chỉ trùng 11 công ty → crawl cả ITviec và LinkedIn là bắt buộc.

**Quyết định đề xuất:** nộp **4 tin Java/Spring đầu bảng** (#1–#4) trong 48 giờ, dùng đúng bộ hồ sơ Phase 7 (1 CV gốc + slot Java backend), và **không** nộp nhóm B/C cho tới khi có 1 dự án Spring Boot chạy thật.

**Vì sao:** 4 tin đầu là những tin Java/Spring duy nhất trong 392 mà JD không đòi quá 1 năm *và* có Java/Spring thật; nộp sớm trong 60 ngày đầu tin đăng là lợi thế duy nhất fresher có.

**Điều gì khiến tôi đổi ý:** nếu 4 tin đầu im lặng >14 ngày → hạ xuống nhóm B (Java "1 năm" + .NET dự bị), **không** dùng tin tester (đã loại 20/11/2026); hoặc nếu CoolWear (.NET, 10.403 LOC) được viết bullet CV xong trước → thêm CEVA *Dotnet Developer (Azure, English)* và Netcompany *Software Developers* vào danh sách nộp.
