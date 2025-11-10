
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import os, datetime, werkzeug

# app = Flask(__name__)
# CORS(app)

# @app.get("/health")
# def health():
#     return {"status": "ok"}

# BASE_DIR = os.environ.get("SAVE_DIR", "saved_results")
# DATA_DIR = os.path.join(BASE_DIR, "data")
# NB_DIR = os.path.join(BASE_DIR, "notebooks")
# os.makedirs(DATA_DIR, exist_ok=True)
# os.makedirs(NB_DIR, exist_ok=True)

# def safe_name(s): 
#     return "".join(c for c in s if c.isalnum() or c in ('-', '_'))

# @app.route("/upload_file", methods=["POST"])
# def upload_file():
#     pid = safe_name(request.form.get("participant_id") or request.args.get("participant_id") or "unknown")
#     f = request.files.get("file")
#     if not f:
#         return jsonify({"status": "error", "msg": "no file"}), 400

#     ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%S")
#     ext = os.path.splitext(werkzeug.utils.secure_filename(f.filename))[1]
#     user_dir = os.path.join(DATA_DIR, pid)
#     os.makedirs(user_dir, exist_ok=True)
#     path = os.path.join(user_dir, f"{pid}_data_{ts}{ext}")
#     f.save(path)

#     print(f"✅ Received {f.filename} from {pid}, saved to {path}")
#     return jsonify({"status": "ok", "path": path})

# @app.route("/upload_notebook", methods=["POST"])
# def upload_notebook():
#     pid = safe_name(request.form.get("participant_id") or request.args.get("participant_id") or "unknown")
#     f = request.files.get("file")
#     if not f:
#         return jsonify({"status": "error", "msg": "no file"}), 400

#     ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%S")
#     user_dir = os.path.join(NB_DIR, pid)
#     os.makedirs(user_dir, exist_ok=True)
#     path = os.path.join(user_dir, f"{pid}_task_{ts}.ipynb")
#     f.save(path)

#     print(f"✅ Received {f.filename} from {pid}, saved to {path}")
#     return jsonify({"status": "ok", "path": path})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5050)))

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import os, datetime, werkzeug

# app = Flask(__name__)
# CORS(app)

# # ✅ 根路径（防止浏览器访问时报 404）
# @app.route("/")
# def index():
#     return (
#         "<h2>✅ Backend is running</h2>"
#         "<p>Available endpoints:</p>"
#         "<ul>"
#         "<li>GET /health</li>"
#         "<li>POST /upload_file</li>"
#         "<li>POST /upload_notebook</li>"
#         "</ul>"
#     )

# # ✅ 健康检查
# @app.get("/health")
# def health():
#     return {"status": "ok"}

# BASE_DIR = os.environ.get("SAVE_DIR", "saved_results")
# DATA_DIR = os.path.join(BASE_DIR, "data")
# NB_DIR = os.path.join(BASE_DIR, "notebooks")
# os.makedirs(DATA_DIR, exist_ok=True)
# os.makedirs(NB_DIR, exist_ok=True)

# def safe_name(s): 
#     return "".join(c for c in s if c.isalnum() or c in ('-', '_'))

# @app.route("/upload_file", methods=["POST"])
# def upload_file():
#     pid = safe_name(request.form.get("participant_id") or request.args.get("participant_id") or "unknown")
#     f = request.files.get("file")
#     if not f:
#         return jsonify({"status": "error", "msg": "no file"}), 400

#     # ✅ 修复 datetime.utcnow() 警告
#     ts = datetime.datetime.now(datetime.UTC).strftime("%Y%m%dT%H%M%S")
#     ext = os.path.splitext(werkzeug.utils.secure_filename(f.filename))[1]
#     user_dir = os.path.join(DATA_DIR, pid)
#     os.makedirs(user_dir, exist_ok=True)
#     path = os.path.join(user_dir, f"{pid}_data_{ts}{ext}")
#     f.save(path)

#     print(f"✅ Received {f.filename} from {pid}, saved to {path}")
#     return jsonify({"status": "ok", "path": path})

