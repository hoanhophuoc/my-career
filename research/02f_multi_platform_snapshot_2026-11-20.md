# 02f — Bốn sàn còn lại: Glints · TopDev · VietnamWorks · NodeFlair

**Ngày crawl:** 20/11/2026 · **Phạm vi:** việc làm IT tại **TP.HCM** · **Người thực hiện:** Buffy (agent)

> Mục đích: trả lời câu "TopDev, VietnamWorks, Glints, JobStreet, NodeFlair nữa đâu?" sau khi đã crawl ITviec (`02e_*`) và LinkedIn (`02d_*`).
> Cách làm: đọc trang công khai, **không đăng nhập** (trừ ITviec ở file khác), không lưu thông tin cá nhân nào ngoài dữ liệu tin đăng.

---

## 1. Kết quả tổng: 4 sàn, thu được gì

| Sàn | Truy cập được? | Tin lấy được | Tin TP.HCM | Lương hiện ra | Kết luận |
|---|---|---|---|---|---|
| **Glints** | ✅ SSR (`__NEXT_DATA__`) | **86** | **86** | **47 (54,7%)** | **Nguồn tốt nhất trong 4 sàn** — xem mục 2 |
| **TopDev** (nay là **Saramin**) | ⚠️ render bằng JS | **8** | 1 | 1 (`Thu nhập từ 400–550 triệu/năm`, tin Hà Nội) | Sàn đã đổi thương hiệu, kho Java rất mỏng, **lương khoá sau đăng nhập** |
| **VietnamWorks** | ✅ **đã đăng nhập → đủ 41** | **41** | **10** | **11 (26,8%)** | Khách chỉ thấy 9 thẻ; sau đăng nhập + cuộn render đủ 42. Nhưng **10 tin TP.HCM, chỉ 2 tin HCM có lương, 0 tin fresher** — vẫn **không phải kênh chính** |
| **NodeFlair** | ✅ trang mở được | **0** | 0 | — | Tìm `java` + Việt Nam trả **0 kết quả**; `/vn/jobs` trả 404 |
| **JobStreet VN** | ❌ (sàn VN **đã ngừng**) | 3 | **0** | — | `jobstreet.vn` → **redirect sang jora.com**; chỉ còn danh sách xuyên biên giới trên `ph.jobstreet.com` — toàn tin **remote**, không có tin onsite TP.HCM |

Tổng dữ liệu mới: **138 tin** (86 Glints + 8 TopDev + **41** VietnamWorks + 3 JobStreet), trong đó **97 tin TP.HCM**. *(Đã lọc bỏ toàn bộ tin tester khỏi dữ liệu thô — Glints mất 5, JobStreet mất 1.)* VietnamWorks là sàn duy nhất trong 4 sàn **tăng được số tin nhờ đăng nhập** (9 → 42).

---

## 2. Glints — phát hiện quan trọng nhất của đợt này

Glints trả toàn bộ danh sách trong `__NEXT_DATA__` (30 tin/trang, có phân trang), **không cần đăng nhập**, và **hiện lương ở 54,7% tin** — gấp gần **2,6 lần** ITviec sau đăng nhập (23,5%) và **38 lần** LinkedIn (1,6%).

### 2.1 Con số

| Chỉ số | Giá trị |
|---|---|
| Tin thô thu được (4 từ khoá × tối đa 6 trang, sau khi lọc role) | **86** |
| Công ty khác nhau | **72** |
| Tin **đúng là IT** (lọc theo tiêu đề + kỹ năng) | **53** |
| Trong 50 tin IT: **yêu cầu 0–1 năm kinh nghiệm** | **24** |
| Trong 24 tin đó: **có lương** | **10** |
| Trung vị lương (điểm giữa dải) của 10 tin | **~25 triệu/tháng** |
| Khoảng lương | **6 – 50 triệu** |

### 2.2 Kỹ năng trong 50 tin IT TP.HCM

