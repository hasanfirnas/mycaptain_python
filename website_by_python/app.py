import os
from flask import Flask, session, redirect, url_for, render_template, request, jsonify, flash, abort, make_response
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_caching import Cache

#from helpers import *
cache=Cache()

if not os.getenv('DATABASE_URL'):
    conn = sqlite3.connect("userdb.db", check_same_thread=False)
    c = conn.cursor()
    print("1")
else:
    engine = create_engine(os.getenv("DATABASE_URL"))
    db = scoped_session(sessionmaker(bind=engine))
    conn = db()
    c = conn
    print("2")


app = Flask(__name__,static_folder='static')
app.config["SECRET_KEY"] = "secretkey"
app.config['CACHE_TYPE'] = 'simple'

cache.init_app(app)

BASE_URL = "0.0.0.0:8080/"


@app.route("/js/preloader.js", methods=["GET", "POST"])
def send_js(path):
    path="js/"
    return send_from_directory('js', path)

@app.route("/", methods=["GET", "POST"])
def mainpage():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if the form is valid
            print("register")
            if not request.form.get("username") or not request.form.get("password") or not request.form.get("confirmation"):
                return "please fill out all fields"

            if request.form.get("password") != request.form.get("confirmation"):
                return "password confirmation doesn't match password"

            # check if email exist in the database
            exist = c.execute("SELECT * FROM users WHERE email=:email", {"email": request.form.get("username")}).fetchall()

            if len(exist) != 0:
                return "user already registered"

            # hash the password
            pwhash =  request.form.get("password") ## request.form.get("password") ###generate_password_hash(request.form.get("password"), method="pbkdf2:sha256", salt_length=8)

            # insert the row
            c.execute("INSERT INTO users (email, password) VALUES (:email, :password)", {"email": request.form.get("username"), "password": pwhash})
            conn.commit()

            # return success
            flash("registered successfully!")
            return render_template("register.html")
    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        # check the form is valid
        if not request.form.get("username") or not request.form.get("password"):
            abort(404)
            return "please fill out all required fields"

        # check if username exist in the database
        user = c.execute("SELECT * FROM users WHERE email=:email", {"email": request.form.get("username")}).fetchall()
        print(user)
        print("user")
        if len(user) != 1:
            abort(404)

        # check the password is same to password hash
        pwhash = user[0][2]
        if pwhash != request.form.get('password') == False: #if     pwhash != request.form.get('password') ##check_password_hash(pwhash, request.form.get("password"))
            return "wrong password"

        # login the user using session
        session["user_id"] = user[0][0]

        # return success
        print(request.form.get('username'))
        print(request.form.get('password')) 
        if request.form.get('username') == user[0][1] and request.form.get('password') == user[0][2]:
            if request.form.get('username') == "Joshwa" and request.form.get('password') == user[0][2]:
                print("got it")
                return render_template("flag.html")
            #return "logged in root successfully! "
            #resp =make_response('setting cookie')
            #resp =set_cookie("test", "abdadad1esddc")
            else:
                return render_template("success.html")
        else:
            #return "wrong password"
            #return render_template("fail.html")
            abort(500)

    else:
        return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/logout")
@cache.cached(timeout=1)
def logout():
    session.clear()
    print("logout......")
    return redirect(url_for("login"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)