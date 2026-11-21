# 01.3 — KIỂM TOÁN CV & LINKEDIN HIỆN TẠI

**Ngày:** 20/11/2026 · **Cập nhật lần cuối:** 21/11/2026 · Nguồn: `HoPhuocHoan_Resume_SoftwareEngineer.pdf`, `Profile.pdf`, `github_repos.txt`, GitHub API (20/11/2026), và tự khai của Hoàn (B4).
**Quy ước:** **Giữ** / **Viết lại** / **Xoá** · Rủi ro phỏng vấn: 🔴 Cao · 🟡 TB · 🟢 Thấp.

> Tiêu chí duy nhất tôi dùng: *dòng này có bảo vệ được sau 2 phút bị hỏi xoáy không?* Không phải "nghe có mạnh không".

---

## 1. CV — từng dòng

### 1.1 Header & Education

| Dòng hiện tại | Quyết định | Lý do | Rủi ro |
|---|---|---|---|
| `Software Engineer` (dưới tên) | **Viết lại** → `Backend Developer (Java) — Fresher` | "Software Engineer" ở người chưa có việc là tự nâng chức danh; "Fresher" định vị đúng và lọc được tin phù hợp | 🟡 |
| `B.Sc. Software Engineering (Graduated with Very Good Degree)` | **Giữ** — đã xác nhận 20/11/2026 | Đã tốt nghiệp, xếp loại **Giỏi**; cổng trường chỉ là độ trễ. M1/M7 đã đóng → `01_graduation_checklist.md` | 🟢 |
| `GPA: 8.74/10.0 • Excellence Scholarship • IELTS 6.5 (B2)` | **Giữ** | Có thật, kiểm chứng được, và GPA 8.74 là điểm mạnh thật | 🟢 |
| `Relevant Coursework: DSA, Database Systems, OOA&D, Advanced Web Programming` | **Viết lại** — thêm mã/điểm hoặc bỏ | Coursework chung chung không tạo khác biệt; nếu giữ thì ghi kèm điểm cao (CSDL 9.0, Java 9.7) | 🟢 |

### 1.2 Work Experience

| Dòng | Quyết định | Lý do | Rủi ro |
|---|---|---|---|
| `Software Engineering Collaborator — Tech Startup, 04/2025 (1 month)` | **Giữ** (đúng) nhưng **Viết lại tiêu đề** → `Collaborator (part-time, 1 month)` | "Software Engineering Collaborator" nghe như chức danh chính thức | 🟡 |
| "Built React video-streaming UI components **for a production frontend**" | **Viết lại** → bỏ chữ "production" | 1 tháng cộng tác, không rõ sản phẩm có live không. Câu hỏi xoáy: "production là gì? bao nhiêu user? em deploy hay ai deploy?" | 🔴 |
| "developed a Go microservice to scrape, process, and persist real-time gold price data **for a production MiniApp pipeline**" | **Viết lại** → `wrote a Go service that collected and stored gold-price data for a MiniApp` | Cùng lý do. Nếu đúng là production thì phải nói được: chạy ở đâu, tần suất, lỗi gì đã gặp | 🔴 |

### 1.3 Technical Competencies — phần nguy hiểm nhất

| Nhóm | Quyết định | Lý do | Rủi ro |
|---|---|---|---|
| `Languages: Go, Java, C# (.NET), Python, TypeScript, JavaScript, SQL` | **Viết lại, đổi thứ tự** → `Java, SQL, C# (.NET), TypeScript/JavaScript, Go (basic), Python (basic)` | **Go đang đứng đầu** trong khi Hoàn tự nhận 30–50% và hướng đi là Java. Đây là lỗi định vị, không chỉ là lỗi kỹ thuật | 🟡 |
| `Frontend: React, Next.js, Vite, TailwindCSS, Backstage` | **Giữ** nhưng hạ xuống cuối, bỏ `Backstage` | Backstage chỉ dùng trong Helios do AI viết | 🟡 |
| `Backend: ASP.NET Core, NestJS, EF Core, TypeORM, RESTful API` | **Giữ** `ASP.NET Core, EF Core, REST API`; **bỏ** `NestJS, TypeORM` | .NET có repo thật (IT-Tools); NestJS chỉ có Learnix (AI) | 🟡 |
| `Database: PostgreSQL, Redis, SQL Server` | **Giữ** `PostgreSQL, SQL Server`; **bỏ Redis** | Không có bằng chứng nào về Redis trong repo | 🔴 (nếu bị hỏi "em dùng Redis cho case nào?") |
| `Infrastructure: **Kubernetes, Tekton CI, Argo CD, CUE, Kubebuilder**, GitHub Actions, Git, Linux` | **XOÁ 4 mục đầu**; giữ `Git, Linux, Docker, GitHub Actions (basic)` | Đây là toàn bộ stack của Helios do AI viết, Hoàn nhớ 5–10%. Đây là **dòng dễ bị đánh sập nhất** trong cả CV | 🔴🔴 |
| `AI-Assisted Dev: Gemini API integration, prompt engineering, AI-driven code generation & debugging workflows` | **Viết lại** thành: *"Từ 11/2026 tập viết tay phần lõi và review từng diff trước khi commit; lịch sử commit TaskFlow là bằng chứng"* | "AI-driven code generation" đọc như quảng cáo; và **không được viết ở thì hiện tại** khi chưa có chuỗi commit tay để chứng minh | 🟡 |
| `Core Engineering: OOP, SOLID, Design Patterns, N-Tier Architecture, Microservices, JWT, RBAC` | **Viết lại** → `OOP, layered architecture, JWT auth, role-based access control`; **bỏ** `SOLID, Design Patterns, Microservices` | SOLID/Design Patterns/microservices là thứ interviewer sẽ hỏi sâu; Hoàn tự đánh giá L2 | 🔴 |

