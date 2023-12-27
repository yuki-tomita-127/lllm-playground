class OpenChat3_5:
    @staticmethod
    def single_turn(message):
        prompt = f"GPT4 Correct User: {message}<|end_of_turn|>GPT4 Correct Assistant:"
        return prompt

    @staticmethod
    def multi_turn(message_log):
        prompt = ""
        for message in message_log:
            if message["name"] == "user":
                prompt += f"GPT4 Correct User: {message['msg']}<|end_of_turn|>"
            elif message["name"] == "assistant":
                prompt += f"GPT4 Correct Assistant: {message['msg']}<|end_of_turn|>"

        prompt += "GPT4 Correct Assistant:"
        return prompt

    @staticmethod
    def single_turn_code_completion(message):
        prompt = f"Code User: {message}<|end_of_turn|>Code Assistant:"
        return prompt
    
    @staticmethod
    def single_turn_solving_math(message):
        prompt = f"Math Correct User: {message}<|end_of_turn|>Math Correct Assistant:"
        return prompt
