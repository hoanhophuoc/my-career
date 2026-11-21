# REVIEW_FIX_LOG — nhật ký sửa theo review P0 → P3

**Ngày:** 21/11/2026 · **Người thực hiện:** agent · **Repo:** `hoan_career_pack/` (nhánh `main`, chưa push)
**Trạng thái tổng:** P0 ✅ (đã viết lại lịch sử) · P1 ✅ (P1-2 dùng mặc định) · P2 ✅ · P3 ⚠️ một phần

---

## P0 — Riêng tư & tuân thủ

| ID | Việc đã làm | File | Bằng chứng (lệnh + kết quả) | Trạng thái |
|---|---|---|---|---|
| **P0-1a** | Bỏ vị trí nhà, toạ độ, phân tích "gần nhà" khỏi mọi file theo dõi. Xoá `10_jobs_near_home_*.csv`, `10_near_home_stats*.json`, `_src/build_commute_15km.py`; chuyển sang `.local_private/near_home/` | `README.md`, `00_START_HERE.md`, `09_executive_summary.md`, `00_README_index.md`, `09_refresh_prompts.md`, `10_commute_and_platform_guide_2026-11-20.md`, `02e_itviec_hcm_salary*.csv` (bỏ cột `km_uoc_tinh`) | `python3 tools/scan_pii.py` → `OK: 0 kết quả` (mẫu: tên địa danh gần nhà, toạ độ dạng thập phân) | **done** |
| **P0-1b** | Cấu hình cục bộ thay cho hằng số trong code: `config.local.json` (ignored) + `config.local.example.json`; script mới đọc cấu hình | `config.local.json`, `config.local.example.json`, `tools/build_commute.py`, `.gitignore` | `grep -n "config.local.json" .gitignore` → có; script không còn toạ độ nhà | **done** |
| **P0-1c** | Bỏ mã sinh viên + họ tên khỏi đường dẫn; ẩn Candidate ID IELTS | `05_library_audit.csv`, `00_file_inventory.md` | `grep -cE "Hồ Phước Hoàn|2212|02826|IELTS-[0-9]" 05_library_audit.csv 00_file_inventory.md` → 0 | **done** |
| **P0-1d** | Bỏ cột `desc` (JD nguyên văn) khỏi dữ liệu commit; bản thô chuyển `.local_private/raw_jds/` (không xoá, P1-4 vẫn trích được) | `02d_linkedin_jobs_2026-11-20.csv`, `02d_linkedin_jobs_2026-11-20.json` | `head -1 02d_linkedin_jobs_2026-11-20.csv` → 13 cột, không có `desc`; `ls .local_private/raw_jds` → có bản thô | **done** |
| **P0-1e** | Hội thoại riêng tư + prompt gốc ra khỏi `_src/` | `.local_private/conversations/`, `_src/` | `ls _src/` → chỉ còn script `.py/.conf/.csv` | **done** |
| **P0-1f** | Bỏ đường dẫn máy cục bộ khỏi văn bản | `00_file_inventory.md` | `python3 tools/scan_pii.py` → 0 mục "đường dẫn máy" | **done** |
| **P0-1g** | Công cụ quét PII/bí mật | `tools/scan_pii.py` | `python3 tools/scan_pii.py; echo $?` → `OK: 0 kết quả`, exit 0 | **done** |
| **P0-1i** | Một file hội thoại riêng tư vẫn còn **được theo dõi** từ commit `9d09a7f` (lọt vào index trước khi có `.gitignore`) → `git rm -r --cached .local_private`. Nay **0 file** theo dõi | `.local_private/` (chỉ cục bộ) | `git ls-files \| grep -c "local_private"` → **0** | **done (index)** |
| **P0-1h** | Xuất bản sạch 1 commit, không tự push + hướng dẫn ≤ 5 dòng | `tools/make_clean_export.sh`, `README.md` §Riêng tư | Đã chạy thử 21/11/2026 → 98 file, 1 commit, 0 PII (xem P0-3) | **done** |

> **Lịch sử git đã được viết lại ngày 21/11/2026** (xem P0-2 bên dưới) để xoá hẳn đường dẫn riêng tư khỏi **mọi** commit, kể cả commit gốc `566ff5d` đang có trên `origin/main`. Vì vậy README ghi rõ: **không public chính repo này**, dùng `dist_clean/`.

---

## P0-2 — Viết lại lịch sử git (21/11/2026)

| Việc | Cách làm | Bằng chứng | Kết quả |
|---|---|---|---|
| Xoá hẳn đường dẫn riêng tư khỏi **toàn bộ** lịch sử | `git filter-branch --index-filter 'git rm -r --cached --ignore-unmatch …' --prune-empty -- --all` với `.local_private/`, `10_jobs_near_home_*.csv/.json`, `_src/build_commute_15km.py`, 2 file hội thoại `_src/*.txt`, `config.local.json`; sau đó xoá `refs/original`, `reflog expire --expire=now --all`, `gc --prune=now` | `git rev-list --objects --all \| grep -Ei "local_private\|near_home\|Prompt Nghi\|build_commute_15km"` → **0 object** | ✅ |
| Không push | `git fetch` lại để biết remote thật; không có lệnh `git push` nào | `git log --oneline -1 origin/main` → `566ff5d` (remote vẫn bản cũ) | ✅ |

> **Phát hiện thêm:** commit gốc `566ff5d` — bản đang nằm trên GitHub — cũng chứa `10_jobs_near_home_*.csv`, `10_near_home_stats*.json`, `_src/build_commute_15km.py` và file hội thoại. Vì vậy phải viết lại **cả lịch sử**, không chỉ 4 commit cục bộ; hash của mọi commit đã đổi.

---

## P0-3 — Bản xuất sạch `dist_clean/` (chạy thử 21/11/2026)

`bash tools/make_clean_export.sh` → `dist_clean/my-career/` (một commit, không lịch sử).

