# 09.2 — Red-team, nhật ký quyết định & bảng nguồn

**Ngày:** 21/11/2026 · **Cập nhật lần cuối:** 21/11/2026
**Đây là nơi duy nhất định nghĩa mã nguồn [S#].** Mọi file khác trích `[S3]` phải trỏ về bảng ở mục 3.

---

## 1. Red-team pass — 5 đòn đánh vào chính pack này

Viết theo kiểu: nếu một người hoài nghi đọc pack, họ sẽ nói gì, và câu trả lời trung thực là gì.

| # | Đòn đánh | Câu trả lời trung thực | Pack đã sửa gì |
|---|---|---|---|
| 1 | **"Mẫu của mày không đại diện thị trường."** | Đúng. 602 tin từ 5 sàn, chủ yếu ITviec + LinkedIn + Glints; không có trang công ty, không có referral — nơi fresher thật sự được tuyển. Mọi tỉ lệ trong pack là **tỉ lệ trên mẫu**, không phải tỉ lệ thị trường. | `02_market_report.md` §0 ghi định nghĩa + cỡ mẫu từng con số; `02_methodology_and_limits.md` §3–4 |
| 2 | **"Số 121 tin gần nhà với 84 dòng là mâu thuẫn."** | Đúng, và đó là lỗi cũ. Bản 121 dòng tính trước khi lọc tester; bản 84 sau khi lọc. Cả hai đều **đã bị xoá** khỏi repo vì lý do riêng tư. Con số thay thế là **phân bố theo quận** (không phụ thuộc vị trí nhà). | `10_commute_and_platform_guide_2026-11-20.md` |
| 3 | **"Nộp đơn trong 72 giờ bằng CV chưa sửa là tự bắn vào chân."** | Đúng. Đó là lỗi nghiêm trọng nhất của bản trước: dùng "cửa thật" (Netcompany/EPAM/KMS/MoMo) để làm thí nghiệm đo CV. | Đổi thành **0 đơn tới W7**, nộp luyện tập từ W8 (`04_master_roadmap.md` §2) |
| 4 | **"CV vẫn có dòng không bảo vệ được."** | Đúng — mọi dòng kỹ năng Java/Spring/IT-Tools đều ⏳ cho tới khi qua T1–T6. Bản gửi đi hiện chỉ còn học vấn + Git/Linux + IELTS. | `07_cv_truth_checklist.md` |
| 5 | **"Lịch 24 tuần là giả định, không phải kế hoạch."** | Đúng một phần: 36h/tuần trong 24 tuần là giả định chưa kiểm chứng. Pack có bản 3h/ngày (48 tuần) làm phương án, và G2/G3 là cổng chặn thật. | `04_master_roadmap.md` §2 + §8 |

**Điều red-team này KHÔNG kiểm được:** liệu Hoàn có giữ được 6h/ngày hay không, và liệu thị trường có mở cửa fresher trong 6 tháng tới hay không. Cả hai chỉ trả lời được bằng việc làm.

---

## 2. Nhật ký quyết định

| Ngày | Quyết định | Lý do | Phương án đã bỏ |
|---|---|---|---|
| 20/11/2026 | **Java/Spring Boot** là hướng chính; .NET là dự bị duy nhất | Java 8,3% tin (lớn nhất); backend 19% nhóm lớn nhất `[S1]` | Go (2,4%, toàn senior), PHP, mobile |
| 20/11/2026 | **Không làm tester/QA** | Hoàn tự quyết; tester không phải đường vào backend | Tester làm bàn đạp 6 tháng |
| 20/11/2026 | **`nexus` không vào CV tới G6** | AI viết 100%, Hoàn nhớ 5–10% | Đưa `nexus` lên CV ngay (đã bỏ) |
| 20/11/2026 | **Không mua chứng chỉ, không thi lại IELTS** | Ngân sách 0 đồng; IELTS 6.5 đủ | Oracle 1Z0-831 (245 USD) để sau |
| 21/11/2026 | **Bỏ toàn bộ phân tích "gần nhà"** khỏi repo | Riêng tư: toạ độ + bán kính suy ngược ra chỗ ở | Giữ nhưng ẩn số nhà (vẫn suy ra được) |
| 21/11/2026 | **Bỏ cột `desc` (JD nguyên văn)** khỏi dữ liệu commit | Bản quyền bên thứ ba + có thể chứa email/SĐT người đăng | Giữ nguyên văn, ghi nguồn (rủi ro pháp lý) |
| 21/11/2026 | **0 đơn tới W7; 5 đơn/tuần từ W8** vào công ty không mục tiêu | *Mặc định của câu hỏi 1* — Hoàn chưa trả lời, dùng mặc định B | (A) nộp 5 đơn trong 72h |
| 21/11/2026 | **Repo giữ private**, chỉ xuất bản sạch khi cần portfolio | *Mặc định của câu hỏi 2* | Public ngay |
| 21/11/2026 | **Không mở lại tester** khi chạm ngưỡng W17 | *Mặc định của câu hỏi 3* | Mở tester làm dự phòng |
| 21/11/2026 | **TaskFlow = dự án 1, MiniWallet = dự án 2**; bỏ tên `task-api`/"Project 1" | Một dự án ba tên gây lệch lịch | Giữ 3 tên theo từng file |

> Ba quyết định ghi "*mặc định*" là ba câu hỏi dành cho Hoàn. Nếu Hoàn chọn khác, sửa đúng một chỗ: `04_master_roadmap.md` §2 (lịch + nhịp nộp) và ghi lại ở bảng này.

---

## 3. Bảng nguồn [S#]

| Mã | Nguồn | Đơn vị phát hành | Ngày xuất bản | Ngày truy cập | Độ tin cậy | URL |
|---|---|---|---|---|---|---|
| S1 | *Vietnam IT Hiring Pulse*, edition 10 | vitX | cập nhật 31/10/2026 | 20/11/2026 | **Cao** (census, có phương pháp) | https://www.vitx.global/insights/vietnam-hiring-pulse |
| S2 | *IT Salary & Recruitment Market Report 2025–2026* (1.839 người) | ITviec | 11/11/2025 | 20/11/2026 | Cao (khảo sát tự khai) | https://itviec.com/bao-cao/luong-it-va-thi-truong-tuyen-dung-it-vietnam |
| S3 | *Điểm tin thị trường IT Q1-2026* | ITviec Marketing | Q1-2026 | 20/11/2026 | TB–Cao | https://marketing.itviec.com/insight-article-q12026 |
| S4 | *Q3-2025 market overview* | ITviec Blog | 15/10/2025 | 20/11/2026 | TB | https://itviec.com/blog/vietnam-it-job-market-q3-2025-shifting-skill-requirements |
| S5 | *Q2-2025 market overview* | ITviec Blog | 19/09/2025 | 20/11/2026 | TB | https://itviec.com/blog/vietnam-it-job-market-q2-2025-python-ai-see-strong-growth/ |
| S6 | Danh mục *java tại TP.HCM* | ITviec | — | 20/11/2026 | TB (số thay đổi theo ngày) | https://itviec.com/viec-lam-it/java/ho-chi-minh-hcm |
| S7 | *Fresher Backend tại HCM* | TopCV | 15/11/2026 | 20/11/2026 | TB | https://www.topcv.vn/tim-viec-lam-fresher-backend-tai-ho-chi-minh-kl2 |
| S8 | *Backend Developer tại HCM* | TopCV | 19/11/2026 | 20/11/2026 | TB | https://www.topcv.vn/tim-viec-lam-backend-developer-tai-ho-chi-minh-kl2 |
| S9 | *backend developer fresher* | CareerViet | 18/11/2026 | 20/11/2026 | TB | http://careerviet.vn/viec-lam/backend-developer-fresher-k-vi.html |
| S10 | *Fresher Java HCM* | Indeed VN | 14/11/2026 | 20/11/2026 | TB | https://vn.indeed.com/q-fresher-java-l-th%C3%A0nh-ph%E1%BB%91-h%E1%BB%93-ch%C3%AD-minh-vi%E1%BB%87c-l%C3%A0m.html |
| S11 | *Fresher Software Engineer HCM* | Indeed VN | 18/11/2026 | 20/11/2026 | TB | https://jobs.vn.indeed.com/q-fresher-software-engineer-l-th%C3%A0nh-ph%E1%BB%91-h%E1%BB%93-ch%C3%AD-minh-jobs.html |
| S12 | *Fresher Techie.26* (thể lệ entry test) | CMC Global | — | 20/11/2026 | TB | https://fresher.cmcglobal.com.vn/ |
| S14 | *Back-End Developer (Intern)* | FPT Telecom | — | 20/11/2026 | TB | https://fptjobs.com/back-end-developer-intern-25312 |
| S15 | *Fresher Java Developer* | Hybird/Aptech | 02/01/2026 | 20/11/2026 | TB | https://aptechvietnam.com.vn/tuyen-dung/hcm-tuyen-dung-fresher-java-developer |
| S16 | *MB Bank BackEnd Engineer (Java, Spring Boot)* | CareerViet | 04/11/2026 | 20/11/2026 | TB | http://careerviet.vn/viec-lam/backend-developer-fresher-k-vi.html |
| S17 | *Mức lương lập trình viên 2026* (tổng hợp) | Big-O Coding | 10/11/2026 | 20/11/2026 | Thấp–TB (tổng hợp lại) | https://bigocoding.com/bai-viet/muc-luong-lap-trinh-vien-2026-tai-viet-nam/ |
| S18 | *Câu hỏi phỏng vấn Java theo cấp độ* | CareerLink | 19/10/2026 | 20/11/2026 | Thấp–TB | https://www.careerlink.vn/cam-nang-viec-lam/phong-van-viec-lam/cau-hoi-phong-van-lap-trinh-vien-java |
| S19 | Review phỏng vấn CMC Global | PassInterview | — | 20/11/2026 | Thấp (tự khai) | https://passinterview.app/vi/companies/cmc-global |
| S20 | Review phỏng vấn fresher Java (TMA, FPT, công ty Hàn) | Voz | 2022–2025 | 20/11/2026 | Thấp (tự khai, survivorship) | https://voz.vn/t/xin-it-review-ve-quy-trinh-phong-van-frehser-java-tai-tma-solutions.1069043 |
| S21 | Lịch nghỉ Tết Nguyên đán Đinh Mùi 2027 (04–10/02/2027) | Bộ Nội vụ — Thông báo 11483/TB-BNV (qua Cổng TTĐT Chính phủ) | 09/10/2026 | 21/11/2026 | **Cao** (văn bản chính thức) | https://xaydungchinhsach.chinhphu.vn/lich-nghi-tet-nghi-le-2027-119261115134738791.htm |
| S22 | Yêu cầu hệ thống & vòng đời hỗ trợ Spring Boot | Spring (docs.spring.io) | cập nhật 2026 | 21/11/2026 | **Cao** | https://docs.spring.io/spring-boot/system-requirements.html |
| S23 | *Spring Boot 4.2.0 available now* — GA 19/11/2026; deprecate `RestTemplate`/`TestRestTemplate` | Spring Blog (Moritz Halbritter) | 19/11/2026 | 21/11/2026 | **Cao** | https://spring.io/blog/2026/11/19/spring-boot-4-2-0-available-now |
| T1 | career-ops — README (MIT, CLI-agnostic, model free/local, không tự nộp) | career-ops-hq | — | 21/11/2026 | Cao (đọc mã + docs) | https://github.com/career-ops-hq/career-ops |
| T2 | career-ops — chạy trên ngân sách 0 đồng | career-ops-hq | — | 21/11/2026 | Cao | https://github.com/career-ops-hq/career-ops/blob/main/docs/RUNNING_ON_A_BUDGET.md |
| T3 | career-ops — sàn hỗ trợ | career-ops-hq | — | 21/11/2026 | Cao | https://github.com/career-ops-hq/career-ops/blob/main/docs/SUPPORTED_JOB_BOARDS.md |
| T4 | ai-job-search — SETUP (Claude Code + API key/Pro) | ai-job-search-dev | — | 21/11/2026 | Cao | https://github.com/ai-job-search-dev/ai-job-search/blob/master/SETUP.md |
| T5 | ai-job-search — README (portal Đan Mạch) | ai-job-search-dev | — | 21/11/2026 | Cao | https://github.com/ai-job-search-dev/ai-job-search |

**Quy ước độ tin cậy:** *Cao* = census/văn bản chính thức/tài liệu dự án; *TB* = số đếm trên trang có thể đổi theo ngày; *Thấp* = tự khai, có thiên lệch người đậu hoặc người bức xúc.

**Nguồn đã bỏ:** S13 (tester) — bỏ cùng quyết định không làm tester; JobStreet VN — sàn đã ngừng; NodeFlair — không có dữ liệu VN.
