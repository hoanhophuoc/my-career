# 07.5 — Đánh giá hai công cụ tìm việc bằng AI

**Ngày đánh giá:** 21/11/2026 · **Người đánh giá:** agent · **Cập nhật lần cuối:** 21/11/2026
**Câu hỏi của Hoàn:** hai repo này có dùng được không, với ngân sách **0 đồng** và hồ sơ phải trung thực?
**Cách đánh giá:** đọc README + file cấu hình + `SETUP.md` trên GitHub (link và ngày truy cập ghi ở từng mục), không cài đặt.

---

## 0. Kết luận trước, giải thích sau

| Công cụ | Kết luận | Dùng phần nào |
|---|---|---|
| **`career-ops-hq/career-ops`** | **Dùng một phần** | Chỉ dùng chế độ **đánh giá 1 tin** (`oferta`/`triage`) trên model miễn phí, để trả lời "tin này có đáng nộp không". **Không** dùng phần sinh CV/cover letter mà không qua `07_cv_truth_checklist.md`. |
| **`ai-job-search-dev/ai-job-search`** | **Không dùng** | Bắt buộc **Claude Code + API key/Claude Pro** (tốn tiền), portal mặc định là **thị trường Đan Mạch**, không có sàn Việt Nam. Không thoả ràng buộc 0 đồng. |

Nguyên tắc chung: **mọi đầu ra của công cụ phải đi qua `07_cv_truth_checklist.md` trước khi gửi đi.** Công cụ không biết bạn đã làm gì; nó chỉ biết bạn *viết* gì.

---

## 1. `career-ops-hq/career-ops`

- **Nguồn:** https://github.com/career-ops-hq/career-ops — truy cập 21/11/2026. Giấy phép **MIT**; dữ liệu trong `employers/` là CC BY 4.0. Tạo 04/2026, ~4.568 commit.
- **Nó làm gì:** dán URL/tin tuyển vào AI CLI → chấm điểm phù hợp với CV (khối A–H), kiểm tra tin còn mở hay là tin đăng lại (Block G), sinh CV PDF theo ATS, viết cover letter, chuẩn bị phỏng vấn, ghi vào tracker.

### Chín điểm cần kiểm chứng

| # | Điểm | Kết quả | Bằng chứng / ghi chú |
|---|---|---|---|
| 1 | **Cần AI coding CLI nào, có gói miễn phí?** | Cần **một** AI coding CLI bất kỳ: Claude Code, Codex, OpenCode, Qwen, Grok, Antigravity (`agy`), Cursor. **Có đường 0 đồng** | README FAQ: *"CLI-agnostic and runs on free and local models (OpenRouter free models, Ollama or any OpenAI-compatible endpoint)"* → `docs/RUNNING_ON_A_BUDGET.md` |
| 2 | **Chạy được với model miễn phí/local?** | **Có** — OpenRouter free tier hoặc Ollama local | như trên. Chất lượng chấm điểm sẽ thấp hơn model trả tiền; đây là đánh đổi phải chấp nhận |
| 3 | **Nguồn việc làm có ITviec/TopDev/TopCV/VietnamWorks?** | **Không.** 55+ module nhưng là ATS (Greenhouse/Ashby/Lever/Workable), Wellfound, RSS; portal cấu hình sẵn là công ty **US/EU** (Anthropic, Vercel, n8n…) | `docs/SUPPORTED_JOB_BOARDS.md`; danh sách portal trong README |
| 4 | **Liên quan LinkedIn và điều khoản?** | Chỉ **nhập email job alert LinkedIn** (`node linkedin-import.mjs`), không crawl tài khoản. Đây là đường an toàn nhất về điều khoản | `docs/LINKEDIN_JOBS.md`; README mục "LinkedIn job alerts" |
| 5 | **Rủi ro fork công khai làm lộ hồ sơ?** | **Có, rất thật.** Hồ sơ/CV nằm trong thư mục làm việc; nếu bạn fork repo **public** rồi commit dữ liệu cá nhân → lộ toàn bộ CV, email, lịch sử nộp | Phải để repo **private** (đúng quyết định của Hoàn) và không commit `data/`, `cv/`, `profile` |
| 6 | **Có cổng kiểm số liệu CV không?** | **Không có cổng sự thật.** Nó "tailor CV from *your own experience*" nhưng không kiểm chứng bạn có làm việc đó hay không → **có thể thổi phồng** nếu đầu vào đã phồng | Đây là lý do bắt buộc dùng `07_cv_truth_checklist.md` |
| 7 | **Có tự nộp đơn không?** | **Không.** *"It drafts and fills; it never submits. You press Submit."* | README FAQ, mục Human-in-the-Loop |
| 8 | **Chi phí thực tế** | 0 đồng nếu dùng model free/local + Node có sẵn. Playwright Chromium chỉ cần cho PDF | README Quick Start |
| 9 | **Độ phù hợp với thị trường VN** | **Thấp cho phần tìm tin**, **cao cho phần đánh giá một tin bạn tự chọn** | Portal không có sàn VN; nhưng chế độ dán JD thì độc lập thị trường |

### Cài tối thiểu an toàn (nếu muốn thử)

```bash
# 1. Chỉ trong thư mục riêng, KHÔNG trong repo career pack
mkdir -p ~/career-ops-local && cd ~/career-ops-local
npx @santifer/career-ops init

# 2. Mở bằng CLI + model miễn phí (ví dụ OpenCode + OpenRouter free / Ollama)
#    Không đăng nhập tài khoản trả tiền, không nhập CV thật ở bước setup đầu.
# 3. Chỉ dùng chế độ đánh giá: dán 1 JD → "run triage" hoặc "run oferta"
# 4. KHÔNG dùng "tailor CV" trước khi đọc 07_cv_truth_checklist.md
```

