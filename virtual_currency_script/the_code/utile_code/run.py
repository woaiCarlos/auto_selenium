import os
import subprocess
import time


def run(filepath):
    # path = f'the_code/data/{filepath}'
    folder_path = 'the_code/data'  # 将此替换为你要列出文件的文件夹路径
    # 使用os.listdir获取文件夹中的所有文件和子文件夹名称
    for filename in os.listdir(folder_path):
        if filename == '模板.yaml':
            continue
        # 使用os.path.join连接文件夹路径和文件名，并使用os.path.isfile检查它是否是文件
        if os.path.isfile(os.path.join(folder_path, filename)):
            result = subprocess.run(['python', 'json_operation.py', f'data/{filename}'])
