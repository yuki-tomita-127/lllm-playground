import json

import requests


class RequestHandler:
    def __init__(self, model_manager):
        self.request_header = { 'Content-Type': 'application/json' }

        self.server_url = model_manager.get_server_url()
    
    def send_request(self, prompt, params, stream):
        data = json.dumps({
            'prompt': prompt,
            'temperature': params['temperature'],
            'top_k': params['top_k'],
            'top_p': params['top_p'],
            'repetition_penalty': params['repetition_penalty'],
            'n_predict': params['n_predict'],
            'stream': stream
            })
        
        print(prompt)

        response = requests.post(
            self.server_url,
            headers=self.request_header,
            data=data,
            stream=stream
            )
        
        return response
