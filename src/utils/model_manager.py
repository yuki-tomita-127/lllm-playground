import json


class ModelManager:
    def __init__(self):
        self.model_info = json.load(open("data/model_info.json", "r", encoding="utf-8"))

        self.server_app_path = self.model_info["default_server_app_path"]
        self.gguf_path = self.model_info["default_gguf_dir_path"]
        self.models = []
        for model in self.model_info["local_models"]:
            self.models.append(model["model_name"])
        self.active_model = self.models[0]
    
    def get_quantize(self):
        quantize = []
        for model in self.model_info["local_models"]:
            if model["model_name"] == self.active_model:
                quantize = model["quantize"]
                break
        
        return quantize
    
    def get_mode(self):
        mode = []
        for model in self.model_info["local_models"]:
            if model["model_name"] == self.active_model:
                mode = model["mode"]
                break
        
        return mode
    
    def load_model_data(self):
        print(json.dumps(self.model_info, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    model_manager = ModelManager()
    model_manager.load_model_data()
