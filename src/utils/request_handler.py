import json
import requests


class RequestHandler:
    def __init__(self):
        self.request_header = { 'Content-Type': 'application/json' }
    
    def set_ip_and_port(self, ip, port):
        self.server_url = f"http://{ip}:{port}/completion"

    def send_request(self, prompt, params, stream):
        data = json.dumps({
            'prompt': prompt,
            'temperature': params['temperature'],
            'top_k': params['top_k'],
            'top_p': params['top_p'],
            'repetition_penalty': params['repetition_penalty'],
            'n_predict': params['n_predict'],
            'stream': stream,
            })

        response = requests.post(
            self.server_url,
            self.request_header,
            data=data,
            stream=stream
            )
        
        return response