### 1.4 Academic Projects — quyết định lớn nhất

| Dự án | Quyết định | Lý do | Rủi ro |
|---|---|---|---|
| **Helios Platform** (4 bullet, "Lead Operator Developer") | **XOÁ khỏi CV** (hoặc giữ **1 dòng** ở mục "Other" không có bullet) | Toàn bộ 4 bullet mô tả công việc mà Hoàn không làm được khi bị hỏi ("reconciling CRDs", "CUE rendering engine", "scaffolder actions", "Ginkgo E2E against ephemeral K3d"). Với fresher Java, nó **không liên quan** và chỉ tạo bẫy | 🔴🔴 |
| **Learnix – LMS** (3 bullet) | **Viết lại mạnh** hoặc **tạm ẩn** | NestJS/React, không phải Java. Giữ được **1 bullet** nếu Hoàn giải thích được luồng auth + RBAC | 🟡 |
| **IT-Tools** (3 bullet, solo, ASP.NET Core) | **Giữ nhưng Viết lại** thành 2 bullet, hạ từ ngữ | Đây là dự án **có thật, solo, có test, có Docker** → tốt nhất trong 3 dự án. Nhưng "N-Tier architecture, DTO separation, LINQ projections" là ngôn ngữ AI; nói lại bằng việc cụ thể | 🟡 |
| *(thiếu)* **Chat-System** (Java, 11–12/2024) | **THÊM vào** — 2 bullet, sau khi làm bài T6 | Nghịch lý lớn nhất của CV hiện tại: **ứng tuyển Java mà CV không có dòng nào về Java**. Chat-System là dự án Java **duy nhất** thuộc giai đoạn AI 20–40% → khả năng bảo vệ cao nhất | 🟡 (phải bảo vệ được) |
| **`nexus`** (Java, 11/2026, 11 module) | **Thêm sau G6** (Hoàn đổi quyết định 20/11) | Dự án mạnh nhất trong hồ sơ nếu học được: 137 test/7 suite, Redis fan-out, WS xác thực, Flyway, OpenAPI 55 KB, coverage gate theo class. Điều kiện: qua **G6a+G6b** (`05_how_to_learn.md`) | 🟡 → 🟢 |

### 1.5 Professional Attributes (3 bullet cuối)

| Dòng | Quyết định | Lý do |
|---|---|---|
| `AI-First Mindset: ... shipped AI-powered features (quiz gen) using Gemini API in production` | **XOÁ** | "in production" lần thứ ba trong 1 trang CV. Đây là dòng khiến interviewer nghi ngờ toàn bộ phần còn lại |
| `End-to-End Ownership: ... in both solo and multi-person team contexts` | **XOÁ** | Sáo rỗng, ai cũng viết |
| `Continuous Learning: Follow cloud-native, Kubernetes, and AI-assisted development trends` | **XOÁ** | Không phải kỹ năng; và nhắc Kubernetes lần nữa |

---

## 2. LinkedIn — từng phần

