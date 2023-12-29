import json


class SettingFileLoader:
    def __init__(self):
        self.model_info = json.load(open("data/model_info.json", "r", encoding="utf-8"))
        self.persona_info = json.load(open("data/persona_info.json", "r", encoding="utf-8"))

    def get_mode_list(self):
        mode_list= []
        for model in self.model_info["local_models"]:
            for mode in model["mode"]:
                if mode not in mode_list:
                    mode_list.append(mode)
        
        return mode_list

    def get_prompt_format_list(self):
        prompt_format_list= []
        for model in self.model_info["local_models"]:
            if model["prompt_format"] not in prompt_format_list:
                prompt_format_list.append(model["prompt_format"])
        
        return prompt_format_list

    def get_port_number(self, ip_address):
        max_port_num = 0
        for model in self.model_info["local_models"]:
            if model["ip"] == ip_address:
                if int(model["port"]) > max_port_num:
                    max_port_num = int(model["port"])
        
        if max_port_num == 0:
            return "8080"
        
        return str(max_port_num + 1)
    
    def register_data(self, data):
        self.model_info["local_models"].append(data)

        with open("data/model_info.json", 'w') as f:
            json.dump(self.model_info, f, indent=4)
