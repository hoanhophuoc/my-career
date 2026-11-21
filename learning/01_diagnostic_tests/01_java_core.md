# T1 — JAVA CORE (90 phút · KHÔNG AI · KHÔNG Google)

**Quy tắc:** Phần A và B **không được tra cứu gì**. Phần C được xem Java API docs (docs.oracle.com) nhưng **không dùng AI/IDE gợi ý**.
Ghi đáp án ra giấy theo mẫu `1-A, 2-C, ...`. Không mở `09_answer_key.md` trước khi hết giờ.

---

## PHẦN A — 30 câu trắc nghiệm (30 điểm, 45 phút)

**A1.** Đoạn nào in ra `"hello"`?
```java
String s = "  hello  ";
s.trim();
System.out.println(s);
```
A. `hello`　B. `  hello  `　C. lỗi biên dịch　D. `null`

**A2.** Kết quả?
```java
String a = "java";
String b = "java";
String c = new String("java");
System.out.println((a == b) + " " + (a == c) + " " + a.equals(c));
```
A. `true true true`　B. `true false true`　C. `false false true`　D. `true false false`

**A3.** `ArrayList.get(i)` và `LinkedList.get(i)` có độ phức tạp trung bình lần lượt là:
A. O(1), O(1)　B. O(1), O(n)　C. O(n), O(n)　D. O(log n), O(1)

**A4.** `HashMap` cho phép bao nhiêu key `null`?
A. 0　B. 1　C. nhiều　D. phụ thuộc kích thước map

**A5.** Điều gì đúng với `final List<String> list = new ArrayList<>();`
A. Không thể gọi `list.add(...)`　B. Có thể `list.add(...)` nhưng không thể gán `list = ...`　C. Không thể đọc phần tử　D. Lỗi biên dịch

**A6.** Từ Java 8, một `interface` có thể chứa:
A. Chỉ method trừu tượng　B. Method `default` và `static` có thân hàm　C. Constructor　D. Field non-static

**A7.** `NullPointerException` thuộc loại nào?
A. Checked exception　B. Unchecked exception (RuntimeException)　C. Error　D. Throwable trực tiếp

**A8.** `try`-with-resources yêu cầu resource phải:
A. kế thừa `Closeable` hoặc implement `AutoCloseable`　B. có method `close()` bất kỳ　C. là `final`　D. implement `Serializable`

**A9.** Vòng lặp nào nhanh hơn khi nối rất nhiều chuỗi?
A. `s = s + x`　B. `s += x`　C. `StringBuilder.append(x)`　D. `String.format`

**A10.** Kết quả?
```java
Integer a = 127, b = 127;
Integer c = 128, d = 128;
System.out.println((a == b) + " " + (c == d));
```
A. `true true`　B. `true false`　C. `false false`　D. `false true`

**A11.** Khác nhau giữa `map` và `flatMap` trong Stream?
A. Không khác　B. `map` biến 1 phần tử thành 1 phần tử; `flatMap` biến 1 phần tử thành một Stream rồi trải phẳng　C. `flatMap` chỉ dùng cho số　D. `map` là lazy, `flatMap` là eager

**A12.** `Collectors.toMap(k, v)` khi có 2 phần tử cùng key sẽ:
A. ghi đè key cũ　B. giữ key đầu　C. ném `IllegalStateException`　D. trả về map rỗng

**A13.** `Optional<T>` được tạo ra chủ yếu để:
A. tăng hiệu năng　B. biểu diễn "có thể không có giá trị" ở kiểu trả về, giảm null-check rải rác　C. thay thế mọi `null`　D. cho phép generic với kiểu nguyên thuỷ

**A14.** Method `static` trong lớp con trùng chữ ký với lớp cha gọi là:
A. override　B. hide (che khuất)　C. overload　D. shadow

**A15.** Overload được chọn dựa trên:
A. kiểu thực tế lúc chạy　B. kiểu khai báo lúc biên dịch　C. tên biến　D. thứ tự khai báo trong file

