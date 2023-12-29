import streamlit as st


st.session_state.register_result = ""


def check_inputs(data):
    if not data["model_name"]:
        return False
    elif not data["repo_id"]:
        return False
    elif not data["original_repo_id"]:
        return False
    elif not data["quantize"]:
        return False
    elif not data["file_name"]:
        return False
    elif not data["mode"]:
        return False
    elif not data["prompt_format"]:
        return False
    elif not data["ip"]:
        return False
    elif not data["branch"]:
        return False
    
    return True

def register_data(model_name, repo_id, original_repo_id, quantize, file_name, max_ngl, language, mode, prompt_format, ip, port, branch, ctx_size, default_params, stop_token):
    data = {
        "model_name": model_name,
        "repo_id": repo_id,
        "original_repo_id": original_repo_id,
        "quantize": quantize,
        "file_name": file_name,
        "max_ngl": max_ngl,
        "language": language,
        "mode": mode,
        "prompt_format": prompt_format,
        "ip": ip,
        "port": port,
        "branch": branch,
        "ctx_size": ctx_size,
        "default_params": {
            "temperature": temperature,
            "top_k": top_k,
            "top_p": top_p,
            "repetition_penalty": repetition_penalty,
            "n_predict": n_predict
            },
        "stop_token": stop_token,
        "note": ""
        }
    
    if check_inputs(data):
        file_name_list = []
        for q in data["quantize"]:
            file_name_list.append(data["file_name"].replace("(Q)", q))
        data["file_name"] = file_name_list
        
        if not isinstance(data["mode"], list):
            data["mode"] = [data["mode"]]
        
        if not data["stop_token"]:
            data["stop_token"] = []
        else:
            data["stop_token"] = data["stop_token"].split(",")

        st.session_state.setting_file_loader.register_data(data)
        st.session_state.register_result = "Success!!"
        return

    st.session_state.register_result = "Failed..."


model_info, persona_info = st.columns(spec=2, gap="large")

with model_info:
    with st.container(border=True):
        model_name = st.text_input(
            label="Model Name",
            placeholder="airoboros-l2-13b-3.1.1"
            )
        
        repo_id = st.text_input(
            label="Repository ID",
            placeholder="TheBloke/Airoboros-L2-13B-3.1.1-GGUF"
            )
        
        original_repo_id = st.text_input(
            label="Original Repository ID",
            placeholder="jondurbin/airoboros-l2-13b-3.1.1"
            )
        
        quantize = st.multiselect(
            label='Select downloaded quantize',
            options=('Q4_K_M', 'Q5_K_M', 'Q8_0', 'Q6_K', 'Q3_K_M', 'Q2_K', 'Q3_K_S', 'Q3_K_L', 'Q4_0', 'Q4_K_S', 'Q5_0', 'Q5_K_S')
            )

        file_name = st.text_input(
            label="File Name (quantize part should be '(Q)')",
            placeholder="airoboros-l2-13b-3.1.1.(Q).gguf"
            )
        
        max_ngl = st.number_input(
            label="Max Number of GPU Layer",
            min_value=1,
            value=33,
            step=1
            )
        
        language = st.selectbox(
            label="Language",
            options=('en', 'ja')
            )
        
        with st.container(border=True):
            is_new_mode = st.radio(
                label="Is New Mode?",
                options=("No", "Yes"),
                horizontal=True
                )
            
            if is_new_mode == "No":
                mode = st.multiselect(
                    label="Mode",
                    options=st.session_state.setting_file_loader.get_mode_list()
                    )
            
            else:
                mode = st.text_input(
                    label="Mode(If Not Chat, Contain '(Single-turn)')",
                    placeholder="Instruction (Single-turn)"
                    )

        with st.container(border=True):
            is_new_prompt_format = st.radio(
                label="Is New Prompt Format?",
                options=("No", "Yes"),
                horizontal=True
                )
            
            if is_new_prompt_format == "No":
                prompt_format = st.selectbox(
                    label="Prompt Format",
                    options=st.session_state.setting_file_loader.get_prompt_format_list()
                    )
            
            else:
                prompt_format = st.text_input(
                    label="Prompt Format",
                    placeholder="Vicuna"
                    )

        ip = st.text_input(
            label="IP Address",
            value="localhost"
            )
        
        port = st.text_input(
            label="Listen Port",
            value=st.session_state.setting_file_loader.get_port_number(ip),
            disabled=True
            )
        
        branch = st.text_input(
            label="Branch of llama.cpp",
            value="master"
            )
        
        ctx_size = st.selectbox(
            label="Context Length",
            options=(512, 1024, 2048, 4096, 8192, 16384),
            index=3
            )
        
        with st.container(border=True):
            temperature = st.slider(
                label="Temperature",
                min_value=0.0,
                max_value=1.0,
                value=0.8,
                step=0.1,
                format="%f"
            )

            top_k = st.slider(
                label="Top-k",
                min_value=1,
                max_value=100,
                value=40,
                step=1
            )

            top_p = st.slider(
                label="Top-p",
                min_value=0.0,
                max_value=1.0,
                value=0.95,
                step=0.05
            )

            repetition_penalty = st.slider(
                label="Repetition Penalty",
                min_value=1.0,
                max_value=2.0,
                value=1.1,
                step=0.1,
                format="%f"
            )

            n_predict = st.slider(
                label="N Predict",
                min_value=-1,
                max_value=256,
                value=-1,
                step=1
            )

        stop_token = st.text_input(
            label="Stop Token (Separator is ',')",
            placeholder="A,B,C"
            )
        
        register_button = st.button(
            label="Register",
            on_click=register_data,
            kwargs={
                "model_name": model_name,
                "repo_id": repo_id,
                "original_repo_id": original_repo_id,
                "quantize": quantize,
                "file_name": file_name,
                "max_ngl": max_ngl,
                "language": language,
                "mode": mode,
                "prompt_format": prompt_format,
                "ip": ip,
                "port": port,
                "branch": branch,
                "ctx_size": ctx_size,
                "default_params": {
                    "temperature": temperature,
                    "top_k": top_k,
                    "top_p": top_p,
                    "repetition_penalty": repetition_penalty,
                    "n_predict": n_predict
                },
                "stop_token": stop_token
            }
        )

        register_result = st.write(
            st.session_state.register_result
        )

with persona_info:
    with st.container(border=True):
        st.text_input(
            label="Persona Name"
            )
