from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("vid31.html")

@app.route("/test")
def test():
    return render_template("new.html")

if __name__ == "__main__":
    app.run(debug=True);