**A16.** Constructor:
A. được kế thừa　B. không được kế thừa　C. phải là `public`　D. có thể là `abstract`

**A17.** Trong constructor, lời gọi `super(...)` hoặc `this(...)` phải:
A. ở bất kỳ đâu　B. là câu lệnh đầu tiên　C. là câu lệnh cuối cùng　D. bọc trong `try`

**A18.** Điều nào **chỉ** abstract class có mà interface (trước Java 8) không có?
A. method trừu tượng　B. field non-static, non-final　C. hằng số　D. nhiều method

**A19.** Hợp đồng giữa `equals` và `hashCode`:
A. không liên quan　B. `equals` bằng nhau ⇒ `hashCode` phải bằng nhau　C. `hashCode` bằng nhau ⇒ `equals` phải true　D. cả hai phải là duy nhất

**A20.** Generic trong Java bị "erasure" nghĩa là:
A. thông tin kiểu generic bị xoá lúc chạy　B. generic chậm hơn mảng　C. không dùng được với class　D. mọi generic thành `Object` lúc biên dịch và bị cấm

**A21.** Với `List<? extends Number> list`, điều nào **không** làm được?
A. đọc phần tử ra `Number`　B. `list.add(Integer.valueOf(1))`　C. truyền `List<Integer>` vào　D. gọi `list.size()`

**A22.** `synchronized` trên method instance sẽ khoá:
A. class　B. đối tượng `this`　C. mọi đối tượng cùng class　D. không khoá gì

**A23.** `volatile` bảo đảm:
A. tính nguyên tử của `count++`　B. khả năng thấy giá trị mới nhất giữa các thread (visibility)　C. loại bỏ deadlock　D. sắp xếp lại lệnh

**A24.** `ExecutorService.submit(...)` khác `execute(...)` ở chỗ:
A. `submit` trả về `Future` và bắt được exception　B. `execute` nhanh hơn　C. `submit` chỉ nhận `Runnable`　D. không khác

**A25.** Cách phòng deadlock thực dụng nhất khi cần nhiều lock:
A. dùng càng nhiều lock càng tốt　B. luôn acquire lock theo một thứ tự cố định toàn cục　C. dùng `synchronized` thay `ReentrantLock`　D. tăng timeout của thread

**A26.** Kết quả?
```java
static int f() { try { return 1; } finally { return 2; } }
```
A. 1　B. 2　C. lỗi biên dịch　D. ném exception

**A27.** Kết quả?
```java
Object[] arr = new String[1];
arr[0] = Integer.valueOf(1);
```
A. chạy bình thường　B. `ArrayStoreException` lúc chạy　C. lỗi biên dịch　D. `ClassCastException`

**A28.** `switch` với `String` được hỗ trợ từ Java:
A. 6　B. 7　C. 8　D. 11

**A29.** `var` (Java 10) dùng được ở đâu?
A. field của class　B. tham số method　C. biến local có khởi tạo ngay　D. kiểu trả về

**A30.** `record Point(int x, int y)` (Java 16):
A. có setter `setX()`　B. accessor là `x()` và `y()`, các field là `private final`　C. có thể kế thừa class khác　D. không có `equals`

---

## PHẦN B — 10 câu đọc code, đoán output/lỗi (20 điểm, 25 phút)

Với mỗi đoạn: ghi **output chính xác**, hoặc **loại exception**, hoặc **lỗi biên dịch** + 1 dòng giải thích.

**B1.**
```java
List<Integer> list = Arrays.asList(1, 2, 3);
list.add(4);
System.out.println(list);
```

**B2.**
```java
class A { static void s() { System.out.println("A"); } }
class B extends A { static void s() { System.out.println("B"); } }
A x = new B();
x.s();
```

**B3.**
```java
Map<String, Integer> m = new HashMap<>();
m.put("a", 1);
m.put("a", 2);
System.out.println(m.size() + " " + m.get("a"));
```

