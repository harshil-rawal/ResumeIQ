from flask import Flask, render_template, request, jsonify
from services.resume_analyzer import analyze_resume

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload-page")
def upload_page():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():

    resume = request.files["resume"]

    filepath = f"uploads/{resume.filename}"

    resume.save(filepath)

    analysis = analyze_resume(filepath)

    # Temporary while result.html is under development
    return jsonify(analysis)


if __name__ == "__main__":
    app.run(debug=True)