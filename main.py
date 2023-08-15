import panel as pn
import pandas as pd
import subprocess
import folium
from folium.plugins import MarkerCluster, HeatMap
from flask import Flask, render_template

app = Flask(__name__)

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

@app.route("/book")
def book():
    return render_template("book.html")


if __name__ == "__main__":
    processes = [
        subprocess.Popen(['panel', 'serve', 'heatmaps.py', '--port', '5007', '--allow-websocket-origin=*']),
        subprocess.Popen(['panel', 'serve', 'other_maps.py', '--port', '5008', '--allow-websocket-origin=*'])
    ]

    app.run(debug=True)

    for process in processes:
        process.wait()
