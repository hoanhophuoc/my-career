# 🎯 My Career Pack — Hồ Phước Hoàn

**Cập nhật lần cuối:** 21/11/2026

> **Pack sự nghiệp cá nhân** — Lộ trình 24 tuần để trở thành Java/Spring Boot Backend Engineer tại TP.HCM.
> Xây từ dữ liệu crawl thực: **602 tin tuyển dụng** từ 5 nền tảng (sau khi lọc tester/role không làm), audit **212 tài liệu**, phân tích **36 repo**.

> **Đây là README duy nhất của pack.** Trước 21/11/2026 pack có thêm `00_README_index.md` (đã xoá); nội dung của nó (thứ tự đọc, danh sách file, CHANGELOG) đã gộp vào file này. CHANGELOG gốc nằm ở **phụ lục cuối `REVIEW_FIX_LOG.md`**.

---

## 1. Bắt đầu từ đây

Đọc theo thứ tự này, đừng đọc hết một lượt:

| Bước | File | Vì sao đọc |
|---|---|---|
| **0** | [`00_START_HERE.md`](00_START_HERE.md) | Bản đồ pack + việc cần làm tuần này — đọc trước, khỏi mở gì khác |
| 1 | [`plan/09_executive_summary.md`](plan/09_executive_summary.md) | Toàn bộ kết luận trong 1 trang — mở mỗi sáng (6 phút) |
| 2 | [`data/02d_linkedin_shortlist_2026-11-20.csv`](data/02d_linkedin_shortlist_2026-11-20.csv) | Tin để nộp tuần này |
| 3 | [`plan/04_master_roadmap.md`](plan/04_master_roadmap.md) | Lộ trình 24 tuần, từng ngày 28 ngày đầu |
| 4 | [`plan/04_readiness_rubric.md`](plan/04_readiness_rubric.md) | 9 điều kiện "đủ để nộp" — tự chấm ở W4/W10/W16/W24 |

