from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    return render_template("result.html")


# @app.route("/upload", methods=["POST"])
# def upload():

#     resume = request.files["resume"]

#     return f"Received file: {resume.filename}"

@app.route("/upload-page")
def upload_page():
    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)