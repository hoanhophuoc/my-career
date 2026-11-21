# Phase 9 — Prompt làm mới pack (copy-paste)

**Dùng khi nào:** Chủ nhật cuối mỗi 2 tuần (prompt 1), sau 20 đơn (prompt 2), cuối mỗi tháng (prompt 3), mỗi quý (prompt 4).
**Nguyên tắc:** mỗi prompt phải nói rõ **file nào cần sửa** và **số liệu nào phải là số thật**. Không prompt nào được phép thêm tài liệu mới (R7).

---

## Prompt 1 — Crawl lại thị trường (15 phút, mỗi 2 tuần)

```
Chạy lại crawl LinkedIn trong hoan_career_pack:
1. python3 tools/crawl_linkedin_jobs.py  (đổi ngày trong tên file sang hôm nay)
2. python3 tools/purge_tester_rows.py  ← BẮT BUỘC: Hoàn KHÔNG làm tester/QA, phải lọc theo cột title
   (regex trong script; nếu thấy title mới kiểu "quality engineer" thì bổ sung vào regex)
3. python3 tools/analyze_linkedin_jobs.py
4. So sánh với 02d_linkedin_stats_2026-11-20.json và trả lời đúng 4 câu:
   - Số tin chạm tới được (không senior, ≤2 năm) tăng hay giảm, bao nhiêu?
   - Số tin Java vừa sức là bao nhiêu, có tin nào mới trong 14 ngày qua?
   - Có công ty nào tuyển ≥3 tin vừa sức mà lần trước không có?
   - Tỉ lệ tin có lương thay đổi thế nào?
5. Cập nhật 02d_linkedin_market_snapshot_*.md: chỉ sửa mục số liệu + thêm 1 dòng CHANGELOG.
Không thêm từ khoá mới trừ khi tôi nói. Không mở từng tin.
```

### Prompt 1b — Lấy quận cho tin ITviec (10 phút, khi có tin mới)

```
Với mỗi URL tin ITviec mới trong 02e_itviec_hcm_salary_*.csv:
1. curl trang JD, tìm khối "address" trong application/ld+json → streetAddress + addressLocality.
2. Ghi vào cột quan / dia_chi_trong_jd. Muốn tính khoảng cách: chạy tools/build_commute.py (đọc config.local.json, không commit).
3. addressLocality = "Not Available" → ghi "không khai", KHÔNG đoán.
4. Cập nhật 02e_itviec_districts_stats_*.json + 1 dòng CHANGELOG.
Lưu ý: khoảng 1/3 tin giấu địa chỉ — nói rõ số tin biết quận / tổng, đừng làm tròn thành "tất cả".
```

---

## Prompt 2 — Review CV sau 20 đơn (30 phút)

```
Đọc 07_application_tracker.csv và trả lời bằng số, không bằng cảm nhận:
1. Tỉ lệ phản hồi = số có phản hồi / số đơn đã nộp. So với ngưỡng 10% ở 09_executive_summary.md mục 6.
2. Nhóm đơn nào có phản hồi (theo slot CV S1/S2/S3 và theo kênh)? Nhóm nào 0 phản hồi?
3. Đọc lại 3 JD của nhóm 0 phản hồi và chỉ ra ĐÚNG 2 dòng trong CV đang lệch với JD.
4. Đề xuất sửa tối đa 5 dòng trong 01_honest_cv_v1.md — không viết lại cả CV, không thêm kỹ năng tôi chưa có bằng chứng.
5. Nếu tỉ lệ < 10%: nói thẳng là vấn đề ở CV hay ở kênh, và chọn 1 thứ để sửa trong 7 ngày.
```

---

## Prompt 3 — Review 30 ngày (20 phút, cuối tháng)

```
Đọc 09_kpi_tracker.csv (4 tuần gần nhất) và 09_executive_summary.md mục 6.
1. Với từng KPI trong 8 KPI: đạt / trượt, kèm số thật.
2. Chỉ số nào trượt 2 tuần liền → áp đúng biện pháp ở cột "Nếu trượt 2 tuần liền".
3. Có cổng nào (G1–G6) sắp tới? Tôi đã đủ điều kiện qua chưa, thiếu gì?
4. Nếu giờ code tay < 15h/tuần trong 2 tuần liền → đề xuất chuyển sang bản 3h/ngày (mục 8 roadmap), đừng khuyên "cố thêm".
5. Cập nhật 09_executive_summary.md mục 1 (trạng thái) + 1 dòng CHANGELOG. Không thêm file mới.
```

---

## Prompt 4 — Làm mới toàn pack (mỗi quý, 60 phút)

```
Rà soát hoan_career_pack và chỉ sửa chỗ nào dữ kiện đã đổi:
1. Phiên bản: Java LTS mới nhất và Spring Boot bản ổn định (kiểm tra docs.spring.io + dev.java). Nếu lệch với 04_master_roadmap.md mục 0 → sửa và ghi CHANGELOG.
2. Học phí thạc sĩ + lịch tuyển đợt mới (`08_education_competitions_community.md` mục 1). Nếu có đợt mới → cập nhật ngày, giữ nguyên kết luận trừ khi học phí đổi >20%.
3. Giá chứng chỉ (`08_education_competitions_community.md` mục 3) — chỉ cập nhật nếu chênh >10%.
4. Sự kiện cộng đồng 30 ngày tới (GDG HCMC, GDG Cloud HCMC) — kiểm tra HTTP 200 và ngày thật.
5. Kiểm tra lại 3 sự thật dễ lệch nhất: (a) `nexus` đã qua G6 chưa; (b) TaskFlow đã chạy chưa; (c) CV đã có Spring Boot chưa.
Trả lời bằng bảng "cũ → mới → file đã sửa". Không viết lại file không có dữ kiện thay đổi.
```

---

## Checklist trước khi kết thúc mỗi lần làm mới

- [ ] Số liệu mới có **ngày truy cập** và **URL** đi kèm
- [ ] Đã chạy `tools/purge_tester_rows.py` → **0 dòng tester/QA** trong mọi CSV/shortlist
- [ ] Tin ITviec mới đã có cột `quan` + `km_uoc_tinh` (hoặc ghi rõ "không khai")
- [ ] Không file nào bị mâu thuẫn với `09_executive_summary.md` mục 2 (7 quyết định đã chốt)
- [ ] `REVIEW_FIX_LOG.md` có dòng CHANGELOG mới
- [ ] Không thêm file mới nếu có thể sửa file đang có
- [ ] Nếu phải đổi một quyết định đã chốt → ghi rõ **lý do + dữ kiện mới**, không sửa lặng lẽ
