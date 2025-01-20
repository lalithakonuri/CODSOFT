
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/details", methods=["GET", "POST"])
def details():
    return render_template("details.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)