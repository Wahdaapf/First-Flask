from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    def __init__(self, name, email):
        self.name = name
        self.email = email

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

@app.route("/user", methods=['POST', 'GET'])
def user():
    email = None
    if "user" in session:
        user = session['user']
        if request.methods == 'POST':
            email = request.form['email']
            session['email'] = email
            flash("email was saved")
        else:
            if "email" in session:
                email = session['email']
        return render_template("user.html", user=user, email=email)
    else:
        flash("Login First")
        return render_template("login.html")
    
@app.route("/logout")
def logout():
    flash(f"you have been log out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True);