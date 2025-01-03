from flask import Flask, send_file, render_template
import os

app = Flask(__name__)

RESUME_FOLDER = "files"
RESUME_FILENAME = "resume.pdf"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/skill", methods=["GET","POST"])
def skill():
    return render_template("skill.html")

@app.route("/project", methods=["GET","POST"])
def project():
    return render_template("project.html")

@app.route('/resume', methods=['GET'])
def resume():
    return render_template("resume.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    return render_template("contact.html")

@app.route("/about", methods=["GET","POST"])
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
