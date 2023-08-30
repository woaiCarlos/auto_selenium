import time

import streamlit as st
import subprocess
import glob
import pandas as pd
import yaml
import copy
import os
from streamlit_autorefresh import st_autorefresh

grandparent_directory = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + f'/the_code/data/'
run_file = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + f'/the_code/utile_code/'

if 'should_stop' not in st.session_state:
    st.session_state.should_stop = False


def run(filepath):
    for filename in os.listdir(grandparent_directory + filepath):
        if st.session_state.should_stop:
            st.session_state.should_stop = False  # 重置标志
            break  # 停止循环
        if filename == '模板.yaml':
            continue
        if os.path.isfile(os.path.join(grandparent_directory + filepath, filename)):
            result = subprocess.run(
                ['python', f'{run_file}json_operation.py', f'{grandparent_directory}/{filepath}/{filename}'])


def generateScript(xlsfile, path):
    df = pd.read_excel(xlsfile)
    key = df['钱包密钥'].tolist()
    with open(grandparent_directory + path + '/模板.yaml', 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    for i in range(len(key)):
        target_keyword = '输入密钥'
        # 创建原始数据的深度副本
        data_copy = copy.deepcopy(data)
        for step in data_copy:
            for value in step.values():
                if isinstance(value, str) and target_keyword in value:
                    step['input_text'] = key[i]
        with open(f'{grandparent_directory}{path}/{key[i]}.yaml', 'w', encoding="utf-8") as file:
            yaml.dump(data_copy, file, sort_keys=False, allow_unicode=True)
            # 一旦找到并修改了关键字，就跳出循环


def get_folder(path=''):
    file_name = os.listdir(grandparent_directory + f'{path}')
    list1 = []
    for item in os.listdir(grandparent_directory):
        item_path = os.path.join(grandparent_directory, item)
        if os.path.isdir(item_path):
            subfolder_name = os.path.basename(item_path)
            list1.append(subfolder_name)
    return [list1, file_name]


def check_excel_files(folder_path):
    os.chdir(folder_path)
    excel_files = glob.glob("*.xls") + glob.glob("*.xlsx")

    if excel_files:
        for file in excel_files:
            return [True, file]
    else:
        return [False]


def check_yaml_files(folder_path):
    os.chdir(folder_path)
    excel_files = glob.glob("模板.yaml")

    if excel_files:
        for file in excel_files:
            return [True, file]
    else:
        return [False]


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


st.set_page_config(page_title="平台列表V1.0.0", page_icon="💼", layout='wide')
st.markdown("# 平台列表V1.0.0 👋")

# 在侧边栏中添加文件选择组件
with st.sidebar:
    selected_option = st.selectbox("选择平台：", ['--选择平台--'] + get_folder()[0], index=0, key="selectbox2")

if selected_option != '--选择平台--':

    # st.write(selected_option + check_excel_files(grandparent_directory + selected_option))
    if check_excel_files(grandparent_directory + selected_option)[0]:
        data_path = grandparent_directory + selected_option + '/' + \
                    check_excel_files(grandparent_directory + selected_option)[
                        1]
        st.markdown(
            '平台' + selected_option + f'配置文件 : {check_excel_files(grandparent_directory + selected_option)[1]}')
        df = pd.read_excel(data_path)
        print(data_path)
        st.dataframe(df)
        with st.expander("根据配置文件生成脚本"):
            col1, col2 = st.columns(2)
            with col1:
                result = check_yaml_muban(grandparent_directory + selected_option)
                if result:
                    run_thread = None
                    st.write(f'脚本数量:{result[1]}')
                    button_run = st.button('运行脚本')
                    if button_run:
                        run(selected_option)
                    button_stop = st.button('停止运行')
                    if button_stop:
                        st.session_state.should_stop = True
            with col2:
                if check_yaml_files(grandparent_directory + selected_option)[0]:
                    st.write('找到配置文件')
                    jiaoben = st.button('生成脚本', key='112233')
                    if jiaoben:
                        generateScript(data_path, selected_option)
                        st.success('脚本生成成功')
                        st_autorefresh()
                else:
                    st.write('没有脚本模板,请添加脚本模板')
                    uploaded_file = st.file_uploader("上传脚本模板", type=["yaml"])
                    if uploaded_file is not None:
                        file_name = os.path.join(grandparent_directory + selected_option, uploaded_file.name)
                        with open(file_name, "wb") as f:
                            f.write(uploaded_file.getbuffer())
                        placeholder = st.empty()
                        placeholder.success(f"配置文件上传成功!")
                        time.sleep(2)
                        placeholder.empty()
                        st_autorefresh()
    else:
        st.write('平台' + selected_option + '没有找到配置文件,请在平台管理中添加配置文件')
