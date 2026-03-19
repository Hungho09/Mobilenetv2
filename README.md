# MobileNetV2: Face Recognition AI Experience 📱🤖

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Face-API.js](https://img.shields.io/badge/Model-MobileNetV2-brightgreen.svg)](https://arxiv.org/abs/1801.04381)

Một dự án nghiên cứu và ứng dụng thực tế về thuật toán **MobileNetV2**, tập trung vào nhận diện khuôn mặt thời gian thực với hiệu suất cực cao trên thiết bị di động. Dự án bám sát bài báo khoa học: *"MobileNetV2: Inverted Residuals and Linear Bottlenecks"*.

---

## 🌟 Tính năng nổi bật (Features)

- **Kiến trúc Cốt lõi (Core Architecture):** Triển khai chính xác MobileNetV2 từ scratch bằng PyTorch (Inverted Residuals, Linear Bottlenecks, ReLU6).
- **Nhận diện Thời gian thực (Real-time AI):** Ứng dụng Web sử dụng `face-api.js` (MobileNet backbone) để nhận diện khuôn mặt, điểm mốc (landmarks) và cảm xúc qua Camera.
- **Tối ưu hóa Di động (Mobile Optimization):** Sử dụng các kỹ thuật tích chập tách biệt chiều sâu (Depthwise Separable Convolutions) giảm 10x tham số so với VGG-16.
- **Giao diện Hiện đại (Modern UI):** Thiết kế Glassmorphism cao cấp, mang lại trải nghiệm người dùng mượt mà.

---

## 📁 Cấu trúc Dự án (Project Structure)

```text
mobilenetv2-face-recognition/
├── core/                   # Triển khai thuật toán chính (Python/PyTorch)
│   └── mobilenet_v2.py     # Mô hình kiến trúc chi tiết (Table 1 & 2)
├── web-app/                # Ứng dụng web thực tế (Front-end)
│   ├── index.html          # Cấu trúc ứng dụng & SEO
│   ├── index.css           # Giao diện Premium & Animations
│   └── script.js           # Logic xử lý AI & Camera
├── docs/                   # Tài liệu hướng dẫn và lý thuyết
│   └── paper_summary.md    # Tóm tắt bài báo MobileNetV2
├── requirements.txt        # Các thư viện Python cần thiết
├── .gitignore              # Các file bỏ qua khi up lên GitHub
└── LICENSE                 # Giấy phép MIT
```

---

## 🚀 Hướng dẫn Sử dụng (Quick Start)

### 1. Trải nghiệm Ứng dụng Web
Không cần cài đặt phức tạp, bạn chỉ cần mở file `web-app/index.html` bằng trình duyệt (Chrome/Edge khuyến nghị) và cấp quyền Camera.

### 2. Chạy Mô hình Python (Nghiên cứu)
Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```
Kiểm tra kiến trúc mô hình:
```bash
python core/mobilenet_v2.py
```

---

## 📑 Các khái niệm khoa học chủ chốt

1. **Inverted Residuals:** Thay vì "Rộng -> Hẹp -> Rộng", chúng tôi dùng "Hẹp -> Rộng -> Hẹp" để tiết kiệm bộ nhớ khi lan truyền ngược.
2. **Linear Bottlenecks:** Loại bỏ hàm kích hoạt phi tuyến tính ở lớp hẹp cuối của mỗi khối để tránh mất mát thông tin đặc trưng (Manifold Collapse).
3. **ReLU6:** Ngăn chặn các kích hoạt quá lớn, giúp mô hình ổn định hơn khi chạy trên các hệ thống số nguyên 8-bit hoặc di động ít tài nguyên.

---

## ✍️ Tác giả & Tham khảo

- **Tác giả:** [Tên của bạn]
- **Nguồn:** Theo bài báo *"MobileNetV2: Inverted Residuals and Linear Bottlenecks"* (Sandler, Howard, et al. - Google Inc.)

---

## 📄 Giấy phép (License)
Dự án được phát hành dưới giấy phép **MIT**. Xem file `LICENSE` để biết thêm chi tiết.
