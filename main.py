import subprocess
import pandas as pd
from flask import Flask, render_template, url_for, redirect
from register import RegistrationForm, LoginForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "SOME_PASSWORD_OVER_HERE"

conquests = pd.read_csv("data.csv")
conquests["Opponent leader"].fillna("Bilinmiyor", inplace=True)
conquests["Sene"].fillna("Bilinmiyor", inplace=True)
conquests["Success"]=conquests["Success"].astype(str)
conquests["isOpponentMuslim"]=conquests["isOpponentMuslim"].astype(str)

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

@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for("index"))
    return render_template("register.html", form=form)


if __name__ == "__main__":
    processes = [
        subprocess.Popen(['panel', 'serve', 'heatmaps.py', '--port', '5007', '--allow-websocket-origin=*']),
        subprocess.Popen(['panel', 'serve', 'other_maps.py', '--port', '5008', '--allow-websocket-origin=*']),
        subprocess.Popen(['panel', 'serve', 'plot.py', '--port', '5010', '--allow-websocket-origin=*'])
    ]

    app.run(debug=True)

    for process in processes:
        process.wait()
