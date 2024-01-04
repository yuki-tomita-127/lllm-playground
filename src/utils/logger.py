from datetime import datetime
import json
import os


class Logger:
    def __init__(self):
        self.file_save_dir = "data/log/chat"

    def save_log(self, chat_log, temperature, top_k, top_p, repetition_penalty, n_predict):
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{current_time}.json"

        data_to_save = {
            "chat_log": chat_log,
            "temperature": temperature,
            "top_k": top_k,
            "top_p": top_p,
            "repetition_penalty": repetition_penalty,
            "n_predict": n_predict
        }
        json_data = json.dumps(data_to_save, indent=4, ensure_ascii=False)

        with open(os.path.join(self.file_save_dir, file_name), 'w') as file:
            file.write(json_data)
