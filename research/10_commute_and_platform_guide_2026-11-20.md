# 10 — Khoảng cách đi làm & sàn nào nên dùng nhiều nhất

> Ngày: **20/11/2026** · Người lập: Hồ Phước Hoàn · Cập nhật lần cuối: 21/11/2026
>
> **File này không chứa vị trí nơi ở.** Bộ lọc khoảng cách dùng **cấu hình cục bộ** `config.local.json`
> (đã nằm trong `.gitignore`; mẫu ở `config.local.example.json`). Mọi kết quả lọc theo khoảng cách
> được ghi vào `.local_private/` và **không commit** — vì chúng suy ngược ra được chỗ ở.
> Script: `tools/build_commute.py`.

Mục đích: trả lời hai câu —

1. "Chọn tin theo thời gian đi lại thế nào cho hợp lý?"
2. "Trong các trang tuyển dụng hiện nay, trang nào nên dùng **nhiều nhất**?"

Ràng buộc thêm: **chỉ tiếng Anh và tiếng Việt** → mọi tin đòi tiếng Trung/Nhật/Hàn bị đánh dấu loại.
**Ràng buộc (20/11/2026): Hoàn KHÔNG làm tester/QA** → toàn bộ tin tester/QA/QC đã bị loại khỏi pack.

---

## 0. Kết luận trong 4 dòng

1. **Bán kính không phải bộ lọc mạnh** — trong mẫu Glints, gần như toàn bộ tin nội thành nằm trong bán kính thường dùng; cái quyết định thời gian chạy xe là **quận cụ thể** và việc có phải qua cầu/kênh hay không.
2. **Glints** ghi địa chỉ tới **cấp quận** ngay trên thẻ tin; **ITviec** có địa chỉ + quận trong dữ liệu cấu trúc của trang JD (56/75 tin khai quận); LinkedIn và VietnamWorks chỉ ghi "Hồ Chí Minh".
3. **Dùng nhiều nhất: ① ITviec → ② Glints → ③ LinkedIn**; **bỏ**: TopDev, JobStreet, NodeFlair.
4. Tin đòi tiếng Trung/Nhật/Hàn bị loại thẳng — dùng được với tiếng Anh + tiếng Việt.

---

## 1. Phân bố tin theo quận (không kèm khoảng cách từ nhà)

Số liệu dưới đây là **đếm tin theo quận**, không phải khoảng cách từ một điểm gốc. Bạn tự chấm
quận nào đi lại được với mình, rồi dùng `tools/build_commute.py` nếu muốn lọc tự động.

### 1.1 Glints — 86 tin TP.HCM, tất cả có quận

| Quận | Tin | Ghi chú đi lại |
|---|---|---|
| **Quận 7** | **26** | Nhiều tin nhất; qua cầu Nguyễn Văn Cừ/Kênh Tẻ, kẹt xe giờ cao điểm |
| **Quận 1** | **18** | Trung tâm; xe buýt/metro thuận |
| **Quận 3** | **13** | Trung tâm |
| **Quận Phú Nhuận** | **11** | Nội thành, ít kẹt hơn Quận 7 |
| Quận 2 (TP Thủ Đức) | 11 | Đường Nguyễn Hữu Cảnh / Xa lộ Hà Nội |
| Quận Bình Thạnh | 7 | Sát trung tâm |
| Quận Tân Bình | 7 | Sân bay, nhiều trục đường lớn |
| Quận Thủ Đức | 7 | Xa trung tâm, 45–60 phút giờ cao điểm |
| Quận 12 | 5 | |
| Quận 11 | 4 | |
| Quận 10 | 3 | |
| Quận Bình Tân | 3 | |
| Tân Phú · Gò Vấp · Quận 5 · Quận 6 | 1 mỗi quận | |
| Bình Chánh · Nhà Bè · Quận 9 | 1–4 | Ngoại thành, chỉ nhận nếu chấp nhận đi xa |

### 1.2 ITviec — 75 tin TP.HCM, 56 tin khai quận

| Quận | Tin |
|---|---|
| **Quận 1** | **12** |
| Quận 10 | 8 |
| TP Thủ Đức (gồm Quận 2 cũ) | 8 |
| **Quận 7** | **7** |
| Bình Thạnh | 7 |
| Quận 12 | 6 |
| **Quận 3** | **6** |
| Quận 11 · Quận 4 | 1 mỗi quận |

