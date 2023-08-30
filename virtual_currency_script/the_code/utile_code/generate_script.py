import pandas as pd
import yaml
import copy
import os
import glob

grandparent_directory = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + f'/the_code/data/'


def check_yaml_muban(folder_path):
    try:
        # Using os.path.join to concatenate the folder path and the file extension
        all_yaml_files = glob.glob(os.path.join(folder_path, "*.yaml"))
    except Exception as e:
        return [False, 0]

    # Exclude "模板.yaml"
    filtered_yaml_files = [file for file in all_yaml_files if os.path.basename(file) != "模板.yaml"]

    if filtered_yaml_files:
        return [True, len(filtered_yaml_files)]
    else:
        return [False, 0]
