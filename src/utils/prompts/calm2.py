def single_turn(message):
    prompt = f"USER: {message}\nASSISTANT: "

    return prompt

def multi_turn(message_log):
    prompt = ""

    for message in message_log:
        if message["name"] == "user":
            prompt += f"USER: {message['msg']}\n"
        elif message["name"] == "assistant":
            prompt += f"ASSISTANT: {message['msg']}\n"

    prompt += "ASSISTANT: "

    return prompt
