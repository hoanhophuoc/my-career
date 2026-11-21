# 05 — Cách học, cách nhớ, cách giữ tập trung (gộp)

**Cập nhật lần cuối:** 21/11/2026

> Gộp ngày **20/11/2026** từ: `05_how_to_learn.md`, `05_how_to_learn.md`, `05_how_to_learn.md`, `05_how_to_learn.md`. Nội dung giữ nguyên; chỉ đổi cấp tiêu đề (thêm 1 dấu #) để không phá mục lục.

---

## Phần 1 — Phương pháp học

## Phase 5.1 — Phương pháp học (chẩn đoán từ dữ liệu thật của Hoàn)

**Ngày viết:** 20/11/2026

---

### 1. Chẩn đoán: bạn không thiếu tài liệu, bạn thiếu *đầu ra*

Số liệu thật, đếm từ chính thư mục của bạn:

| Tài sản | Số lượng thật | Nguồn |
|---|---|---|
| Sách/file PDF trong thư viện | **197** (681 dòng gồm cả thư mục) | `books.txt`, đếm bằng script ngày 20/11/2026 |
| Bookmark Chrome | **1.861 link** (1.859 URL duy nhất) | `bookmarks_11_19_26.html` |
| Trong đó thuộc cây học nghề | **1.454** (Software Engineering 1.199 + Java 255) | cùng file |
| Bản chiến lược do AI viết (ChatGPT/Gemini/Bộ Prompt) | **3 tài liệu, ~250 trang** | `tools/` |
| Điểm học phần Java (CSC13102) | **9.7** | bảng điểm |
| Điểm Cơ sở dữ liệu (CSC10006) | **9.0** | bảng điểm |
| **Mức kỹ năng đo được (bài test Phase 1)** | **Java L2, SQL L2, Spring L1, testing L1–L2** | `01_skills_matrix.md` |

**Kết luận (Suy luận, độ tin cậy cao):** với **212 sách** + 1.861 link + 3 bản chiến lược mà mức kỹ năng vẫn là L1–L2, nguyên nhân **không thể** là thiếu tài liệu. Nguyên nhân là **chưa có vòng lặp biến đầu vào thành đầu ra**: đọc → hiểu → đóng lại → quên. `nexus` là bằng chứng mạnh nhất: 1,39 MB code Java nằm trong repo của bạn mà bạn không giải thích được một dòng.

**Hệ quả cho Phase 5:** nhiệm vụ **không phải** "sắp xếp lại thư viện cho gọn" mà là **cắt xuống một bộ nhỏ + gắn mỗi cuốn vào một tuần cụ thể + đổi tỉ lệ đọc/gõ**. Nếu Phase 5 chỉ tạo ra một danh sách đẹp hơn, nó đã thất bại (đúng rủi ro số 1 trong `00_START_HERE.md`).

---

### 2. Bốn luật học (thay cho mọi "phương pháp học hiệu quả" khác)

#### Luật 1 — Một nguồn chính cho mỗi tuần
Mỗi tuần chọn **1** tài nguyên chính (xem `04_master_roadmap.md`). Tài nguyên khác chỉ được mở khi **bị kẹt quá 15 phút**. Mở 4 tab cùng lúc = học 0.

#### Luật 2 — 40/60
**40% thời gian đọc, 60% gõ.** Với ngày 6h: tối đa 2h20 đọc, tối thiểu 3h30 gõ/chạy/sửa. Nếu một ngày bạn đọc 4h và gõ 1h — ngày đó **không tính là đã học**.

#### Luật 3 — Không có "viết lại từ trí nhớ" thì không có kỹ năng
Cuối mỗi ngày, 60' đóng hết tài liệu và viết lại thứ vừa học. Đây là **bước duy nhất** phân biệt "biết về" và "biết làm". Nó khó chịu — đó là dấu hiệu nó đang hoạt động.

#### Luật 4 — Test trước khi tuyên bố "hiểu"
Trước khi nói "em hiểu X": làm được **một bài nhỏ** dùng X mà không tra cứu. Không làm được → chưa hiểu, chỉ mới *nhận ra* X.

---

### 3. Cách đọc một cuốn sách kỹ thuật (3 lượt, không đọc tuyến tính)

| Lượt | Thời gian | Việc | Không làm |
|---|---|---|---|
| **1. Quét** | 10' | Đọc mục lục + tên chương + phần cuối mỗi chương. Đánh dấu **3 chương** liên quan nhất tới việc đang làm | Không đọc trang 1 |
| **2. Đục lỗ** | 60–90' | Đọc đúng 3 chương đó, **gõ lại code mẫu bằng tay** (không copy), chạy, làm vỡ, sửa | Không đọc chương 1 chỉ vì nó là chương 1 |
| **3. Đóng sách** | 30' | Viết 1 trang tóm tắt **bằng lời mình** + 1 đoạn code áp dụng vào TaskFlow/MiniWallet | Không highlight |

**Ví dụ thật với sách của bạn:**
- *Learning Spring Boot 4*: quét mục lục → tuần 3 đọc chương MVC + Data; tuần 4 đọc chương Testing + Security. Không đọc 12 chương còn lại.
- *Effective Java*: **không đọc hết 90 items**. Tuần 2 đọc items về `equals/hashCode`, immutability, exceptions; tuần 11 đọc items về concurrency. Mỗi item: đọc → viết 5 dòng thử.
- *A Philosophy of Software Design* (190 trang): đọc **cả cuốn** ở W1 — ngắn, nền tảng, và là cuốn thay hẳn *Clean Code*. *Clean Code* chỉ mở khi cần tra đúng 1 chương.

---

### 4. Cách dùng 1.861 bookmark và 212 sách (đúng cách, không tích trữ thêm)

| Đúng | Sai |
|---|---|
| Dùng làm **tra cứu**: gặp lỗi → tìm trong bookmark → đọc 1 trang → sửa → đóng | Duyệt bookmark để "tìm cảm hứng học" |
| Mỗi tuần **tối đa 1** tài nguyên mới được mở (đã ghi trong lộ trình) | Mở 10 link "hay quá, để mai đọc" |
| Bookmark chỉ để khi URL là nguồn chính thức (docs, blog kỹ thuật) | Bookmark video "roadmap 2026" rồi không xem |
| **Xuất ra file CSV** để tìm bằng từ khoá khi cần | Sống trong thư mục bookmark |

**Luật chống tích trữ (áp dụng 24 tuần):** muốn thêm 1 bookmark/tài liệu mới → phải **dùng nó trong 48 giờ** hoặc không thêm. Số lượng không phải tiến bộ.

---

### 5. Cách dùng AI để học mà không đánh mất kỹ năng

Bạn đã mất một dự án (`nexus`) vì AI viết 100%. Quy tắc để không lặp lại:

| Dùng AI để | Không dùng AI để |
|---|---|
| Hỏi khái niệm: "giải thích `Propagation.REQUIRES_NEW` như đang dạy người mới" | Nhờ viết nguyên feature rồi commit |
| Nhờ **kiểm tra mình**: "đây là lời giải thích của tôi về N+1, chỗ nào sai?" | Nhờ viết code mà mình chưa tự viết bản đầu |
| Nhờ tạo **bài tập biến thể** từ bài đã làm | Nhờ "sửa lỗi" khi chưa tự đọc stack trace |
| Nhờ review code **mình đã viết xong** | Dán code AI vào khi không hiểu dòng nào |

**Bài kiểm tra 60 giây** (từ `03_strategy.md`): nếu không giải thích được 4/6 điểm về đoạn code đó → **chưa phải code của bạn**, không được commit, không được đưa vào CV.

**Ngân sách NO-AI:** tối thiểu **8 giờ/tuần** không AI (đã thành bắt buộc sau vụ `nexus`).

---

### 6. Ghi chép: 3 thứ, không hơn

1. **`LEARNING.md`** — mỗi ngày 3 dòng: *học gì / vướng gì / mai làm gì*. Không viết essay.
2. **`MISTAKES.md`** — mỗi lỗi thật 1 dòng: *ngày / lỗi / nguyên nhân gốc / sửa bằng gì / lần sau tránh thế nào*. Đây là tài liệu giá trị nhất sau 6 tháng (và là nguyên liệu cho câu STAR).
3. **1 trang tóm tắt mỗi chủ đề** — chỉ viết **sau khi** đã làm được, không phải trước.

**Không** làm: highlight sách, ghi chép lại lời giảng, "second brain" phức tạp, Notion nhiều database. Ba thứ trên là đủ; thêm nữa là để trốn việc gõ code.

---

### 7. Nhịp tuần (20' Chủ nhật)

1. Đọc lại `LEARNING.md` + `MISTAKES.md` của tuần (10').
2. Trả lời 3 câu: tuần này **gõ** được bao nhiêu giờ? bài nào **viết lại từ trắng** được? đã mở **bao nhiêu tài nguyên mới**? (5')
3. Chọn **1** việc sửa cho tuần sau (5') — chỉ một.

---

### Checkpoint Phase 5.1

- Chẩn đoán dựa trên số thật: **212 sách, 1.861 bookmark, 3 bản chiến lược → kỹ năng L1–L2**. Vấn đề là đầu ra, không phải đầu vào.
- 4 luật: một nguồn/tuần · 40/60 · viết lại từ trí nhớ · test trước khi nói "hiểu".
- Cách đọc sách 3 lượt (quét → đục lỗ 3 chương → đóng sách), áp dụng ngay cho 3 cuốn cụ thể của bạn.
- Luật chống tích trữ: tài nguyên mới phải được dùng trong 48 giờ.

**Quyết định đề xuất:** giữ nguyên 212 sách trên ổ nhưng **chỉ 12 cuốn được mở** trong 24 tuần (`05_shelf_and_books.md`); phần còn lại chuyển vào một thư mục `_archive_books`.
**Vì sao:** 197 lựa chọn tạo ra "chi phí quyết định" mỗi ngày; 12 lựa chọn đã đủ cho mọi tuần của lộ trình.
**Điều gì sẽ khiến tôi đổi ý:** nếu W4 kiểm tra cho thấy lỗ hổng cụ thể mà không cuốn nào trong 12 cuốn phủ (ví dụ: bạn không hiểu GC) → lấy đúng 1 cuốn từ `_archive_books` vào, đổi 1 cuốn ra, giữ nguyên số 12.

---

## Phần 2 — Hệ thống tập trung 14 ngày

## Phase 5.5 — Thí nghiệm tập trung 14 ngày (20/11 → 03/12/2026)

**Vì sao thí nghiệm, không phải "kế hoạch tập trung":** kế hoạch dựa trên niềm tin ("tôi sẽ tập trung hơn"); thí nghiệm dựa trên **số đo 14 ngày**. Bạn đã có 1.861 bookmark và 197 sách — thứ thiếu không phải ý chí, mà là **phản hồi chính xác về thời gian đang đi đâu**.

---

### 1. Giả thuyết (phải bị chứng minh sai được)

> "Nếu mỗi block học chỉ cho phép **1 tab + 1 cuốn + 1 project**, thì số giờ gõ code thật mỗi ngày sẽ ≥ 2,5 giờ và số lần mở tài nguyên mới sẽ ≤ 2/ngày — trong 14 ngày."

Nếu sau 14 ngày số liệu nói khác → giả thuyết sai, và ta biết **cần sửa cái gì** (không phải "cố gắng hơn").

### 2. Sáu luật trong 14 ngày

| # | Luật | Cách thực hiện cụ thể |
|---|---|---|
| 1 | **1 tab tài liệu** | Trình duyệt: đóng hết, chỉ mở 1 tab docs. Không dùng bookmark bar |
| 2 | **1 cuốn** | Chỉ cuốn MVS của tuần (xem `05_shelf_and_books.md`) |
| 3 | **1 project** | Chỉ `java-backend-lab` / `java-backend-lab`. Không tạo repo mới |
| 4 | **Điện thoại ra khỏi phòng** | Không "để trên bàn úp mặt" — úp mặt vẫn tốn 20% trí nhớ |
| 5 | **Block 45/15** | 45' làm → 15' đứng dậy (không mở mạng xã hội trong 15') |
| 6 | **Ghi log ngay** | Cuối mỗi block, ghi 1 dòng. Không ghi cuối ngày (sẽ quên/sai) |

**Được phép:** nghe nhạc không lời, dùng AI để hỏi khái niệm (không sinh code), nghỉ 1 ngày/tuần.

### 3. Bảng log 14 ngày (in ra, điền tay)

| Ngày | Block (số) | Giờ gõ thật | Giờ đọc | Commit | Số lần mở tài nguyên mới | Số lần bị ngắt | Việc khó nhất hôm nay |
|---|---|---|---|---|---|---|---|
| 1 (20/11) | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |
| 6 | | | | | | | |
| 7 (nghỉ) | — | — | — | — | — | — | — |
| 8 | | | | | | | |
| 9 | | | | | | | |
| 10 | | | | | | | |
| 11 | | | | | | | |
| 12 | | | | | | | |
| 13 | | | | | | | |
| 14 (03/12) | | | | | | | |

### 4. Bốn chỉ số quyết định (không đo gì thêm)

| Chỉ số | Cách tính | Ngưỡng "đạt" |
|---|---|---|
| **A. Tỉ lệ gõ** | giờ gõ / tổng giờ học | **≥ 60%** |
| **B. Commit/ngày** | số commit có nghĩa (không phải "update") | **≥ 1** |
| **C. Tài nguyên mới/ngày** | số link/sách mới mở lần đầu | **≤ 2** |
| **D. Ngắt/ngày** | số lần tự rời ghế vì lý do không phải nghỉ 15' | **≤ 3** |

### 5. Cổng quyết định ngày 14

| Kết quả | Nghĩa | Hành động |
|---|---|---|
| **Cả 4 chỉ số đạt** | Hệ thống chạy | Giữ nguyên cho 24 tuần; không thêm luật mới |
| **A đạt, C/D không đạt** | Vấn đề là **môi trường** (thông báo, tab) | Cài chặn site trong giờ học; để điện thoại ở phòng khác cả ngày |
| **A không đạt (< 50%)** | Vấn đề là **nội dung quá khó hoặc quá mơ hồ** | Chia bài nhỏ hơn (mỗi block 1 việc ≤ 45'), hạ xuống bản 3h/ngày |
| **B không đạt** | Đang học mà không tạo ra gì | Bắt buộc commit trước khi kết thúc block thứ 2, kể cả commit nhỏ |
| **Không ghi log được 5 ngày** | Hệ thống không phù hợp với bạn (không phải bạn yếu) | Bỏ bảng log, chỉ giữ 2 luật: 1 tab + commit/ngày |

### 6. Điều **không** làm trong 14 ngày

- Không đổi lộ trình, không thêm sách, không cài app quản lý thời gian mới (mỗi app mới là một lần trốn việc).
- Không đánh giá bản thân ("mình lười") — chỉ đọc số.
- Không thí nghiệm 2 thứ cùng lúc (nếu đổi cả lịch ngủ và lịch học, sẽ không biết cái nào có tác dụng).
- Không khoe tiến độ lên mạng (phần thưởng xã hội làm giảm động lực làm thật — hiệu ứng đã được ghi nhận trong tâm lý học, nhưng tôi không có nguồn trong pack này nên chỉ nêu như **giả thuyết cần tự kiểm**).

---

### Checkpoint Phase 5.5

- Thí nghiệm 14 ngày với **giả thuyết có thể sai**, 6 luật cụ thể, bảng log 14 dòng, 4 chỉ số và **cổng quyết định** ngày 14.
- Khác biệt so với "kế hoạch tập trung": nếu thất bại, ta biết **sửa gì** (môi trường / độ khó / cách chia việc), không quy về ý chí.
- Chỉ 4 chỉ số — đo nhiều hơn sẽ không ghi nổi.

**Quyết định đề xuất:** chạy thí nghiệm **song song** với 14 ngày đầu của lộ trình (20/11–03/12), không chờ "chuẩn bị xong".
**Vì sao:** 14 ngày này chính là tuần 1–2 của Stage 1 (Java core + SQL) — vừa học vừa đo, không tốn thêm thời gian.
**Điều gì sẽ khiến tôi đổi ý:** nếu trong 14 ngày bạn có việc phải đi phỏng vấn/phỏng vấn thử → tạm dừng thí nghiệm, vì dữ liệu sẽ nhiễu và kết luận sẽ sai.

---

## Phần 3 — Giao thức nexus

## Phase 4.4b — Giao thức làm chủ `nexus` (để dùng được trên CV)

**Ngày:** 20/11/2026 · **Quyết định của Hoàn:** hoàn thành dự án → public repo → đưa `nexus` lên CV thay Chat-System → học mọi thứ từ chính dự án này.
**Vai trò của file này:** không phản đối quyết định. Nó biến "tôi sẽ học từ dự án" thành **6 cổng kiểm tra đo được**, vì đó là khác biệt duy nhất giữa "dự án mạnh" và "bẫy phỏng vấn".

---

### 0. Sự thật phải biết trước (đọc 2 phút, đừng bỏ qua)

Đọc repo thật ngày 20/11/2026 (qua GitHub API, không phải phỏng đoán):

| Hạng mục | Số liệu thật |
|---|---|
| Ngôn ngữ | Java **1.390.096 byte** (chính), CSS 27.831, JS 12.486, Python 5.945, **PLpgSQL 3.188**, Shell 36.304 |
| Module | `server`, `client-sdk`, `desktop-shared`, `desktop-user`, `desktop-admin`, `api`, `contract`, `perf`, `scripts`, `fx-test-support`, `ui-spike` |
| Server | Spring Boot: **REST + WebSocket có xác thực, Flyway, Redis presence & fan-out, Prometheus meters** |
| Test | **137 test / 7 suite** (4 skipped by design), coverage gate **theo từng class** |
| Contract | `api/v1/openapi.yaml` **55 KB**; `contract/realtime/*.json` 6 event |
| Hạ tầng | PostgreSQL **18**, Redis **8.10**, Docker Compose (có cả `docker-compose.perf.yml`) |
| JDK desktop | **JDK 27 + JavaFX 27.0.1** |
| Tài liệu | `docs/`: architecture, api, development, operations, ci-cd, performance |
| **Commit** | Mọi commit **PGP-signed**, author `Ho Phuoc Hoan`, **trailer `🤖 Generated with Codebuff / Co-Authored-By: Codebuff`** |

#### Vì sao dòng cuối quan trọng với kế hoạch CV

Bạn muốn **không** ghi "built with heavy AI assistance" trong README/CV — điều đó hợp lý và tôi không phản đối: README là tài liệu sản phẩm, không phải lời khai.

Nhưng: **git log đã tự khai**. Bất kỳ kỹ sư nào mở repo public cũng thấy `🤖 Generated with Codebuff` trong mọi commit. Vậy có đúng 3 lựa chọn:

| Lựa chọn | Đánh giá |
|---|---|
| **A. Giữ trailer, không banner trong README** ✅ đề xuất | Trung thực mà không tự hạ mình. Nếu bị hỏi: "Đúng, tôi dùng AI agent để triển khai; từ 11/2026 tôi viết tay phần lõi và review diff trước khi commit — lịch sử TaskFlow là bằng chứng, và tôi giải thích được mọi phần đã qua G6." Đây là câu trả lời **mạnh**, không phải yếu |
| B. Xoá trailer khỏi history (rebase/rewrite) | **Không** làm: viết lại history để che dấu là hành vi gây nhầm lẫn chủ động, phá chữ ký PGP, và nếu bị phát hiện thì mất toàn bộ uy tín |
| C. Banner "heavy AI assistance" trong README | Bạn nói đúng: bất lợi khi nộp CV, và không cần thiết vì trailer đã đủ |

**Kết luận:** giữ A. Không thêm disclaimer, không xoá dấu vết, **chuẩn bị câu trả lời**. Khác biệt giữa "không nêu" và "phủ nhận" là toàn bộ vấn đề đạo đức ở đây — A nằm ở phía an toàn.

#### Ba việc phải làm **trước khi** public (R10 + chất lượng repo)

1. **`.agents/profile.md` (4,9 KB)** — kiểm tra có thông tin cá nhân không (email, SĐT, địa chỉ, tên trường…). Nếu có → xoá hoặc thay bằng bản trung tính.
2. **`.idea/`** (IntelliJ) — nên xoá khỏi repo và thêm vào `.gitignore`; `dataSources.xml` có thể chứa thông tin DB.
3. **`.superpowers/sdd/nexus/progress.md` (54 KB)** — log quá trình agent làm việc. Giữ cũng được (trung thực), nhưng nó dài và có thể chứa ghi chú nội bộ; nếu giữ, hãy đọc lướt 1 lần.
4. **`Project.pdf` (154 KB)** — kiểm tra không chứa thông tin cá nhân/đề bài trường.

---

### 1. Ranh giới học: phần nào thuộc bạn, phần nào không

| Phần | Có học để phỏng vấn? | Ghi chú |
|---|---|---|
| `server` (Spring Boot, REST, WS, Redis, Flyway, metrics) | ✅ **Trọng tâm** | Đây là toàn bộ giá trị CV Java backend |
| `api/v1` + `client-sdk` (OpenAPI → SDK) | ✅ Học | Contract-first là điểm cộng hiếm ở fresher |
| `contract/realtime` + Redis fan-out + reconnect | ✅ Học | Chỗ bị hỏi xoáy nhất, và là chỗ bạn có test để chỉ |
| `desktop-shared/MLS` (mã hoá đầu cuối) | ⚠️ Hiểu **khái niệm** | Không cần code; nhưng phải nói được "vì sao E2EE khó" (key rotation, multi-device) |
| `desktop-user` / `desktop-admin` (JavaFX 27, FXML, golden screenshot) | ❌ **Không học sâu** | Ngoài mảng bạn nhắm; chỉ cần 2 câu: "JavaFX vì cần desktop native; golden screenshot để bắt hồi quy UI" |
| `fx-test-support`, `ui-spike`, `perf` | ❌ | Chỉ biết tồn tại |

**Ước lượng thời gian:** 40–60 giờ để qua 6 cổng, chia **W11–W16** (song song Phase 4 Stage 3). Không cần đọc hết 1,39 MB — chỉ cần **đọc theo luồng** (dưới đây).

---

### 2. Sáu cổng (G1–G6) — qua cổng nào ghi vào bảng dưới

#### G1. Bản đồ hệ thống — 3 giờ
**Việc:** vẽ tay (giấy) sơ đồ 5 module chính + luồng 1 tin nhắn: `desktop-user` → `server (REST/WS)` → `PostgreSQL (Flyway table)` → `Redis channel` → `desktop-user (peer)`.
**Đạt khi:** giải thích 10 phút **không mở code**, và trả lời được: "vì sao cần cả Postgres và Redis?" (lưu bền vs phát nhanh).
**Nguồn:** `docs/architecture.md`, `README.md`.

#### G2. Vòng đời một request — 4 giờ
**Việc:** chọn đúng **một** endpoint (`POST` tạo tin nhắn), lần theo: controller → validation → service → repository → transaction → publisher.
**Đạt khi:** kể lại trong **3 phút** với tên class thật; chỉ ra được chỗ nào là `@Transactional` và **vì sao** nó ở đó (không phải ở controller).
**Nguồn:** `server/src/main/java/...`, `api/v1/openapi.yaml`.

#### G3. Dữ liệu — 5 giờ
**Việc:** đọc **1** migration Flyway; viết lại schema 3 bảng chính từ trí nhớ (cột, FK, index); tìm hiểu `PLpgSQL` (3.188 byte) dùng để làm gì.
**Đạt khi:** giải thích được vì sao có logic ở DB (nếu có), và **1 index** trong schema tồn tại để phục vụ truy vấn nào (chỉ đúng tên truy vấn).

#### G4. Realtime + độ bền — 6 giờ
**Việc:** đọc `RealtimeConnection` + test của nó (commit 17/11 nói: backoff trong khoảng **nửa đến một lần** của ceiling tăng gấp đôi; open reset counter; close/error → 1 retry; branch coverage 44% → 100%).
**Đạt khi:** trả lời 3 câu — (a) client mất mạng vào lại thì tin nhắn có mất không, cơ chế nào đảm bảo? (b) vì sao dùng Redis pub/sub chứ không Kafka ở đây? (c) vì sao phải có "seam" (attempt + scheduler) để test backoff?

#### G5. Chất lượng & cổng CI — 4 giờ
**Việc:** đọc `build.gradle` (18,8 KB) phần coverage floor + `docs/ci-cd.md` + 1 file contract fixture.
**Đạt khi:** giải thích được: coverage floor **theo class** khác gì theo tổng; contract fixture ngăn được lỗi gì (đổi tên field ở 1 phía); vì sao 4 test bị skip; CodeQL/GitGuardian/release workflow làm gì.

#### G6. Tự tay thay đổi (cổng quan trọng nhất) — 15–25 giờ
Ba việc, **không AI viết code** (được hỏi khái niệm):

| Việc | Yêu cầu | Bằng chứng |
|---|---|---|
| **G6a. Thêm 1 endpoint nhỏ** | Ví dụ `GET /api/v1/conversations/{id}/members` — có validation, phân quyền, test `@WebMvcTest` + 1 integration | PR/commit của chính bạn, test xanh, coverage floor không tụt |
| **G6b. Sửa 1 bug thật** | Lấy từ **2 issue đang mở** của repo (hoặc bug bạn tự tìm) | Commit + test tái hiện bug trước khi sửa |
| **G6c. Đo 1 thứ** | 1 truy vấn chậm: `EXPLAIN ANALYZE` trước/sau index, ghi số ms | `docs/performance.md` bổ sung 5 dòng có số thật |

**Vì sao G6 là cổng chính:** đây là phần biến "tôi đọc code AI viết" thành "tôi làm việc được trên codebase này". Không có G6, mọi câu trả lời ở G1–G5 đều có thể sụp bằng một câu: *"Vậy em sửa gì trong đó?"*

---

### 3. Bảng theo dõi

| Cổng | Ngày bắt đầu | Ngày đạt | Ghi chú |
|---|---|---|---|
| G1 Bản đồ | | | |
| G2 Request | | | |
| G3 Dữ liệu | | | |
| G4 Realtime | | | |
| G5 CI/gate | | | |
| G6a Endpoint | | | |
| G6b Bug | | | |
| G6c Đo | | | |

**Luật:** `nexus` chỉ được lên CV sau khi **G1–G5 + G6a + G6b** đạt (G6c khuyến khích). Trước đó, CV giữ Chat-System.

---

### 4. Mười câu sẽ bị hỏi (chuẩn bị trước, đừng nghĩ tại chỗ)

| Câu | Điều họ đang kiểm |
|---|---|
| "Vì sao Redis mà không Kafka?" | Hiểu trade-off: pub/sub nhẹ cho fan-out tức thời; Kafka cho durability/replay — và biết dự án **cần** gì |
| "Tin nhắn có mất khi client offline không?" | Persistence ở Postgres + reconnect + sync history (`desktop-shared` có "history sync") |
| "WebSocket xác thực thế nào?" | Token lúc handshake; vì sao không để token trong query string (log) |
| "E2EE làm thế nào?" | MLS concept: group key, epoch, welcome message; biết **vì sao** khó (multi-device, key rotation) |
| "Coverage floor theo class để làm gì?" | Chặn "test 1 class cho đẹp tổng"; bảo vệ đúng class quan trọng |
| "137 test mà 4 skip — vì sao?" | Phải biết lý do thật (đọc code/nhãn); nếu không biết → nói "em chưa kiểm tra" chứ không đoán |
| "Vì sao JDK 27 mà không phải 25 LTS?" | Câu bẫy: 27 không phải LTS. Trả lời thật: desktop dùng 27 vì JavaFX 27; **server nên/đang ở LTS** — kiểm tra lại trước khi trả lời |
| "OpenAPI 55 KB — ai viết, để làm gì?" | Contract-first; sinh SDK → server/SDK không lệch |
| "Phần nào em tự viết?" | **Câu quyết định.** Trả lời thật + chỉ G6: "em thêm endpoint X, sửa bug Y, tối ưu query Z". Nếu nói dối ở đây, cả buổi phỏng vấn mất giá trị |
| "Nếu làm lại, em đổi gì?" | Cần **1 ý thật**: ví dụ "em sẽ tách module `server` theo bounded context thay vì package-by-layer" hoặc "em sẽ thêm test cho phần migration rollback" |

---

### 5. CV: cách viết để không phải nói dối mà cũng không tự hạ mình

**Nguyên tắc:** mô tả **hệ thống** (đúng) + mô tả **việc bạn làm** (đúng) — không cần câu "tôi viết từng dòng".

Bản nháp (điền sau khi qua G6; các chỗ `[...]` là việc **bạn** đã làm):

```
Nexus — nền tảng nhắn tin thời gian thực · Java, Spring Boot, PostgreSQL, Redis, Docker · 11/2026 · cá nhân
- Server Spring Boot: REST + WebSocket có xác thực, Flyway migration, Redis cho presence và fan-out,
  Prometheus metrics; 137 test qua 7 suite, coverage gate theo từng class trong CI.
- Contract-first: OpenAPI (api/v1) sinh client SDK nên server và SDK không lệch hợp đồng.
- [Thêm endpoint ... + test], [sửa bug ...], [tối ưu truy vấn ...: 120ms → 18ms].
```

**Nếu bị hỏi "AI viết bao nhiêu?"** → không né: *"Phần lớn code dự án này do AI agent viết; em đọc lại, tự tay thêm [X] và sửa [Y] sau khi qua G6, và em giải thích được kiến trúc cùng các luồng chính — anh/chị muốn hỏi luồng nào trước?"* (Chỉ nói "em review từng diff" khi việc đó **đã xảy ra** và có commit để chỉ.)

---

### 6. Điều gì sẽ khiến kế hoạch này hỏng (và cách phát hiện sớm)

| Rủi ro | Dấu hiệu sớm | Xử lý |
|---|---|---|
| **Học kiểu đọc** — đọc docs 20 giờ, không mở code | Sau 1 tuần chưa làm được G2 (3 phút kể luồng) | Chuyển sang "trace 1 request" ngay, bỏ đọc |
| **G6 không bao giờ bắt đầu** vì "chưa hiểu hết" | 3 tuần vẫn ở G1–G3 | Bắt buộc G6a trong tuần thứ 3, hiểu một nửa vẫn làm |
| **Phỏng vấn hỏi phần JavaFX/MLS** | Bạn không trả lời được 2 câu đầu | Học đúng 2 câu khái niệm (mục 1), nói thẳng "mảng này em chỉ hiểu ở mức kiến trúc" |
| **Bị hỏi sâu hơn mức hiểu** | Câu hỏi tầng 3–4 về một class cụ thể | Trả lời thật + hướng: "em chưa đọc class đó; em sẽ đọc theo luồng X" — **không đoán** |
| **Dự án không bao giờ "xong"** | Agent vẫn push sau 2 tuần nữa | Chốt **1 commit làm mốc CV** (tag `v1.0-cv`), mọi thứ sau đó là bonus |

---

### Checkpoint Phase 4.4b

- Dữ liệu thật từ repo: 11 module, 1,39 MB Java, **137 test/7 suite**, Redis + Postgres 18, OpenAPI 55 KB, coverage gate theo class, CI có CodeQL/GitGuardian/release.
- **Sự thật then chốt:** mọi commit đã có trailer `Generated with Codebuff` và PGP-signed → "không nêu trong README" hợp lý, nhưng **không thể phủ nhận khi bị hỏi**; và không được rewrite history.
- **6 cổng**, trong đó **G6 (tự thêm endpoint + sửa bug + đo)** là điều kiện để `nexus` lên CV thay Chat-System.
- 3 việc phải làm trước khi public: kiểm `.agents/profile.md`, bỏ `.idea/`, đọc lướt `progress.md` + `Project.pdf`.

**Quyết định đề xuất:** giữ kế hoạch của bạn, nhưng **CV chỉ đổi sau G6b**, và chốt 1 tag làm mốc.
**Vì sao:** dự án đủ mạnh để làm tâm điểm CV (hơn hẳn một CRUD), và 40–60 giờ học có cổng là khoản đầu tư hợp lý — với điều kiện có phần "tay mình làm".
**Điều gì sẽ khiến tôi đổi ý:** nếu đến cuối W14 vẫn chưa xong G6a (thêm 1 endpoint) → dự án chưa sẵn sàng làm tâm điểm CV; khi đó để `nexus` ở mức "dự án phụ" và giữ TaskFlow (tự viết) làm dự án chính.

---

## Phần 4 — Hệ thống ghi nhớ

## Phase 4.8 — Hệ thống ôn tập (chống quên, không chống học)

**Vấn đề thật:** Hoàn đã học Java (CSC13102 **9.7**), CSDL (**9.0**) — kiến thức **đã từng có**. Nhưng 2 năm sau, kỹ năng đo được là **L2**, không phải L3. Nghĩa là vấn đề không phải "học chưa đủ" mà là **không giữ được**. File này giải quyết phần giữ.

**Ba trụ cột — theo thứ tự quan trọng:**

| # | Cơ chế | Vì sao quan trọng hơn cái dưới | Thời lượng |
|---|---|---|---|
| 1 | **Viết lại từ trí nhớ** (retrieval trong ngữ cảnh thật) | Không có tài liệu, không gợi ý → đo đúng "biết làm" | 60'/ngày (bản 6h) |
| 2 | **Dự án thật** (TaskFlow/MiniWallet) | Mỗi lần sửa bug là một lần ôn tự nhiên | Trong giờ học |
| 3 | **Thẻ Anki** (spaced repetition cho chi tiết) | Chỉ giữ **chi tiết**, không giữ kỹ năng | 20'/ngày |

> **Cảnh báo:** Anki **không** tạo ra kỹ năng code. Học 500 thẻ Java mà không gõ code = biết nói về Java, không viết được Java. Anki là trụ cột số 3, không phải số 1.

---

### 1. Lịch ôn (spaced repetition thủ công — không cần app trả phí)

| Khi học một thứ mới | Ôn lại vào | Cách ôn |
|---|---|---|
| Ngày 0 | cuối ngày | Viết lại từ trí nhớ, không nhìn |
| +1 ngày | Ngày 1 | Tự hỏi 3 câu về nó (không mở tài liệu) |
| +3 ngày | Ngày 3 | Làm lại bài tập biến thể (đổi input) |
| +7 ngày | Ngày 7 (ngày nghỉ) | Giải thích cho chính mình bằng giọng nói, ghi âm 2' |
| +14 ngày | Ngày 14 | Dùng nó trong dự án (nếu chưa dùng được → chưa hiểu) |
| +30 ngày | Ngày 30 | Làm lại bài test của chủ đề đó (T1/T2/T4) |

**Luật:** nếu ở mốc +7 mà **không giải thích được trong 2 phút**, coi như chưa học → quay lại học lại (đừng đánh dấu "đã xong").

### 2. Nguồn tạo thẻ — chỉ 4 nguồn (không tạo thẻ từ mọi thứ)

1. **Chỗ mình làm sai** trong bài tập/bug (giá trị cao nhất).
2. **Chỗ mình phải tra cứu 2 lần** (nghĩa là chưa nhớ).
3. **Câu hỏi phỏng vấn** trong `04_interview_prep.md` mà mình trả lời vấp.
4. **Khái niệm cốt lõi** của ngày (tối đa 5 thẻ/ngày).

**Cấm:** tạo thẻ từ câu trong sách (học thuộc chữ, không hiểu), hoặc tạo 30 thẻ/ngày (sẽ bỏ sau 1 tuần).

**Luật viết thẻ:** 1 thẻ = 1 ý; **viết bằng lời mình**; mặt sau phải có **ví dụ hoặc "vì sao"**, không chỉ định nghĩa.

### 3. Ba mẫu thẻ hay dùng

| Loại | Mặt trước | Mặt sau |
|---|---|---|
| **Định nghĩa có ví dụ** | "N+1 là gì?" | "1 câu SQL lấy N bản ghi cha, rồi N câu nữa cho con → N+1 câu. Trong TaskFlow: 21 task → 22 câu SQL. Sửa: `JOIN FETCH`." |
| **Vì sao** | "Vì sao `@Transactional` mất tác dụng khi gọi hàm trong cùng class?" | "Vì Spring dùng proxy; gọi nội bộ không qua proxy nên không có transaction." |
| **Lỗi mình đã mắc** | "Lỗi: HashMap mất phần tử dù `equals` đúng" | "Vì `hashCode` chưa override → 2 object cùng giá trị rơi vào 2 bucket khác nhau." |

### 4. Nhật ký lỗi (quan trọng hơn thẻ Anki)

Một file `MISTAKES.md` trong repo `java-backend-lab`. Mỗi dòng: **ngày · lỗi · nguyên nhân gốc · đã sửa bằng gì · lần sau tránh thế nào**.

Ví dụ thật (điền khi gặp):
```
2026-11-25 | Test rollback không rollback | thiếu @Transactional ở service (đặt ở test) | thêm ở service, đọc lại docs | kiểm tra proxy trước khi debug tiếp
```

**Đọc lại `MISTAKES.md` mỗi Chủ nhật.** Đây là tài liệu cá nhân giá trị nhất sau 6 tháng — và là thứ trả lời rất tốt câu "lần em làm sai và tự sửa là khi nào?" ở vòng 5.

### 5. Lịch tuần (không nặng thêm)

| Thời điểm | Việc | Thời lượng |
|---|---|---|
| Mỗi ngày | Anki thẻ đến hạn + tạo ≤ 5 thẻ mới từ việc hôm nay | 20' |
| Cuối mỗi ngày | Viết lại từ trí nhớ + `LEARNING.md` 3 dòng | 60' |
| Chủ nhật | Đọc `MISTAKES.md` + `LEARNING.md` tuần; làm 1 bài test cũ (luân phiên T1/T2/T4) | 60' |
| Cuối tháng | Viết lại **1 bài code** đã làm cách đó 30 ngày, không nhìn | 60' |

### 6. Bảng theo dõi (điền tay, 1 dòng/tuần)

| Tuần | Thẻ mới | Thẻ đến hạn đã ôn | Bài viết lại đạt | Lỗi mới ghi | Ghi chú |
|---|---|---|---|---|---|
| W1 | | | /1 | | |

---

### Checkpoint Phase 4.8

- 3 trụ cột theo đúng thứ tự: viết lại > dự án > Anki. Anki chỉ 20'/ngày, tối đa 5 thẻ mới.
- Thẻ chỉ lấy từ **4 nguồn** (lỗi, phải tra 2 lần, câu phỏng vấn vấp, khái niệm cốt lõi của ngày).
- `MISTAKES.md` là tài sản chính — nó vừa chống quên, vừa là nguyên liệu cho câu STAR.

**Quyết định đề xuất:** không cài app ôn tập trả phí, dùng Anki desktop (miễn phí) + lịch thủ công ở mục 1.
**Vì sao:** lịch thủ công đã đủ cho 60 thẻ/tháng, và giảm nguy cơ "ôn thẻ thay vì code".
**Điều gì sẽ khiến tôi đổi ý:** nếu sau 4 tuần số thẻ đến hạn > 150 và không theo kịp → chuyển sang Anki thuần (FSRS) và **giảm** số thẻ mới xuống 3/ngày, không tăng giờ.
