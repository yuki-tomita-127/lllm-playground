from utils.prompts.vicuna import Vicuna
from utils.prompts.alpaca import Alpaca
from utils.prompts.alma import ALMA
from utils.prompts.deepseek_coder import DeepseekCoder
from utils.prompts.openchat3_5 import OpenChat3_5
from utils.prompts.chatml import ChatML
from utils.prompts.tulu import Tulu
from utils.prompts.capybara import Capybara
from utils.prompts.mistral import Mistral


def convert_prompt(message, model_info, mode):
    prompt_template = model_info["prompt_format"]
    if prompt_template == "Vicuna":
        if mode == "Instruction (Single-turn)":
            prompt = Vicuna.single_turn(message)
        else:
            prompt = Vicuna.multi_turn(message)

    elif prompt_template == "Calm2":
        if mode == "Instruction (Single-turn)":
            prompt = Vicuna.single_turn_without_system(message)
        else:
            prompt = Vicuna.multi_turn_without_system(message)
    
    elif prompt_template.startswith("Alpaca"):
        if "ja" in prompt_template:
            prompt = Alpaca.single_turn_ja(message)
        else:
            prompt = Alpaca.single_turn_en(message)

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
    
    elif prompt_template == "Tulu":
        prompt = Tulu.single_turn(message)
    
    elif prompt_template == "Capybara":
        prompt = Capybara.single_turn(message)
    
    elif prompt_template == "Mistral":
        prompt = Mistral.single_turn(message)
    
    # NOTE: Used to check that prompts are being converted correctly. Will be deleted in the future.
    print(prompt)
    print("="*60)
    print()

    return prompt
