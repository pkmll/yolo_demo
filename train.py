import torch
from ultralytics import YOLO

import argparse
if __name__ == "__main__":
    device = "cuda" if torch.cuda.is_available() else "cpu"  # 设置设备
    model = YOLO("yolov8s.yaml").load(r"yolov8s.pt")        # 加载模型配置，并加载预训练权重
    model.to(device)  # 加载到设备
    parser = argparse.ArgumentParser(description='训练模型')
    parser.add_subparsers('--data_path', type=str, default='dataset.yaml', 
                               help='数据集配置路径')
    parser.add_argument('--epochs', type=int, default=1000, help='训练轮数')
    parser.add_argument('--imgsz', type=int, default=640, help='图片尺寸')
    parser.add_argument('--workers', type=int, default=4, help='加载数据的线程数')
    parser.add_argument('--batch', type=int, default=8, help='批处理大小')
    parser.add_argument('--device', type=str, default=device, help='训练设备')
    parser.add_argument('--augment', action='store_true', help='数据增强')
    args = parser.parse_args()

    results = model.train(
        data=args.data_path,    # 数据集路径
        epochs=args.epochs,     # 训练轮数
        imgsz=args.imgsz,       # 图片尺寸
        workers=args.workers,   # 加载数据的线程数
        batch=args.batch,       # 批处理大小
        device=args.device,     # 训练设备
        flipud=0.2,             # 上下翻转概率
        fliplr=0.5,             # 左右翻转概率
        mosaic=0.8,             # Mosaic 概率
        mixup=0.1,              # Mixup 概率
        augment=args.augment,   # 数据增强
    )