**Ba điều cấm:** (a) không `git init` + push thư mục này lên repo công khai; (b) không dán CV có email/SĐT vào prompt của model free (nhà cung cấp có thể dùng dữ liệu để huấn luyện); (c) không dùng output CV của nó mà chưa đối chiếu từng dòng với checklist.

---

## 2. `ai-job-search-dev/ai-job-search`

- **Nguồn:** https://github.com/ai-job-search-dev/ai-job-search — truy cập 21/11/2026. Giấy phép **MIT**, tạo 03/2026, ~471 commit, branch `master`.
- **Nó làm gì:** framework 6 lệnh trên Claude Code: `/setup`, `/scrape`, `/rank`, `/apply`, `/interview`, `/outcome`; sinh CV + cover letter có vòng "drafter–reviewer".

### Chín điểm cần kiểm chứng

| # | Điểm | Kết quả | Bằng chứng / ghi chú |
|---|---|---|---|
| 1 | **Cần AI CLI nào, có gói miễn phí?** | **Bắt buộc Claude Code**; cần **Anthropic API key hoặc Claude Pro/Team**. Không có đường 0 đồng | `SETUP.md` mục 1: *"Install Claude Code… You'll need an Anthropic API key or a Claude Pro/Team subscription"* |
| 2 | **Model miễn phí/local?** | **Không** — thiết kế gắn với Claude Code | `SETUP.md`, `CLAUDE.md`, `.claude/` |
| 3 | **Sàn VN (ITviec/TopDev/TopCV/VietnamWorks)?** | **Không.** Portal mặc định là **Đan Mạch** (Jobindex, Jobnet, Akademikernes Jobbank); có `linkedin-search` và `freehire-search` không gắn quốc gia. Muốn có sàn VN phải tự viết skill (repo `community-portals`) | README: *"The job portal search skills are built for the Danish market… designed to be swapped for your local job boards"* |
| 4 | **LinkedIn & điều khoản** | Có module `linkedin-search` chạy bằng Bun; cách lấy dữ liệu cần kiểm tra trước khi dùng, vì scrape LinkedIn có thể vi phạm điều khoản | `SETUP.md` mục 1 (Bun), `job_scraper/` |
| 5 | **Rủi ro fork công khai** | **Cao hơn career-ops**: README hướng dẫn **fork** và hồ sơ nằm ngay trong `CLAUDE.md` (tên, học vấn, kinh nghiệm). Fork public = lộ hồ sơ | `SETUP.md` mục 2; cảnh báo `gh repo set-default` về việc vô tình đăng issue lên repo upstream |
| 6 | **Cổng kiểm số liệu CV** | Có **reviewer pass** (kiểm tra nhất quán, không bịa số liệu), nhưng vẫn là **LLM tự chấm LLM** — không phải bằng chứng | `.claude/skills/`, README mục drafter–reviewer |
| 7 | **Tự nộp đơn?** | Không thấy cơ chế nộp tự động; `/apply` tạo hồ sơ | README workflow |
| 8 | **Chi phí thực tế** | **> 0 đồng**: Claude Pro (~20 USD/tháng) hoặc trả theo token API | `SETUP.md` |
| 9 | **Độ phù hợp** | **Thấp**: sai thị trường, sai ngân sách | — |

**Kết luận: không dùng.** Không phải vì công cụ kém, mà vì nó vi phạm hai ràng buộc cứng của pack: **0 đồng** và **thị trường TP.HCM**.

---

## 3. Nếu chỉ chọn một việc để làm với công cụ

**Đừng cài gì cả trong 4 tuần đầu.** Việc đáng làm nhất mà công cụ chỉ *có thể* giúp là **lọc tin trước khi nộp**, và việc đó pack đã làm sẵn bằng `02_postings_master.csv` + shortlist, không tốn token.

Khi nào nên thử: **sau W8**, khi đã có CV gửi đi và bắt đầu nộp 5 đơn/tuần. Lúc đó dùng `career-ops` chế độ `triage` cho 5 tin/tuần là đủ, và **luôn** đối chiếu với `07_cv_truth_checklist.md`.

**Điều gì khiến agent đổi kết luận:** nếu `career-ops` bổ sung module cho ITviec/TopCV/VietnamWorks **và** vẫn chạy được với model local miễn phí → nâng lên "dùng toàn phần, trừ phần sinh CV".

---

## 4. Nguồn

| Mã | Nội dung | URL | Truy cập |
|---|---|---|---|
| T1 | career-ops README (MIT, CLI-agnostic, model free/local, không tự nộp, LinkedIn alert import) | https://github.com/career-ops-hq/career-ops | 21/11/2026 |
| T2 | career-ops — chạy trên ngân sách 0 đồng | https://github.com/career-ops-hq/career-ops/blob/main/docs/RUNNING_ON_A_BUDGET.md | 21/11/2026 |
| T3 | career-ops — sàn hỗ trợ | https://github.com/career-ops-hq/career-ops/blob/main/docs/SUPPORTED_JOB_BOARDS.md | 21/11/2026 |
| T4 | ai-job-search SETUP (Claude Code + API key/Pro, Python, Bun) | https://github.com/ai-job-search-dev/ai-job-search/blob/master/SETUP.md | 21/11/2026 |
| T5 | ai-job-search README (portal Đan Mạch, workflow 6 lệnh) | https://github.com/ai-job-search-dev/ai-job-search | 21/11/2026 |
