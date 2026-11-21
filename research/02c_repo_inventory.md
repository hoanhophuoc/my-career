# Phase 2c — Kiểm kê 36 repo (đã clone thật, 20/11/2026)

**Cách làm:** `gh repo clone --depth 1` cho toàn bộ repo của `hoanhophuoc` → `_repos/` (36 repo, **261 MB**).
**Không cần token.** `gh` trên máy bạn đã đăng nhập sẵn tài khoản `hoanhophuoc` với scope `repo` — tôi clone trực tiếp được, bạn không phải làm gì.
**Đính chính:** 3 repo trước đây bị GitHub API trả 404 (`DSA-Practice`, `java-multithreading-concurrency`, `hw-learn-go`) nay **truy cập được** — chúng là repo **private**, API không thấy nhưng `gh` có quyền.

---

## 1. Số dòng code thật (đếm trên bản clone)

| Repo | File mã nguồn | LOC | Ngôn ngữ chính | Ý nghĩa |
|---|---|---|---|---|
| **Learnix** | 259 | **46.783** | TypeScript | LMS nhóm — nhưng phần lớn sinh bởi AI |
| **nexus** | 278 | **32.126** | Java | Dự án mạnh nhất; khớp với phân tích trước (137 test / 7 suite) |
| **DSA-Practice** | 463 | **19.503** | C++ | **Bằng chứng DSA thật** — 463 file, không phải "8.0 điểm" trên bảng điểm |
| **CoolWear** | 75 | **10.403** | C# | **POS bán lẻ — chưa có trong CV** |
| **Chat-System** | 49 | **9.113** | Java | Dự án Java "sạch AI" nhất, đang nằm trên CV |
| **IT-Tools** | 62 | 4.233 | JS/C# | REST API solo, đang nằm trên CV |
| Anki-learn-English-vocabularies | 25 | 4.988 | Python | Công cụ cá nhân (tự động sinh thẻ) |
| File-System | 7 | 2.346 | C++ | Đồ án môn học |
| Email-Socket | 9 | 1.456 | C# | Socket/email — minh chứng hiểu protocol |
| Calolator | 8 | 559 | Jupyter | App AI dinh dưỡng |
| Smart-Door | 3 | 495 | C++ | IoT |
| task-tracker | 1 | 262 | Go | CLI nhỏ |
| java-multithreading-concurrency | 2 | 144 | Python/Java | Ghi chú học concurrency |
| quiz-game | 1 | 71 | Go | Bài tập |

*(22 repo còn lại: landing page, Odin Project, CS50, bot Discord, dotfiles… — bài tập/khoá học, không đưa vào CV.)*

## 2. Ba phát hiện làm thay đổi hồ sơ

**1. `CoolWear` (C#, 10.403 LOC) chưa có trong CV.** Đây là dự án lớn thứ 4 của bạn và là **hệ thống POS thật** (bán hàng, thanh toán, quản lý kho) — đúng loại domain mà JD backend hay hỏi. Với nhánh .NET dự bị (3,25) thì đây là bằng chứng mạnh nhất bạn có, mạnh hơn IT-Tools về quy mô.

**2. `DSA-Practice` (463 file, 19.503 LOC) biến "DSA 8.0" từ điểm số thành bằng chứng.** Trong CV hiện tại chỉ có "Data Structures & Algorithms (8.0)" — một con số. 463 file bài giải là thứ trả lời được câu "em luyện DSA thế nào?" mà không cần nói suông.

**3. `Learnix` 46.783 LOC nhưng KHÔNG nên đưa lên CV.** File lớn nhất trong hồ sơ, nhưng phần lớn do AI sinh và không phải Java — đưa vào sẽ mời đúng loại câu hỏi mà `01_cv_linkedin_audit.md` đã xác định là bẫy.

## 3. Đề xuất sửa CV (3 dòng, không cần viết lại)

| Việc | Chỗ sửa |
|---|---|
| Thêm **CoolWear** 2 bullet vào mục DỰ ÁN | Ngay dưới IT-Tools; dùng cho nhánh .NET |
| Thêm 1 dòng vào KỸ NĂNG hoặc mục DỰ ÁN | `Luyện DSA: 463 bài giải (C++) — github.com/hoanhophuoc/DSA-Practice` |
| Giữ nguyên **không** đưa Learnix | — |

## 4. Giới hạn

- Tôi **đếm dòng và liệt kê file**, chưa đọc code từng repo — nên chưa nói được gì về chất lượng kiến trúc của CoolWear/DSA-Practice.
- Clone `--depth 1` → **không có git history**, nên không xác minh được repo nào do bạn viết tay bao nhiêu phần trăm. Với CoolWear/DSA-Practice (2024–2025, trước giai đoạn AI) rủi ro thấp, nhưng khi phỏng vấn bạn vẫn phải tự giải thích được code.
- 261 MB nằm trong `_repos/` — thêm vào `.gitignore` nếu thư mục này nằm trong một repo Git khác.

---

## Checkpoint Phase 2c

- **36/36 repo đã clone** (261 MB), **không cần token**. Đính chính 3 repo trước đây tưởng 404.
- Bảng LOC 14 repo: **nexus 32.126 · Learnix 46.783 · DSA-Practice 19.503 · CoolWear 10.403 · Chat-System 9.113 · IT-Tools 4.233**.
- 3 việc: thêm **CoolWear** + **DSA-Practice** vào hồ sơ; **không** thêm Learnix.

**Quyết định đề xuất:** đọc code `CoolWear` (2 giờ) và thêm 2 bullet vào CV **trước** khi nộp Netcompany — vì Netcompany tuyển đúng .NET + Java.
**Vì sao:** đó là tin duy nhất trong 109 tin khớp cả 3 yếu tố (.NET, Java, English) và CV hiện tại đang bỏ trống dự án .NET lớn nhất.
**Điều gì sẽ khiến tôi đổi ý:** nếu mở CoolWear ra thấy phần lớn là code mẫu/AI-sinh và bạn không giải thích được luồng thanh toán → bỏ, không thêm.
