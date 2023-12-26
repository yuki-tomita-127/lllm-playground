import json

import requests


def to_calm2(user_msg):
    return f"USER: {user_msg}\nASSISTANT: "

def to_wizardcoder(user_msg):
    return f"Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n{user_msg}\n\n### Response:"

def to_llama2(user_msg):
    return f"[INST] <<SYS>>\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don’t know the answer to a question, please don’t share false information.\n<</SYS>>\n\n{user_msg} [/INST]"

def to_openchat3_5(user_msg):
    return f"GPT4 Correct User: Hello<|end_of_turn|>GPT4 Correct Assistant: Hi. I'm Rosa.<|end_of_turn|>GPT4 Correct User: {user_msg}<|end_of_turn|>GPT4 Correct Assistant:"

def to_Xwin_LM(user_msg):
    return f"A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. USER: {user_msg} ASSISTANT: "

def to_v1olet_marcoroni(user_msg):
    return f"template_format = Below is an instruction that describes a task. Write a response that appropriately completes the request.\n### Instruction:\n{user_msg}\n\n### Response:\n"

def to_stablelm_4e1t(user_msg):
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
    
def to_nekomata(user_msg):
    if "|" in user_msg:
        user_msg, input = user_msg.split("|", 1)
    else:
        input = None

    instruction = user_msg
    prompt = f"""
    以下は、タスクを説明する指示と、文脈のある入力の組み合わせです。要求を適切に満たす応答を書きなさい。

    ### 指示:
    {instruction}

    ### 入力:
    {input}

    ### 応答:
    """

    return prompt

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
