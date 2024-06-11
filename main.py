import subprocess
import pandas as pd
from flask import Flask, render_template, url_for, redirect, request, flash, session
#from register import RegistrationForm, LoginForm
#rom passlib.hash import sha256_crypt
#from flask_mysqldb import MySQL


app = Flask(__name__)
app.config["SECRET_KEY"] = "SOME_PASSWORD_OVER_HERE"

conquests = pd.read_csv("data.csv")
conquests["Opponent leader"].fillna("Bilinmiyor", inplace=True)
conquests["Sene"].fillna("Bilinmiyor", inplace=True)
conquests["Success"]=conquests["Success"].astype(str)
conquests["isOpponentMuslim"]=conquests["isOpponentMuslim"].astype(str)

#mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/heatmaps")
def heatmaps():
    return render_template("heatmaps.html")

@app.route("/other_maps")
def other_maps():
    return render_template("other_maps.html")

@app.route("/plot")
def plots():
    return render_template("plot.html")

@app.route("/book")
def book():
    return render_template("book.html")
"""
@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()

        inquiry = "INSERT into users(username, email, password) VALUES(%s,%s,%s)"

        cursor.execute(inquiry, (username, email, password))  # if you gave one elemnt tuple to inquiry you should write like this: (name,)
        mysql.connection.commit()

        cursor.close()

        flash(message="Başarıyla kayıt oldunuz...", category="success")

        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        username = form.username.data
        password_entered = form.password.data

        cursor = mysql.connection.cursor()

        inquiry = "Select * From users where username = %s"

        result = cursor.execute(inquiry, (username,))

        if result > 0:
            data = cursor.fetchone()
            real_password = data["password"]
            cursor.close()

            if sha256_crypt.verify(password_entered, real_password):
                flash(message="Başarıyla giriş yaptınız!", category="success")

                session["logged_in"] = True
                session["username"] = username

                return redirect(url_for("index"))
            else:
                flash(message="Şifrenizi yanlış girdiniz...", category="danger")

                return redirect(url_for("login"))
        else:
            flash("Böyle bir kullanıcı bulunmuyor", "danger")
            return redirect(url_for("login"))
    else:

        return render_template("login.html", form=form)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()

    flash("Başarıyla çıkış yaptınız...", "success")

    return redirect(url_for("index"))
"""

if __name__ == "__main__":
    processes = [
        subprocess.Popen(['panel', 'serve', 'heatmaps.py', '--port', '5007', '--allow-websocket-origin=*']),
        subprocess.Popen(['panel', 'serve', 'other_maps.py', '--port', '5008', '--allow-websocket-origin=*']),
        subprocess.Popen(['panel', 'serve', 'plot.py', '--port', '5010', '--allow-websocket-origin=*'])
    ]

    app.run(debug=True)

    for process in processes:
        process.wait()