Sau đó, khi cần: CV ở [`cv/`](#2-cấu-trúc-thư-mục), thị trường ở [`research/`](#2-cấu-trúc-thư-mục), sách/phương pháp ở [`learning/`](#2-cấu-trúc-thư-mục).

---

## 2. Cấu trúc thư mục

```
hoan_career_pack/
│
├── README.md                  # File này — điểm vào duy nhất
├── 00_START_HERE.md           # Bản đồ + việc cần làm tuần này
├── REVIEW_FIX_LOG.md          # Nhật ký sửa theo review P0–P3 (+ CHANGELOG gốc)
│
├── cv/          (8)   # Hồ sơ: CV trung thực, audit CV/LinkedIn, ma trận kỹ năng,
│                      # học vấn, truth-check từng dòng CV, bộ hồ sơ nộp, LinkedIn copy
│
├── plan/        (15)  # Chiến lược chọn hướng, lộ trình 24 tuần, rubric nộp,
│                      # sau khi có việc, học lên/thi đấu, bản điều hành, KPI,
│                      # playbook 1 trang, nhật ký quyết định, prompt làm mới pack
│
├── research/    (10)  # Báo cáo thị trường, phương pháp & giới hạn, chương trình fresher,
│                      # dạng bài test, kiểm kê repo, ảnh chụp 4 sàn, đi lại & chọn sàn
│
├── learning/    (20)  # Spec 2 dự án, 70 câu phỏng vấn, danh mục tài nguyên,
│                      # 60 thẻ Anki, kệ sách 12 cuốn, cách học, tiếng Anh 12 tuần,
│                      # 01_diagnostic_tests/ (T1–T6 + đáp án)
│
├── data/        (20)  # Dữ liệu crawl đã lọc role: 5 sàn, master 671 dòng,
│                      # stats JSON, shortlist, 705 job title — script đọc, người không cần mở
│
└── tools/       (19)  # Script crawl/lọc/phân tích/audit/xuất bản + excluded_roles.conf
                       # + purge_log + make_file_index.py (sinh mục 6) + check_links.py
```

Cây này là **nguồn duy nhất** cho đường dẫn: mọi link trong pack đều tương đối và được kiểm bằng
`python3 tools/check_links.py`.

---

## 3. Số liệu chính (cập nhật 20/11/2026, sau lọc role)

Mọi con số dưới đây sinh từ `data/02_postings_master.csv` bằng `tools/02_stats.py` — không chép tay.

| Hạng mục | Con số |
|----------|--------|
| Tin tuyển dụng đã crawl | **602 tin / 5 nền tảng** (LinkedIn 392 · Glints 86 · ITviec 75 · VietnamWorks 41 · TopDev 8) |
| Đã loại khỏi dữ liệu thô | **212 tin tester/QA + 69 tin role khác** (PHP, BrSE, hardware, support, sales/designer/giáo viên…) |
| Tin theo quận (Glints) | Quận 7: 26 · Quận 1: 18 · Quận 3: 13 · Phú Nhuận: 11 (xem `research/10_commute_and_platform_guide_2026-11-20.md`) |
| LinkedIn chạm tới được | **153/392 (39,0%)**; trong đó Java/Spring **63 tin** (định nghĩa ở `research/02_market_report.md` §0) |
| Lương fresher Java/Spring Boot HCM | **10–15 triệu** (junior có Spring: 19–20 triệu) |
| Thời gian lộ trình | **24 tuần** (W1: 24/11/2026 → W24: 04/05/2027) |
| Sách đã có (kệ tối thiểu) | **12/12 cuốn, 0 đồng** |
| Thẻ Anki đã tạo | **60 thẻ** (Java/Spring/SQL) |
| Repo code cá nhân | **36 repo, 261 MB** |

---

## 4. 7 quyết định đã chốt

1. **Java/Spring Boot 12 tháng đầu** — .NET là dự bị duy nhất; **không làm tester/QA (kể cả pentester)**
2. **Java 25 LTS + Spring Boot 4.2.0** — không học phiên bản cũ
3. **`nexus` không vào CV** cho tới khi qua cổng G6
4. **Không học thạc sĩ ngay** — xem lại 10/2029
5. **Không mua chứng chỉ** trong 12 tháng (ngân sách: 0 đồng)
6. **Không thi lại IELTS** — chỉ luyện nói 15'/ngày
7. **Nộp đơn có hệ thống**: 0 đơn tới W7, 5/tuần từ W8 (công ty không mục tiêu), 10–15/tuần từ W17

---

## 5. Ba việc làm ngay

```
1. Sửa 8 dòng CV theo cv/01_cv_linkedin_audit.md (30–45 phút)
2. Chốt danh sách 20 công ty theo cv/07_application_kit.md — chưa nộp đơn nào tới W8
3. Làm bài T1 (Java core) + T6 (project defense) trong learning/01_diagnostic_tests/
```

---

## 6. Danh sách file (tự sinh từ đĩa)

> Sinh bằng `python3 tools/make_file_index.py` — chạy lại mỗi khi thêm/xoá/đổi tên file.
> Tiêu đề lấy từ dòng `#` đầu tiên của chính file, nên không thể lệch với nội dung.
> Nhóm dùng: **A** = mở thường xuyên · **B** = đọc một lần · **C** = tra khi cần · **D** = dữ liệu thô (chỉ script đọc).
> Xếp nhóm trong `00_START_HERE.md` mục 2.

<!-- BEGIN FILE INDEX -->

### Gốc pack — điều hướng & nhật ký — 4 file

| File | Nội dung (tiêu đề trong file) |
|---|---|
| `.gitignore` | .gitignore |
| `00_START_HERE.md` | 00 — BẮT ĐẦU TỪ ĐÂY |
| `REVIEW_FIX_LOG.md` | REVIEW_FIX_LOG — nhật ký sửa theo review P0 → P3 |
| `config.local.example.json` | dữ liệu JSON |

### `cv/` — hồ sơ, CV, LinkedIn, kỹ năng — 8 file

| File | Nội dung (tiêu đề trong file) |
|---|---|
| `cv/01_cv_linkedin_audit.md` | 01.3 — KIỂM TOÁN CV & LINKEDIN HIỆN TẠI |
| `cv/01_graduation_checklist.md` | 01.4 — HỌC VẤN: ĐÃ CHỐT (bản v3, 20/11/2026) |
| `cv/01_honest_cv_v1.md` | 01_HONEST CV v1 — BẢN TRUNG THỰC (VI + EN) |
| `cv/01_skills_matrix.csv` | cột: id, group, skill, cv_or_linkedin_says |
| `cv/01_skills_matrix.md` | 01.1 — MA TRẬN KỸ NĂNG CÓ BẰNG CHỨNG |
| `cv/07_application_kit.md` | Phase 7.2 — Bộ hồ sơ nộp đơn & hệ thống ứng tuyển |
| `cv/07_cv_truth_checklist.md` | 07.6 — Cổng sự thật cho CV & LinkedIn |
| `cv/07_linkedin_copy_paste.md` | Phase 7.1 — LinkedIn: copy-paste (VI + EN) |

### `plan/` — chiến lược, lộ trình, vận hành — 15 file

| File | Nội dung (tiêu đề trong file) |
|---|---|
| `plan/03_strategy.md` | 03 — Chiến lược: chọn hướng, kịch bản 2027–2031, bằng chứng AI (gộp) |
| `plan/03_track_decision_matrix.csv` | cột: track, c1_entry_openings_25, c2_competition_15, c3_salary_15 |
| `plan/04_after_hire.md` | 04 — Sau khi có việc: 0→5 năm, kỹ năng mềm, 90 ngày đầu (gộp) |
| `plan/04_master_roadmap.md` | Phase 4.1 — Lộ trình tổng 24 tuần (bản 6h/ngày) |
| `plan/04_readiness_rubric.md` | Phase 4.3 — Thang đo "đã đủ để nộp chưa" |
| `plan/07_application_tracker.csv` | cột: ngay_nop, cong_ty, vi_tri, nguon |
| `plan/07_github_cleanup_plan.md` | 07.3 — Kế hoạch dọn GitHub (36 repo) |
| `plan/07_job_alerts_and_routine.md` | 07.4 — Job alerts & thói quen hằng ngày (≤ 45 phút) |
| `plan/07_tools_evaluation.md` | 07.5 — Đánh giá hai công cụ tìm việc bằng AI |
| `plan/08_education_competitions_community.md` | Phase 8 — Học lên, thi đấu, cộng đồng (cho fresher Java backend, TP.HCM) |
| `plan/09_decision_log_and_sources.md` | 09.2 — Red-team, nhật ký quyết định & bảng nguồn |
| `plan/09_executive_summary.md` | Phase 9 — Bản điều hành (executive summary) |
| `plan/09_kpi_tracker.csv` | cột: tuan, ngay_bat_dau, stage, trong_tam |
| `plan/09_playbook_1page.md` | 09.3 — Playbook 1 trang (in ra dán cạnh màn hình) |
| `plan/09_refresh_prompts.md` | Phase 9 — Prompt làm mới pack (copy-paste) |

### `research/` — thị trường, nguồn, giới hạn — 10 file

| File | Nội dung (tiêu đề trong file) |
|---|---|
| `research/00_file_inventory.md` | 00 — KIỂM KÊ FILE ĐÍNH KÈM |
| `research/02_entry_programs_2026_2027.md` | 02.5 — CHƯƠNG TRÌNH DÀNH CHO NGƯỜI MỚI 2026–2027 (**chỉ TP.HCM**) |
| `research/02_interview_formats.md` | 02.6 — QUY TRÌNH & DẠNG BÀI TEST KHI TUYỂN FRESHER/JUNIOR JAVA |
| `research/02_market_report.md` | 02 — BÁO CÁO THỊ TRƯỜNG VIỆC LÀM IT TP.HCM CHO NGƯỜI MỚI (2026–2027) |
| `research/02_methodology_and_limits.md` | 02.1 — PHƯƠNG PHÁP, NGUỒN VÀ GIỚI HẠN |
| `research/02c_repo_inventory.md` | Phase 2c — Kiểm kê 36 repo (đã clone thật, 20/11/2026) |
| `research/02d_linkedin_market_snapshot_2026-11-20.md` | Ảnh chụp thị trường — LinkedIn Jobs (20/11/2026) |
| `research/02e_itviec_market_snapshot_2026-11-20.md` | ITviec TP.HCM — ảnh chụp thị trường (đã đăng nhập, có lương) |
| `research/02f_multi_platform_snapshot_2026-11-20.md` | 02f — Bốn sàn còn lại: Glints · TopDev · VietnamWorks · NodeFlair |
| `research/10_commute_and_platform_guide_2026-11-20.md` | 10 — Khoảng cách đi làm & sàn nào nên dùng nhiều nhất |

### `learning/` — học gì, học thế nào, luyện tập — 20 file

| File | Nội dung (tiêu đề trong file) |
|---|---|
| `learning/01_diagnostic_tests/00_README.md` | BỘ BÀI TEST CHẨN ĐOÁN — HƯỚNG DẪN |
| `learning/01_diagnostic_tests/01_java_core.md` | T1 — JAVA CORE (90 phút · KHÔNG AI · KHÔNG Google) |
| `learning/01_diagnostic_tests/02_sql.md` | T2 — SQL (60 phút · KHÔNG AI · KHÔNG Google) |
| `learning/01_diagnostic_tests/03_dsa.md` | T3 — DSA (120 phút · 12 phút/bài · KHÔNG AI) |
| `learning/01_diagnostic_tests/04_spring_jpa_security.md` | T4 — SPRING BOOT / JPA / SECURITY (60 phút) |
| `learning/01_diagnostic_tests/05_practical.md` | T5 — HTTP / REST / GIT / LINUX / DOCKER (30 phút · KHÔNG tra cứu) |
| `learning/01_diagnostic_tests/06_project_defense.md` | T6 — "GIẢI THÍCH DỰ ÁN" (60 phút · nói thành tiếng · ghi âm) |
| `learning/01_diagnostic_tests/09_answer_key.md` | 09 — ĐÁP ÁN & GIẢI THÍCH |
| `learning/04_anki_starter_decks.md` | Phase 4.9 — Bộ thẻ khởi đầu (import được vào Anki) |
| `learning/04_anki_starter_decks.tsv` | bộ thẻ TSV (import Anki) |
| `learning/04_interview_prep.md` | Phase 4.5 — Chuẩn bị phỏng vấn (thị trường TP.HCM, fresher Java) |
| `learning/04_projects_spec.md` | Phase 4.4 — Hai dự án phải tự viết (thay chỗ `nexus` để lại) |
| `learning/04_resources_catalog.csv` | cột: id, ten, url, loai |
| `learning/04_resources_catalog.md` | Phase 4.2 — Danh mục tài nguyên (chỉ miễn phí, đã kiểm chứng) |
| `learning/05_free_resources_core.md` | Phase 5.6 — Bộ tài nguyên miễn phí cốt lõi (đối chiếu với 212 sách + 1.861 bookmark) |
| `learning/05_how_to_learn.md` | 05 — Cách học, cách nhớ, cách giữ tập trung (gộp) |
| `learning/05_library_audit.csv` | cột: path, folder, subfolder, file |
| `learning/05_shelf_and_books.md` | 05 — Kệ sách: đọc gì, thứ tự nào (gộp) |
| `learning/06_english_plan.md` | Phase 6 — Luyện **nói** tiếng Anh cho phỏng vấn (dựa trên IELTS 6.5 đã có) |
| `learning/06_english_tracking_sheet.csv` | cột: tuan, ngay, cau_da_noi_nguon_04_interview_prep_muc_D, giay |

### `data/` — dữ liệu crawl (nhóm D, chỉ script đọc) — 20 file

| File | Nội dung (tiêu đề trong file) |
|---|---|
| `data/02_postings_master.csv` | cột: id, source, url, posted |
| `data/02_stats_2026-11-20.json` | dữ liệu JSON |
| `data/02d_linkedin_jobs_2026-11-20.csv` | cột: id, keywords, url, title |
| `data/02d_linkedin_jobs_2026-11-20.json` | dữ liệu JSON |
| `data/02d_linkedin_shortlist_2026-11-20.csv` | cột: ﻿rank, score, category, title |
| `data/02d_linkedin_stats_2026-11-20.json` | dữ liệu JSON |
| `data/02e_itviec_districts_stats_2026-11-20.json` | dữ liệu JSON |
| `data/02e_itviec_hcm_salary_2026-11-20.csv` | cột: search, url, title, company |
| `data/02e_itviec_shortlist_2026-11-20.csv` | cột: title, company, level, salary |
| `data/02e_itviec_stats_2026-11-20.json` | dữ liệu JSON |
| `data/02f_glints_jobs_2026-11-20.csv` | cột: search, url, title, company |
| `data/02f_glints_jobs_2026-11-20.json` | dữ liệu JSON |
| `data/02f_glints_shortlist_2026-11-20.csv` | cột: title, company, min_years, max_years |
| `data/02f_glints_stats_2026-11-20.json` | dữ liệu JSON |
| `data/02g_topdev_jobs_2026-11-20.csv` | cột: title, company, salary, location |
| `data/02h_vietnamworks_jobs_2026-11-20.csv` | cột: title, company, salary, location |
| `data/02h_vietnamworks_shortlist_2026-11-20.csv` | cột: title, company, salary, location |
| `data/02h_vietnamworks_stats_2026-11-20.json` | dữ liệu JSON |
| `data/02i_cross_platform_companies_2026-11-20.csv` | cột: cap_san, so_cong_ty_trung, ten_cong_ty |
| `data/11_all_job_titles_2026-11-20.csv` | cột: source, title, company, location |

### `tools/` — script crawl/audit/xuất bản — 20 file

| File | Nội dung (tiêu đề trong file) |
|---|---|
| `tools/02_build_master.py` | Gộp dữ liệu từng nền tảng thành MỘT bộ dữ liệu chuẩn: 02_postings_master.csv |
| `tools/02_stats.py` | Tính MỌI con số tiêu đề từ 02_postings_master.csv. |
| `tools/analyze_glints_platforms.py` | Phân tích Glints TP.HCM + so trùng công ty giữa 3 sàn, sinh shortlist. |
| `tools/analyze_itviec_hcm.py` | Phân tích dữ liệu ITviec TP.HCM đã đăng nhập (có lương). |
| `tools/analyze_linkedin_jobs.py` | Analyse crawled LinkedIn jobs -> stats + ranked shortlist for a fresher |
| `tools/audit_books.py` | Audit thu vien sach cua Hoan (books.txt) -> 05_library_audit.csv |
| `tools/build_commute.py` | Lọc tin theo khoảng cách tới một điểm gốc — điểm gốc KHÔNG nằm trong repo. |
| `tools/calc_overlap.py` | Đếm công ty trùng nhau giữa 3 sàn (ad-hoc, không sinh file). |
| `tools/calc_stats.py` | Kiểm tra nhanh số liệu thô từng sàn (ad-hoc, không sinh file). |
| `tools/check_links.py` | Rà mọi tên file được nhắc trong .md xem có tồn tại thật không. |
| `tools/crawl_glints_jobs.py` | Crawl Glints VN (server-rendered __NEXT_DATA__ JSON), chỉ giữ tin TP.HCM. |
| `tools/crawl_linkedin_jobs.py` | Crawl LinkedIn public job search (guest API) -> CSV + JSON for the career pack. |
| `tools/excluded_roles.conf` | Bộ lọc VĨNH VIỄN các role Hoàn KHÔNG muốn làm (20/11/2026). |
| `tools/make_clean_export.sh` | Xuất một BẢN SẠCH của pack: 1 commit, không lịch sử, không dữ liệu cục bộ. |
| `tools/make_file_index.py` | Sinh lại mục "Danh sách file" trong README.md từ đĩa. |
| `tools/make_title_inventory.py` | Sinh `11_all_job_titles_2026-11-20.csv` từ dữ liệu thô ĐÃ LỌC role. |
| `tools/parse_vnw_cards.py` | Parse 42 thẻ VietnamWorks (đã đăng nhập, trích từ trình duyệt 20/11/2026). |
| `tools/purge_excluded_roles.py` | Xoá khỏi DỮ LIỆU THÔ mọi tin thuộc role Hoàn KHÔNG muốn làm. |
| `tools/purge_log_2026-11-20.csv` | cột: file, nhom_bi_loai, title, company |
| `tools/scan_pii.py` | Quét PII / bí mật trong các file ĐANG ĐƯỢC THEO DÕI. |

<!-- END FILE INDEX -->

---

## 7. Script trong `tools/`

| Script | Chức năng |
|--------|-----------|
| `crawl_linkedin_jobs.py` | Crawl LinkedIn Jobs (API công khai) |
| `crawl_glints_jobs.py` | Crawl Glints TP.HCM |
| `excluded_roles.conf` | **Bộ lọc role vĩnh viễn** (cứng: tester/PHP/BrSE/hardware/support; mềm: sales/designer/giáo viên/HR…) |
| `purge_excluded_roles.py` | Áp bộ lọc lên mọi CSV/JSON thô, ghi `purge_log_*.csv` |
| `analyze_linkedin_jobs.py` | 392 tin LinkedIn → stats + shortlist 30 |
| `analyze_itviec_hcm.py` | 75 tin ITviec → stats + shortlist + snapshot |
| `analyze_glints_platforms.py` | 86 tin Glints → stats + shortlist |
| `02_build_master.py` | Gộp 5 sàn → `data/02_postings_master.csv` (671 dòng) |
| `02_stats.py` | Tính **mọi** con số tiêu đề từ master → `data/02_stats_2026-11-20.json` |
| `build_commute.py` | Lọc theo khoảng cách, đọc `config.local.json` (không commit) |
| `make_title_inventory.py` | Sinh `data/11_all_job_titles_2026-11-20.csv` |
| `parse_vnw_cards.py` | Parse VietnamWorks HTML dump |
| `audit_books.py` | Audit 212 tài liệu → `learning/05_library_audit.csv` |
| `calc_stats.py` / `calc_overlap.py` | Kiểm tra số liệu & trùng công ty giữa sàn |
| `scan_pii.py` | Quét PII/bí mật trong file đang theo dõi (phải ra 0) |
| `check_links.py` | Rà mọi tên file được nhắc trong `.md` xem có tồn tại thật |
| `make_file_index.py` | Sinh lại mục 6 của README từ đĩa |
| `make_clean_export.sh` | Xuất `dist_clean/my-career` (1 commit, để public) |

Mọi script đều tự tìm thư mục pack từ vị trí file, nên chạy được từ bất kỳ đâu:
`python3 tools/02_stats.py`, `python3 tools/check_links.py`.

---

## 8. Nguyên tắc của pack

- ✅ **Không có bước nào yêu cầu trả tiền** (ngân sách 0 đồng)
- ✅ **Không có dòng CV nào không bảo vệ được** khi bị hỏi
- ✅ **Mọi số liệu đều có nguồn** — crawl thực, không ước đoán
- ✅ Chỗ nào chưa chắc → ghi `[Chưa biết]`, không đoán
- ✅ Không lưu số nhà, SĐT, email, CCCD trong bất kỳ file nào
- ✅ Một chủ đề = một file; thêm dữ liệu mới thì cập nhật file sẵn có, không tạo file mới cùng chủ đề

---

## 9. Riêng tư & xuất bản sạch

- **Bản công khai:** https://github.com/hoanhophuoc/my-career — sinh từ `dist_clean/my-career/`, **1 commit, không lịch sử cũ**, `scan_pii` = 0.
- **Repo làm việc (`hoan_career_pack/`) vẫn để private**: lịch sử của nó có blob cũ trước khi làm sạch (cột `km_uoc_tinh`, bản README cũ). Đừng push nhánh này lên repo công khai.
- Cấu hình cục bộ ở `config.local.json` (đã ignore); dữ liệu thô/riêng tư ở `.local_private/` (đã ignore).
- Kiểm tra trước khi chia sẻ: `python3 tools/scan_pii.py` → phải ra **0 kết quả**; `python3 tools/check_links.py` → phải in **OK**.
- Cập nhật bản công khai: `bash tools/make_clean_export.sh` → `dist_clean/my-career/` (tạo lại 1 commit mới) → `git -C dist_clean/my-career push --force origin main`. Script **không tự push**.

---

## 10. Về tác giả

**Hồ Phước Hoàn** — CNTT, tốt nghiệp Giỏi · IELTS 6.5
Mục tiêu: Java/Spring Boot Backend Engineer tại TP.HCM
Timeline: W1 24/11/2026 → W24 04/05/2027

---

*Pack xây dựng 20/11/2026. Dữ liệu thị trường crawl thực tế cùng ngày. Tái cấu trúc thư mục 21/11/2026.*