# @app.route("/upload_notebook", methods=["POST"])
# def upload_notebook():
#     pid = safe_name(request.form.get("participant_id") or request.args.get("participant_id") or "unknown")
#     f = request.files.get("file")
#     if not f:
#         return jsonify({"status": "error", "msg": "no file"}), 400

#     ts = datetime.datetime.now(datetime.UTC).strftime("%Y%m%dT%H%M%S")
#     user_dir = os.path.join(NB_DIR, pid)
#     os.makedirs(user_dir, exist_ok=True)
#     path = os.path.join(user_dir, f"{pid}_task_{ts}.ipynb")
#     f.save(path)

#     print(f"✅ Received {f.filename} from {pid}, saved to {path}")
#     return jsonify({"status": "ok", "path": path})

# if __name__ == "__main__":
#     print("\n🚀 Backend available at:")
#     print("  🔗 http://127.0.0.1:5050")
#     print("  🔗 http://192.168.0.111:5050")
#     app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5050)))

# from flask import Flask, request, jsonify, send_from_directory, render_template_string
# from flask_cors import CORS
# import os, datetime, werkzeug, pathlib

# app = Flask(__name__)
# CORS(app)

# # ✅ 根路径：展示接口列表
# @app.route("/")
# def index():
#     return render_template_string("""
#     <h2>✅ Backend is running</h2>
#     <ul>
#       <li><a href="/health">GET /health</a></li>
#       <li><a href="/upload_file">GET /upload_file (upload form)</a></li>
#       <li>POST /upload_file</li>
#       <li>POST /upload_notebook</li>
#       <li><a href="/files">GET /files (browse uploaded files)</a></li>
#     </ul>
#     """)

# # ✅ 健康检查
# @app.get("/health")
# def health():
#     return {"status": "ok"}

# # ✅ 路径设定
# BASE_DIR = os.environ.get("SAVE_DIR", "saved_results")
# DATA_DIR = os.path.join(BASE_DIR, "data")
# NB_DIR = os.path.join(BASE_DIR, "notebooks")
# os.makedirs(DATA_DIR, exist_ok=True)
# os.makedirs(NB_DIR, exist_ok=True)

# def safe_name(s): 
#     """防止恶意路径注入"""
#     return "".join(c for c in s if c.isalnum() or c in ('-', '_'))

# # ✅ 上传 CSV 文件
# @app.route("/upload_file", methods=["POST"])
# def upload_file():
#     pid = safe_name(request.form.get("participant_id") or request.args.get("participant_id") or "unknown")
#     f = request.files.get("file")
#     if not f:
#         return jsonify({"status": "error", "msg": "no file"}), 400

#     ts = datetime.datetime.now(datetime.UTC).strftime("%Y%m%dT%H%M%S")
#     ext = os.path.splitext(werkzeug.utils.secure_filename(f.filename))[1]
#     user_dir = os.path.join(DATA_DIR, pid)
#     os.makedirs(user_dir, exist_ok=True)
#     path = os.path.join(user_dir, f"{pid}_data_{ts}{ext}")
#     f.save(path)

#     print(f"✅ Received {f.filename} from {pid}, saved to {path}")
#     return jsonify({"status": "ok", "path": path})

# # ✅ 上传 Notebook 文件
# @app.route("/upload_notebook", methods=["POST"])
# def upload_notebook():
#     pid = safe_name(request.form.get("participant_id") or request.args.get("participant_id") or "unknown")
#     f = request.files.get("file")
#     if not f:
#         return jsonify({"status": "error", "msg": "no file"}), 400

#     ts = datetime.datetime.now(datetime.UTC).strftime("%Y%m%dT%H%M%S")
#     user_dir = os.path.join(NB_DIR, pid)
#     os.makedirs(user_dir, exist_ok=True)
#     path = os.path.join(user_dir, f"{pid}_task_{ts}.ipynb")
#     f.save(path)