| Kỹ năng | Số tin | % |
|---|---|---|
| Java (tag) | 26 | 52% |
| **SQL** | 20 | 38% |
| **Spring** | 7 | 13% |
| English (ghi trong tag) | 3 | 6% |

**Đọc con số này cho đúng:** Glints là sàn **đa ngành**, từ khoá `java` khớp cả văn bản JD, nên 86 tin thô có lẫn việc không phải IT (AutoCAD, customer service, giáo viên coding). Vì vậy phải lọc về 53 tin IT trước khi kết luận, và **tỉ lệ Spring 13% ở đây thấp hơn ITviec (35%)** không có nghĩa là Spring ít được dùng — chỉ có nghĩa là **Glints gắn tag kém đầy đủ hơn**.

### 2.3 Địa bàn (50 tin IT)

Quận 1 (9) · Quận 3 (8) · Phú Nhuận (8) · Tân Bình (5) · Quận 2 (5) · Thủ Đức (5) · Bình Thạnh (4) · Quận 7 (3).
→ Toàn bộ nằm trong bán kính đi làm được bằng xe máy từ trung tâm; không có tin ở Bình Dương/Đồng Nai.

### 2.4 Hình thức

Onsite **44** · Hybrid **9** · Remote **0** trong nhóm IT.

### 2.5 Tám tin đáng nộp nhất (trong `02f_glints_shortlist_2026-11-20.csv`)

| Tin | Công ty | KN yêu cầu | Lương |
|---|---|---|---|
| PYTHON SOFTWARE ENGINEER (Junior / Fresher) | Pi Associates | 1 năm | 15–50 triệu |
| Nhân Viên Lập Trình Java | Gsoft | 1 năm | 15–20 triệu |
| Full Stack Developer | New Day | 1 năm | 18–25 triệu |
| MIDDLE LEVEL MOBILE & WEB DEVELOPER | Tizo Việt Nam | 1 năm | 17–25 triệu |
| Software Engineer – Back End | Edtronaut | 0 năm | không công bố |
| Software Engineer Intern – Fullstack | Edtronaut | 0 năm | không công bố |
| Software Developer – Intern | Bouygues Construction IT | 0 năm | 6,0–6,6 triệu |

> **Lưu ý về lương:** dải `15–50 triệu` là **dải công ty ghi trong tin**, không phải mức chắc chắn nhận được. Trung vị ~20 triệu của nhóm 0–1 năm **khớp** với benchmark 19–20 triệu (Java junior 0,5–1 năm) trong `02_market_report.md` → hai nguồn độc lập xác nhận nhau.

---

## 3. Ba sàn còn lại: vì sao không dùng được nhiều

### TopDev (đã đổi tên thành Saramin)
- Trang `/jobs/search?keyword=java` render bằng JS, chỉ **9 tin** toàn quốc, **8/9 khoá lương** sau đăng nhập.
- API công khai `api.topdev.vn/td/v2/jobs` trả **9 tin** nhưng thiếu trường mô tả/công ty khi không đăng nhập.
- **Kết luận:** với mục tiêu fresher Java TP.HCM, TopDev **không đáng ưu tiên**; giữ 8 tin trong `02g_topdev_jobs_2026-11-20.csv` làm dấu vết (đã bỏ 1 tin tester).

### VietnamWorks — sau khi Hoàn đăng nhập: **crawl đủ 42 tin**

**Trước đăng nhập** tôi chỉ lấy được **9 thẻ** và tưởng trang bị hỏng. Kiểm tra thêm mới thấy nguyên nhân: trang là SPA, **không có nút phân trang**, và có banner *"Tải app để có trải nghiệm tốt"* — khách bị chặn danh sách đầy đủ.

**Sau khi Hoàn đăng nhập** (20/11/2026): cuộn hết trang → **42/42 thẻ** được render (khớp đúng số trang tự công bố). Lấy đủ 42 tin bằng cách trích DOM thẻ tin, không đụng vào API riêng.

