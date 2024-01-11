from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("vid31.html")

@app.route("/login", methods=["POST", "GET"])
def test():
    if request.method == "POST":
        session.permanent = True
        user = request.form['nm']
        session["user"] = user
        flash("Login Successfull")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Login")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session['user']
        return render_template("user.html", user=user)
    else:
        flash("Login First")
        return render_template("login.html")
    
@app.route("/logout")
def logout():
    flash(f"you have been log out!", "info")
    session.pop("user", None)
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True);