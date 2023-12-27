class DeepseekCoder:
    @staticmethod
    def single_turn_code_completion(message):
        prompt = f"#{message}"
        return prompt

    @staticmethod
    def single_turn_code_insertion(message):
        message = message.replace("[MASK]", "<｜fim▁hole｜>")
        prompt = f"<｜fim▁begin｜>{message}<｜fim▁end｜>"
        return prompt

    @staticmethod
    def single_turn_repo_code_completion(message):
        assert False, "Not implemented yet"

    @staticmethod
    def single_turn_code_completion_for_instruct(message):
        prompt = f"""You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer.
### Instruction:
{message}
### Response:
"""
        return prompt
