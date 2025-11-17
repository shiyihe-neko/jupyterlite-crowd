import os
import requests
from tqdm import tqdm


def upload_to_backend(file_path, participant_id, kind="data"):
    """
    Upload file (CSV or notebook) to backend with progress bar.
    """

    url = {
        "data": "https://jupyterlite-crowd.onrender.com/upload_file",
        "notebook": "https://jupyterlite-crowd.onrender.com/upload_notebook",
    }[kind]

    file_size = os.path.getsize(file_path)

    # tqdm progress bar
    progress = tqdm(
        total=file_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
        desc=f"Uploading {os.path.basename(file_path)}"
    )

    class ProgressFileWrapper:
        def __init__(self, fileobj):
            self.file = fileobj
            self.read_bytes = 0

        def read(self, size=-1):
            chunk = self.file.read(size)
            if chunk:
                progress.update(len(chunk))
            return chunk

        def __getattr__(self, attr):
            return getattr(self.file, attr)

    with open(file_path, "rb") as f:
        wrapped_file = ProgressFileWrapper(f)

        res = requests.post(
            url,
            files={"file": wrapped_file},
            data={"participant_id": participant_id}
        )

    progress.close()

    print(f"✔ Upload {kind} complete! Status: {res.status_code}")
    return res.json()
