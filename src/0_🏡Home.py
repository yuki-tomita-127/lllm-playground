import streamlit as st

from utils.setting_file_loader import SettingFileLoader


if "setting_file_loader" not in st.session_state:
    st.session_state.setting_file_loader = SettingFileLoader()


content = """
# LLLM PlayGround
## ✨About
This space is...

## 🔎Research
Reseach page is...

## 💾Dataset
Dataset page is...

## 👍Eval
Eval page is...

## 🏆LeaderBoard
LeaderBoard page is...

## 💬Chat
Chat page is...
"""

st.markdown(content)
