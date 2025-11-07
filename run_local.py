#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
一键构建并启动 JupyterLite（带 Pyodide 内核）
完全等价于：
1. 清理旧构建
2. jupyter lite build --apps lab --contents lite/files --output-dir dist --ignore-sys-prefix --force
3. python -m http.server -d dist 8000
"""

import os
import shutil
import subprocess
import webbrowser
import socket
import sys
import time


def run(cmd):
    """执行命令并同步输出"""
    print(f"\n>> {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


def clean():
    """清理旧构建"""
    print("🧹 清理旧构建...")
    for path in ["dist", "_output", ".jupyterlite.doit.db", ".doit.db", ".lite_hash", ".doit"]:
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path, ignore_errors=True)
            else:
                os.remove(path)
    print("✅ 清理完成")


def find_free_port(start=8000):
    """查找可用端口"""
    port = start
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", port)) != 0:
                return port
        port += 1


def main():
    print("🐍 一键运行 JupyterLite 前端")
    print("==============================")

    clean()

    # ✅ 使用当前 venv 下的 jupyter 模块，确保内核路径正确
    run([
        sys.executable, "-m", "jupyter", "lite", "build",
        "--apps", "lab",
        "--contents", "lite/files",
        "--output-dir", "dist",
        "--ignore-sys-prefix",
        "--force",
    ])

    # Step 2: 启动 HTTP server
    port = find_free_port(8000)
    url = f"http://127.0.0.1:{port}/"
    print(f"\n🌐 启动本地服务器: {url}")
    # ⚡️ 加 lite=reset 确保更新同步
    cache_bust_url = f"{url}?lite=reset&v={int(time.time())}"
    webbrowser.open(cache_bust_url)

    subprocess.run([sys.executable, "-m", "http.server", str(port), "-d", "dist"])


if __name__ == "__main__":
    main()
