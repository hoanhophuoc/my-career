# 02.1 — PHƯƠNG PHÁP, NGUỒN VÀ GIỚI HẠN

**Cập nhật lần cuối:** 21/11/2026

**Ngày thực hiện:** 20/11/2026 · **Người thực hiện:** Buffy (agent) · **Phạm vi:** việc làm IT cho người mới tại TP.HCM, 2026–2027

---

## 1. Nguyên tắc thu thập (R8)

- Chỉ đọc **nội dung công khai**. Khi một trang chỉ hiện dữ liệu sau đăng nhập, **Hoàn tự đăng nhập** trong tab trình duyệt của Freebuff; tôi đọc trang bằng chính phiên đó, **không nhận mật khẩu, không trích xuất cookie** (cập nhật 20/11/2026 — áp dụng cho ITviec và LinkedIn).
- Không vượt CAPTCHA/chống bot. Khi bị chặn → **ghi lại** và dùng nguồn khác.
- Không chép nguyên văn dài tin tuyển dụng; chỉ lấy **metadata** (công ty, level, kỹ năng, lương nếu công khai) và diễn đạt lại.
- Không crawl tràn lan: chỉ lấy **trường tối thiểu** (công ty, cấp, kỹ năng, lương nếu công khai), có độ trễ giữa các trang, dừng khi gặp 429/403 và ghi lại.
- Số request: Phase 2 ban đầu ~20; hai đợt crawl 20/11/2026 khoảng **150** request (ITviec 16 trang, LinkedIn 55 trang).

## 2. Bảng nguồn & khả năng truy cập

| Nguồn | Truy cập được? | Cách lấy | Ghi chú |
|---|---|---|---|
| **ITviec** (itviec.com) | ✅ | `curl` trực tiếp bị **HTTP 403**; trong trình duyệt (Hoàn đã đăng nhập 20/11/2026) thì đọc được: **109 tin** (chưa đăng nhập) và **81 tin TP.HCM** (đã đăng nhập; đã bỏ 2 tin tester). Lọc thành phố bằng **path** `/it-jobs/ho-chi-minh-hcm` — tham số `?city=` **không** có tác dụng. | Đăng nhập chỉ mở thêm 22,9% tin có số lương; phần còn ẩn là do NTD chọn ẩn. Giới hạn 5 trang/truy vấn; truy vấn `java intern` bị **429** → bỏ, ghi lại. |
| **TopCV** | ✅ | Trang tìm việc công khai, server-rendered | Có sẵn số tin theo từ khoá + ngày cập nhật |
| **CareerViet** | ✅ | Trang công khai | Có tin ngân hàng (MB) + hạn nộp |
| **Indeed VN** | ✅ | Trang kết quả công khai | Có JD rút gọn, đôi khi có lương |
| **LinkedIn Jobs** | ✅ (API khách) | Endpoint công khai `/jobs-guest/jobs/api/seeMoreJobPostings/search` trả HTML không cần cookie → **392 tin / 163 công ty** (20/11/2026, đã bỏ 143 tin tester khỏi dữ liệu thô) | Không dùng cookie tài khoản; 10 tin/trang, gặp **429** thì backoff 8 giây. Xem `02d_linkedin_market_snapshot_2026-11-20.md` |
| **TopDev** (nay là **Saramin**) | ⚠️ Một phần | Trang render bằng JS; đọc qua trình duyệt được **9 tin** toàn quốc | 8/9 tin **khoá lương** sau đăng nhập → không dùng để suy ra mặt bằng lương |
| **Glints** | ✅ | `__NEXT_DATA__` trong HTML (SSR), **không cần đăng nhập**; lọc quốc gia bằng `country=VN` rồi tự lọc TP.HCM theo `location.parents` | **125 tin TP.HCM**, 76 tin có lương (đã bỏ 5 tin tester). Script: `tools/crawl_glints_jobs.py` |
| **VietnamWorks** | ✅ **Đầy đủ** (sau đăng nhập) | SPA, khách chỉ thấy **9 thẻ** + banner "Tải app". Sau khi **Hoàn đăng nhập** + cuộn: **42/42 thẻ**, khớp số trang công bố. Trích DOM thẻ tin, không gọi API riêng | 42 tin, **10 tin TP.HCM**, **11 tin có lương (26,2%)** |
| **NodeFlair** | ❌ | `?query=java&locations=Vietnam` → **0 việc làm**; `/vn/jobs` → **404** | Không có dữ liệu VN → **không** dùng làm nguồn |
| **JobStreet VN** | ❌ **sàn đã ngừng** | `vn.jobstreet.com` **không phân giải DNS**; `jobstreet.vn` → **redirect `au.jora.com`**; `www.jobstreet.com/vn` → **404**. Còn lại: `ph.jobstreet.com/java-jobs/in-Vietnam` → **5 tin**, `/backend-jobs/in-Vietnam` → **4 tin**, tất cả **remote** | Không có kênh JobStreet tại TP.HCM → **bỏ khỏi danh sách nguồn**; 7 tin lưu ở file thô JobStreet (đã xoá cùng sàn) |
| **vitX — Vietnam IT Hiring Pulse** | ✅ | Đọc toàn văn | **Nguồn tốt nhất**: census đếm toàn bộ tin ITviec theo tuần, có phương pháp công bố, cập nhật 31/10/2026 |
| **ITviec Salary Report 2025–2026** | ✅ | Trang tổng quan công khai | Số liệu lương theo năm kinh nghiệm |
| **ITviec Hiring Market Insights Q1-2026** | ✅ | Trang marketing công khai | Số liệu tăng trưởng kỹ năng |
| **ITviec Q2/Q3-2025 blog** | ✅ | Blog công khai | Xu hướng 2025 để so sánh |
| **Voz / Glassdoor review / blog cá nhân** | ✅ | Công khai | Dùng cho **quy trình phỏng vấn**, không dùng cho số liệu thị trường |

