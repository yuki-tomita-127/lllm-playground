import subprocess


def start_server(server_app_path, gguf_path, ctx_size, port, ngl):
    cmd = [
        server_app_path,
        "-m", gguf_path,
        "-c", str(ctx_size),
        "--port", port,
        "-ngl", str(ngl)
        ]
    
    subprocess.Popen(cmd, creationflags=subprocess.CREATE_NEW_CONSOLE)
