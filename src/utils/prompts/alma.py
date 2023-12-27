class ALMA:
    @staticmethod
    def single_turn_ja_to_en(message):
        prompt = f"Translate this from Japanese to English:\nJapanese: {message}\nEnglish:"
        return prompt

    @staticmethod
    def single_turn_en_to_ja(message):
        prompt = f"Translate this from English to Japanese:\nEnglish: {message}\nJapanese:"
        return prompt