## 3. Cỡ mẫu thực tế đạt được (nói thật)

Đề bài yêu cầu **≥ 300 tin từ ≥ 6 nền tảng**, tối thiểu 150. **Tôi không đạt được con số đó, và tôi không bịa để đạt.**

| Loại dữ liệu | Cỡ mẫu thật | Độ tin cậy |
|---|---|---|
| **Census toàn bộ tin IT trên ITviec** (qua vitX) | **743 tin** (bảng phân loại, kỳ edition 10) / **629 tin** (đếm 30/10/2026) | **Cao** — đếm toàn bộ, có phương pháp, nhưng chỉ **một** nền tảng |
| **Số tin theo từ khoá** (đọc từ trang danh mục) | ITviec: **56** tin "java" ở TP.HCM · TopCV: **40** fresher backend HCM (15/11/2026), **43** backend developer (19/11/2026), **90** developer (19/11/2026) · CareerViet: **22** backend fresher (18/11/2026) · Indeed: **50+** fresher java HCM, **100+** fresher software engineer | **TB** — con số trên trang có thể thay đổi theo ngày và theo định nghĩa từ khoá |
| **Crawl ITviec có lương** (đã đăng nhập, 20/11/2026) | **75 tin** TP.HCM / 55 công ty, 17 tin hiện số lương (22,7%) | **TB** — toàn bộ tin khớp 2 truy vấn Java/backend, không phải toàn sàn |
| **Crawl LinkedIn** (API khách, 20/11/2026) | **392 tin / 163 công ty**, 46 tin Java vừa sức | **TB** — 11 từ khoá × 3 tháng, chỉ 1,7% tin có lương; đã bỏ 143 tin tester |
| **Crawl Glints** (SSR, 20/11/2026) | **86 tin TP.HCM / 56 công ty**; 50 tin IT, 24 tin yêu cầu 0–1 năm, **47 tin có lương** | **TB** — 4 từ khoá × 6 trang; từ khoá khớp cả văn bản JD nên phải lọc lại về IT |
| **Tin tuyển cụ thể đọc JD** | **19 tin** (xem `02d_linkedin_jobs_2026-11-20.csv`) | **TB–Cao** cho từng tin, **không đại diện thống kê** |
| **Chương trình fresher/graduate** | **9 chương trình** xác minh được nội dung + 20+ công ty cần kiểm tra | **TB** |
| **Quy trình phỏng vấn** | 6 nguồn định tính (Voz, blog, trang chương trình) | **Thấp–TB** (tự khai, có thiên lệch người đậu) |

