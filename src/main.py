import json
import requests
import streamlit as st

from utils.model_manager import ModelManager
from utils.prompt_converter import to_calm2, to_llama2, to_wizardcoder, to_openchat3_5, to_Xwin_LM, to_v1olet_marcoroni, to_stablelm_4e1t, to_swallow, to_nekomata, to_stablelm_gamma, translate
from utils.prompts.calm2 import Calm2
from utils.server_launcher import start_server

st.title("Local Chat")

USER_NAME = "user"
ASSISTANT_NAME = "assistant"
REQ_HEADER = { 'Content-Type': 'application/json' }

url = 'http://localhost:8080/completion'

# Session State Initialization
if "model_manager" not in st.session_state:
    st.session_state.model_manager = ModelManager()
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
if "server_url" not in st.session_state:
    st.session_state.server_url = "http://localhost:8080/completion"

def change_server_url(model_name):
    if model_name == "Calm2-7B":
        st.session_state.server_url = "http://localhost:8080/completion"
    elif model_name == "WizardCoder-Python-7B":
        st.session_state.server_url = "http://localhost:8081/completion"
    elif model_name == "Llama2-7B":
        st.session_state.server_url = "http://localhost:8082/completion"
    elif model_name == "OpenChat3.5":
        st.session_state.server_url = "http://localhost:8083/completion"
    elif model_name == "Xwin-LM-13B-V0.2":
        st.session_state.server_url = "http://localhost:8084/completion"
    elif model_name == "v1olet_marcoroni-7B":
        st.session_state.server_url = "http://localhost:8085/completion"
    elif model_name == "stablelm-4e1t":
        st.session_state.server_url = "http://localhost:8086/completion"
    elif model_name == "stablelm-gamma-7B":
        st.session_state.server_url = "http://localhost:8099/completion"
    elif model_name == "nekomata-14B":
        st.session_state.server_url = "http://localhost:8100/completion"

def set_model():
    st.session_state.model_manager.active_model = st.session_state.selected_model
    st.session_state.model_quantize_list = st.session_state.model_manager.get_quantize()
    st.session_state.chat_log = []
    change_server_url(st.session_state.selected_model)

def set_translate():
    st.session_state.use_translate = st.session_state.use_translate

def launch_server():
    pass

def response_chatmodel(user_msg):
    if st.session_state.use_translate:
        st.write("[System] Translating...")
        user_msg = translate(user_msg)
        st.write(f"[System] Translated: {user_msg}")
    
    if isinstance(user_msg, list):
        prompt = Calm2.multi_turn(user_msg)
    elif st.session_state.selected_model == "calm2-7b-chat":
        prompt = to_calm2(user_msg)
    elif st.session_state.selected_model == "WizardCoder-Python-7B":
        prompt = to_wizardcoder(user_msg)
    elif st.session_state.selected_model == "Llama2-7B":
        prompt = to_llama2(user_msg)
    elif st.session_state.selected_model == "OpenChat3.5":
        prompt = to_openchat3_5(user_msg)
    elif st.session_state.selected_model == "Xwin-LM-13B-V0.2":
        prompt = to_Xwin_LM(user_msg)
    elif st.session_state.selected_model == "v1olet_marcoroni-7B":
        prompt = to_v1olet_marcoroni(user_msg)
    elif st.session_state.selected_model == "stablelm-4e1t":
        prompt = to_stablelm_4e1t(user_msg)
    elif st.session_state.selected_model == "swallow-70B":
        prompt = to_swallow(user_msg)
    elif st.session_state.selected_model == "stablelm-gamma-7B":
        prompt = to_stablelm_gamma(user_msg)
    elif st.session_state.selected_model == "nekomata-14B":
        prompt = to_nekomata(user_msg)

    req_data = json.dumps({
        'prompt': prompt,
        'n_predict': -1,
        'temperature': 0.7,
        'repeat_penalty': 1.1,
        'stream': True,
        })
    
    response = requests.post(st.session_state.server_url, headers=REQ_HEADER, data=req_data, stream=True)
    
    return response

# Sidebar
with st.sidebar:
    with st.container(border=True):
        model_selectbox = st.selectbox(
            label="Model",
            # options=("Calm2-7B", "WizardCoder-Python-7B", "Llama2-7B", "OpenChat3.5", "Xwin-LM-13B-V0.2", "v1olet_marcoroni-7B", "stablelm-4e1t", "swallow-70B", "stablelm-gamma-7B", "nekomata-14B"),
            options=st.session_state.model_manager.models,
            key="selected_model",
            on_change=set_model,
        )

        model_quantize = st.selectbox(
            label="Quantize",
            options=st.session_state.model_quantize_list,
            key="selected_quantize",
        )

        add_radio = st.toggle(
            label="Translate",
            key="use_translate",
            on_change=set_translate,
        )
        
        mode_selectbox = st.selectbox(
            label="Mode",
            options=("Chat", "Instruction(Single)", "Instruction(Multi)"),
            key="selected_mode",
        )

        server_launch_button = st.button(
            label="Launch Server",
            key="launch_server",
            on_click=launch_server,
        )

    with st.container(border=True):
        temperature = st.slider(
            label="Temperature(default: 0.8)",
            min_value=0.0,
            max_value=1.0,
            value=0.8,
            step=0.1,
            key="temperature",
        )

        top_k = st.slider(
            label="Top-k(default: 40)",
            min_value=1,
            max_value=100,
            value=40,
            step=1,
            key="top_k",
        )

        top_p = st.slider(
            label="Top-p(default: 0.95)",
            min_value=0.0,
            max_value=1.0,
            value=0.95,
            step=0.05,
            key="top_p",
        )

        repetition_penalty = st.slider(
            label="Repetition Penalty(default: 1.1)",
            min_value=1.0,
            max_value=2.0,
            value=1.1,
            step=0.1,
            key="repetition_penalty",
        )

        n_predict = st.slider(
            label="N Predict(default: -1)",
            min_value=-1,
            max_value=256,
            value=-1,
            step=1,
            key="n_predict",
        )

# Chat Area
user_msg = st.chat_input("message to chatbot...")
if user_msg:
    for chat in st.session_state.chat_log:
        with st.chat_message(chat["name"]):
            st.write(chat["msg"])

    with st.chat_message(USER_NAME):
        st.write(user_msg)

    # st.session_state.chat_log.append({"name": USER_NAME, "msg": user_msg})

    response = response_chatmodel(user_msg)
    with st.chat_message(ASSISTANT_NAME):
        assistant_msg = ""
        assistant_response_area = st.empty()
        for chunk in response.iter_lines():
            if chunk.startswith(b'data: '):
                j = json.loads(chunk[6:].decode())
                tmp_assistant_msg = j.get("content", "")
                assistant_msg += tmp_assistant_msg
                assistant_response_area.write(assistant_msg)

    st.session_state.chat_log.append({"name": USER_NAME, "msg": user_msg})
    st.session_state.chat_log.append({"name": ASSISTANT_NAME, "msg": assistant_msg})

    # show chat log for debug(json format)
    st.write(json.dumps(st.session_state.chat_log, indent=4, ensure_ascii=False))
