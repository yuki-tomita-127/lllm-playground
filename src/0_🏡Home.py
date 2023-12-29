import streamlit as st

from utils.setting_file_loader import SettingFileLoader


if "setting_file_loader" not in st.session_state:
    st.session_state.setting_file_loader = SettingFileLoader()


content = """
# LLLM PlayGround
## ✨About
This space is...

## 💬Chat
Chat page is...

## 💾Dataset
Dataset page is...

## ⚙️Settings
Settings page is...
"""

st.markdown(content)