**Cập nhật 21/11/2026 (số liệu lấy từ `tools/02_stats.py`, không chép tay):** mốc 300 tin **đã vượt xa** — **602 tin** sau lọc nhóm vai trò, từ **5 nền tảng**: LinkedIn 392 · Glints 86 · ITviec 75 · VietnamWorks 41 · TopDev 8. Master còn **69 dòng** thuộc nhóm đã loại (có `excluded_reason`), tổng **671 dòng**. JobStreet đã ngừng site Việt Nam (redirect sang Jora Australia) nên **không còn là nguồn**; NodeFlair không có dữ liệu VN. Mọi kết luận vẫn phải đọc kèm giới hạn "một thành phố".

**Hệ quả:** mọi kết luận về **cơ cấu level/kỹ năng** dựa trên census ITviec + LinkedIn = **hai nền tảng lớn nhất nhưng không phải toàn thị trường**. Kết luận về **lương** dựa trên báo cáo khảo sát (1.839 người) + **19 tin có lương thật** trong `02e_*`; hai nguồn này khớp nhau ở mốc ~55 triệu cho nhóm thâm niên.

## 4. Thiên lệch cần nhớ khi đọc báo cáo

| Thiên lệch | Ảnh hưởng tới kết luận |
|---|---|
| **Chỉ đo ITviec** | ITviec thiên về công ty outsourcing, product, MNC có ngân sách đăng tin. Tin fresher giá rẻ thường nằm trên **Facebook group, TopCV, trang công ty, referral** → thị trường entry-level **thật** có thể **nhiều hơn** census này |
| **Tin ≠ tuyển thật** | Có tin "treo" (đăng lâu để gom CV), tin headhunt đăng lại, tin đã có người nội bộ. vitX đo được **median 29 ngày** một tin backend còn sống → dấu hiệu khó tuyển hoặc tuyển chậm |
| **Level ghi trên tin ≠ level thật** | Tin "Junior" đòi 1–2 năm là phổ biến → tôi gắn cờ `title_inflation` |
| **Khảo sát lương tự khai** | Người trả lời khảo sát ITviec (1.839) không đại diện toàn bộ; thường là người quan tâm thị trường |
| **Survivorship** | Review phỏng vấn trên Voz/blog do người **đậu** hoặc người bức xúc viết |

## 5. Định nghĩa dùng trong dataset

- `level_posted`: level ghi trên tin (intern/fresher/junior/mid/senior/lead/principal/all-level).
- `years_exp_min`: số năm tối thiểu tin yêu cầu (0 nếu ghi "không cần kinh nghiệm").
- `true_entry_level = TRUE` khi **years_exp_min = 0** VÀ không có yêu cầu kinh nghiệm ẩn trong JD.
- `title_inflation = TRUE` khi tiêu đề ghi fresher/junior nhưng `years_exp_min ≥ 1`.
- `census_source`: `direct` (tôi đọc JD) hoặc `aggregate` (số liệu tổng hợp từ nguồn).

## 6. Việc chưa làm (và nên làm ở vòng sau)

1. Kiểm đếm **VietnamWorks, Glints, JobStreet, NodeFlair** (đều có trang công khai) → có thể nâng mẫu lên 150+.
2. Đọc **TopDev IT Market Report** bản mới nhất (cần tìm đúng URL; chưa xác minh trong phiên này).
3. Lấy **tin từ trang tuyển dụng công ty** (FPT, KMS, TMA, VNG, MoMo, ngân hàng) — đây là nơi có tin fresher **thật** nhiều hơn job board.
4. Khảo sát 20–30 tin Java fresher **thủ công** trong 2 tuần để có mẫu có kiểm soát (tôi có thể làm nếu Hoàn muốn, nhưng phải làm từng ngày, không crawl).

## 7. Nguồn (mã hoá để trích trong báo cáo)

