class Falcon:
    @staticmethod
    def single_turn(message):
        prompt = "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.\n"
        prompt += f"User: {message}\nAssistant:"
        return prompt

    @staticmethod
    def multi_turn(message_log):
        prompt = "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.\n"
        for message in message_log:
            if message["name"] == "user":
                prompt += f"User: {message['msg']}\n"
            elif message["name"] == "assistant":
                prompt += f"Assistant: {message['msg']}\n"

        prompt += "Assistant:"
        return prompt
