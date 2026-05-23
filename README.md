# YOLO 简单应用

> 轻量级目标检测算法，快速训练与推理

---

## 简介

YOLO（You Only Look Once）是一种高效的目标检测算法，能够实时检测图像中的目标物体。本项目提供目标检测完整的训练与推理流程，帮助你快速上手 YOLO目标检测。

---

## 目录结构

```
yolo_demo/
├── 📁 datasets/           # 数据集目录，包含训练集和验证集
│   ├── 📁 train/          # 训练集目录（自动生成）
│   └── 📁 val/            # 验证集目录（自动生成）
├── 📁 images/             # 未标注图像目录（将原始图像放在这里）
├── 📁 run/                # 训练/推理结果目录（自动生成）
├── 📄 dataset.yaml        # 数据集配置文件
├── 📄 dataset.py          # 数据集处理脚本
├── 📄 train.py            # 模型训练脚本
├── 📄 requirements.txt    # 项目依赖文件
└── 📄 README.md           # 项目介绍文档
```

---

## 准备工作

### 1️⃣ 安装依赖

```bash
pip install -r requirements.txt
```

### 2️⃣ 数据集处理

| 步骤 | 操作 | 说明 |
|------|------|------|
| 1 | 放置图像 | 将原始图像放入 `images/` 目录 |
| 2 | 重命名图像 | 运行 `dataset.py` 中的 `dateset_rename` 函数，确保文件名唯一 |
| 3 | 图像标注 | 使用 `labelme` 工具标注图像 |

#### 标注步骤

```bash
# 启动 labelme 标注工具
labelme ./images/ --output ./labelme_output/
```

> 标注完成后，JSON 文件会自动保存在 `./labelme_output/` 目录

#### 转换格式

将 JSON 标注文件转换为 YOLO 格式：

```bash
labelme2yolo --json_dir ./labelme_output/ --val_size 0.15 --test_size 0.15
```

---

## 自动标注（进阶）

当标注数据达到一定规模后，可使用模型自动标注未标注的图像：

```
1️⃣  使用 labelme 标注至少 10 张图像
2️⃣  修改 train.py 中的 data 参数，指向 dataset.yaml
3️⃣  训练模型
    python train.py
4️⃣  模型保存至 run/ 目录后，运行自动标注
    python dataset.py
```

> 自动标注完成后，会在当前目录生成新的 `dataset.yaml` 文件

---

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 数据集处理
python dataset.py rename --path ./images/

# 开始训练
python train.py --data_path ./labelme_output/YOLODataset/dataset.yaml

# 自动标注
python dataset.py auto_label --model_path runs/detect/train/weights/best.pt --image_path ./images/
```