#     print(f"✅ Received {f.filename} from {pid}, saved to {path}")
#     return jsonify({"status": "ok", "path": path})

# # ✅ 浏览和下载文件功能
# def _list_dirs(path):
#     p = pathlib.Path(path)
#     return sorted([d.name for d in p.iterdir() if d.is_dir()])

# def _list_files(path):
#     p = pathlib.Path(path)
#     return sorted([f.name for f in p.iterdir() if f.is_file()])

# @app.get("/files")
# def list_root():
#     participants = sorted(set(_list_dirs(DATA_DIR) + _list_dirs(NB_DIR)))
#     html = "<h3>Participants</h3><ul>"
#     for pid in participants:
#         html += f'<li>{pid}: ' \
#                 f'<a href="/files/data/{pid}">data</a> | ' \
#                 f'<a href="/files/notebooks/{pid}">notebooks</a></li>'
#     html += "</ul>"
#     return html or "<p>No uploads yet.</p>"

# @app.get("/files/<kind>/<participant>")
# def list_kind(kind, participant):
#     if kind not in ("data", "notebooks"):
#         return "invalid kind", 400
#     base = DATA_DIR if kind == "data" else NB_DIR
#     folder = os.path.join(base, participant)
#     if not os.path.exists(folder):
#         return "<p>Empty.</p>"
#     files = _list_files(folder)
#     items = "".join(
#         f'<li><a href="/download/{kind}/{participant}/{f}">{f}</a></li>'
#         for f in files
#     )
#     return f"<h3>{kind} / {participant}</h3><ul>{items}</ul>"

# @app.get("/download/<kind>/<participant>/<path:filename>")
# def download(kind, participant, filename):
#     if kind not in ("data", "notebooks"):
#         return "invalid kind", 400
#     base = DATA_DIR if kind == "data" else NB_DIR
#     folder = os.path.join(base, participant)
#     return send_from_directory(folder, filename, as_attachment=False)

# # ✅ 简单的网页上传表单（方便调试）
# @app.get("/upload_file")
# def upload_form():
#     return """
#     <h3>Upload CSV</h3>
#     <form method="post" action="/upload_file" enctype="multipart/form-data">
#       <label>participant_id: <input name="participant_id" value="testuser"></label><br><br>
#       <input type="file" name="file" accept=".csv">
#       <button type="submit">Upload CSV</button>
#     </form>
#     <hr/>
#     <h3>Upload Notebook</h3>
#     <form method="post" action="/upload_notebook" enctype="multipart/form-data">
#       <label>participant_id: <input name="participant_id" value="testuser"></label><br><br>
#       <input type="file" name="file" accept=".ipynb">
#       <button type="submit">Upload Notebook</button>
#     </form>
#     """

# # ✅ 启动服务
# if __name__ == "__main__":
#     print("\n🚀 Backend available at:")
#     print("  🔗 http://127.0.0.1:5050")
#     print("  🔗 http://192.168.0.111:5050")
#     app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5050)))


# from flask import Flask, request, jsonify, send_from_directory, render_template_string
# from flask_cors import CORS
# import os, datetime, werkzeug, pathlib

# app = Flask(__name__)
# CORS(app)

# # ==============================
# # ✅ 配置路径
# # ==============================
# BASE_DIR = os.environ.get("SAVE_DIR", "saved_results")
# DATA_DIR = os.path.join(BASE_DIR, "data")
# NB_DIR = os.path.join(BASE_DIR, "notebooks")
# os.makedirs(DATA_DIR, exist_ok=True)
# os.makedirs(NB_DIR, exist_ok=True)


# # ==============================
# # ✅ 工具函数
# # ==============================
# def safe_name(s):
#     """防止路径注入"""
#     return "".join(c for c in s if c.isalnum() or c in ('-', '_'))


# def save_uploaded_file(file, participant_id, kind="data"):
#     """
#     通用文件保存函数
#     kind: 'data' (csv) 或 'notebook' (ipynb)
#     """
#     pid = safe_name(participant_id or "unknown")
#     ts = datetime.datetime.now(datetime.UTC).strftime("%Y%m%dT%H%M%S")