**B4.**
```java
System.out.println(1 / 2);
System.out.println(1 / 2.0);
System.out.println((double) (1 / 2));
```

**B5.**
```java
class C {
    private int count = 0;
    public void inc() { count++; }
}
// Thread 1 và Thread 2, mỗi thread gọi inc() 1000 lần.
// Hỏi: count sau khi cả hai xong LUÔN bằng 2000? Vì sao?
```

**B6.**
```java
var list = List.of(1, 2, 3, 4);
var out = list.stream()
              .filter(i -> i % 2 == 0)
              .map(i -> i * 10)
              .collect(Collectors.toList());
System.out.println(out);
```

**B7.**
```java
try {
    throw new RuntimeException("boom");
} catch (Exception e) {
    System.out.print("caught ");
} finally {
    System.out.println("finally");
}
```

**B8.**
```java
String s = null;
System.out.println(s instanceof String);
```

**B9.**
```java
List<String> names = new ArrayList<>(List.of("b", "a", "c"));
names.sort(Comparator.reverseOrder());
System.out.println(names);
```

**B10.**
```java
class Box<T> {
    private T value;
    void set(T v) { value = v; }
    T get() { return value; }
}
Box<?> b = new Box<String>();
b.set("x");
```

---

## PHẦN C — 3 bài viết code (30 điểm, 20 phút/bài)

Được xem Java API docs. **Không AI.** Viết code chạy được, có `main` để tự test.

### C1 — OOP + interface + sắp xếp
Viết:
- `interface Shape { double area(); String name(); }`
- `Circle(double r)`, `Rectangle(double w, double h)` implement `Shape`
- `static List<Shape> sortedByArea(List<Shape> shapes)` trả về list mới, sắp xếp tăng dần theo `area()`
- `main`: tạo 1 circle bán kính 2, 1 rectangle 3×4, in ra theo thứ tự đã sắp xếp kèm tên và diện tích.

**Yêu cầu thêm:** giải thích tại sao dùng `interface` thay vì abstract class ở đây (2–3 câu).

### C2 — Collections + Generics + Streams
Cho:
```java
record Employee(String name, String dept, double salary) {}
```
Viết các method:
1. `Map<String, Double> avgSalaryByDept(List<Employee> es)` — lương trung bình mỗi phòng.
2. `Map<String, Employee> topEarnerByDept(List<Employee> es)` — người lương cao nhất mỗi phòng.
3. `List<String> namesSortedBySalaryDesc(List<Employee> es)` — tên, sắp theo lương giảm dần.

**Yêu cầu:** dùng Stream API. Xử lý trường hợp list rỗng. Giải thích: nếu 2 người cùng phòng cùng lương cao nhất thì `topEarnerByDept` của em xử lý thế nào?

### C3 — Exception + I/O + concurrency
Viết:
1. `class EmptyFileException extends Exception` (checked).
2. `static Map<String, Integer> wordCount(Path p) throws IOException, EmptyFileException` — đọc file text (UTF-8), đếm số lần xuất hiện của từng từ (tách theo khoảng trắng, chuyển lowercase, bỏ dấu câu đơn giản). Nếu file rỗng → ném `EmptyFileException`. Dùng try-with-resources.
3. `class SafeCounter` có `void inc()` và `long value()`, an toàn khi nhiều thread cùng gọi. Giải thích tại sao chọn cách đó.

---

## TỰ KIỂM TRA SAU KHI LÀM

- [ ] Đã làm đủ 90 phút, không mở Google/AI?
- [ ] Đã ghi đáp án ra giấy trước khi mở `09_answer_key.md`?
- [ ] Đã tự chấm theo rubric ở `00_README.md` mục 2?
- [ ] Đã ghi mức L vào `01_skills_matrix.csv`?

**Câu hỏi tự vấn sau khi chấm:** câu nào sai mà "à, mình biết mà quên" → chỉ cần ôn lại; câu nào sai mà "mình chưa từng hiểu" → phải học lại từ gốc. Hai loại này có lộ trình khác nhau hoàn toàn.
