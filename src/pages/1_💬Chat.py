import json
import os

from plyer import notification
import streamlit as st

from utils.model_manager import ModelManager
from utils.prompt_converter import convert_prompt
from utils.request_handler import RequestHandler
from utils.server_launcher import start_server


# Session State Initialization
if "model_manager" not in st.session_state:
    st.session_state.model_manager = ModelManager()
if "request_handler" not in st.session_state:
    st.session_state.request_handler = RequestHandler(st.session_state.model_manager)

if "selected_model" not in st.session_state:
    st.session_state.selected_model = st.session_state.model_manager.active_model

if "model_quantize_list" not in st.session_state:
    st.session_state.model_quantize_list = st.session_state.model_manager.get_quantize()
if "selected_quantize" not in st.session_state:
    st.session_state.selected_quantize = st.session_state.model_quantize_list[0]

if "use_translate" not in st.session_state:
    st.session_state.use_translate = False

if "model_mode_list" not in st.session_state:
    st.session_state.model_mode_list = st.session_state.model_manager.get_mode()
if "selected_mode" not in st.session_state:
    st.session_state.selected_mode = st.session_state.model_mode_list[0]

if "chat_log" not in st.session_state:
    st.session_state.chat_log = []
if "user_avatar" not in st.session_state:
    st.session_state.user_avatar = "🦖"
if "assistant_avatar" not in st.session_state:
    avatar_file_path = "images/assistant.jpeg"
    st.session_state.assistant_avatar = avatar_file_path if os.path.exists(avatar_file_path) else None

if "temperature" not in st.session_state:
    st.session_state.temperature = 0.8
if "top_k" not in st.session_state:
    st.session_state.top_k = 40
if "top_p" not in st.session_state:
    st.session_state.top_p = 0.95
if "repetition_penalty" not in st.session_state:
    st.session_state.repetition_penalty = 1.1
if "n_predict" not in st.session_state:
    st.session_state.n_predict = -1

if "use_notification" not in st.session_state:
    st.session_state.use_notification = True


def set_model():
    st.session_state.model_manager.change_active_model(st.session_state.selected_model)
    st.session_state.request_handler = RequestHandler(st.session_state.model_manager)
    
    st.session_state.model_quantize_list = st.session_state.model_manager.get_quantize()
    st.session_state.model_mode_list = st.session_state.model_manager.get_mode()

    st.session_state.chat_log = []

def set_quantize():
    st.session_state.model_manager.change_active_quantize(st.session_state.selected_quantize)

def set_translate():
    st.session_state.use_translate = st.session_state.use_translate

def set_n_gpu_layer():
    st.session_state.model_manager.change_gpu_layer(st.session_state.n_gpu_layer)

def set_mode():
    st.session_state.model_manager.change_active_mode(st.session_state.selected_mode)

def launch_server():
    start_server(st.session_state.model_manager)


# Sidebar
with st.sidebar:
    with st.container(border=True):
        model_selectbox = st.selectbox(
            label="Model",
            options=st.session_state.model_manager.models,
            key="selected_model",
            on_change=set_model
        )

        model_quantize = st.selectbox(
            label="Quantize",
            options=st.session_state.model_quantize_list,
            key="selected_quantize",
            on_change=set_quantize
        )

        add_radio = st.toggle(
            label="Translate",
            key="use_translate",
            on_change=set_translate
        )

        n_gpu_layer = st.slider(
            label="N GPU Layer",
            min_value=0,
            max_value=st.session_state.model_manager.get_max_gpu_layer(),
            value=0,
            step=1,
            key="n_gpu_layer",
            on_change=set_n_gpu_layer
        )
        
        mode_selectbox = st.selectbox(
            label="Mode",
            options=st.session_state.model_mode_list,
            key="selected_mode",
            on_change=set_mode
        )

        server_launch_button = st.button(
            label="Launch Server",
            key="launch_server",
            on_click=launch_server
        )

    with st.container(border=True):
        temperature = st.slider(
            label="Temperature (default: 0.8)",
            min_value=0.0,
            max_value=1.0,
            step=0.1,
            key="temperature"
        )

        top_k = st.slider(
            label="Top-k (default: 40)",
            min_value=1,
            max_value=100,
            step=1,
            key="top_k"
        )

        top_p = st.slider(
            label="Top-p (default: 0.95)",
            min_value=0.0,
            max_value=1.0,
            step=0.05,
            key="top_p"
        )

        repetition_penalty = st.slider(
            label="Repetition Penalty (default: 1.1)",
            min_value=1.0,
            max_value=2.0,
            step=0.1,
            key="repetition_penalty"
        )

        n_predict = st.slider(
            label="N Predict (default: -1)",
            min_value=-1,
            max_value=256,
            step=1,
            key="n_predict"
        )
    
    notify_radio = st.toggle(
        label="Notification",
        key="use_notification"
    )


# Chat Area
user_msg = st.chat_input("message to chatbot...")
if user_msg:
    for chat in st.session_state.chat_log:
        if chat["name"] == "user":
            with st.chat_message("user", avatar=st.session_state.user_avatar):
                st.write(chat["msg"])
        else:
            with st.chat_message("assistant", avatar=st.session_state.assistant_avatar):
                st.write(chat["msg"])

    with st.chat_message("user", avatar=st.session_state.user_avatar):
        st.write(user_msg)
    
    st.session_state.chat_log.append({"name": "user", "msg": user_msg})

    if "Single-turn" in st.session_state.selected_mode:
        response = st.session_state.request_handler.send_request(
            convert_prompt(user_msg, st.session_state.model_manager.active_model_info, st.session_state.selected_mode),
            st.session_state,
            stream=True
            )
    else:
        response = st.session_state.request_handler.send_request(
            convert_prompt(st.session_state.chat_log, st.session_state.model_manager.active_model_info, st.session_state.selected_mode),
            st.session_state,
            stream=True
            )

    with st.chat_message("assistant", avatar=st.session_state.assistant_avatar):
        assistant_msg = ""
        assistant_response_area = st.empty()
        for chunk in response.iter_lines():
            if chunk.startswith(b'data: '):
                j = json.loads(chunk[6:].decode())
                tmp_assistant_msg = j.get("content", "")
                assistant_msg += tmp_assistant_msg
                assistant_response_area.write(assistant_msg)

    st.session_state.chat_log.append({"name": "assistant", "msg": assistant_msg})

    if st.session_state.use_notification:
        notification.notify(title='Streamlit', message='\nInference has been completed!', timeout=4)
