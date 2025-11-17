import requests
import os
import time
import math

def estimate_time(size_bytes):
    size_mb = size_bytes / (1024 * 1024)
    return max(5, int(size_mb * 3)) 

def upload_to_backend(file_path, participant_id, kind="data"):
    """
    Upload file (CSV or notebook) to backend with clean progress output.
    """
    file_name = os.path.basename(file_path)

    url = {
        "data": "https://jupyterlite-crowd.onrender.com/upload_file",
        "notebook": "https://jupyterlite-crowd.onrender.com/upload_notebook",
    }[kind]

    size_bytes = os.path.getsize(file_path)
    eta = estimate_time(size_bytes)

    print(f"Uploading {file_name}...")
    print(f"Estimated time: ~{eta} seconds")


    with open(file_path, "rb") as f:
        res = requests.post(url, files={"file": f}, data={"participant_id": participant_id})

    if res.status_code == 200:
        print(f"✔ {file_name} upload complete!\n")
    else:
        print(f"✘ Upload failed for {file_name}. Status: {res.status_code}\n")

    try:
        return res.json().get("path", None)
    except:
        return None
