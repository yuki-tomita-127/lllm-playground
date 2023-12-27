import json

import requests

from utils.prompts.calm2 import Calm2
from utils.prompts.alpaca import Alpaca
from utils.prompts.alma import ALMA
from utils.prompts.deepseek_coder import DeepseekCoder
from utils.prompts.openchat3_5 import OpenChat3_5
from utils.prompts.chatml import ChatML


def convert_prompt(message, model_info, mode):
    prompt_template = model_info["prompt_format"]
    
    if prompt_template == "calm2":
        if mode == "Instruction (Single-turn)":
            prompt = Calm2.single_turn(message)
        else:
            prompt = Calm2.multi_turn(message)
    
    elif prompt_template == "alpaca(ja)":
        prompt = Alpaca.single_turn_ja(message)

    elif prompt_template == "ALMA":
        if mode == "Ja to En (Single-turn)":
            prompt = ALMA.single_turn_ja_to_en(message)
        else:
            prompt = ALMA.single_turn_en_to_ja(message)
    
    elif prompt_template == "Deepseek Coder":
        if mode == "Code Completion (Single-turn)":
            if "instruct" in model_info["model_name"]:
                prompt = DeepseekCoder.single_turn_code_completion_for_instruct(message)
            else:
                prompt = DeepseekCoder.single_turn_code_completion(message)
        elif mode == "Code Insertion (Single-turn)":
            prompt = DeepseekCoder.single_turn_code_insertion(message)
        else:
            prompt = DeepseekCoder.single_turn_repo_code_completion(message)
    
    elif prompt_template == "Openchat3.5":
        if mode == "Chat":
            prompt = OpenChat3_5.multi_turn(message)
        elif mode == "Instruction (Single-turn)":
            prompt = OpenChat3_5.single_turn(message)
        elif mode == "Code Completion (Single-turn)":
            prompt = OpenChat3_5.single_turn_code_completion(message)
        else:
            prompt = OpenChat3_5.single_turn_solving_math(message)
    
    elif prompt_template == "ChatML":
        if mode == "Instruction (Single-turn)":
            prompt = ChatML.single_turn(message)
        else:
            prompt = ChatML.multi_turn(message)
    
    # NOTE: Used to check that prompts are being converted correctly. Will be deleted in the future.
    print(prompt)
    print("="*60)
    print()

    return prompt


def to_swallow(user_msg):
    if "|" in user_msg:
        user_msg, input = user_msg.split("|", 1)
    else:
        input = None

    PROMPT_DICT = {
        "prompt_input": (
            "以下に、あるタスクを説明する指示があり、それに付随する入力が更なる文脈を提供しています。"
            "リクエストを適切に完了するための回答を記述してください。\n\n"
            "### 指示:\n{user_msg}\n\n### 入力:\n{input}\n\n### 応答:"

        ),
        "prompt_no_input": (
            "以下に、あるタスクを説明する指示があります。"
            "リクエストを適切に完了するための回答を記述してください。\n\n"
            "### 指示:\n{user_msg}\n\n### 応答:"
        ),
    }

    if input:
        # Use the 'prompt_input' template when additional input is provided
        return PROMPT_DICT["prompt_input"].format(user_msg=user_msg, input=input)
    else:
        # Use the 'prompt_no_input' template when no additional input is provided
        return PROMPT_DICT["prompt_no_input"].format(user_msg=user_msg)

def to_stablelm_gamma(user_msg):
    if "|" in user_msg:
        user_msg, input = user_msg.split("|", 1)
    else:
        input = None

    sep="\n\n### "

    sys_msg = "以下は、タスクを説明する指示と、文脈のある入力の組み合わせです。要求を適切に満たす応答を書きなさい。"
    p = sys_msg
    roles = ["指示", "応答"]
    msgs = [": \n" + user_msg, ": \n"]
    if input:
        roles.insert(1, "入力")
        msgs.insert(1, ": \n" + input)
    for role, msg in zip(roles, msgs):
        p += sep + role + msg
    return p

def translate(prompt):
    prompt = f"Translate this from Japanese to English:\nJapanese: {prompt}\nEnglish:"
    req_data = json.dumps({
        'prompt': prompt,
        'n_predict': 128,
        'temperature': 0.7,
        'repeat_penalty': 1.1
        })
    
    response = requests.post("http://localhost:8079/completion", headers={ 'Content-Type': 'application/json' }, data=req_data)

    j = response.json()
    return j["content"]
