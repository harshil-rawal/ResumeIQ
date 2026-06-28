from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():

    resume = request.files["resume"]

    return f"Received file: {resume.filename}"


if __name__ == "__main__":
    app.run(debug=True)