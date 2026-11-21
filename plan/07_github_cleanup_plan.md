# 07.3 — Kế hoạch dọn GitHub (36 repo)

**Ngày:** 21/11/2026 · **Cập nhật lần cuối:** 21/11/2026 · **Dữ liệu:** `02c_repo_inventory.md` (clone thật 20/11/2026) + `github_repos.txt`
**Luật:** chỉ **ghim/Featured** repo đã qua **bài bảo vệ** (xem `07_cv_truth_checklist.md`). Repo chưa bảo vệ được thì vẫn để đó, nhưng **không** đặt ở nơi nhà tuyển dụng nhìn đầu tiên.

---

## 1. Năm quyết định, áp lên repo thật

| Quyết định | Nghĩa là gì | Repo áp dụng |
|---|---|---|
| **PIN** | Đưa lên 6 ghim + Featured LinkedIn | `Chat-System` *(sau T6)* · `IT-Tools` *(sau bảo vệ dự án)* · `DSA-Practice` · `CoolWear` *(sau khi đọc lại code)* |
| **GIỮ** | Để public, không ghim, không nhắc trong CV | `Email-Socket` · `File-System` · `task-tracker` · `Calolator` · `Smart-Door` · `java-multithreading-concurrency` · `quiz-game` · `Anki-learn-English-vocabularies` |
| **ARCHIVE** | Đọc-only, thêm dòng "bài tập khoá học" trong README | 22 repo còn lại (Odin Project, CS50, landing page, bot Discord, dotfiles…) |
| **PRIVATE** | Ẩn khỏi profile công khai | `Learnix` (46.783 LOC, phần lớn AI sinh) · `nexus` (chỉ public **sau** G6a+G6b) |
| **XOÁ** | Xoá hẳn | Chỉ repo rỗng/trùng lặp thật sự, sau khi kiểm tra không có commit nào cần giữ |

**Vì sao `Learnix` → private:** đây là repo lớn nhất về số dòng nhưng không phải Java và phần lớn do AI sinh. Public nó mời đúng câu hỏi mà `01_cv_linkedin_audit.md` đã xác định là bẫy.

**Vì sao `nexus` chưa public:** 32.126 LOC Java, mạnh nhất về hình thức, nhưng chưa qua G6. Public trước G6 = đặt một dự án bạn chưa giải thích được ở vị trí dễ thấy nhất.

---

## 2. Thứ tự làm (90 phút, một lần)

| Bước | Việc | Thời gian | Xong khi |
|---|---|---|---|
| 1 | Quét bí mật **trong lịch sử** cả 36 repo (mục 4) | 20' | 0 kết quả, hoặc đã rotate key |
| 2 | Đổi `Learnix`, `nexus` → private | 5' | Mở incognito không thấy |
| 3 | Archive 22 repo bài tập, thêm 1 dòng mô tả | 20' | Trang profile gọn còn ~8 repo |
| 4 | Viết README cho 4 repo sẽ ghim (mẫu mục 3) | 30' | Mỗi README chạy được theo hướng dẫn |
| 5 | Tạo profile README (mục 5) | 10' | Hiện ở đầu trang GitHub |
| 6 | Ghim 4 repo **đủ điều kiện** | 5' | Đúng thứ tự |

---

## 3. Mẫu README cho repo được ghim (≥ 15 dòng)

```markdown
# <Tên dự án> — <một dòng mô tả>

## Chạy trong 3 phút
```bash
git clone <url> && cd <repo>
cp .env.example .env
docker compose up --build
```
Mở http://localhost:8080/actuator/health → `{"status":"UP"}`

## Kiến trúc (3 dòng)
- Spring Boot 4.2 · PostgreSQL · Flyway
- 3 tầng: controller → service → repository; phân quyền theo owner ở tầng service
- Test: unit + @WebMvcTest + Testcontainers

## Test
```bash
./mvnw test     # không cần DB cài sẵn
```

## Ba quyết định thiết kế
1. <quyết định> — vì <lý do>, đánh đổi là <...>
2. ...
3. ...

## Những gì tôi tự viết
<1–2 câu thật. Nếu có phần do AI sinh, ghi rõ.>
```

**Không** để trong repo: `.env`, `target/`, `node_modules/`, file dump > 5 MB, ảnh chụp có email/SĐT.

---

## 4. Kiểm tra bí mật trong lịch sử

```bash
# Cài 1 lần
brew install gitleaks   # hoặc tải binary từ github.com/gitleaks/gitleaks

# Quét từng repo đã clone trong _repos/
for d in _repos/*/; do
  echo "== $d"; gitleaks detect --source "$d" --no-banner --redact -v || true
done
```

Nếu có kết quả: **rotate key trước**, rồi mới tính chuyện viết lại lịch sử (`git filter-repo`). Xoá file ở commit mới **không** xoá khỏi lịch sử.

---

## 5. Bản nháp profile README (repo tên = username)

```markdown
### Hồ Phước Hoàn — Backend Developer (Java), TP.HCM

Tốt nghiệp loại Giỏi, CNTT (GPA 8.74/10) — ĐH Khoa học Tự nhiên, ĐHQG-HCM.
Đang xây nền backend bằng Java/Spring Boot, viết tay phần lõi và viết test cho từng phần.

**Đang làm:** TaskFlow — REST API quản lý công việc (Spring Boot 4.2, PostgreSQL, JWT, Testcontainers).
**Đã có:** Chat System (Java, Hibernate, PostgreSQL) · IT-Tools (ASP.NET Core, EF Core, JWT).
**Luyện tập:** 463 bài DSA (C++) → [DSA-Practice](https://github.com/hoanhophuoc/DSA-Practice)

Liên hệ: [email] · [LinkedIn](https://linkedin.com/in/hoanho)
```

**Quy tắc:** chỉ liệt kê repo **đã qua bài bảo vệ**. Không ghi "137 tests" hay bất kỳ con số nào bạn không tự chạy lại được.

---

## 6. Điều kiện để một repo được ghim

- [ ] README ≥ 15 dòng, có lệnh chạy và lệnh test
- [ ] `docker compose up` chạy được từ máy sạch (hoặc hướng dẫn rõ nếu không)
- [ ] Có ít nhất 1 test thật, chạy xanh
- [ ] Không có `.env`, key, token trong repo **và** trong lịch sử
- [ ] Bạn giải thích được 3 quyết định thiết kế mà không mở code
- [ ] Bạn nói được phần nào mình tự viết

Không đạt 6 ô trên → **giữ public nhưng không ghim**.
