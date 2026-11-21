# T2 — SQL (60 phút · KHÔNG AI · KHÔNG Google)

**Quy tắc:** được xem schema. Không tra Google, không AI. Viết SQL chạy được trên **PostgreSQL 16+** (dùng cú pháp Postgres; nếu quen MySQL, ghi chú chỗ khác).

---

## Schema

```sql
CREATE TABLE categories (
    id       SERIAL PRIMARY KEY,
    name     VARCHAR(100) NOT NULL
);

CREATE TABLE products (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(200) NOT NULL,
    category_id INT REFERENCES categories(id),
    price       NUMERIC(12,2) NOT NULL,
    stock       INT NOT NULL DEFAULT 0
);

CREATE TABLE customers (
    id         SERIAL PRIMARY KEY,
    name       VARCHAR(200) NOT NULL,
    city       VARCHAR(100),
    created_at TIMESTAMP NOT NULL DEFAULT now()
);

CREATE TABLE orders (
    id          SERIAL PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customers(id),
    status      VARCHAR(20) NOT NULL,   -- 'pending' | 'paid' | 'cancelled'
    created_at  TIMESTAMP NOT NULL DEFAULT now()
);

CREATE TABLE order_items (
    id         SERIAL PRIMARY KEY,
    order_id   INT NOT NULL REFERENCES orders(id),
    product_id INT NOT NULL REFERENCES products(id),
    quantity   INT NOT NULL,
    unit_price NUMERIC(12,2) NOT NULL
);
```

**Giả định:** `orders` không có cột tổng tiền; doanh thu của một order = `SUM(order_items.quantity * unit_price)`.

---

## 10 câu (mỗi câu 10 điểm)

**Q1.** Liệt kê **tất cả** khách ở `'Hồ Chí Minh'` kèm số đơn hàng của họ — khách chưa có đơn vẫn phải xuất hiện với số 0. Sắp theo số đơn giảm dần.

**Q2.** Tổng doanh thu theo từng category, **chỉ tính đơn `status = 'paid'`**. Cột: `category_name`, `revenue`. Sắp giảm dần.

**Q3.** Top 5 sản phẩm bán chạy nhất theo **tổng số lượng** (chỉ đơn `paid`). Cột: `product_name`, `total_quantity`.

**Q4.** Khách hàng **chưa từng** đặt đơn nào. Viết bằng **2 cách**: `NOT IN`/`NOT EXISTS` và `LEFT JOIN`.

**Q5.** Doanh thu trung bình mỗi tháng trong năm 2026 (chỉ `paid`). Cột: `month` (dạng `2026-01`), `revenue`.

**Q6.** Sản phẩm **chưa từng** được bán (không có trong bất kỳ `order_items` nào).

**Q7.** Với mỗi khách, ngày đặt đơn **gần nhất** và tổng số đơn. Cột: `customer_name`, `last_order_at`, `order_count`. Dùng window function.

**Q8.** Doanh thu theo ngày trong tháng 10/2026 kèm **doanh thu luỹ kế** (running total) theo ngày. Cột: `day`, `daily_revenue`, `running_total`.

**Q9.** Khách có **tổng chi tiêu > 2 lần** mức chi tiêu trung bình của tất cả khách (chỉ đơn `paid`). Cột: `customer_name`, `total_spent`.

**Q10.** Cho truy vấn chậm sau:
```sql
SELECT * FROM orders
WHERE status = 'paid'
ORDER BY created_at DESC
LIMIT 20;
```
a) Viết `CREATE INDEX` phù hợp và giải thích tại sao chọn cột/thứ tự đó.
b) Chạy `EXPLAIN ANALYZE` sẽ thấy gì trước và sau khi có index? (mô tả bằng lời: `Seq Scan` → `Index Scan`/`Bitmap Heap Scan`)
c) Vì sao `SELECT *` ở đây là vấn đề nếu bảng có 40 cột?
d) Nếu bảng có 50 triệu dòng và `status` chỉ có 3 giá trị, index trên `status` một mình có hiệu quả không? Vì sao?

---

## Câu hỏi hiểu biết (không tính điểm nhưng phải trả lời được miệng)

1. `INNER JOIN` khác `LEFT JOIN` ở đâu — cho ví dụ Q1 nếu dùng sai.
2. `WHERE` và `HAVING` khác nhau thế nào?
3. `COUNT(*)` khác `COUNT(column)` ở đâu?
4. Transaction là gì; khi nào cần `BEGIN ... COMMIT`?
5. Index làm chậm thao tác nào, vì sao vẫn nên có?

---

## Tự kiểm tra

- [ ] Đã viết đủ 10 câu trong 60 phút?
- [ ] Q4 viết được **cả hai** cách?
- [ ] Q7, Q8 dùng window function (không dùng subquery tương quan)?
- [ ] Q10 giải thích được bằng lời, không chỉ viết câu lệnh?
- [ ] Đã chấm theo `09_answer_key.md` và ghi L vào `01_skills_matrix.csv`?
