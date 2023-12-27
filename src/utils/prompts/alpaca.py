class Alpaca:
    @staticmethod
    def single_turn_ja(message):
        if "|" in message:
            message, input = message.split("|", 1)
        else:
            input = ""

        PROMPT_DICT = {
            "prompt_input": (
                "以下は、タスクを説明する指示と、文脈のある入力の組み合わせです。要求を適切に満たす応答を書きなさい。\n\n"
                "### 指示:\n{instruction}\n\n### 入力:\n{input}\n\n### 応答:\n"

            ),
            "prompt_no_input": (
                "以下は、タスクを説明する指示です。要求を適切に満たす応答を書きなさい。\n\n"
                "### 指示:\n{instruction}\n\n### 応答:\n"
            ),
        }

        if input:
            # Use the 'prompt_input' template when additional input is provided
            return PROMPT_DICT["prompt_input"].format(instruction=message, input=input)
        else:
            # Use the 'prompt_no_input' template when no additional input is provided
            return PROMPT_DICT["prompt_no_input"].format(instruction=message)
