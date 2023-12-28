class Alpaca:
    @staticmethod
    def single_turn_ja(message):
        if "|" in message:
            message, input = message.split("|", 1)
        else:
            input = None

        PROMPT_DICT = {
        "prompt_input": (
            "以下に、あるタスクを説明する指示があり、それに付随する入力が更なる文脈を提供しています。"
            "リクエストを適切に完了するための回答を記述してください。\n\n"
            "### 指示:\n{instruction}\n\n### 入力:\n{input}\n\n### 応答:"

        ),
        "prompt_no_input": (
            "以下に、あるタスクを説明する指示があります。"
            "リクエストを適切に完了するための回答を記述してください。\n\n"
            "### 指示:\n{instruction}\n\n### 応答:"
        ),
    }

        if input:
            # Use the 'prompt_input' template when additional input is provided
            return PROMPT_DICT["prompt_input"].format(instruction=message, input=input)
        else:
            # Use the 'prompt_no_input' template when no additional input is provided
            return PROMPT_DICT["prompt_no_input"].format(instruction=message)
        
    @staticmethod
    def single_turn_en(message):
        if "|" in message:
            message, input = message.split("|", 1)
        else:
            input = None

        PROMPT_DICT = {
        "prompt_input": (
            "Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.\n\n"
            "### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n### Response:"

        ),
        "prompt_no_input": (
            "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n"
            "### Instruction:\n{instruction}\n\n### Response:"
        ),
    }

        if input:
            # Use the 'prompt_input' template when additional input is provided
            return PROMPT_DICT["prompt_input"].format(instruction=message, input=input)
        else:
            # Use the 'prompt_no_input' template when no additional input is provided
            return PROMPT_DICT["prompt_no_input"].format(instruction=message)
