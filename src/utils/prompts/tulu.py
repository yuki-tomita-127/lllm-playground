class Tulu:
    @staticmethod
    def single_turn(message):
        prompt = f"""<|user|>
{message}
<|assistant|>
"""
        return prompt