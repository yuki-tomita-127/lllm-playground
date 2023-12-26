import json


class ModelManager:
    def __init__(self):
        self.model_info = json.load(open("data/model_info.json", "r", encoding="utf-8"))

        self.server_app_path = self.model_info["default_server_app_path"]
        self.gguf_path = self.model_info["default_gguf_dir_path"]

        self.models = []
        for model in self.model_info["local_models"]:
            self.models.append(model["model_name"])

        self.active_model_info = self.model_info["local_models"][0]
        self.active_model = self.active_model_info["model_name"]
        self.active_quantize = self.active_model_info["quantize"][0]
        self.active_mode = self.active_model_info["mode"][0]
        self.n_gpu_layer = 0
    
    def change_active_model(self, model_name):
        self.active_model = model_name

        for model in self.model_info["local_models"]:
            if model["model_name"] == model_name:
                self.active_model_info = model
                break
    
    def change_active_quantize(self, quantize):
        self.active_quantize = quantize
    
    def change_gpu_layer(self, n_gpu_layer):
        self.n_gpu_layer = n_gpu_layer

    def change_active_mode(self, mode):
        self.active_mode = mode
    
    def get_quantize(self):
        quantize = self.active_model_info["quantize"]
        
        self.active_quantize = quantize[0]
        
        return quantize
    
    def get_max_gpu_layer(self):
        return self.active_model_info["max_ngl"]
    
    def get_mode(self):
        mode = self.active_model_info["mode"]
        
        self.active_mode = mode[0]
        
        return mode
    
    def get_file_name(self):
        index = self.active_model_info["quantize"].index(self.active_quantize)

        return self.active_model_info["file_name"][index]
    
    def get_server_url(self):
        ip = self.active_model_info["ip"]
        port = self.active_model_info["port"]

        server_url = f"http://{ip}:{port}/completion"
        
        return server_url