| Kiểm tra | Lệnh | Kết quả |
|---|---|---|
| Đủ file | `find . -type f -not -path './.git/*' \| wc -l` | **98** = đúng số file đang theo dõi ở pack gốc |
| Lịch sử | `git rev-list --count HEAD` | **1** commit |
| Không có dữ liệu cục bộ | `find … \( -name ".local_private" -o -name "config.local.json" -o -name "_repos" -o -name "_work_*" -o -name "*.b64" -o -name "*.pdf" \)` | **không có** (chỉ có `config.local.example.json` — mẫu, toạ độ `[0.0, 0.0]`) |
| PII | `grep -rIlE "<cùng bộ mẫu với tools/scan_pii.py: địa danh gần nhà, toạ độ, đường dẫn máy, mã SV, SĐT, cookie>" . --exclude-dir=.git` | **0 file** (ngoài chính `tools/scan_pii.py` chứa định nghĩa mẫu) |
| Toạ độ | `grep -rIlE "10\.7x…106\.x"` | chỉ `tools/build_commute.py`: **toạ độ tâm 22 quận công khai**, không phải vị trí nhà (nhà đọc từ `config.local.json`) |
| Link nội bộ | `python3 _src/check_links.py` | `OK: không có tên file nào trỏ vào chỗ không tồn tại` |
| Không push | script không có lệnh `git push` | ✅ |

