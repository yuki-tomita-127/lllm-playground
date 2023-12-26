class OpenChat3_5:
    def single_turn(user_message):
        "GPT4 Correct User: Hello<|end_of_turn|>GPT4 Correct Assistant: Hi<|end_of_turn|>GPT4 Correct User: How are you today?<|end_of_turn|>GPT4 Correct Assistant:"
        return f"GPT4 Correct User: {user_message}<|end_of_turn|>GPT4 Correct Assistant:"
    
    def multi_turn(chat_history, user_message):
        return f"USER: {user_message}\nASSISTANT: "
    
    def single_turn_for_math_solving(user_message):
        return f"Math Correct User: {user_message}<|end_of_turn|>Math Correct Assistant:"