| Chỉ số | Giá trị |
|---|---|
| Tin thu được | **42 / 42** (đầy đủ) |
| Tin tại **TP.HCM** | **10** |
| Tin hiện lương | **11 (26,8%)** |
| Trong 10 tin TP.HCM: có lương | **2** |
| Tin junior/fresher/middle | **6** (nhưng **0 tin fresher thật**, và **0 tin fresher tại TP.HCM**) |
| Trung vị lương (11 tin có lương) | **~30 triệu/tháng** |

**Đọc kết quả:** VietnamWorks nghiêng hẳn về **Hà Nội** (22/42 tin) và về **bank/chứng khoán** (VietinBank, MB Bank, VPBank, BIDV MetLife, Woori, Shinhan, KIS, MB Securities, An Bình…). Tại TP.HCM chỉ có 10 tin, trong đó:

- **Backend Java dùng được:** *Java Backend Developer* (KIS Việt Nam), *Back-end Developer (Java, SQL, Spring, English/Chinese)* (Clever Creations, **$500–1.500**), *Senior Backend Engineer (Java)* (VINSMART Future), *Java Developer (AI-Driven Development)* và *Java Development Assistant Manager* (Shinhan), *CG Phát Triển Giải Pháp CNTT* (VPBank, **$500**).
- **Không phải backend:** IT BA (Bảo hiểm Toàn Cầu), IT BA (Shinhan Bank), IT Specialist (COSCO — đòi tiếng Trung), Technical Lead (RT Holdings).
- **0 tin ghi rõ fresher/0–1 năm tại TP.HCM.**

**Kết luận:** VietnamWorks **không phải kênh chính** cho fresher backend Java TP.HCM, nhưng **không còn là "vô dụng"** như tôi ghi lúc chưa đăng nhập: 6 tin backend Java TP.HCM là **danh sách nộp thêm** đáng đọc, đặc biệt Clever Creations (dải lương thấp, chấp nhận tiếng Anh/Trung) và VPBank (gói $500). Dữ liệu đầy đủ: `02h_vietnamworks_jobs_2026-11-20.csv` (42 dòng), shortlist `02h_vietnamworks_shortlist_2026-11-20.csv` (6 tin).

### NodeFlair
- `nodeflair.com/jobs?query=java&locations=Vietnam` → **0 việc làm** ("Xin lỗi, chúng tôi không tìm thấy kết quả nào").
- `nodeflair.com/vn/jobs` → **404**. Trang tự mô tả là "tổng hợp từ các trang tìm việc phổ biến".
- **Kết luận:** NodeFlair **không có dữ liệu Việt Nam** ở thời điểm 20/11/2026 — không dùng làm nguồn.

### JobStreet — sàn Việt Nam **đã ngừng hoạt động**

Đây không phải "bị chặn" như tôi ghi lần trước, mà là **không còn tồn tại**. Bằng chứng thu được ngày 20/11/2026:

| Kiểm tra | Kết quả |
|---|---|
| DNS `vn.jobstreet.com` | **Không phân giải được** (NXDOMAIN) — subdomain VN không tồn tại |
| `https://jobstreet.vn` và `https://www.jobstreet.vn` | **HTTP 200 nhưng redirect sang `au.jora.com`** ("Job Search Australia \| Jora") |
| `vn.jora.com` (site VN cũ của Jora) | redirect sang **`au.jora.com`** — không còn bản Việt Nam |
| `www.jobstreet.com/vn` | **404** |
| `ph.jobstreet.com/java-jobs/in-Vietnam` | **200 — 5 tin** (qua được Cloudflare bằng trình duyệt thật) |
| `ph.jobstreet.com/backend-jobs/in-Vietnam` | **200 — 4 tin** (trùng 3 tin với danh sách trên) |

