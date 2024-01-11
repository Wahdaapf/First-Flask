from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello My Name is <h1>Wahda</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/admin1")
def admin1():
    return redirect(url_for("user", name="wahda"))

if __name__ == "__main__":
    app.run();