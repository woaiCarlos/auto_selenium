import streamlit as st
import os

import pandas as pd
import requests
import requests as re
from streamlit_autorefresh import st_autorefresh
import json, time
import glob

import asyncio
import streamlit.components.v1 as components



grandparent_directory = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + f'/the_code/data/'


def check_excel_files(folder_path):
    os.chdir(folder_path)
    excel_files = glob.glob("*.xls") + glob.glob("*.xlsx")

    if excel_files:
        for file in excel_files:
            return [True, file]
    else:
        return [False]


def get_folder(path=''):
    file_name = os.listdir(grandparent_directory + f'{path}')
    list1 = []
    for item in os.listdir(grandparent_directory):
        item_path = os.path.join(grandparent_directory, item)
        if os.path.isdir(item_path):
            subfolder_name = os.path.basename(item_path)
            list1.append(subfolder_name)
    return [list1, file_name]


def mkdir(dir=' '):
    if os.path.exists(grandparent_directory + f'{dir}'):
        st.warning('⚠️平台已存在!')
    else:
        os.makedirs(grandparent_directory + f'{dir}')
        st.success(f"✅创建成功{platform_name}")
        st_autorefresh()


st.set_page_config(page_title="平台管理V1.0.0", page_icon="💼", layout='wide')
st.markdown("# 平台管理V1.0.0 👋")
col1, col2 = st.columns(2)
with col1:
    selected_option = st.selectbox("选择平台：", ['--选择平台--'] + get_folder()[0], index=0,key="selectbox1")
with col2:
    platform_name = st.text_input('输入要创建的平台名称:')
    platform_name1 = platform_name.strip()
    platform_name2 = platform_name1.replace(" ", "")
    print(platform_name2)
    # 检查输入框是否有值，并据此设置按钮的 disabled 状态
    creat_pingtai = st.button("创建平台", disabled=not bool(platform_name2))
    if creat_pingtai:
        mkdir(platform_name2)

disable_upload = True if selected_option == '--选择平台--' else False
if selected_option == '--选择平台--' or check_excel_files(grandparent_directory + selected_option)[0] == True:
    disable_upload = True
else:
    disable_upload = False
# 上传 XLS 文件
uploaded_file = st.file_uploader("上传脚本文件", type=["xls", "xlsx"], disabled=disable_upload)
if selected_option != '--选择平台--' and check_excel_files(grandparent_directory + selected_option)[0] == False:
    if uploaded_file is not None:
        file_name = os.path.join(grandparent_directory + selected_option, uploaded_file.name)
        with open(file_name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        placeholder = st.empty()
        placeholder.success(f"配置文件上传成功!")
        time.sleep(2)
        placeholder.success(f"文件位置: {file_name}!")
        time.sleep(2)
        placeholder.success("上传成功后请添加脚本模板!")
        time.sleep(5)
        placeholder.empty()
elif selected_option != '--选择平台--' and check_excel_files(grandparent_directory + selected_option)[0] == True:
    placeholder1 = st.empty()
    placeholder1.error('此平台已有配置文件')
    time.sleep(2)
    placeholder1.empty()
