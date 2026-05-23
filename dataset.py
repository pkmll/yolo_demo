import os
import torch
from tqdm import tqdm
import shutil
import argparse

from ultralytics import YOLO
from ultralytics.data.split import autosplit
import yaml

def dateset_rename(dir_path:str="dataset/image")->bool:
    """数据重命名

    :param dir_path str: 数据集路径(包含图片的文件夹路径)
    :return bool: 是否成功
    """
    dir_path = os.path.join(os.getcwd(), dir_path)
    if not os.path.exists(dir_path) or len(os.listdir(dir_path))==0:
        print("数据目录不存在或为空")
        return False
    for i, filename in enumerate(tqdm(os.listdir(dir_path))):
        old_name = os.path.join(dir_path, filename)
        new_name = os.path.join(dir_path, f'{i:07d}.png')
        tqdm.write(f'Renaming {old_name} to {new_name}')
        shutil.move(old_name, new_name)
    return True


def dataset_auto_label(model_path:str="best.pt", image_path:str="dataset",weights=(0.8, 0.15, 0.05),device="cuda" if torch.cuda.is_available() else "cpu",conf=0.01,iou=0.1)->str:
    """自动标注，自动生成yaml文件

    :param model_path str: 用于自动标注的模型文件路径
    :param image_path str: 准备标注的数据集路径
    :param weights tuple: 训练集、验证集、测试集比例
    :param device str: 使用的设备["cuda","cpu"]
    :param conf float: 置信度阈值, 模型判断检测物体的置信度，越大越严格，conf=0.01表示模型判断的置信度大于0.01的物体才会被认为是目标
    :param iou float: iou阈值，模型判断检测物体的重叠程度，越小越严格，iou=0.1表示重叠程度大于0.1的物体会被判定为同一个物体
    :return str: {{image_path}}.yaml文件绝对路径
    """
    model = YOLO(model_path)
    model.to(device)
    results = model.predict(source=os.path.join(image_path, "images"), save_txt=True, conf=conf,iou=iou, device=device)
    shutil.copytree(os.path.join(results[0].save_dir,"labels"), os.path.join(image_path, "labels"), dirs_exist_ok=True)
    # split dataset
    autosplit(path=image_path, weights=weights, annotated_only=True)
    yaml_data = {
        "path": os.getcwd(),
        "train": "autosplit_train.txt",
        "val": "autosplit_val.txt",
        "test": "autosplit_test.txt",
        "names": list(results[0].names.values())
    }

    with open(f"{image_path}.yaml", "w") as f:
        yaml.dump(yaml_data, f)

    return os.path.join(os.getcwd(), f"{image_path}.yaml")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='数据集处理工具')
    subparsers = parser.add_subparsers(dest='command', help='子命令', required=True)
    
    # rename 子命令
    parser_rename = subparsers.add_parser('rename', help='数据重命名')
    parser_rename.add_argument('--path', type=str, default='dataset/image', 
                               help='图片目录路径')
    
    # auto_label 子命令
    parser_auto = subparsers.add_parser('auto_label', help='自动标注')
    parser_auto.add_argument('--model_path', type=str, 
                             default=r'runs\detect\train\weights\best.pt',
                             help='模型权重路径')
    parser_auto.add_argument('--image_path', type=str, default='dataset',
                             help='数据集路径')
    
    args = parser.parse_args()
    
    if args.command == 'rename':
        # 使用 args.path
        dateset_rename(dir_path=args.path)
        
    elif args.command == 'auto_label':
        # 使用 args.model_path 和 args.data_path
        dataset_auto_label(model_path=args.model_path, data_path=args.image_path)
        
    else:
        parser.print_help()