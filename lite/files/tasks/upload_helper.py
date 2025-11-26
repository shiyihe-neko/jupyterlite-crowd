import requests
import os


def estimate_time(size_bytes):
    size_mb = size_bytes / (1024 * 1024)
    return max(5, int(size_mb * 3)) 

def upload_to_backend(file_path, participant_id, kind="data"):
    """
    Upload file (CSV or notebook) to backend. Returns True on success, False on failure.
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

    try:
        with open(file_path, "rb") as f:
            res = requests.post(url, files={"file": f}, data={"participant_id": participant_id})
    except Exception as e:
        print(f"✘ Upload failed due to network error: {e}\n")
        return False 

    if res.status_code == 200:
        print(f"✔ {file_name} upload complete!")
        return True 
    else:
        print(f"✘ Upload failed for {file_name}. Status: {res.status_code}\n")
        return False

def submit_all_files(data_file_path, notebook_file_path, participant_id):
    all_success = True
    
    data_success = upload_to_backend(data_file_path, participant_id, kind="data")
    if not data_success:
        all_success = False
        print("-" * 40)
        print("data upload failed! Please check the logs.")

    if all_success:
        print("") 
        notebook_success = upload_to_backend(notebook_file_path, participant_id, kind="notebook")
        if not notebook_success:
            all_success = False
            print("-" * 40)
            print("notebook upload failed! Please check the logs.")


    print("\n" + "=" * 40)
    if all_success:
        print("Your files were all uploaded successfully. You can proceed to the next page!")
    else:
        print("Files upload Failed.")
    print("=" * 40)
    
    return None