25 tin còn lại giấu địa chỉ (`Not Available`) hoặc chỉ có văn phòng Hà Nội/Đà Nẵng.

**5 tin trong shortlist ITviec — tất cả đều ở nội thành:**

| Công ty | Vị trí | Quận | Địa chỉ ghi trong JD |
|---|---|---|---|
| DMSpro | Technical Consultant | Quận 3 | 34 Bạch Đằng *(trang ghi Quận 3 — cần xác nhận)* |
| GeoComply | Software Engineer Intern | Quận 1 | Saigon Trade Center, 37 Tôn Đức Thắng |
| Netcompany | Software Developer (Fresher/Junior) | Bình Thạnh | Opal Tower 92 Nguyễn Hữu Cảnh |
| MoMo | MoMo Talent 2027 | Quận 7 | Phú Mỹ Hưng Tower, 08 Hoàng Văn Thái |
| Motorist | Junior Android (Kotlin/Java) | TP Thủ Đức | 258 Nam Kỳ Khởi Nghĩa |

> Cách tự kiểm: mở JD → `Ctrl+U` → tìm `"addressLocality"`. Cột `quan`, `dia_chi_trong_jd` có trong
> `02e_itviec_hcm_salary_2026-11-20.csv`; số liệu ở `02e_itviec_districts_stats_2026-11-20.json`.

---

## 2. Tin đáng nộp ngay (Java/backend/dev, 0–2 năm, nội thành)

Bỏ các tin đã cũ từ 2025 (đánh dấu ⚠️ — gần như chắc chắn hết hạn). Không còn vai trò tester nào.

