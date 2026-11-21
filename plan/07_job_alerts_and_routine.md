# 07.4 — Job alerts & thói quen hằng ngày (≤ 45 phút)

**Ngày:** 21/11/2026 · **Cập nhật lần cuối:** 21/11/2026 · **Liên quan:** `04_master_roadmap.md` §2 (nhịp nộp), `07_application_kit.md` (mẫu hồ sơ)

> Nhịp nộp: **0 đơn tới W7** · 5 đơn/tuần W8–W12 (chỉ công ty không phải mục tiêu) · 10/tuần từ W13.
> File này nói **cách tìm** tin, không nói nộp bao nhiêu.

---

## 1. Bốn alert LinkedIn hiện có của Hoàn — đánh giá

Nguồn: ảnh chụp `screencapture-www-linkedin-com-jobs-2026-11-18-21_26_01.png` (Phụ lục B của prompt gốc).

| # | Alert hiện có (theo ảnh) | Đánh giá | Sửa thành |
|---|---|---|---|
| 1 | Java Developer — Hồ Chí Minh | **Giữ** — đúng trục chính | thêm `"Spring Boot" OR "Backend"` |
| 2 | Backend Developer — Hồ Chí Minh | **Giữ** — bắt được tin không ghi Java | thêm loại trừ senior |
| 3 | Software Engineer — Hồ Chí Minh | **Loãng**: trả về cả mobile, embedded, QA | thay bằng Boolean có `Java OR Spring` |
| 4 | Fresher/Intern IT — Hồ Chí Minh | **Giữ nhưng đổi từ khoá**: "fresher" trên LinkedIn gắn sai nhãn (đã có tin 4–5 năm gắn Entry) | dùng `"thực tập" OR intern OR graduate` + lọc company size |

---

## 2. Sáu alert nên tạo (LinkedIn + 3 sàn VN)

Từ khoá dưới đây lấy từ **kỹ năng thật sự xuất hiện trong tin `true_entry_level`** của `02_postings_master.csv`
(chạy `python3 tools/02_stats.py` để xem lại `top_ky_nang`), không phải từ cảm giác.

| # | Nền tảng | Chuỗi tìm / bộ lọc | Vì sao |
|---|---|---|---|
| 1 | LinkedIn | `("Java" OR "Spring Boot") AND ("Backend" OR "Software Engineer")` · Location **Ho Chi Minh City** · Date posted **Past week** | Trục chính; Boolean loại bớt mobile/embedded |
| 2 | LinkedIn | `("fresher" OR "graduate" OR "intern" OR "thực tập") AND ("Java" OR "backend")` · HCM · Past week | Bắt chương trình đầu vào |
| 3 | LinkedIn | `("Java" OR ".NET") AND ("junior" OR "associate")` · HCM · Past 2 weeks | Bắt nhóm "associate" mà alert fresher bỏ sót |
| 4 | ITviec | Keyword `Java`; Level **Fresher/Junior**; City **Hồ Chí Minh**; bật **email alert** hằng ngày | Cấu trúc level rõ nhất |
| 5 | Glints | `java`, `spring boot`, `backend`; Location **Hồ Chí Minh**; lọc **0–1 năm**; bật thông báo | Sàn có tỉ lệ lương công khai cao nhất |
| 6 | TopCV | `Java fresher`, `backend fresher`; HCM; sắp xếp **Mới nhất** | Nơi có nhiều tin gắn nhãn fresher hơn ITviec |

**VietnamWorks**: tạo saved search `java` + HCM, nhưng coi là **kênh phụ** (10 tin TP.HCM, 0 tin fresher thật).

**Từ khoá tiếng Việt nên dùng song song:** `lập trình viên Java`, `thực tập sinh Java`, `backend`, `fresher Java`, `mới tốt nghiệp`.
Từ khoá loại trừ (dán vào ô tìm nếu sàn hỗ trợ): `tester`, `QA`, `QC`, `BrSE`, `PHP`, `embedded`, `sales`.

---

## 3. Trang tuyển dụng công ty — theo dõi thay vì chờ alert

Lấy từ `02_entry_programs_2026_2027.md` (6 chương trình Java đã xác minh) + các công ty lặp lại nhiều nhất trong master.

| Nhóm | Công ty | Theo dõi ở đâu | Tần suất |
|---|---|---|---|
| Chương trình đầu vào | Netcompany (*Talented IT Graduates*) · EPAM (*Hire-to-Train*) · KMS · MoMo (*Talent*) | trang careers của công ty + LinkedIn công ty | 1 lần/tuần |
| Outsourcing lớn | DXC · TMA · FPT Software · CMC Global | trang tuyển dụng riêng | 1 lần/tuần |
| Product/fintech | Zalo · MoMo · GeoComply · Money Forward · WorldQuant | trang careers | 2 tuần/lần |
| Ngân hàng | MB · VietinBank · ACB | mục tuyển dụng | 2 tuần/lần |

**Quy tắc:** nộp qua **trang công ty** khi có, vì tỉ lệ hồ sơ được đọc cao hơn nộp qua board.

---

## 4. Quy trình 45 phút/ngày

| Phút | Việc | Ở đâu |
|---|---|---|
| 0–10 | Đọc email alert (LinkedIn + ITviec + Glints) — **chỉ mở tin đăng ≤ 7 ngày** | hộp thư |
| 10–20 | Mở `02_postings_master.csv`, lọc `true_entry_level = True` + Java → chọn tin khớp ≥ 60% yêu cầu | file |
| 20–35 | 1–2 đơn: đổi 3 slot (S1/S2/S3 trong `07_application_kit.md`), xuất PDF, gửi | — |
| 35–45 | Ghi tracker + **ghi 1 dòng "vì sao tin này"** | `07_application_tracker.csv` |

**Ngày không có tin mới:** dùng 45 phút đó để **viết 1 bullet dự án** hoặc luyện 1 câu phỏng vấn. Không lướt thêm.

---

## 5. Trường dữ liệu của tracker (đang dùng 14 cột)

`ngay_nop` · `cong_ty` · `vi_tri` · `nguon` · `link_jd` · `cv_da_dung` · `trang_thai` · `ngay_phan_hoi` ·
`kenh_phan_hoi` · `cau_hoi_bi_hoi` · `lo_hong_phat_hien` · `follow_up_ngay` · `ket_qua` · `ghi_chu`

**Cột giá trị nhất:** `lo_hong_phat_hien`. Sau 5 buổi phỏng vấn, đọc lại sẽ thấy 2–3 lỗ hổng lặp lại — đó là nội dung học tuần sau.

---

## 6. Ba lỗi cần tránh

1. **Bật 10 alert trùng nhau** → 40 email/ngày, rồi tắt hết sau 1 tuần. 6 alert là đủ.
2. **Nộp tin đăng > 14 ngày** — thường đã có ứng viên; ưu tiên ≤ 7 ngày.
3. **Để alert tự quyết định** — alert chỉ là danh sách đầu vào; quyết định nộp dựa trên JD + mức khớp, không dựa trên số lượng.
