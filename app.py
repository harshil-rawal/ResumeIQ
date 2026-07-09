import os
import uuid
from flask import Flask, render_template, request
from services.resume_analyzer import analyze_resume
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload-page")
def upload_page():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    
    if "resume" not in request.files:
        return "Resume file is required.", 400

    resume = request.files["resume"]
    
    if not resume.filename:
        return "No file selected.", 400
    
    original_filename = secure_filename(resume.filename)

    extension = os.path.splitext(original_filename)[1]

    filename = f"{uuid.uuid4()}{extension}"
    print(f"Generated filename: {filename}")

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    resume.save(filepath)

    try:

        analysis = analyze_resume(filepath)

    finally:

        if os.path.exists(filepath):

            os.remove(filepath)

    return render_template(
        "result.html",
        analysis=analysis
    )

if __name__ == "__main__":
    app.run(debug=True)