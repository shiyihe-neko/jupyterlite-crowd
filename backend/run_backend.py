import os
import subprocess

def run_backend():
    port = 5050
    backend_dir = os.path.abspath(os.path.dirname(__file__))
    print(f"🚀 启动 Flask 后端 (http://127.0.0.1:{port})")
    subprocess.run(["python", "app.py"], cwd=backend_dir)

if __name__ == "__main__":
    run_backend()
