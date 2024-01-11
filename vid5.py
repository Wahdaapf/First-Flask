from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("vid31.html")

@app.route("/login", methods=["POST", "GET"])
def test():
    if request.method == "POST":
        user = request.form['nm']
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session['user']
        return f"Hello {user}"
    else:
        return render_template("login.html")
    
@app.route("/logout")
def logout():
    session.pop("user", None)
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True);