#     if kind == "data":
#         # ✅ 统一 CSV 命名方式
#         ext = ".csv"
#         user_dir = os.path.join(DATA_DIR, pid)
#         os.makedirs(user_dir, exist_ok=True)
#         filename = f"{pid}_{ts}{ext}"
#         save_path = os.path.join(user_dir, filename)

#     elif kind == "notebook":
#         # ✅ 保存 notebook
#         ext = ".ipynb"
#         user_dir = os.path.join(NB_DIR, pid)
#         os.makedirs(user_dir, exist_ok=True)
#         filename = f"{pid}_{ts}{ext}"
#         save_path = os.path.join(user_dir, filename)

#     else:
#         raise ValueError("kind must be 'data' or 'notebook'")

#     file.save(save_path)
#     print(f"✅ Saved {filename} to {save_path}")
#     return save_path


# # ==============================
# # ✅ 首页（API概览）
# # ==============================
# @app.route("/")
# def index():
#     return render_template_string("""
#     <h2>✅ Backend is running</h2>
#     <ul>
#       <li><a href="/health">GET /health</a></li>
#       <li><a href="/upload_file">GET /upload_file (upload form)</a></li>
#       <li>POST /upload_file — Upload CSV</li>
#       <li>POST /upload_notebook — Upload Notebook</li>
#       <li><a href="/files">GET /files — Browse uploaded files</a></li>
#     </ul>
#     """)


# # ==============================
# # ✅ 健康检查
# # ==============================
# @app.get("/health")
# def health():
#     return {"status": "ok"}


# # ==============================
# # ✅ 上传 CSV
# # ==============================
# @app.route("/upload_file", methods=["POST"])
# def upload_file():
#     f = request.files.get("file")
#     pid = request.form.get("participant_id") or request.args.get("participant_id") or "unknown"
#     if not f:
#         return jsonify({"status": "error", "msg": "no file"}), 400

#     path = save_uploaded_file(f, pid, kind="data")
#     return jsonify({"status": "ok", "path": path})


# # ==============================
# # ✅ 上传 Notebook（保存修改后的文件）
# # ==============================
# @app.route("/upload_notebook", methods=["POST"])
# def upload_notebook():
#     f = request.files.get("file")
#     pid = request.form.get("participant_id") or request.args.get("participant_id") or "unknown"
#     if not f:
#         return jsonify({"status": "error", "msg": "no file"}), 400

#     path = save_uploaded_file(f, pid, kind="notebook")
#     return jsonify({"status": "ok", "path": path})


# # ==============================
# # ✅ 文件浏览和下载
# # ==============================
# def _list_dirs(path):
#     p = pathlib.Path(path)
#     return sorted([d.name for d in p.iterdir() if d.is_dir()])


# def _list_files(path):
#     p = pathlib.Path(path)
#     return sorted([f.name for f in p.iterdir() if f.is_file()])


# @app.get("/files")
# def list_root():
#     participants = sorted(set(_list_dirs(DATA_DIR) + _list_dirs(NB_DIR)))
#     html = "<h3>Participants</h3><ul>"
#     for pid in participants:
#         html += f'<li>{pid}: ' \
#                 f'<a href="/files/data/{pid}">data</a> | ' \
#                 f'<a href="/files/notebooks/{pid}">notebooks</a></li>'
#     html += "</ul>"
#     return html or "<p>No uploads yet.</p>"


# @app.get("/files/<kind>/<participant>")
# def list_kind(kind, participant):
#     if kind not in ("data", "notebooks"):
#         return "invalid kind", 400
#     base = DATA_DIR if kind == "data" else NB_DIR
#     folder = os.path.join(base, participant)
#     if not os.path.exists(folder):
#         return "<p>Empty.</p>"
#     files = _list_files(folder)
#     items = "".join(
#         f'<li><a href="/download/{kind}/{participant}/{f}">{f}</a></li>'
#         for f in files
#     )
#     return f"<h3>{kind} / {participant}</h3><ul>{items}</ul>"