| Phần | Hiện tại | Quyết định | Ghi chú |
|---|---|---|---|
| **Headline** | `Junior Backend Developer \| Java & Spring Boot \| Software Engineering Graduate` | **Viết lại** (3 phương án ở `07_linkedin_copy_paste.md` — Phase 7) | "Graduate" có vấn đề M1. "Junior" + chưa có việc là ổn, nhưng "Java & Spring Boot" khi chưa có dự án Spring là **khai không có bằng chứng** (M4) |
| **Summary** | "specializing in robust Backend Development using Java and the Spring Boot ecosystem... building scalable microservices, optimizing database performance" | **Viết lại toàn bộ** | 3 cụm không có bằng chứng: "specializing", "scalable microservices", "optimizing database performance". Một câu hỏi duy nhất — *"em optimize DB performance ở dự án nào, bằng cách nào?"* — là đủ sập |
| **Experience** | 1 tháng collaborator, có "production" 2 lần | **Viết lại** như CV | |
| **Top skills** | Software Development · Back-End Web Development · Web Development | **Đổi** → `Java`, `SQL`, `Spring Boot` (chỉ sau khi có dự án), `REST APIs`, `Git` | Top skills là thứ recruiter search |
| **Certifications** | AI Fundamentals, Foundations of PM, Intro to Front-End, IELTS 6.5, Programming with JavaScript | **Giữ IELTS, giữ 1–2 cái còn lại, bỏ bớt** | 5 cert, trong đó 3 cái là khoá Coursera nhập môn → loãng. IELTS là cái duy nhất có giá trị thị trường |
| **Honors** | Academic Merit Scholarship | **Giữ** | Thật |
| **Featured / Projects** | **Trống** | **Thêm 1–2** (Chat-System, IT-Tools) — **không** `nexus` | Đây là chỗ trống lớn nhất — LinkedIn không có bằng chứng code nào |
| **Open to Work** | Đang bật | **Giữ**, nhưng đọc mục 4 bên dưới | |

---

## 3. Bản vá sự thật — làm ngay hôm nay (30–45 phút)

Thứ tự ưu tiên, mỗi việc ≤ 10 phút:

1. **Sửa dòng Education** (M1/M7) — quan trọng nhất.
2. **Xoá Kubernetes/Tekton/Argo CD/CUE/Kubebuilder** khỏi Technical Competencies.
3. **Xoá cả 3 dòng Professional Attributes** (đặc biệt "shipped ... in production").
4. **Xoá Helios** khỏi Academic Projects (hoặc rút còn 1 dòng, không bullet).
5. **Đổi thứ tự Languages**: Java lên đầu, Go xuống.
6. **Bỏ "production"** ở cả 2 bullet Experience.
7. **LinkedIn Summary**: thay bằng bản ở `01_honest_cv_v1.md` mục 4.

8. **`nexus`: chỉ thêm sau khi qua cổng G6** (tự thêm 1 endpoint + tự sửa 1 bug). Trước đó giữ **Chat-System** — nhưng chỉ sau khi trả lời được 8/10 câu T6. Không thêm disclaimer "built with AI" vào README; **không phủ nhận** nếu bị hỏi (xem `05_how_to_learn.md` mục 0 và 5).

> Sau 8 việc này, CV sẽ **ngắn hơn và yếu hơn về từ khoá** — và đó chính là mục tiêu. Một CV 1 trang chỉ toàn thứ bảo vệ được sẽ tạo ra phỏng vấn tốt hơn một CV 1 trang mà 60% là bẫy.

---

## 4. Ba điều tôi khuyên **không** làm

1. **Đừng tắt "Open to Work"** chỉ vì sợ nhà tuyển dụng hiện tại thấy — Hoàn chưa có việc, không có gì để mất ở đây.
2. **Đừng thêm chứng chỉ mới** để lấp chỗ trống. Khoá Coursera 4 giờ không thay được một dự án Java.
3. **Đừng dùng AI viết lại CV lần nữa.** Chính vòng lặp đó đã tạo ra CV hiện tại. Nếu dùng AI, chỉ dùng để **hỏi ngược** ("câu này tôi sẽ bị hỏi gì?") như mô tả ở `03_strategy.md` (Phase 3).

---

## 5. Chẩn đoán tổng quát (một đoạn)

`[Suy luận — Tin cậy: Cao]` CV hiện tại không phải "hơi phóng đại" — nó **được tối ưu cho một người khác**: một platform engineer có 2–3 năm kinh nghiệm Kubernetes. Với vị trí fresher Java, nó gây ba tác hại cùng lúc: (a) mời những câu hỏi Hoàn không trả lời được, (b) **không có một dòng nào về Java/Spring** — đúng thứ nhà tuyển dụng cần thấy, (c) làm loãng hai tài sản thật: GPA 8.74 và IT-Tools. Sửa không cần viết thêm gì mới; chỉ cần **bỏ**.
