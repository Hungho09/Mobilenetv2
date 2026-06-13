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
├── ai-engine/              # Python (MobileNetV2 và xử lý ảnh)
│   ├── mobilenet_v2.py     # Kiến trúc mô hình
│   └── requirements.txt    # Thư viện AI cần thiết
├── backend/                # Java Spring Boot / Node.js (NestJS)
├── frontend-web/           # Angular Web App
├── frontend-mobile/        # Flutter Mobile App
├── infrastructure/         # Docker, Nginx, CI/CD
├── docs/                   # Sơ đồ Database, API Spec
├── .gitignore              # Git configuration
└── LICENSE                 # MIT License
```

---

## 🚀 Hướng dẫn Chạy & Kiểm thử (Setup & Testing)

Dưới đây là các bước chi tiết để bạn có thể cài đặt và kiểm tra từng thành phần của dự án.

### ⚡ Chạy nhanh (Quick Start)
Nếu bạn muốn khởi động nhanh toàn bộ hệ thống, hãy thực hiện:

| Thành phần | Lệnh thực thi | Cửa sổ Terminal |
| :--- | :--- | :--- |
| **1. Backend** | `cd backend && npm install express cors && node index.js` | Terminal 1 |
| **2. Frontend** | `python3 -m http.server 8080 --directory frontend-web` | Terminal 2 |
| **3. AI Engine** | `cd ai-engine && pip install -r requirements.txt && python mobilenet_v2.py` | Terminal 3 |
| **4. Toàn bộ (Docker)** | `docker-compose -f infrastructure/docker-compose.yml up --build` | 1 Terminal duy nhất |

---

### 🧠 1. AI Engine (Kiểm tra kiến trúc MobileNetV2)
Thành phần này được viết bằng Python và PyTorch để mô phỏng lại kiến trúc mạng nơ-ron.

**Các bước thực hiện:**
1. Di chuyển vào thư mục `ai-engine`:
   ```bash
   cd ai-engine
   ```
2. Cài đặt các thư viện cần thiết:
   ```bash
   pip install -r requirements.txt
   ```
3. Chạy script kiểm thử kiến trúc:
   ```bash
   python mobilenet_v2.py
   ```
   *Kết quả mong đợi:* Màn hình hiển thị "Kiến trúc MobileNetV2 đã hoàn thành".

---

### ⚙️ 2. Backend API (Cung cấp dữ liệu hệ thống)
Backend được xây dựng bằng Node.js để quản lý thông tin và trạng thái của mô hình AI.

**Các bước thực hiện:**
1. Mở một Terminal mới và di chuyển vào thư mục `backend`:
   ```bash
   cd backend
   ```
2. Cài đặt các thư viện cần thiết:
   ```bash
   npm install express cors
   ```
3. Khởi chạy server:
   ```bash
   node index.js
   ```
   *Kết quả mong đợi:* Terminal báo `Backend listening at http://localhost:3000`.

---

### 🌐 3. Frontend Web (Giao diện người dùng)
Giao diện Web giúp bạn trải nghiệm nhận diện khuôn mặt và kết nối trực tiếp với Backend.

**Các bước thực hiện:**
1. Mở một Terminal mới (khác với terminal chạy Backend) và đảm bảo bạn đang ở thư mục gốc của dự án.
2. Chạy server ảo cho Frontend:
   ```bash
   python3 -m http.server 8080 --directory frontend-web
   ```
3. Truy cập trình duyệt: [http://localhost:8080](http://localhost:8080)
   *Kết quả mong đợi:* Giao diện hiện ra, Camera hoạt động và phần "Backend Status" sẽ hiển thị trạng thái **Online** màu xanh.

---

### 🐳 4. Chạy với Docker (Khuyên dùng - Nhanh nhất)
Nếu bạn có Docker, đây là cách đơn giản nhất để chạy toàn bộ hệ thống cùng lúc mà không cần mở nhiều Terminal.

1. Tại thư mục gốc của dự án, chạy lệnh:
   ```bash
   docker-compose -f infrastructure/docker-compose.yml up --build
   ```
2. Sau khi build xong, truy cập: [http://localhost](http://localhost) (Nginx sẽ tự động điều phối cả Frontend và Backend).

---

### 🧪 4. Quy trình Kiểm thử (Testing Workflow)
- **Unit Test (Model):** Đảm bảo rằng việc thay đổi thông số `width_mult` trong `mobilenet_v2.py` vẫn cho ra output đúng định dạng.
- **Integration Test:** Kiểm tra khả năng kết nối giữa Camera và thư viện `face-api.js` trên giao diện Web.

---

## 📑 Các khái niệm khoa học chủ chốt

1. **Inverted Residuals:** Thay vì "Rộng -> Hẹp -> Rộng", chúng tôi dùng "Hẹp -> Rộng -> Hẹp" để tiết kiệm bộ nhớ khi lan truyền ngược.
2. **Linear Bottlenecks:** Loại bỏ hàm kích hoạt phi tuyến tính ở lớp hẹp cuối của mỗi khối để tránh mất mát thông tin đặc trưng (Manifold Collapse).
3. **ReLU6:** Ngăn chặn các kích hoạt quá lớn, giúp mô hình ổn định hơn khi chạy trên các hệ thống số nguyên 8-bit hoặc di động ít tài nguyên.

---

## ✍️ Tác giả & Tham khảo

- **Tác giả:** [Hồ SỸ Mạnh Hùng]
- **Nguồn:** Theo bài báo *"MobileNetV2: Inverted Residuals and Linear Bottlenecks"* (Sandler, Howard, et al. - Google Inc.)

---

## 📄 Giấy phép (License)
Dự án được phát hành dưới giấy phép **MIT**. Xem file `LICENSE` để biết thêm chi tiết.
