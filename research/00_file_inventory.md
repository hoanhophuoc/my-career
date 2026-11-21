# 00 — KIỂM KÊ FILE ĐÍNH KÈM

Ngày kiểm kê: 20/11/2026 · Thư mục làm việc cục bộ (không ghi đường dẫn tuyệt đối vào pack)
Phương pháp: `pdftotext -layout` cho PDF, đọc trực tiếp cho TXT/MD/HTML, GitHub REST API cho repo.

## 1. Bảng kiểm kê

| # | File | Loại | Đọc được? | Nội dung lấy được | Vấn đề |
|---|---|---|---|---|---|
| 1 | `HoPhuocHoan_Resume_SoftwareEngineer.pdf` | CV 1 trang | ✅ | Toàn văn (4.3 KB text) | Xem mâu thuẫn M2–M7 |
| 2 | `Profile.pdf` | LinkedIn export | ✅ | Toàn văn (2.6 KB) | Thiếu phần Projects/Skills chi tiết; có **địa chỉ nhà + SĐT + email** → đã loại khỏi mọi file đầu ra (R10) |
| 3 | `screencapture-www-linkedin-com-jobs-...png` | Ảnh job alerts | ✅ (ảnh) | 4 alert (đã có trong Phụ lục B) | Chỉ là ảnh, không đọc được nội dung job bên trong |
| 4 | `IELTS-TRF.pdf` | IELTS TRF | ✅ | Scores: L7.0 R6.0 W6.5 S6.0, Overall 6.5 | **Có Candidate ID/CCCD → không trích vào pack** |
| 5 | `Gmail - Scores Breakdown Outcome.pdf` | IELTS breakdown | ✅ | 30/24; T1 6-7-6-6; T2 7-6-7-6; FC6 LR6 GRA6 P7 | Không có vấn đề |
| 6 | `screencapture-portal-ctdb-hcmus-...pdf` | Ảnh chụp cổng SV | ❌ | **0 byte text** — là ảnh nhúng trong PDF | Không OCR được bằng `pdftotext`. Nội dung đã được mô tả ở B1 nên vẫn dùng được, nhưng **tôi không tự kiểm chứng được ảnh này**. Nếu cần, Hoàn chụp lại dạng PNG. |
| 7 | `DeCuongTomTat_CNTT_CLC.pdf` | 306 trang đề cương | ✅ | 620 KB text; tra được theo mã môn | Bản 2022–2023, có thể khác bản đang áp dụng |
| 8 | `FIT-Course-Information-Handbook-Short-form-2023.pdf` | 202 trang | ✅ | 402 KB text | Bản 2023 |
| 9 | `books.txt` | Danh sách 681 dòng | ✅ | Cây thư mục ~180–200 tài liệu | Tên file có năm **có thể là năm dự kiến** (nhiều sách ghi 2026) → phải xác minh edition ở Phase 5 |
| 10 | `bookmarks_11_19_26.html` | Chrome bookmarks | ✅ | 3.415 dòng, 1.861 link | Chưa phân tích (Phase 5.4). Không đọc mục giải trí/cá nhân |
| 11 | `github_repos.txt` | 59 repo | ✅ | Danh sách repo + mô tả | **3 repo đã 404** (xem M8) |
| 12 | `BOOKS_MASTER_AUDIT_AND_BLUEPRINT.md` | Audit cũ | ✅ | 661 dòng, 69 KB | Do AI khác viết (Antigravity), tháng 11/2026. **Không kế thừa kết luận** — chỉ đối chiếu. Có lỗi: ghi "Thiếu vắng hoàn toàn mảng Testing" nhưng Phụ lục C lại có *TDD by Example* và *Unit Testing: Principles, Practices, Patterns* |
| 13 | `Chiến Lược Nghề Nghiệp IT - ChatGPT.pdf` | Bản tư vấn cũ | ✅ | 70 KB | Đọc để tránh lặp lại; không coi là nguồn |
| 14 | `Chiến Lược Nghề Nghiệp IT - Gemini.pdf` | Bản tư vấn cũ | ✅ | 90 KB | Như trên |
| 15 | `Bộ Prompt Nghiên cứu Toàn diện...pdf` | Bản prompt | ✅ | 108 KB | Chính là prompt hiện tại |
| 16 | `MASTER_PROMPT_Career_Roadmap_Hoan.md` | Prompt gốc | ✅ | 93 KB | Trùng nội dung yêu cầu |
| 17 | `dự đoán tương lai.txt` | Yêu cầu thô | ✅ | 25 KB | Nguồn gốc của prompt; **chứa địa chỉ nhà → không trích** |

## 2. Mâu thuẫn phát hiện (theo Phase 0.3)

