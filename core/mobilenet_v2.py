import torch
import torch.nn as nn
import math

def _make_divisible(v, divisor, min_value=None):
    """
    Điều chỉnh số lượng kênh để chia hết cho divisor.
    Tham khảo: https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/mobilenet.py
    """
    if min_value is None:
        min_value = divisor
    new_v = max(min_value, int(v + divisor / 2) // divisor * divisor)
    # Đảm bảo việc làm tròn không làm giảm số lượng kênh quá 10%
    if new_v < 0.9 * v:
        new_v += divisor
    return new_v

class ConvBNReLU(nn.Sequential):
    def __init__(self, in_planes, out_planes, kernel_size=3, stride=1, groups=1):
        padding = (kernel_size - 1) // 2
        super(ConvBNReLU, self).__init__(
            nn.Conv2d(in_planes, out_planes, kernel_size, stride, padding, groups=groups, bias=False),
            nn.BatchNorm2d(out_planes),
            nn.ReLU6(inplace=True)
        )

class InvertedResidual(nn.Module):
    """
    Inverted Residual Block (Bảng 1 trong bài báo)
    Gồm 3 bước chính:
    1. Expansion (1x1 Conv + ReLU6): Mở rộng kích thước kênh dựa trên expansion factor 't'.
    2. Depthwise Convolution (3x3 Dwise + ReLU6): Lọc đặc trưng nhẹ.
    3. Linear Bottleneck (1x1 Conv Linear): Giảm chiều dữ liệu về bottleneck, không dùng non-linearity để bảo toàn thông tin.
    """
    def __init__(self, inp, oup, stride, expand_ratio):
        super(InvertedResidual, self).__init__()
        self.stride = stride
        assert stride in [1, 2]

        hidden_dim = int(round(inp * expand_ratio))
        self.use_res_connect = self.stride == 1 and inp == oup

        layers = []
        if expand_ratio != 1:
            # 1. Expansion (1x1 pointwise convolution)
            layers.append(ConvBNReLU(inp, hidden_dim, kernel_size=1))
        
        layers.extend([
            # 2. Depthwise Convolution (3x3)
            ConvBNReLU(hidden_dim, hidden_dim, stride=stride, groups=hidden_dim),
            # 3. Linear Bottleneck (1x1 pointwise convolution, linear)
            nn.Conv2d(hidden_dim, oup, 1, 1, 0, bias=False),
            nn.BatchNorm2d(oup),
        ])
        self.conv = nn.Sequential(*layers)

    def forward(self, x):
        if self.use_res_connect:
            return x + self.conv(x)
        else:
            return self.conv(x)

class MobileNetV2(nn.Module):
    """
    Kiến trúc MobileNetV2 (Bảng 2 trong bài báo)
    """
    def __init__(self, num_classes=1000, width_mult=1.0):
        super(MobileNetV2, self).__init__()
        block = InvertedResidual
        input_channel = 32
        last_channel = 1280
        
        # Cấu hình kiến trúc (Bảng 2: t, c, n, s)
        # t: expansion factor, c: output channels, n: repeat times, s: stride của layer đầu tiên
        self.interverted_residual_setting = [
            [1, 16, 1, 1],
            [6, 24, 2, 2],
            [6, 32, 3, 2],
            [6, 64, 4, 2],
            [6, 96, 3, 1],
            [6, 160, 3, 2],
            [6, 320, 1, 1],
        ]

        # Xây dựng layer đầu tiên
        input_channel = _make_divisible(input_channel * width_mult, 8)
        self.last_channel = _make_divisible(last_channel * max(1.0, width_mult), 8)
        features = [ConvBNReLU(3, input_channel, stride=2)]
        
        # Xây dựng các Inverted Residual Blocks
        for t, c, n, s in self.interverted_residual_setting:
            output_channel = _make_divisible(c * width_mult, 8)
            for i in range(n):
                stride = s if i == 0 else 1
                features.append(block(input_channel, output_channel, stride, expand_ratio=t))
                input_channel = output_channel
        
        # Xây dựng layer cuối (Table 2 cuối trang 5: 1x1 conv 1280)
        features.append(ConvBNReLU(input_channel, self.last_channel, kernel_size=1))
        
        # Chuyển list features thành nn.Sequential
        self.features = nn.Sequential(*features)

        # Xây dựng bộ phân loại (Classifier)
        self.classifier = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(self.last_channel, num_classes),
        )

        # Khởi tạo trọng số (Weight initialization)
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out')
                if m.bias is not None:
                    nn.init.zeros_(m.bias)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.ones_(m.weight)
                nn.init.zeros_(m.bias)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)
                nn.init.zeros_(m.bias)

    def forward(self, x):
        x = self.features(x)
        # Global Average Pooling (7x7 avgpool trong Table 2)
        x = x.mean([2, 3])
        x = self.classifier(x)
        return x

def mobilenet_v2(num_classes=1000, width_mult=1.0):
    return MobileNetV2(num_classes=num_classes, width_mult=width_mult)

if __name__ == "__main__":
    # Test mô hình với giá trị giả định (Dummy input)
    model = mobilenet_v2()
    test_input = torch.randn(1, 3, 224, 224)
    output = model(test_input)
    print(f"Kiến trúc MobileNetV2 đã hoàn thành.")
    print(f"Kích thước tensor đầu vào: {test_input.size()}")
    print(f"Kích thước tensor đầu ra: {output.size()}")