**Đọc kết quả:** JobStreet từng thuộc SEEK Asia (có mặt ở VN từ 2012), nhưng đến 20/11/2026 **không còn site Việt Nam**: tên miền VN redirect sang Jora Australia, và tin "Việt Nam" chỉ còn xuất hiện trong danh sách **xuyên biên giới** của JobStreet Philippines.

3 tin thu được (file thô đã xoá cùng sàn — xem dòng CHANGELOG 20/11/2026) — **không tin nào dùng được cho mục tiêu của Hoàn**:

- Toàn bộ ghi địa điểm **`Vietnam (Remote)`** — không có tin onsite TP.HCM.
- Các tin tuyển dụng/SEO/sales đã bị bộ lọc role loại từ dữ liệu thô.
- Phần còn lại là remote xuyên biên giới (Full Stack Intern, ServiceNow CSM…), trả USD/SGD.
- **0 tin backend Java onsite**.

**Kết luận:** bỏ JobStreet khỏi danh sách nguồn. Nếu sau này cần tin remote quốc tế trả USD/SGD thì `ph.jobstreet.com` là một cửa, nhưng **không phải** kênh tìm việc tại TP.HCM.

---

## 4. Ba sàn lớn trùng nhau rất ít (đây là lý do phải đọc nhiều sàn)

| Cặp sàn | Công ty trùng | Tỉ lệ |
|---|---|---|
| ITviec ↔ LinkedIn | **11** | 11/163 công ty LinkedIn (6,7%) |
| Glints ↔ LinkedIn | **4** | 4/163 (2,5%) |
| Glints ↔ ITviec | **1** | 1/55 (1,8%) |

Danh sách đầy đủ: `02i_cross_platform_companies_2026-11-20.csv` (Ekino Vietnam và TMA Solutions có mặt ở cả ba sàn).

**Hệ quả thực dụng:** nộp đơn chỉ trên một sàn = bỏ lỡ **90%+** công ty. Trình tự nên dùng: **ITviec** (cấu trúc level rõ) → **Glints** (lương công khai, nhiều tin entry) → **LinkedIn** (nhiều công ty nhất, ít lương) → TopDev/VietnamWorks chỉ để kiểm tra chéo.

---

## 5. Giới hạn của đợt crawl này

1. **Một ngày, một thời điểm**; tin trôi theo ngày, không đại diện cả quý.
2. **Glints lọc theo `country=VN` rồi tự lọc TP.HCM** — sàn không cho lọc thành phố bằng tham số, nên 86 tin là kết quả của 4 từ khoá × 6 trang, **không phải toàn bộ** tin Java của Glints.
3. **VietnamWorks cần đăng nhập**: khách chỉ thấy **9/42** thẻ; sau đăng nhập + cuộn mới đủ 42. Số 42 khớp số trang tự công bố, nhưng vẫn có thể có tin Java không lọt vào từ khoá `java`.
4. **TopDev/Saramin**: 7/8 tin khoá lương → không dùng để suy ra mặt bằng lương.
5. **Không có tin nào được xác minh còn hạn** bằng cách mở từng JD; "còn hạn" dựa vào ngày đăng trên trang danh sách.
6. Không lưu tên/email/SĐT người tuyển dụng (R10).

---

## 6. Việc nên làm tiếp (đề xuất, không tự làm)

- Glints: thêm 3–4 từ khoá (`java fresher`, `backend intern`, `spring boot`, `java junior`) và chạy lại **hàng tuần** — đây là nguồn có tỉ lệ lương công khai cao nhất.
- JobStreet: **bỏ** — sàn VN đã ngừng, chỉ còn tin remote xuyên biên giới (đã kiểm tra, xem mục 3).
- NodeFlair: **bỏ** — không có dữ liệu VN.
- VietnamWorks: **đã xong** sau khi Hoàn đăng nhập (42/42 tin). Nếu muốn theo dõi, chạy lại **hàng tuần** bằng phiên đã đăng nhập.