# @app.get("/download/<kind>/<participant>/<path:filename>")
# def download(kind, participant, filename):
#     if kind not in ("data", "notebooks"):
#         return "invalid kind", 400
#     base = DATA_DIR if kind == "data" else NB_DIR
#     folder = os.path.join(base, participant)
#     return send_from_directory(folder, filename, as_attachment=False)


# # ==============================
# # ✅ 简易网页上传表单（方便手动测试）
# # ==============================
# @app.get("/upload_file")
# def upload_form():
#     return """
#     <h3>Upload CSV</h3>
#     <form method="post" action="/upload_file" enctype="multipart/form-data">
#       <label>participant_id: <input name="participant_id" value="testuser"></label><br><br>
#       <input type="file" name="file" accept=".csv">
#       <button type="submit">Upload CSV</button>
#     </form>
#     <hr/>
#     <h3>Upload Notebook</h3>
#     <form method="post" action="/upload_notebook" enctype="multipart/form-data">
#       <label>participant_id: <input name="participant_id" value="testuser"></label><br><br>
#       <input type="file" name="file" accept=".ipynb">
#       <button type="submit">Upload Notebook</button>
#     </form>
#     """


# # ==============================
# # ✅ 启动
# # ==============================
# if __name__ == "__main__":
#     print("\n🚀 Backend available at:")
#     print("  🔗 http://127.0.0.1:5050")
#     print("  🔗 http://192.168.0.111:5050")
#     app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5050)))

from flask import Flask, request, jsonify, send_from_directory, render_template_string
from flask_cors import CORS
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
import os, datetime, werkzeug, pathlib

app = Flask(__name__)
CORS(app)

# ==============================
# ✅ 配置路径
# ==============================
BASE_DIR = os.environ.get("SAVE_DIR", "saved_results")
DATA_DIR = os.path.join(BASE_DIR, "data")
NB_DIR = os.path.join(BASE_DIR, "notebooks")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(NB_DIR, exist_ok=True)

# ==============================
# ✅ Google Drive 配置
# ==============================
CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("GOOGLE_REFRESH_TOKEN")
FOLDER_ID = os.getenv("GOOGLE_DRIVE_FOLDER_ID", None)  # 可选，Drive 文件夹 ID

def get_drive_service():
    """创建 Drive API 客户端"""
    creds = Credentials(
        None,
        refresh_token=REFRESH_TOKEN,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scopes=["https://www.googleapis.com/auth/drive.file"]
    )
    return build("drive", "v3", credentials=creds)

def upload_to_drive(local_path, participant_id):
    """上传文件到 Google Drive"""
    service = get_drive_service()
    filename = os.path.basename(local_path)

    metadata = {"name": filename}
    if FOLDER_ID:
        metadata["parents"] = [FOLDER_ID]

    media = MediaFileUpload(local_path, resumable=True)
    file = service.files().create(body=metadata, media_body=media, fields="id, webViewLink").execute()
    print(f"☁️ Uploaded to Drive: {file['id']} → {file['webViewLink']}")
    return file["webViewLink"]

# ==============================
# ✅ 工具函数
# ==============================
def safe_name(s):
    return "".join(c for c in s if c.isalnum() or c in ('-', '_'))

def save_uploaded_file(file, participant_id, kind="data"):
    pid = safe_name(participant_id or "unknown")
    ts = datetime.datetime.now(datetime.UTC).strftime("%Y%m%dT%H%M%S")

    if kind == "data":
        ext = ".csv"
        user_dir = os.path.join(DATA_DIR, pid)
    elif kind == "notebook":
        ext = ".ipynb"
        user_dir = os.path.join(NB_DIR, pid)
    else:
        raise ValueError("kind must be 'data' or 'notebook'")

    os.makedirs(user_dir, exist_ok=True)
    filename = f"{pid}_{ts}{ext}"
    save_path = os.path.join(user_dir, filename)
    file.save(save_path)
    print(f"✅ Saved {filename} to {save_path}")
    return save_path

