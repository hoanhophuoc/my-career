#!/usr/bin/env bash
# Xuất một BẢN SẠCH của pack: 1 commit, không lịch sử, không dữ liệu cục bộ.
# Dùng khi muốn tạo repo công khai để làm portfolio. KHÔNG tự push.
#
#   bash tools/make_clean_export.sh
#   → dist_clean/my-career/   (đã git init + 1 commit)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${ROOT}/dist_clean/my-career"

# Giữ lại remote đã cấu hình (nếu có) để lần xuất sau push tiếp được
REMOTE_URL="$(git -C "${DEST}" remote get-url origin 2>/dev/null || true)"

rm -rf "${DEST}"
mkdir -p "${DEST}"

# Chỉ lấy file đang được theo dõi; .local_private/ và config.local.json không bao giờ nằm trong đó.
cd "${ROOT}"
git ls-files -z | while IFS= read -r -d '' f; do
  mkdir -p "${DEST}/$(dirname "$f")"
  cp -p "$f" "${DEST}/$f"
done

cd "${DEST}"
git init -q
if [ -n "${REMOTE_URL}" ]; then git remote add origin "${REMOTE_URL}"; fi
git add -A
# Danh tính PHẢI là email noreply của tài khoản hoanhophuoc; email cá nhân sẽ bị GitHub
# gán cho một tài khoản lạ và hiện sai trong Contributors.
git -c user.name="Hồ Phước Hoàn" -c user.email="89370644+hoanhophuoc@users.noreply.github.com" commit -q -m "Career pack — bản xuất sạch (không lịch sử)"

echo "Xong: ${DEST}"
echo "Kiểm tra trước khi tạo repo công khai:  python3 tools/scan_pii.py  (trong thư mục pack gốc)"
echo "Cập nhật bản public:  git -C \"${DEST}\" push --force origin main  (script này KHÔNG tự push)."
