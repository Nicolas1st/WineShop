from flask import Flask, render_template, url_for, request, redirect, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)
app.secret_key = "Hello to the World"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)


db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    login = db.Column(db.String(100))
    address = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, login, email, address):
        self.login = login
        self.email = email
        self.address = address

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login/", methods=["GET", "POST"])
def login():
    if "user" in session:
        return redirect(url_for("profile"))
    if request.method == "POST":
        user = users.query.filter_by(login=request.form["login"]).first()
        if user:
            session['user'] = user
            return redirect(url_for("profile", user_login=user.__dict__))
        # else:
        #     return redirect(url_for("register"))
        return redirect(url_for("login"))
    else:
        return render_template("login.html")


@app.route("/profile/")
def profile(user_login):
    if "user" in session:
        return render_template("profile.html")
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/basket/")
def basket():
    return render_template("basket.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        login = request.form["login"]
        email = request.form["email"]
        address = request.form["address"]
        password = request.form["password"]
        repeated_password = request.form["repeated_password"]
        if users.query.filter_by(login=login).first():
            flash("The login you chose is already occupied")
        elif users.query.filter_by(email=email).first():
            flash("There is already an account using this email")
        elif password != repeated_password:
            flash("Password don't match")
        else:
            user = users(login, email, address)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('profile', context=user.__dict__))
    return render_template("registering.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
