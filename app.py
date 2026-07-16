import os
import uuid
from flask import Flask, render_template, request, session, jsonify
from services.resume_analyzer import analyze_resume
from werkzeug.utils import secure_filename

from utils.pdf_report import generate_pdf_report
from flask import send_file

app = Flask(__name__)
app.secret_key = "resumeiq-dev-secret"
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
        session["resume_report"] = {

            "ats": analysis["ats"],

            "skills": analysis["skills"],

            "statistics": analysis["statistics"],

            "top_missing_skills": analysis["top_missing_skills"],

            "ai_feedback": analysis["ai_feedback"]

        }
        
    except Exception as e:
        app.logger.exception("Resume analysis failed")
        return (
            "Something went wrong while analyzing the resume. Please try again.",
            500
        )

    finally:

        if os.path.exists(filepath):

            os.remove(filepath)

    return render_template(
        "result.html",
        analysis=analysis
    )

@app.route("/test-session")
def test_session():

    report = session.get("resume_report")

    if report is None:
        return jsonify({"message": "No report found in session"}), 404

    return jsonify(report)

@app.route("/download-report")
def download_report():

    report = session.get("resume_report")

    if report is None:
        return "No report available.", 404

    from datetime import datetime
    filename = (
        f"ResumeIQ_Report_"
        f"{datetime.now().strftime('%Y-%m-%d')}.pdf"
    )

    output_path = filename

    generate_pdf_report(
        report,
        output_path
    )

    return send_file(
        output_path,
        as_attachment=True,
        download_name=filename
    )

if __name__ == "__main__":
    app.run(debug=True)