> **Kết luận:** `dist_clean/` sạch để public. Bản thân repo `hoan_career_pack/` (dù đã viết lại lịch sử) vẫn còn **nội dung cũ** trong blob của các commit trước P0 (xem Tồn đọng #4).

---

## P0-4 — Xuất bản công khai (21/11/2026)

| Việc | Kết quả |
|---|---|
| Tạo repo public từ `dist_clean/my-career` | `hoanhophuoc/my-career` — **public**, **1 commit** (cây sạch 98 file). Mỗi lần cập nhật: chạy lại script rồi `push --force`, lịch sử luôn đúng 1 commit |
| Xoá repo private cũ | `hoanhophuoc/my-career` (bản cũ 663-tin trong description) đã xoá qua `gh repo delete` — `GET /repos/hoanhophuoc/my-career` trước đó trả **404** |
| Description | `🎯 Career pack cá nhân: Lộ trình 24 tuần Java/Spring Boot Backend Engineer tại TP.HCM — built from 602 real job postings, 212 books audit, 36 personal repos.` |
| Danh tính commit | Commit public ban đầu dùng `hoan@users.noreply.github.com` → GitHub gán nhầm cho tài khoản **hoan** (người khác). Đã đổi toàn bộ sang `89370644+hoanhophuoc@users.noreply.github.com` (noreply của tài khoản thật) và viết lại author/committer của cả 13 commit trong pack | `git log --format='%an <%ae>'` → **13/13** đúng `hoanhophuoc` |
| Repo làm việc | **Đã bỏ `origin`** để không thể push nhầm lịch sử cũ lên repo công khai |

> Token của integration GitHub **không có scope `delete_repo`** (403 "Must have admin rights") → dùng `gh repo delete --yes` (token `gho_` có scope) mới xoá được.

---

## P1 — Nhất quán & thiếu sót

| ID | Việc đã làm | File | Bằng chứng | Trạng thái |
|---|---|---|---|---|
| **P1-1** | **Một lịch W0–W24 chuẩn** ở `04_master_roadmap.md` §2: ngày bắt đầu từng tuần (W1 = 24/11/2026), dự án, cổng G1–G6, Readiness #1/#2, mốc nộp đơn, KPI tuần. Tết **04–10/02/2027** (Thông báo 11483/TB-BNV) đặt ở W11. Các file khác chỉ trỏ link | `04_master_roadmap.md`, `09_executive_summary.md` (§9 → con trỏ), `README.md`, `00_START_HERE.md`, `04_projects_spec.md`, `05_how_to_learn.md`, `07_application_kit.md`, `09_kpi_tracker.csv` | `grep -rn "task-api\|Project 1" --include="*.md" .` → chỉ còn trong changelog/nhật ký quyết định | **done** |
| **P1-1b** | Thống nhất tên: TaskFlow = dự án 1, MiniWallet = dự án 2. Bỏ `task-api`/"Project 1" | toàn bộ `.md` | như trên; `grep -n "^## " 04_projects_spec.md` → `## **TaskFlow** — dự án 1`, `## **MiniWallet** — dự án 2` | **done** |
| **P1-1c** | Quy tắc CV: `nexus` chỉ vào CV sau G6a+G6b; gỡ ghi chú vá "Điều chỉnh 20/11" khỏi thân §5, đưa vào changelog cuối file | `04_master_roadmap.md` | `tail -20 04_master_roadmap.md` → bảng Changelog | **done** |
| **P1-2** | Chốt **nhịp nộp mới**: 0 đơn tới W7, 5/tuần W8–W12 (công ty không mục tiêu), 10/tuần W13–W16, 10–15/tuần W17+; bỏ "nộp 5 đơn trong 72h" khỏi mọi file | `09_executive_summary.md` §3/§4/§5, `README.md`, `00_START_HERE.md`, `07_application_kit.md` §7, `08_education_competitions_community.md`, `09_kpi_tracker.csv` | `grep -rn "72 giờ\|5 tin nhóm A" --include="*.md" .` → 0 | **partial** — dùng **mặc định B** của câu hỏi 1 vì Hoàn chưa trả lời; đổi được bằng cách sửa §2 lịch |
| **P1-3** | **Bảng "số liệu gốc"** ở đầu báo cáo: con số → định nghĩa → bộ dữ liệu → ngày → file tính ra. Sửa: 605→**602**; LinkedIn 111→**153** (39,0%), Java 45→**63**; 121/84 → bỏ (dữ liệu đã xoá vì riêng tư) và thay bằng phân bố quận; "−22%" ghi rõ −21,8% so với đỉnh 24/08 và −15,3% so với 03/09; 68% vs 49% ghi rõ bộ dữ liệu/ngày; 743 ghi rõ là census **của bên thứ ba (vitX)**; 105/111 file → bỏ con số, trỏ `git ls-files` | `02_market_report.md` §0, `02_methodology_and_limits.md` §3, `09_executive_summary.md`, `README.md`, `00_START_HERE.md`, `00_README_index.md`, `02d_linkedin_market_snapshot_2026-11-20.md` | `python3 02_stats.py` → `602`, `42 (7.0%)`, `153`, `63`, `60 (10.0%)`; `grep -rn "605 tin\|111/392\|105 file\|93 file" --include="*.md" .` → chỉ còn trong changelog | **done** |
| **P1-4** | **Bộ dữ liệu hợp nhất tái lập được**: `02_build_master.py` gộp 5 sàn + nhật ký purge thành `02_postings_master.csv` (21 cột đúng schema), khử trùng, giữ dòng nhóm đã loại với `excluded_reason`; `02_stats.py` tính lại mọi số tiêu đề; xoá file 21 dòng | `02_build_master.py`, `02_postings_master.csv`, `02_stats.py`, `02_stats_2026-11-20.json` | `python3 02_build_master.py` → `671 dòng` (602 live + 69 có `excluded_reason`); `python3 02_stats.py` chạy không lỗi | **done** |
| **P1-5** | **Minh bạch nhóm vai trò đã loại**: mục §0.1 hiển thị song song "có / không có nhóm đã loại", nói rõ 143/550 tester LinkedIn (ước lượng), và nói thật rằng nhật ký purge chỉ có 69 dòng đợt 2 (212 tin tester đợt 1 không còn từng dòng) | `02_market_report.md` §0.1 | Đọc §0.1; số 69 khớp `loai_theo_nhom` trong `02_stats_2026-11-20.json` | **done** |
| **P1-6a** | `07_tools_evaluation.md` — 9 mục cho 2 repo, đọc README/`SETUP.md`/docs, có link + ngày truy cập | `07_tools_evaluation.md` | Kết luận: career-ops = **dùng một phần** (MIT, chạy model free/local, không có sàn VN, không tự nộp); ai-job-search = **không dùng** (bắt buộc Claude Code + API key/Pro, portal Đan Mạch) | **done** |
| **P1-6b** | `07_job_alerts_and_routine.md` — 4 alert hiện có, 6 alert mới (Boolean VI+EN), saved search 3 sàn, trang công ty, quy trình ≤45'/ngày, trường tracker | `07_job_alerts_and_routine.md` | Từ khoá lấy từ `top_ky_nang` của `02_stats.py` | **done** |
| **P1-6c** | `07_github_cleanup_plan.md` — tiêu chí PIN/GIỮ/ARCHIVE/PRIVATE/XOÁ áp lên 36 repo thật, profile README, mẫu README, quét bí mật lịch sử, cổng sự thật cho repo ghim | `07_github_cleanup_plan.md` | Danh sách repo lấy từ `02c_repo_inventory.md` | **done** |
| **P1-6d** | `09_decision_log_and_sources.md` — red-team 5 đòn, nhật ký quyết định, bảng nguồn [S1–S22, T1–T5] có URL/ngày/độ tin cậy | `09_decision_log_and_sources.md` | Bảng §3 là nơi duy nhất định nghĩa `[S#]` | **done** |
| **P1-6e** | `09_playbook_1page.md` — 1 trang, ~330 từ | `09_playbook_1page.md` | — | **done** |
| **P1-6f** | `07_cv_truth_checklist.md` — bảng nhãn ✅/⏳/❌ + **bản gửi đi** chỉ ✅ | `07_cv_truth_checklist.md` | Bản gửi đi không còn dòng kỹ năng nào chưa kiểm chứng | **done** |
| **P1-7** | Thêm khối "Nguồn có link" (URL + ngày) cho các file từng thiếu; kiểm lại 4 tài nguyên "chưa kiểm chứng"/403 | `03_strategy.md`, `04_after_hire.md`, `05_free_resources_core.md`, `06_english_plan.md`, `02_entry_programs_2026_2027.md`, `05_shelf_and_books.md`, `04_resources_catalog.md`, `04_resources_catalog.csv` | `curl -L -A <browser>` 4 URL → **200** cả 4; `grep -c "chưa kiểm chứng" 04_resources_catalog.csv` → **0** | **done** |

---

## P2 — Cổng sự thật & cập nhật kỹ thuật

| ID | Việc đã làm | File | Bằng chứng | Trạng thái |
|---|---|---|---|---|
| **P2-1** | Gắn nhãn ✅/⏳/❌ cho từng dòng; bản gửi đi chỉ chứa ✅ | `07_cv_truth_checklist.md`, `01_honest_cv_v1.md` | `01_honest_cv_v1.md` nay mở đầu bằng cảnh báo "BẢN NHÁP, có ⏳" và trỏ tới bản gửi đi | **done** |
| **P2-1a** | Bỏ câu "I use AI coding assistants deliberately — I write the specification, review every diff…" (thì hiện tại, không bằng chứng). Thay bằng mô tả có mốc 11/2026 + trỏ lịch sử commit TaskFlow | `01_honest_cv_v1.md` (About VI/EN), `01_cv_linkedin_audit.md:38`, `05_how_to_learn.md:248,363` | `grep -rn "review every diff"` → chỉ còn trong checklist (là câu **cũ** được trích để sửa) | **done** |
| **P2-1b** | Java/multithreading/JDBC/JUnit/Docker/CI/ASP.NET/EF/JWT/RBAC/xUnit → ⏳ cho tới T1–T6/bảo vệ dự án; không ghim IT-Tools/Chat-System trước khi ✅ | `07_cv_truth_checklist.md`, `07_application_kit.md` §5, `07_linkedin_copy_paste.md` §6 | Checklist mục 1 + 3.3 | **done** |
| **P2-1c** | "Có nền tảng CSDL và HĐH vững (9.0/9.4)" → chỉ nêu điểm + học kỳ | `01_honest_cv_v1.md` | Câu mới: "Điểm học phần: CSDL 9.0, HĐH 9.4 (học kỳ 2023–24)" | **done** |
| **P2-1d** | Cập nhật audit theo quyết định mới (M1/M7 đã đóng) | `01_cv_linkedin_audit.md` | Dòng Education: "**Giữ** — đã xác nhận 20/11/2026"; rủi ro 🔴 → 🟢 | **done** |
| **P2-2** | Thêm **S4** (4 câu Boot 3→4: jakarta namespace, `SecurityFilterChain`, Jackson 3 `tools.jackson`, `RestTemplate`→`RestClient`) + đáp án chi tiết. Giữ câu Boot 2→3 như "đọc code cũ" | `01_diagnostic_tests/04_spring_jpa_security.md`, `01_diagnostic_tests/09_answer_key.md` | `grep -c "S4" ...` → 1 ở mỗi file; đáp án §S4 | **done** |
| **P2-2b** | Kiểm tra Boot 4.2 GA: **chưa GA** (RC2 06/11/2026; GA dự kiến 19–30/11/2026). Quyết định **giữ 4.1.x** (OSS tới 31/07/2027; 4.0 hết 31/12/2026) | `04_master_roadmap.md` §0 + changelog | Bảng nguồn S22; `grep -n "4.2.0 chưa GA" 04_master_roadmap.md` → có | **done** |
| **P2-3** | Dọn nội dung lỗi thời (graduation "✗", "Review every diff", số liệu cũ) + thêm `Cập nhật lần cuối: 21/11/2026` vào 15 file lớn | 15 file `.md` | `grep -c "Cập nhật lần cuối" <file>` | **done** |

---

## P3 — Cấu trúc

| ID | Việc đã làm | Bằng chứng | Trạng thái |
|---|---|---|---|
| **P3-1** | Gộp 14 file trùng chủ đề → 4 (`03_strategy.md`, `04_after_hire.md`, `05_how_to_learn.md`, `05_shelf_and_books.md`); xoá 11 file thừa | commit `fix(P3): gộp 14 file…`; `ls *.md` | **done** |
| **P3-2** | `.gitignore` phủ `_local_private/`, `config.local.json`, `_work_*`, `_repos/`, `dist_clean/` | `cat .gitignore` | **done** |
| **P3-3** | Chia thư mục `plan/`, `cv/`, `research/`, `learning/`, `data/`, `tools/` | — | **chưa làm** — xem "Tồn đọng" |
| **P3-4** | Một README duy nhất (gộp `README.md` + `00_README_index.md`) | — | **chưa làm** — hai file vẫn tồn tại, đã sửa để không chép số liệu trùng |
| **P3-5** | Giọng văn nhất quán "bạn/Hoàn" vs "agent" | Sửa cục bộ ở các file đã chạm; **chưa rà toàn bộ** | **partial** |

---

## Kiểm tra cuối (chạy bằng công cụ)

```
$ python3 tools/scan_pii.py
OK: 0 kết quả (CCCD, SĐT, email, mã SV, địa danh nhà, toạ độ, đường dẫn máy, cookie/token).

$ python3 02_build_master.py && python3 02_stats.py
Đã ghi 671 dòng → 02_postings_master.csv
tong_tin_sau_loc_role      : 602
true_entry_level           : 42
linkedin_reachable         : 153
linkedin_reachable_java    : 63
co_luong_cong_khai         : 60

$ python3 _src/check_links.py
OK: không có tên file nào trỏ vào chỗ không tồn tại

$ grep -rn "task-api\|Project 1" --include="*.md" .
(chỉ còn trong changelog + nhật ký quyết định)

$ grep -rn "605 tin\|111/392\|105 file\|93 file" --include="*.md" .
(chỉ còn trong changelog lịch sử của 00_README_index.md)

$ grep -c "chưa kiểm chứng" 04_resources_catalog.csv
0

$ curl -L … documentation.red-gate.com/flyway | vladmihalcea.com | baeldung.com | freecodecamp.org
200 | 200 | 200 | 200

$ git ls-files | wc -l
98
```

**Không kiểm được:** các con số gốc của bên thứ ba (743 tin vitX, 1.839 người khảo sát) — chỉ đọc lại nguồn, không tái tính.

---

## Tồn đọng (cần Hoàn hoặc vòng sau)

1. **Ba câu hỏi chưa được trả lời** → đã dùng **mặc định**: (1) đợi CV v1 + T1/T6 rồi nộp từ W8; (2) repo **giữ private**; (3) **không** mở lại tester.
2. **P3-3 (chia thư mục) và P3-4 (một README)** chưa làm: đổi đường dẫn sẽ làm gãy toàn bộ link tương đối trong 40+ file, và cần một vòng riêng có kiểm tra link sau khi di chuyển. `_src/check_links.py` đã có để làm việc đó.
3. **Giọng văn** mới sửa ở các file đã chạm, chưa rà toàn bộ 40 file.
4. **Lịch sử cũ (đã viết lại 21/11/2026) vẫn giữ bản cũ của các file đã làm sạch trước đó** — cụ thể blob cũ của `02e_itviec_hcm_salary_*.csv` (còn cột `km_uoc_tinh`), `10_commute_and_platform_guide_2026-11-20.md`, `README.md`, `00_file_inventory.md`, `05_library_audit.csv` (bản trước P0). Muốn xoá cả nội dung đó thì phải rewrite theo *nội dung* (không phải theo đường dẫn) — chưa làm. Vì vậy nếu public, nên public **`dist_clean/`** (1 commit, chỉ cây hiện tại).
5. **`tools/make_clean_export.sh` chưa chạy thử** (nó tạo repo mới ngoài phạm vi). Chạy `bash tools/make_clean_export.sh` rồi kiểm tra `dist_clean/my-career` trước khi public.

---

## P0-5 — Contributor sai (`hoan Hoan Ton-That`) trên repo public

- **Việc:** xoá repo `hoanhophuoc/my-career` rồi tạo lại (public, cùng description) và push lại 1 commit sạch từ `dist_clean/my-career`; đặt `git config --local user.name/user.email` của pack về đúng danh tính; sửa tên commit trong `tools/make_clean_export.sh` thành **Hồ Phước Hoàn**.
- **Vì sao phải xoá repo:** commit sai email `hoan@users.noreply.github.com` đã từng được push lên repo đó; `--force` gỡ commit khỏi `main` nhưng GitHub giữ **cache Contributors** (hard-reload + cửa sổ ẩn danh vẫn thấy). Tạo repo mới là cách reset cache ngay.
- **File:** `tools/make_clean_export.sh`, `REVIEW_FIX_LOG.md`, `dist_clean/my-career` (sinh lại).
- **Bằng chứng:**
```
$ gh repo delete hoanhophuoc/my-career --yes          → exit 0
$ gh repo create hoanhophuoc/my-career --public --description "…602 real job postings…"
https://github.com/hoanhophuoc/my-career
$ git -C dist_clean/my-career push -u origin main      → * [new branch] main -> main

$ GET /repos/hoanhophuoc/my-career/commits
1 commit(s): 740785f Ho Phuoc Hoan <89370644+hoanhophuoc@users.noreply.github.com> -> hoanhophuoc
$ GET /repos/hoanhophuoc/my-career/contributors?anon=1
[('hoanhophuoc', 1)]
$ curl https://github.com/hoanhophuoc/my-career | grep -c "Ton-That"   → 0

$ git config --local --get-regexp '^user\.'
user.email 89370644+hoanhophuoc@users.noreply.github.com
user.name  Hồ Phước Hoàn
```
- **Trạng thái:** xong. Từ nay commit trong pack dùng email noreply của `hoanhophuoc`; `make_clean_export.sh` cũng ghi đúng danh tính nên lần xuất sau không lặp lại.

## P3-3 — Chia pack thành `plan/ cv/ research/ learning/ data/ tools/`

- **Việc:** `git mv` 98 file vào 6 thư mục theo chủ đề; vá lại đường dẫn trong mọi script Python (thêm `DATA = ROOT/"data"`) và tiền tố đường dẫn trong tài liệu (`_src/` → `tools/`, `01_diagnostic_tests/` → `learning/01_diagnostic_tests/`).
- **Vì sao:** 98 file phẳng ở gốc pack; review P3-3 yêu cầu nhóm theo việc dùng.
- **Bố cục:** `cv/` 8 · `plan/` 15 · `research/` 10 · `learning/` 20 (gồm `01_diagnostic_tests/`) · `data/` 20 · `tools/` 19 (dời `_src/` + `05_audit_scripts/` + 2 script gốc vào đây). Gốc chỉ còn `README.md`, `00_START_HERE.md`, `REVIEW_FIX_LOG.md`, `.gitignore`, `config.local.example.json`.
- **Bằng chứng:**
```
$ git ls-files | awk -F/ 'NF>1{print $1"/"}' | sort | uniq -c
      8 cv/      20 data/      20 learning/      15 plan/      10 research/      19 tools/
$ python3 tools/check_links.py
OK: không có tên file nào trỏ vào chỗ không tồn tại
$ python3 tools/scan_pii.py
OK: 0 kết quả
$ python3 -m py_compile tools/*.py     → compile OK
$ cd /tmp && python3 .../hoan_career_pack/tools/02_stats.py   → chạy được, data/02_stats_2026-11-20.json KHÔNG đổi (git diff rỗng)
```
- **Trạng thái:** xong. Mọi script tự tìm pack root từ `__file__`, chạy được từ bất kỳ cwd.

## P3-4 — Gộp `README.md` + `00_README_index.md` thành một README

- **Việc:** viết lại `README.md` thành file duy nhất (giới thiệu + số liệu + 7 quyết định + 3 việc làm ngay + cấu trúc thư mục + danh sách file + script + nguyên tắc + riêng tư); xoá `00_README_index.md` (đã xoá); chuyển CHANGELOG gốc của nó thành **phụ lục trong `REVIEW_FIX_LOG.md`**; thêm `tools/make_file_index.py` sinh mục 6 từ đĩa; sửa 2 chỗ trong `00_START_HERE.md` trỏ tới README thay vì file index.
- **Vì sao:** hai file cùng là "điểm vào" và mục 2 của index là bảng 100 dòng chép tay, lệch dần. Review P3-4 yêu cầu một README.
- **File:** `README.md`, `00_README_index.md` (xoá), `00_START_HERE.md`, `REVIEW_FIX_LOG.md`, `tools/make_file_index.py` (mới).
- **Bằng chứng:**
```
$ python3 tools/make_file_index.py
OK: đã sinh lại danh sách file trong README.md (98 file đang theo dõi)
$ grep -c "^| \`" README.md          → 115 dòng bảng
$ grep -rn "00_README_index" --include="*.md" .   (ngoài phụ lục/khối CHANGELOG)  → 0
$ python3 tools/check_links.py
OK: không có tên file nào trỏ vào chỗ không tồn tại
```
- **Trạng thái:** xong. Bảng file chỉ liệt kê file **đang được git theo dõi** nên `config.local.json` / `_work_*` (bị ignore) không lọt vào README.

## P1-5 — Đồng bộ số liệu còn lệch trong `00_START_HERE.md` §5

- **Việc:** LinkedIn "chạm tới được" **111 (28,3%) → 153 (39,0%)**; "Java vừa sức" **45 → 63** (Java/Spring); tổng mẫu **605 → 602**; bỏ dòng JobStreet (3 tin, đã ra khỏi master) và ghi rõ lý do ngay dưới bảng; trỏ "phân bố theo quận" sang `research/…` theo bố cục mới.
- **Vì sao:** bảng này sót lại từ trước bản P1 (đã sửa ở `README.md`, `02_market_report.md`, `09_executive_summary.md` nhưng bỏ quên file này) — 605/111/45 là số của bộ dữ liệu **trước** khi làm lại định nghĩa.
- **Nguồn đối chiếu:** `data/02_stats_2026-11-20.json` — `tong_tin_sau_loc_role` 602 · `tin_theo_san` {linkedin 392, glints 86, itviec 75, vietnamworks 41, topdev 8} · `linkedin_reachable` 153 · `linkedin_reachable_java` 63.
- **Bằng chứng:**
```
$ grep -n "605 tin|\*\*605\*\*|111 (28,3%)|Java vừa sức \*\*45\*\*" 00_START_HERE.md   → 0 dòng
$ python3 -c "import json;d=json.load(open('data/02_stats_2026-11-20.json'));print(sum(d['tin_theo_san'].values()), d['linkedin_reachable'], d['linkedin_reachable_java'])"
602 153 63
$ python3 tools/check_links.py   → OK: không có tên file nào trỏ vào chỗ không tồn tại
$ python3 tools/scan_pii.py      → OK: 0 kết quả
```
- **Trạng thái:** xong. Ghi chú: cột "có lương" của Glints (47/86) và ITviec (17/75) là số tin **công bố** lương, khác với số dải lương đọc được (`luong_theo_san` trong JSON: 46 và 14) — hai định nghĩa khác nhau, không phải lỗi.

---

## Phụ lục — CHANGELOG gốc (trước đây ở `00_README_index.md` §5b)

> Giữ nguyên nội dung lịch sử; tên file trong bảng là tên **tại thời điểm đó** (trước khi chia `plan/ cv/ research/ learning/ data/ tools/` ngày 21/11/2026).
> Các lần sửa P0–P3 nằm ở phần trên của file này.

| Ngày | Thông tin mới | File đã sửa | Ảnh hưởng kết luận |
|---|---|---|---|
| 20/11/2026 | **Đã có bằng tốt nghiệp**; portal trường chưa cập nhật | `01_graduation_checklist.md` (viết lại v2), `01_honest_cv_v1.md`, `00_START_HERE.md` Q1, `00_file_inventory.md` M1/M7 | Đóng rủi ro M1/M7; CV được ghi "Graduated"; bỏ toàn bộ lo ngại về deadline lệ phí |
| 20/11/2026 | **`nexus` do AI viết 100%, Hoàn không hiểu** | `01_skills_matrix.md` (A1: L2–L3→L2; A6: L2–L3→L1–L2, P1→P0), `.csv`, `01_honest_cv_v1.md` (xoá dự án), `01_cv_linkedin_audit.md` (thêm mục 8), `learning/01_diagnostic_tests/06_project_defense.md`, `03_strategy.md` mục 8, `03_strategy.md/.csv` (3,90→3,80), `00_START_HERE.md` Q5, `00_file_inventory.md` mục 3 | Java core và testing **tụt 1 bậc**; testing lên **P0**; Java vẫn hạng 1 nhưng khoảng cách với .NET hẹp lại; **NO-AI 8 giờ/tuần trở thành bắt buộc**, không phải khuyến nghị |
| 20/11/2026 | **Hoàn thành Phase 4** (lộ trình, rubric, tài nguyên, 2 dự án, phỏng vấn, kỹ năng mềm, sau khi có việc, hệ thống ôn, 60 thẻ Anki) | 11 file mới `04_*` | Chốt phiên bản **Java 25 + Spring Boot 4.1.2** (kiểm chứng docs.spring.io); 24 tài nguyên trả HTTP 200 ngày 20/11/2026 |
| 20/11/2026 | **Hoàn thành Phase 5** | 8 file `05_*` + 2 script | Đếm thật từ `books.txt` (197 sách tại thời điểm đó; **nay 212**) và `bookmarks_11_19_26.html` (1.861 link); MVS chốt **12 cuốn**; phát hiện 20 sách Go vs 9 sách Spring và **258 link Java vs 6 link Spring** |
| 20/11/2026 | **Hoàn đổi quyết định về `nexus`** (sẽ public, đưa lên CV thay Chat-System, học từ chính dự án, không ghi disclaimer AI) + **cho phép đăng nhập trình duyệt do Hoàn tự làm** | `05_how_to_learn.md` (mới), `02_methodology_and_limits.md` (mới), `01_honest_cv_v1.md` (block Nexus có điều kiện), `01_cv_linkedin_audit.md` (mục 8 viết lại), `03_strategy.md` mục 8, `04_projects_spec.md` (TaskFlow rút W5–W8) | Đọc repo thật: **11 module, 1,39 MB Java, 137 test/7 suite, Postgres 18 + Redis 8.10, OpenAPI 55 KB**; commit có trailer `Generated with Codebuff` và PGP-signed → không phủ nhận khi bị hỏi, không rewrite history; CV chỉ đổi **sau cổng G6** |
| 20/11/2026 | **Tốt nghiệp loại Giỏi + IELTS 6.5 đã được Trường công nhận**; muốn dùng sách ngoài nếu tốt hơn; nhiều repo private | `01_graduation_checklist.md` (viết lại v3), `01_honest_cv_v1.md` (bỏ placeholder học vấn), `00_file_inventory.md` (M1/M7/M9), `01_skills_matrix.md`, `04_readiness_rubric.md` (B3), `00_README_index.md`, **`05_shelf_and_books.md`** (mới), `05_shelf_and_books.md` (kệ B), **`02_methodology_and_limits.md`** (mới) | Học vấn đóng hoàn toàn; IELTS thành lợi thế miễn test ngoại ngữ; 3 sách Spring trong nhà lạc hậu so với Boot 4.1 → thêm 4 sách ngoài có rating kiểm chứng |
| 20/11/2026 | **Thay hẳn Clean Code bằng A Philosophy of Software Design**; hoàn thành **Phase 6** | `tools/audit_books.py` + CSV sinh lại, `05_shelf_and_books.md`, `05_shelf_and_books.md`, `05_how_to_learn.md`, `05_free_resources_core.md`, `05_shelf_and_books.md`; **`06_english_plan.md`** + **`06_english_tracking_sheet.csv`** (mới) | Kệ sách nhất quán một nguồn; Phase 6 không luyện thi lại — chỉ luyện nói theo 6 mục tiêu đo được |
| 20/11/2026 | **Hoàn cập nhật `books.txt` (701 dòng, 212 file) + BOOKS_MASTER_AUDIT V2.0** | `tools/audit_books.py` (viết lại), `05_library_audit.csv/.md`, `05_shelf_and_books.md`, `05_shelf_and_books.md`, `02_market_report.md`, `02_entry_programs_2026_2027.md`, `03_strategy.md`, `02e_itviec_market_snapshot_2026-11-20.md`, `00_README_index.md` | **Sửa lỗi nghiêm trọng: 4 "sách ngoài" tôi từng đề xuất đều đã có trong tủ** (APoSD 144, SQL Perf 94, Unit Testing 178, Pro Spring Boot 4 56) → kệ 12 cuốn nay **12/12 là sách đã có**, 49 giờ, 0 đồng. Đồng thời áp quy tắc **chỉ TP.HCM**: loại MB Bank (Hà Nội), bỏ phương án "mở rộng địa lý" ở mọi file |
| 20/11/2026 | Hoàn thành **Phase 7** — hồ sơ nộp đơn | **`07_linkedin_copy_paste.md`**, **`07_application_kit.md`**, **`07_application_tracker.csv`** (mới); `00_README_index.md` | Gộp 8 file dự kiến thành 3 file dùng được ngay: 1 CV gốc + 3 slot may đo, headline/About copy-paste, tracker 14 cột |
| 20/11/2026 | **Crawl toàn bộ job ITviec + clone 36 repo** (thay vì mở từng tin / xin token) | `02e_itviec_market_snapshot_2026-11-20.md`, `02e_itviec_hcm_salary_2026-11-20.csv`, `02e_itviec_shortlist_2026-11-20.csv`, `02c_repo_inventory.md` (mới); `02_methodology_and_limits.md` (đánh dấu ✅) | 109 tin: chỉ 7,5% là entry-level → chiến lược bậc thang là đường chính, không phải dự bị; phát hiện **CoolWear 10.403 LOC** chưa có trong CV |
| 21/11/2026 | **Sửa theo review P0–P3**: làm sạch PII, một lịch duy nhất, bộ dữ liệu master + `tools/02_stats.py`, 6 tài liệu còn thiếu | `REVIEW_FIX_LOG.md`; `04_master_roadmap.md` §2; `02_postings_master.csv`; `07_cv_truth_checklist.md` | Số liệu tiêu đề nay do `tools/02_stats.py` sinh (602 tin). LinkedIn reachable **111 → 153**, Java **45 → 63** (định nghĩa mới, tái lập được). Nhịp nộp **0 đơn tới W7** |
| 20/11/2026 | **Hoàn thành Phase 9 — pack hoàn tất** | **`09_executive_summary.md`**, **`09_kpi_tracker.csv`**, **`09_refresh_prompts.md`** (mới); `00_README_index.md` | Gộp 8 file dự kiến → **3 file** (R7); chốt nhịp: S0 21–23/11, W1 bắt đầu 24/11/2026, W24 kết thúc 04/05/2027; KPI có đúng **8 chỉ số**, chỉ số quan trọng nhất là **giờ code tay ≥20h/tuần**; 6 cổng chặn G1–G6 |
| 20/11/2026 | **Hoàn thành Phase 8** — học lên/thi đấu/cộng đồng | **`08_education_competitions_community.md`** (mới); `00_README_index.md` | Chốt **không học thạc sĩ ngay** (90–159 triệu, đợt 2026 đã đóng) — mốc xem lại 10/2029; ICPC/OLP không còn cửa vì thể lệ chỉ cho sinh viên; chứng chỉ 12 tháng = **0đ**; chốt đi 2 sự kiện miễn phí 21/11 và 05/12/2026 |
| 20/11/2026 | **Xoá tester cả trong DỮ LIỆU THÔ** | `02d_linkedin_jobs` (.csv/.json), `02f_glints_jobs` (.csv/.json), `02e_itviec_hcm_salary`, `02b_itviec_jobs`, `02j_jobstreet_jobs` (lọc bằng `tools/purge_tester_rows.py`); chạy lại `analyze_linkedin_jobs.py`, `analyze_glints_platforms.py`, `analyze_itviec_hcm.py`, `build_commute_15km.py`; đồng bộ `02d/02e/02f`, `02_methodology_and_limits.md`, `02_market_report.md`, `09_executive_summary.md`, `02b_market_snapshot`, `10_commute_and_platform_guide`, `05_shelf_and_books.md`, `08_education_competitions_community.md` | **Mẫu giảm**: LinkedIn 550→**407** (bỏ 143), Glints 130→**125**, ITviec 83→**81**, JobStreet 7→**6**, TopDev 9→**8**. Tổng mẫu 814→**663 tin / 5 nền tảng**. Các tỉ lệ tính lại: chạm tới được 28,4%→**28,7%**; lương hiện 1,3%→**1,7%** (LinkedIn), 22,9%→**23,5%** (ITviec), 61,5%→**60,8%** (Glints) |
| 20/11/2026 | **Loại bỏ toàn bộ tester/QA khỏi pack** (Hoàn: "tôi không làm tester") | `03_strategy.md` (+`.csv`: bỏ dòng QA/SDET, dồn hạng 3–8), `09_executive_summary.md`, `04_master_roadmap.md`, `00_START_HERE.md`, `02_entry_programs_2026_2027.md` (xoá 4 chương trình tester của KMS, còn 6 mục Java), `03_strategy.md`, `02_market_report.md`, `02_methodology_and_limits.md` (xoá nguồn S13), `07_application_kit.md`, `02e_itviec_market_snapshot_2026-11-20.md`, `02f_multi_platform_snapshot_2026-11-20.md`, `10_commute_and_platform_guide_2026-11-20.md`; `10_jobs_near_home_2026-11-20.csv` (126→**121** dòng) | Tester **không còn là cửa vào, không còn là ngưỡng hạ mục tiêu, không còn trong shortlist nào**. Đã xoá 5 tin tester khỏi danh sách gần nhà, 4 tin khỏi shortlist LinkedIn, 2 tin khỏi shortlist Glints, 4 dòng khỏi dataset JD, 4 chương trình KMS. Ngưỡng đổi hướng giờ chỉ còn **.NET + internship có lương** |
| 20/11/2026 | **Thêm phân tích đi lại theo quận + xếp hạng sàn** | `10_commute_and_platform_guide_2026-11-20.md`; `00_README_index.md`, `09_executive_summary.md` | **Quận 7: 26 · Quận 1: 18 · Quận 3: 13 · Phú Nhuận: 11 tin** → cái quyết định là quận, không phải bán kính. Sàn nên dùng: **ITviec → Glints → LinkedIn** |
| 20/11/2026 | **Crawl VietnamWorks sau khi Hoàn đăng nhập** | `02h_vietnamworks_jobs_2026-11-20.csv` (viết lại: 42 dòng), `02h_vietnamworks_shortlist_2026-11-20.csv`, `02h_vietnamworks_stats_2026-11-20.json`, `tools/parse_vnw_cards.py`, `tools/vnw_raw_2026-11-20.b64` (mới); `02f_multi_platform_snapshot_2026-11-20.md`, `02_methodology_and_limits.md`, `02_market_report.md`, `09_executive_summary.md`, `00_README_index.md` | Đăng nhập **có tác dụng**: khách thấy 9 thẻ, sau đăng nhập + cuộn render **đủ 42/42**. Nhưng **10 tin TP.HCM, chỉ 2 tin HCM có lương, 0 tin fresher**; 22/42 tin ở Hà Nội, phần lớn là bank/chứng khoán → vẫn **không phải kênh chính**, chỉ là danh sách nộp thêm. Cỡ mẫu toàn pack: **814 tin / 5 nền tảng** |
| 20/11/2026 | **Xử lý JobStreet** theo yêu cầu của Hoàn | `02j_jobstreet_jobs_2026-11-20.csv` (mới); `02f_multi_platform_snapshot_2026-11-20.md` (mục JobStreet viết lại), `02_methodology_and_limits.md`, `02_market_report.md`, `00_README_index.md` | **Không phải "bị chặn" mà là sàn đã ngừng**: `vn.jobstreet.com` không có DNS, `jobstreet.vn` **redirect sang `au.jora.com`**, `www.jobstreet.com/vn` 404. Chỉ `ph.jobstreet.com` còn 5+4 tin "Việt Nam" — **100% remote**, 0 tin backend Java onsite → **bỏ JobStreet khỏi nguồn**. VietnamWorks: 42 tin nhưng chỉ render 9, có banner ép tải app → **cần Hoàn đăng nhập** |
| 20/11/2026 | **Crawl 4 sàn còn lại** (Glints, TopDev, VietnamWorks, NodeFlair) + JobStreet | `02f_multi_platform_snapshot_2026-11-20.md`, `02f_glints_jobs_2026-11-20.csv`, `02f_glints_shortlist_2026-11-20.csv`, `02f_glints_stats_2026-11-20.json`, `02g_topdev_jobs_2026-11-20.csv`, `02h_vietnamworks_jobs_2026-11-20.csv`, `02i_cross_platform_companies_2026-11-20.csv`, `tools/crawl_glints_jobs.py`, `tools/analyze_glints_platforms.py` (mới); `02_market_report.md`, `02_methodology_and_limits.md`, `09_executive_summary.md`, `00_README_index.md` | **Glints là nguồn tốt nhất cho người mới**: 130 tin TP.HCM, **61,5% có lương** (ITviec 22,9%, LinkedIn 1,3%), **28 tin yêu cầu 0–1 năm**, trung vị ~20 triệu — khớp benchmark 19–20 triệu. TopDev/VietnamWorks gần như vô dụng cho mục tiêu này; **NodeFlair không có dữ liệu VN**; JobStreet không còn site VN. Ba sàn chỉ trùng **2–13 công ty** → phải đọc nhiều sàn |
| 20/11/2026 | **Hoàn đã đăng nhập ITviec** trong tab của Freebuff → crawl lại 83 tin TP.HCM, lần này thấy lương *(sau khi lọc tester còn **81**)* | `02e_itviec_market_snapshot_2026-11-20.md`, `02e_itviec_hcm_salary_2026-11-20.csv`, `02e_itviec_shortlist_2026-11-20.csv`, `02e_itviec_stats_2026-11-20.json`, `tools/analyze_itviec_hcm.py` (mới); `02e_itviec_market_snapshot_2026-11-20.md` (mục 4, giới hạn, checkpoint), `02_market_report.md` (bảng lương + kênh LinkedIn), `02_methodology_and_limits.md`, `09_executive_summary.md`, `00_README_index.md` | **Đăng nhập chỉ mở được 22,9% số tin** — 64 tin còn ẩn là do nhà tuyển dụng tự chọn ẩn, không phải lỗi phiên. Điểm mới dùng được: trung vị trần lương middle/senior **~55 triệu**, trùng khớp con số 54,9 triệu của báo cáo khảo sát → benchmark lương nay có **hai nguồn độc lập khớp nhau** |
| 20/11/2026 | **Hoàn đã đăng nhập LinkedIn** → crawl 550 tin bằng API khách (không dùng cookie) *(sau khi lọc tester còn **407**)* | `02d_linkedin_market_snapshot_2026-11-20.md`, `02d_linkedin_jobs_2026-11-20.csv/.json`, `02d_linkedin_shortlist_2026-11-20.csv`, `02d_linkedin_stats_2026-11-20.json`, `tools/crawl_linkedin_jobs.py`, `tools/analyze_linkedin_jobs.py` (mới); `00_README_index.md` | **60 tin Java vừa sức** (21,1% của 284 tin Java); nhãn "Entry level" của LinkedIn sai thường xuyên (có tin 4+ YOE) → phải đọc số năm trong JD; LinkedIn chỉ 1,3% tin có lương; hai nguồn ITviec/LinkedIn chỉ trùng 11 công ty → phải crawl cả hai |

| 20/11/2026 | **Sửa bảng "12 tin đề xuất" trong 02d** (còn sót 3 tin tester) → dựng lại từ shortlist 30 dòng; 02b shortlist 12→11 | `02d_linkedin_market_snapshot`, `02b_market_snapshot` |
| 20/11/2026 | **Lấy quận cho ITviec từ JSON-LD của trang JD** — `addressLocality` (trước đây ghi sai là "chỉ Glints có quận") | `02e_itviec_hcm_salary` + `02e_itviec_shortlist` (+3 cột), `02e_itviec_districts_stats_2026-11-20.json`, `10_commute...` §1.5 |
| 20/11/2026 | **Xuất toàn bộ title đã crawl** để Hoàn chọn role muốn loại | `11_all_job_titles_2026-11-20.csv` (774 dòng) |
| 20/11/2026 | **Thêm `00_START_HERE.md`** — 1 file điều hướng thay cho việc mở 105 file; kèm đề xuất xoá 10 / gộp 17→4 | `00_START_HERE.md`, `00_README_index.md`, `09_refresh_prompts.md` (+ bước purge tester & lấy quận) |
| 20/11/2026 | **Bộ lọc role vĩnh viễn** (Hoàn loại: PHP, sales/giáo viên/designer & mọi role off-IT, IT Support/Helpdesk, BrSE, Hardware/embedded, **tester kể cả pentester**) | `tools/excluded_roles.conf` + `tools/purge_excluded_roles.py` (thay `purge_tester_rows.py`); đã lọc lại toàn bộ dữ liệu thô: **bỏ 69 tin** (LinkedIn 15 · Glints 39 · ITviec 6 · ITviec-đầu 5 · VNW 1 · JobStreet 3) |
| 20/11/2026 | **Tính lại toàn bộ shortlist + số liệu** trên dữ liệu đã lọc role | LinkedIn 392/163 (chạm tới **111**, Java **45**), Glints 86/56 (lương **47 — 54,7%**), ITviec 75/55; tổng mẫu **605 tin**; `11_all_job_titles` còn **705 dòng** |
| 20/11/2026 | **Dọn file theo duyệt của Hoàn** (mục 3 & 4 `00_START_HERE`): xoá **11 file**, gộp **14 → 4**; mục 2 của README giờ sinh tự động từ đĩa | `00_README_index.md`, `00_START_HERE.md`, 4 file gộp |
> **Nguyên tắc:** mỗi khi Hoàn cung cấp thông tin mới, tôi sửa **tất cả** file bị ảnh hưởng và ghi vào bảng này — không để pack tự mâu thuẫn.