| Quận | Tin | Công ty | Lương | KN | Đăng |
|---|---|---|---|---|---|
| Tân Bình | **Software Developer – Intern** | Bouygues Construction IT Vietnam | **6–6,6 triệu** | 0 năm | 19/10/2026 |
| Tân Bình | Hiring: Intern Fullstack Developer | Công ty CP Starack | Không công bố | 0 năm | 30/06/2026 ⚠️ |
| Phú Nhuận | **Full Stack Developer** | Công ty CP Hàng Tiêu Dùng | **18–25 triệu** | 1 năm | 05/11/2026 |
| Phú Nhuận | Backend Engineer (Golang) | Anfin | Không công bố | 1 năm | 23/04/2026 |
| Quận 10 | **Nhân Viên Lập Trình Java** | Gsoft | **15–20 triệu** | 1 năm | 02/06/2026 |
| Quận 3 | Software Engineer – Back End | Edtronaut | Không công bố | 0 năm | 14/07/2025 ⚠️ |
| Quận 3 | Thực Tập Sinh .NET (ASP.NET, C#) | W2SOLUTION Việt Nam | 2–3 triệu | 0 năm | 06/11/2026 |

**Đọc bảng này thế nào:** 3 tin đáng gửi CV nhất là **Bouygues (intern có trợ cấp, Tân Bình)**,
**Full Stack 18–25 triệu ở Phú Nhuận**, **Java Gsoft 15–20 triệu ở Quận 10**.

---

## 3. Chỉ tiếng Anh + tiếng Việt

- Tin có dấu hiệu đòi **tiếng Trung / Nhật / Hàn** (từ khoá: `chinese`, `mandarin`, `japanese`, `JLPT`,
  `korean`, `TOPIK`, `tiếng trung`, `tiếng nhật`, `tiếng hàn`) → không nộp.
- Con số này khớp với phát hiện ở LinkedIn: **DXC đăng 16 tin chạm tới được nhưng 7 tin đòi tiếng Trung/Nhật**
  → nếu không có ngoại ngữ 3, DXC co lại còn ~9 tin.
- **IELTS 6.5 là lợi thế, không phải rào cản**: các tin "Good English" (Netcompany, Bouygues, GeoComply,
  Clever Creations) đều nằm trong tầm.

---

## 4. Sàn nào nên dùng **nhiều nhất**? (xếp theo số liệu của chính pack này)

| Hạng | Sàn | Tin lấy được | Có lương | Địa chỉ tới quận? | Điểm mạnh thật | Nên dùng thế nào |
|---|---|---|---|---|---|---|
| **1** | **ITviec** | 75 tin TP.HCM | **17 (22,7%)** | ⚠️ trong dữ liệu cấu trúc JD | **Cấu trúc level rõ nhất** (Fresher/Junior/Middle), 5 tin entry-level | **Nơi nộp chính.** Đọc JD để biết địa chỉ |
| **2** | **Glints** | 86 tin TP.HCM | **47 (54,7%)** | ✅ **có, tới cấp quận** | **Tỉ lệ lương công khai cao nhất** (gấp 2,7 lần ITviec), 24 tin yêu cầu 0–1 năm | **Nơi lọc theo quận** trước khi nộp |
| **3** | **LinkedIn** | 392 tin | **7 (1,8%)** | ❌ | **Nhiều công ty nhất** (163 công ty), nhiều tin không đăng ở sàn VN | **Nơi dò công ty**, đừng lọc theo nhãn "Entry level" (LinkedIn gắn sai) |
| 4 | VietnamWorks | 41 (sau đăng nhập) | 11 (26,2%) | ❌ | Bank/chứng khoán, 10 tin TP.HCM | Chỉ để **kiểm tra chéo**, không phải kênh chính |
| ✗ | TopDev (Saramin) | 8 | 1 (và tin Hà Nội) | ❌ | Kho Java rất mỏng, phần lớn khoá lương | **Bỏ** |
| ✗ | JobStreet | 3 (remote) | — | ❌ | **Sàn VN đã ngừng** (redirect sang Jora Australia) | **Bỏ** |
| ✗ | NodeFlair | **0** | — | — | Không có dữ liệu Việt Nam | **Bỏ** |

**Cách phối hợp (thực dụng, 30 phút/ngày):**

1. **Glints** (10 phút): lọc quận bạn đi lại được → ứng tuyển tin có lương công khai.
2. **ITviec** (10 phút): lọc Java + Fresher/Junior → mở JD xem địa chỉ, giữ tin nội thành.
3. **LinkedIn** (10 phút): tìm **công ty** (không phải tin) trong các quận đó, theo dõi để bắt tin mới.

Lý do **không dùng một sàn duy nhất**: ba sàn chỉ trùng **2–13 công ty** trên hàng trăm công ty
(`02i_cross_platform_companies_2026-11-20.csv`) → nộp một sàn là bỏ lỡ >90% công ty.

---

## 5. Giới hạn của file này (đọc trước khi tin)

1. **Bảng quận là đếm tin**, không phải khoảng cách. Thời gian đi thật còn phụ thuộc giờ, tuyến, phương tiện.
2. **Không tính kẹt xe**: cùng một quãng đường, giờ tan tầm có thể gấp đôi thời gian.
3. **Glints khai quận ngay trên thẻ tin; ITviec khai trong dữ liệu cấu trúc của trang JD**; LinkedIn và
   VietnamWorks chỉ ghi "Hồ Chí Minh" → muốn biết quận phải đọc mô tả hoặc hỏi recruiter.
4. **Tin cũ**: một số tin đăng 2025 (đánh dấu ⚠️) gần như chắc chắn đã hết hạn — kiểm tra ngày trước khi nộp.
5. Một ngày, một thời điểm; tin trôi theo ngày.
6. Không lưu số nhà, SĐT, email, CCCD trong bất kỳ file nào (R10).

---

## 6. Tệp liên quan

| Tệp | Nội dung |
|---|---|
| `tools/build_commute.py` | Lọc theo khoảng cách, đọc `config.local.json` (không commit) |
| `config.local.example.json` | Mẫu cấu hình cục bộ |
| `02f_glints_jobs_2026-11-20.csv` | Nguồn: 86 tin Glints có địa chỉ quận |
| `02e_itviec_hcm_salary_2026-11-20.csv` | Nguồn ITviec: 75 tin, có cột `quan` |
| `02e_itviec_districts_stats_2026-11-20.json` | Phân bố quận của 75 tin ITviec |
| `02i_cross_platform_companies_2026-11-20.csv` | Mức trùng công ty giữa các sàn |
