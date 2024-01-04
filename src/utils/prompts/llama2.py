class Llama2:
    @staticmethod
    def single_turn(message):
        prompt = f"[INST] <<SYS>>\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don’t know the answer to a question, please don’t share false information.\n<</SYS>>\n\n{message} [/INST]"
        return prompt

    @staticmethod
    def multi_turn(message_log):
        prompt = "[INST] <<SYS>>\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don’t know the answer to a question, please don’t share false information.\n<</SYS>>\n\n"
        for message in message_log:
            if message["name"] == "user":
                prompt += f"USER: {message['msg']}\n"
            elif message["name"] == "assistant":
                prompt += f"ASSISTANT: {message['msg']}\n"

        prompt += "ASSISTANT:"
        return prompt