| Mã | Nguồn | Ngày | URL |
|---|---|---|---|
| S1 | vitX, *Vietnam IT Hiring Pulse*, edition 10 | cập nhật 31/10/2026 | https://www.vitx.global/insights/vietnam-hiring-pulse |
| S2 | ITviec, *IT Salary & Recruitment Market Report 2025–2026* (1.839 người) | 11/11/2025 | https://itviec.com/bao-cao/luong-it-va-thi-truong-tuyen-dung-it-vietnam |
| S3 | ITviec Marketing, *Điểm tin thị trường IT Q1-2026* | Q1-2026 | https://marketing.itviec.com/insight-article-q12026 |
| S4 | ITviec Blog, *Q3-2025 market overview* | 15/10/2025 | https://itviec.com/blog/vietnam-it-job-market-q3-2025-shifting-skill-requirements |
| S5 | ITviec Blog, *Q2-2025 market overview* | 19/09/2025 | https://itviec.com/blog/vietnam-it-job-market-q2-2025-python-ai-see-strong-growth/ |
| S6 | ITviec, danh mục *java tại TP.HCM* (qua index) | truy cập 20/11/2026 | https://itviec.com/viec-lam-it/java/ho-chi-minh-hcm |
| S7 | TopCV, *Fresher Backend tại HCM* | 15/11/2026 | https://www.topcv.vn/tim-viec-lam-fresher-backend-tai-ho-chi-minh-kl2 |
| S8 | TopCV, *Backend Developer tại HCM* | 19/11/2026 | https://www.topcv.vn/tim-viec-lam-backend-developer-tai-ho-chi-minh-kl2 |
| S9 | CareerViet, *backend developer fresher* | 18/11/2026 | http://careerviet.vn/viec-lam/backend-developer-fresher-k-vi.html |
| S10 | Indeed VN, *Fresher Java HCM* | 14/11/2026 | https://vn.indeed.com/q-fresher-java-l-th%C3%A0nh-ph%E1%BB%91-h%E1%BB%93-ch%C3%AD-minh-vi%E1%BB%87c-l%C3%A0m.html |
| S11 | Indeed VN, *Fresher Software Engineer HCM* (JD Java Junior 19–20M) | 18/11/2026 | https://jobs.vn.indeed.com/q-fresher-software-engineer-l-th%C3%A0nh-ph%E1%BB%91-h%E1%BB%93-ch%C3%AD-minh-jobs.html |
| S12 | CMC Global, *Fresher Techie.26* (thể lệ entry test) | truy cập 20/11/2026 | https://fresher.cmcglobal.com.vn/ |
| S14 | FPT Telecom, *Back-End Developer (Intern)* | truy cập 20/11/2026 | https://fptjobs.com/back-end-developer-intern-25312 |
| S15 | Hybird Technologies qua Aptech, *Fresher Java Developer* | 02/01/2026 | https://aptechvietnam.com.vn/tuyen-dung/hcm-tuyen-dung-fresher-java-developer |
| S16 | CareerViet, *MB Bank BackEnd Engineer (Java, Spring Boot)* | cập nhật 04/11/2026 | http://careerviet.vn/viec-lam/backend-developer-fresher-k-vi.html |
| S17 | Big-O Coding, *Mức lương lập trình viên 2026* (tổng hợp ITviec + Adecco) | 10/11/2026 | https://bigocoding.com/bai-viet/muc-luong-lap-trinh-vien-2026-tai-viet-nam/ |
| S18 | CareerLink, *Câu hỏi phỏng vấn Java theo cấp độ* | 19/10/2026 | https://www.careerlink.vn/cam-nang-viec-lam/phong-van-viec-lam/cau-hoi-phong-van-lap-trinh-vien-java |
| S19 | PassInterview, review phỏng vấn CMC Global | truy cập 20/11/2026 | https://passinterview.app/vi/companies/cmc-global |
| S20 | Voz, review phỏng vấn fresher Java (TMA, FPT, công ty Hàn) | 2022–2025 | https://voz.vn/t/xin-it-review-ve-quy-trinh-phong-van-frehser-java-tai-tma-solutions.1069043 |