| Mã | Mâu thuẫn | Bằng chứng | Ảnh hưởng |
|---|---|---|---|
| **M1** | ~~Cổng trường ghi "Đủ điều kiện tốt nghiệp: ✗"~~ | Hoàn xác nhận 20/11/2026 | ✅ **ĐÓNG HOÀN TOÀN.** Đã tốt nghiệp, **bằng loại Giỏi**; portal chỉ là độ trễ. → `01_graduation_checklist.md` (bản v3) |
| **M2** | `nexus` mô tả "Private clean rewrite" nhưng repo **PUBLIC**; AI viết phần lớn | GitHub API 20/11/2026 | **Cao.** Hoàn chốt 20/11: sẽ public chính thức, dùng làm dự án chính trên CV **sau khi qua cổng G6**, **không** ghi disclaimer trong README (trailer `Generated with Codebuff` trong git log đã đủ) → xem `05_how_to_learn.md`. Trước khi public: kiểm `.agents/profile.md`, bỏ `.idea/` |
| **M3** | CV ghi "shipped AI-powered features ... in production", "for a production frontend", "production MiniApp pipeline" | CV vs B3: cộng tác **1 tháng**, không có hợp đồng lao động | **Cao** khi phỏng vấn: "production là gì, bao nhiêu user, ai vận hành, em làm phần nào?" |
| **M4** | LinkedIn khai Spring Boot/Spring MVC/Spring Security/Hibernate + "building scalable microservices, optimizing database performance", nhưng **không có dự án Spring nào** trên CV hay GitHub | CV, `github_repos.txt`, GitHub API (không repo nào là Spring) | **Rất cao** — đúng kỹ năng Hoàn muốn theo, nhưng hiện là khai không có bằng chứng |
| **M5** | CV ghi "Lead Operator Developer" cho nhóm 6 người; không có bằng chứng vai trò lead | B4 (Hoàn tự nói AI viết CV) | **TB–Cao**: chức danh tự phong dễ bị hỏi xoáy |
| **M6** | CV liệt kê Kubernetes/Tekton/Argo CD/CUE/Kubebuilder như "competencies", thực tế từ đồ án do AI viết, Hoàn nhớ 5–10% | B4 | **Cao**: đây là bộ kỹ năng bị hỏi sâu nhất nếu ứng tuyển DevOps/platform |
| **M7** | CV ghi "Graduated with Very Good Degree" | CV + xác nhận 20/11/2026 | ✅ **ĐÓNG.** Xếp loại **Giỏi** đã được xác nhận — dòng CV hiện tại là đúng, không phải sửa |
| **M8** | `github_repos.txt` liệt kê `DSA-Practice`, `java-multithreading-concurrency`, `hw-learn-go` nhưng cả 3 trả **404** | GitHub API | **TB**: mất bằng chứng DSA/concurrency/Go — đúng những thứ cần nhất lúc này |
| **M9** | CV ghi "IELTS 6.5 (B2)" ✅ đúng; và 20/11/2026 Hoàn xác nhận **IELTS 6.5 đã được Trường xét duyệt, công nhận** (không còn là chứng chỉ cá nhân chưa dùng được) | TRF + M1 | **TB** |
| **M10** | Prompt nói "hôm nay 19/11/2026", hệ thống 20/11/2026 | — | Không đáng kể |
| **M11** | `BOOKS_MASTER_AUDIT` nói thiếu hoàn toàn sách Testing, nhưng tủ sách có 2 cuốn testing | File audit cũ vs Phụ lục C | Thấp, nhưng cho thấy **không nên tin audit cũ** |

## 3. Điểm mạnh về dữ liệu (đáng dùng)

> **⚠️ SỬA 20/11/2026 — đoạn dưới đây là kết luận SAI, giữ lại để thấy mình đã sai ở đâu.**

- ~~**`nexus` là bằng chứng tốt nhất trong toàn bộ hồ sơ.**~~ Repo Java 1,39 MB, commit 17–18/11/2026, có test coverage floor, outbox, WebSocket, PostgreSQL.
  **Sai vì:** commit do Hoàn thực hiện nhưng **code do AI viết 100%**; Hoàn xác nhận **không hiểu code**. Commit message hay **không** chứng minh người commit hiểu code. Đây là bài học phương pháp: *bằng chứng phải là "giải thích được", không phải "có trong repo"*.

- **Bằng chứng Java thật sự còn lại:** (1) CSC13102 **9.7** + đề cương cho thấy đã học Java IO/Collections/JDBC/Multithread/JUnit; (2) **Chat-System** (11–12/2024) — thuộc giai đoạn AI 20–40%, có commit `phuochoan` ngày 19/12/2024; (3) bài test chẩn đoán T1 (chưa làm).
- Có 2 bản tư vấn cũ (ChatGPT/Gemini) → tôi sẽ **không lặp lại** và sẽ chỉ ra chỗ chúng sai/nông ở Phase 3–4.
- Có đề cương theo mã môn → chứng minh được **đã học gì**, khác với "nhớ gì".

## 4. Việc Hoàn cần làm để tôi làm chính xác hơn

1. Chụp lại màn hình cổng sinh viên thành **PNG** (file PDF hiện tại là ảnh, không đọc được).
2. ~~Trả lời Q5: `nexus` tự viết hay AI viết?~~ → **Đã trả lời: AI 100%.** Không còn gì để hỏi.
3. Quyết định `nexus` public hay private (M2) — vẫn còn, nhưng không ảnh hưởng CV.