# ==============================
# ✅ 首页（API概览）
# ==============================
@app.route("/")
def index():
    return render_template_string("""
    <h2>✅ Backend with Google Drive Sync</h2>
    <ul>
      <li><a href="/health">GET /health</a></li>
      <li><a href="/upload_file">GET /upload_file (upload form)</a></li>
      <li>POST /upload_file — Upload CSV (auto sync to Drive)</li>
      <li>POST /upload_notebook — Upload Notebook (auto sync to Drive)</li>
      <li><a href="/files">GET /files — Browse uploaded files</a></li>
    </ul>
    """)

@app.get("/health")
def health():
    return {"status": "ok"}

# ==============================
# ✅ 上传 CSV + 同步到 Google Drive
# ==============================
@app.route("/upload_file", methods=["POST"])
def upload_file():
    f = request.files.get("file")
    pid = request.form.get("participant_id") or "unknown"
    if not f:
        return jsonify({"status": "error", "msg": "no file"}), 400

    local_path = save_uploaded_file(f, pid, kind="data")
    try:
        drive_link = upload_to_drive(local_path, pid)
    except Exception as e:
        drive_link = None
        print(f"❌ Drive upload failed: {e}")

    return jsonify({
        "status": "ok",
        "path": local_path,
        "drive_link": drive_link
    })

# ==============================
# ✅ 上传 Notebook + 同步到 Google Drive
# ==============================
@app.route("/upload_notebook", methods=["POST"])
def upload_notebook():
    f = request.files.get("file")
    pid = request.form.get("participant_id") or "unknown"
    if not f:
        return jsonify({"status": "error", "msg": "no file"}), 400

    local_path = save_uploaded_file(f, pid, kind="notebook")
    try:
        drive_link = upload_to_drive(local_path, pid)
    except Exception as e:
        drive_link = None
        print(f"❌ Drive upload failed: {e}")

    return jsonify({
        "status": "ok",
        "path": local_path,
        "drive_link": drive_link
    })

# ==============================
# ✅ 文件浏览和下载（保留原逻辑）
# ==============================
def _list_dirs(path):
    p = pathlib.Path(path)
    return sorted([d.name for d in p.iterdir() if d.is_dir()])

def _list_files(path):
    p = pathlib.Path(path)
    return sorted([f.name for f in p.iterdir() if f.is_file()])

@app.get("/files")
def list_root():
    participants = sorted(set(_list_dirs(DATA_DIR) + _list_dirs(NB_DIR)))
    html = "<h3>Participants</h3><ul>"
    for pid in participants:
        html += f'<li>{pid}: <a href="/files/data/{pid}">data</a> | <a href="/files/notebooks/{pid}">notebooks</a></li>'
    html += "</ul>"
    return html or "<p>No uploads yet.</p>"

@app.get("/files/<kind>/<participant>")
def list_kind(kind, participant):
    if kind not in ("data", "notebooks"):
        return "invalid kind", 400
    base = DATA_DIR if kind == "data" else NB_DIR
    folder = os.path.join(base, participant)
    if not os.path.exists(folder):
        return "<p>Empty.</p>"
    files = _list_files(folder)
    items = "".join(f'<li><a href="/download/{kind}/{participant}/{f}">{f}</a></li>' for f in files)
    return f"<h3>{kind} / {participant}</h3><ul>{items}</ul>"

@app.get("/download/<kind>/<participant>/<path:filename>")
def download(kind, participant, filename):
    base = DATA_DIR if kind == "data" else NB_DIR
    folder = os.path.join(base, participant)
    return send_from_directory(folder, filename, as_attachment=False)

# ==============================
# ✅ 启动
# ==============================
if __name__ == "__main__":
    print("\n🚀 Backend with Google Drive Sync running:")
    print("  🔗 http://127.0.0.1:5050")
    print("  🔗 http://192.168.0.111:5050")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5050)))
