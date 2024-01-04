import os
import subprocess


def start_server(model_manager):
    server_app_path = model_manager.server_app_path

    directory_paths = model_manager.gguf_path
    file_path = model_manager.get_file_name()

    for dir_path in directory_paths:
        gguf_full_path = os.path.join(dir_path, file_path)
        if os.path.exists(gguf_full_path):
            break

    ctx_size = model_manager.active_model_info["ctx_size"]
    port = model_manager.active_model_info["port"]
    ngl = model_manager.n_gpu_layer

    cmd = [
        server_app_path,
        "-m", gguf_full_path,
        "-c", str(ctx_size),
        "--port", port,
        "-ngl", str(ngl)
        ]
    
    subprocess.Popen(cmd, creationflags=subprocess.CREATE_NEW_CONSOLE)
