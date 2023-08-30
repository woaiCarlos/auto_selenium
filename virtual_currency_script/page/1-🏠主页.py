import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.sidebar.success("Select a demo above.")

st.title('Selenium自动化区块链交易')

st.markdown(
"""
---
### 简介
这个平台使用Selenium自动化执行区块链交易任务。
---
### 特点
- 自动执行买入和卖出订单
- 使用Selenium进行API交互
---
### 好处
- 节省时间：自动化交易流程
- 提高准确性：减少人为错误
- 遵守标准：确保所有操作符合预设指导方针
---
### 总结
如果你正在寻找一个可靠且有效的解决方案进行自动化区块链交易，这个基于Selenium的平台是你的理想选择。
"""
)


