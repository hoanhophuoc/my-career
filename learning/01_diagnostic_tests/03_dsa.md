# T3 — DSA (120 phút · 12 phút/bài · KHÔNG AI)

**Quy tắc:** không Google, không AI, không xem lời giải. Được dùng giấy nháp.
Với mỗi bài, ghi: **(1)** ý tưởng bằng 2–3 câu · **(2)** độ phức tạp thời gian/bộ nhớ · **(3)** code chạy được · **(4)** test với ví dụ cho sẵn.
Ngôn ngữ: Java (đúng stack mục tiêu).

> **Cách chấm:** không phải "giải được bài khó" mà là "nhận ra **pattern** trong 3 phút đầu". Ghi lại bài nào em nhận ra pattern ngay, bài nào phải mò — đó mới là dữ liệu cho lộ trình.

---

## Nhóm 1 — Array / Hash (bài 1–3)

**Bài 1 — Two Sum.** Cho mảng `int[] nums` và `int target`. Trả về **chỉ số** của 2 phần tử có tổng bằng `target`. Giả định có đúng 1 đáp án, không dùng cùng 1 phần tử 2 lần.
`nums = [2,7,11,15], target = 9` → `[0,1]`
Kỳ vọng: O(n) thời gian, O(n) bộ nhớ.

**Bài 2 — Valid Parentheses.** Cho chuỗi chỉ gồm `()[]{}`. Xác định chuỗi có hợp lệ (mở/đóng đúng thứ tự) không.
`"()[]{}"` → true · `"(]"` → false · `"([)]"` → false
Kỳ vọng: O(n) thời gian, O(n) bộ nhớ.

**Bài 3 — Group Anagrams.** Cho `String[] words`, nhóm các từ là anagram của nhau.
`["eat","tea","tan","ate","nat","bat"]` → `[[eat,tea,ate],[tan,nat],[bat]]` (thứ tự nhóm không quan trọng)
Kỳ vọng: O(n·k log k) hoặc O(n·k) với k = độ dài từ.

## Nhóm 2 — Two pointers / Sliding window (bài 4–5)

**Bài 4 — Best Time to Buy and Sell Stock.** Cho `int[] prices`, `prices[i]` là giá ngày i. Chọn 1 ngày mua và 1 ngày bán **sau đó** để lợi nhuận lớn nhất. Trả về lợi nhuận (0 nếu không có lãi).
`[7,1,5,3,6,4]` → `5`
Kỳ vọng: O(n), O(1) bộ nhớ.

**Bài 5 — Longest Substring Without Repeating Characters.** Cho `String s`, tìm độ dài chuỗi con dài nhất không có ký tự lặp.
`"abcabcbb"` → `3` (`"abc"`) · `"pwwkew"` → `3` (`"wke"`)
Kỳ vọng: O(n).

## Nhóm 3 — Stack / Linked list (bài 6)

**Bài 6 — Reverse Linked List.** Đảo ngược một singly linked list, trả về head mới. Viết **cả hai cách**: lặp và đệ quy.
`1→2→3→null` → `3→2→1→null`
Kỳ vọng: O(n) thời gian, O(1) bộ nhớ với cách lặp.

## Nhóm 4 — Tree / Graph (bài 7–8)

**Bài 7 — Binary Tree Level Order Traversal.** Cho root của binary tree, trả về `List<List<Integer>>` theo từng tầng.
```
    3
   / \
  9  20
     / \
    15  7
```
→ `[[3],[9,20],[15,7]]`
Kỳ vọng: O(n). Gợi ý: nghĩ tới Queue.

**Bài 8 — Number of Islands.** Cho lưới `char[][] grid` gồm `'1'` (đất) và `'0'` (nước). Đếm số đảo (nhóm `'1'` liền kề 4 hướng).
```
11110
11010
11000
00000
```
→ `1`
Kỳ vọng: O(m·n). Viết **cả DFS và BFS**; nêu nhược điểm của DFS đệ quy với lưới lớn.

## Nhóm 5 — DP nhập môn (bài 9)

**Bài 9 — Climbing Stairs.** Có `n` bậc thang; mỗi bước đi được 1 hoặc 2 bậc. Đếm số cách lên tới bậc `n`.
`n = 2` → `2` · `n = 3` → `3`
Viết **3 cách**: đệ quy (nêu vì sao chậm), DP mảng, và DP tối ưu bộ nhớ O(1).
Kỳ vọng: O(n).

## Nhóm 6 — Heap / chọn lựa (bài 10)

**Bài 10 — Top K Frequent Elements.** Cho `int[] nums` và `int k`, trả về `k` phần tử xuất hiện nhiều nhất (thứ tự bất kỳ).
`nums = [1,1,1,2,2,3], k = 2` → `[1,2]`
Kỳ vọng: tốt hơn O(n log n). Nêu được ít nhất 2 cách (heap, bucket/counting).

---

## Bảng tự chấm (điền ngay sau khi làm)

| Bài | Pattern nhận ra trong 3' ? | Giải được? | Đúng độ phức tạp? | Ghi chú |
|---|---|---|---|---|
| 1 Two Sum | ☐ | ☐ | ☐ | |
| 2 Valid Parentheses | ☐ | ☐ | ☐ | |
| 3 Group Anagrams | ☐ | ☐ | ☐ | |
| 4 Stock | ☐ | ☐ | ☐ | |
| 5 Longest Substring | ☐ | ☐ | ☐ | |
| 6 Reverse List | ☐ | ☐ | ☐ | |
| 7 Level Order | ☐ | ☐ | ☐ | |
| 8 Islands | ☐ | ☐ | ☐ | |
| 9 Climbing Stairs | ☐ | ☐ | ☐ | |
| 10 Top K | ☐ | ☐ | ☐ | |

**Quy tắc đọc kết quả:** nếu ≥ 8/10 giải được **nhưng** chỉ nhận ra pattern ở 4–5 bài → vấn đề không phải kiến thức mà là **tốc độ nhận diện** → luyện theo pattern (Phase 4), không học thêm lý thuyết.

Nộp bài xong mới mở `09_answer_key.md` (phần DSA).
