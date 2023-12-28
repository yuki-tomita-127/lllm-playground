class Mistral:
    @staticmethod
    def single_turn(message):
        prompt = f"[INST] {message} [/INST]"
        return prompt
