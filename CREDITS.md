# 开源引用声明 / Open Source Credits

本项目基于以下开源组件构建，遵循各组件对应的开源许可证。

---

## 第三方开源组件 / Third-Party Open Source Components

| 组件 | 版本 | 许可证 | 用途 |
|------|------|--------|------|
| [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) | latest | AGPL-3.0 | 目标检测模型与训练框架 |
| [PyTorch](https://github.com/pytorch/pytorch) | latest | BSD-3-Clause | 深度学习框架 |
| [torchvision](https://github.com/pytorch/vision) | latest | BSD-3-Clause | 计算机视觉工具库 |
| [tqdm](https://github.com/tqdm/tqdm) | latest | MIT | 进度条显示 |
| [OpenCV](https://github.com/opencv/opencv) | latest | Apache-2.0 | 计算机视觉处理 |
| [PyYAML](https://github.com/yaml/pyyaml) | latest | MIT | YAML 配置文件解析 |
| [labelme](https://github.com/wkentaro/labelme) | latest | GPL-3.0 | 图像标注工具 |
| [labelme2yolo](https://github.com/wkentaro/labelme2yolo) | latest | GPL-3.0 | 标注格式转换工具 |

---

## 许可证说明 / License Notes

### 本项目 (YOLO Demo)
- **许可证**: MIT License
- **适用文件**: `train.py`, `dataset.py`, `README.md`, `requirements.txt`, `dataset.yaml`

### 重要提示 / Important Notice

- **Ultralytics YOLO**: 采用 AGPL-3.0 许可证。如果你修改或分发 YOLO 相关代码，需遵守 AGPL 条款
- **labelme / labelme2yolo**: 采用 GPL-3.0 许可证，确保兼容你的分发计划
- **PyTorch 生态**: 采用 BSD-3-Clause，对商业使用限制较少

---

## 预训练模型 / Pre-trained Models

本项目使用的 `yolov8s.pt` 预训练权重来自 Ultralytics。

- 模型权重遵循 [AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.en.html) 许可证
- 详细许可证信息请参阅: https://docs.ultralytics.com/

---

## 免责声明 / Disclaimer

本项目仅供学习与研究使用。各第三方组件的版权归其各自的作者/所有者所有。使用第三方组件时，请确保遵守相应的开源许可证。

---
