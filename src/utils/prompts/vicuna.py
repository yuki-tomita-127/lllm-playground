class Vicuna:
    @staticmethod
    def single_turn(message):
        prompt = "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.\n\n"
        prompt += f"USER: {message}\nASSISTANT:"
        return prompt

    @staticmethod
    def multi_turn(message_log):
        prompt = "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.\n\n"
        for message in message_log:
            if message["name"] == "user":
                prompt += f"USER: {message['msg']}\n"
            elif message["name"] == "assistant":
                prompt += f"ASSISTANT: {message['msg']}\n"

        prompt += "ASSISTANT:"
        return prompt
    
    @staticmethod
    def single_turn_without_system(message):
        prompt = f"USER: {message}\nASSISTANT: "
        return prompt

    @staticmethod
    def multi_turn_without_system(message_log):
        prompt = ""
        for message in message_log:
            if message["name"] == "user":
                prompt += f"USER: {message['msg']}\n"
            elif message["name"] == "assistant":
                prompt += f"ASSISTANT: {message['msg']}\n"

        prompt += "ASSISTANT: "
        return prompt
