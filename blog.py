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

def update_map(event):
#deneme commiti
    selected_king = king_selector.value
    subset = conquests[conquests["Era"] == selected_king]

    color_map = {
        "Ertuğrul Gazi": "blue",
        "Osman Gazi": "red",
        "Orhan Gazi": "pink",
        "Murad I (Hüdavendigar)": "orange",
        "Bayezid I (Yıldırım)": "purple",
        "Fetret Dönemi": "black",
        "Mehmed I (Çelebi)": "brown",
        "Murad II": "cadetblue",
        "Mehmed II (Fatih)": "gray",
        "Bayezid II": "darkred",
    }
    map_plot = folium.Map(location=[subset["lat"].mean()-2, subset["lon"].mean()+5], zoom_start=5, width=800, height=600)
    marker_cluster = MarkerCluster().add_to(map_plot)

    for _, row in subset.iterrows():
        html = f""" <h1> Fetih Hakkında</h1>
                    <p> Dönem: {row['Era']}  <br>
                    Sene: {row['Sene']}   <br>
                    Yerin Adı: {row['Yerin Adı']}  <br>
                    Olay: {"Başarılı " if (row['Success']== "1") else "Başarısız "} {row['Niyet']} <br>
                    Osmanlı Lideri: {row['Ottoman leaders']}  <br>
                    Düşman Lideri: {row['Opponent leader']}   <br>
                    Yöntem: {row['Method'].capitalize()}  <br>
                    Düşman Müslüman mı: {"Evet" if row['isOpponentMuslim'] == "1.0" else "Hayır"}</p> 
                    <a href="https://tr.wikipedia.org/wiki/{row['Yerin Adı']}" target="_blank">
                        <button>{row['Yerin Adı']} nasıl bir yer?</button>
                    </a>
                """
        iframe = folium.IFrame(html,
                               width=250,
                               height=225)
        popup = folium.Popup(iframe, parse_html=True, max_width=245)
        folium.Marker([row["lat"], row["lon"]], icon=folium.Icon(color=color_map[row["Era"]]), popup=popup).add_to(
            marker_cluster)

    map_div.object = map_plot._repr_html_()


def update_slider_map(event):
    n = slider.value
    subset = conquests.loc[0:n, :]

    color_map = {

        "Ertuğrul Gazi": "blue",
        "Osman Gazi": "red",
        "Orhan Gazi": "pink",
        "Murad I (Hüdavendigar)": "orange",
        "Bayezid I (Yıldırım)": "purple",
        "Fetret Dönemi": "black",
        "Mehmed I (Çelebi)": "brown",
        "Murad II": "cadetblue",
        "Mehmed II (Fatih)": "gray",
        "Bayezid II": "darkred",

    }
    map_plot = folium.Map(location=[subset["lat"].mean()-1, subset["lon"].mean()+5], zoom_start=5, width=800, height=600)
    marker_cluster = MarkerCluster().add_to(map_plot)

    for _, row in subset.iterrows():
        html = f""" <h1> Fetih Hakkında</h1>
                    <p> Dönem: {row['Era']}  <br>
                    Sene: {row['Sene']}   <br>
                    Yerin Adı: {row['Yerin Adı']}  <br>
                    Olay: {"Başarılı " if (row['Success']== "1") else "Başarısız "} {row['Niyet']} <br>
                    Osmanlı Lideri: {row['Ottoman leaders']}  <br>
                    Düşman Lideri: {row['Opponent leader']}   <br>
                    Yöntem: {row['Method'].capitalize()}  <br>
                    Düşman Müslüman mı: {"Evet" if row['isOpponentMuslim'] == "1.0" else "Hayır"}</p> 
                    <a href="https://tr.wikipedia.org/wiki/{row['Yerin Adı']}" target="_blank">
                        <button>{row['Yerin Adı']} nasıl bir yer?</button>
                    </a>
                """
        iframe = folium.IFrame(html,
                               width=250,
                               height=225)
        popup = folium.Popup(iframe, parse_html=True, max_width=245)
        folium.Marker([row["lat"], row["lon"]], icon=folium.Icon(color=color_map[row["Era"]]), popup=popup).add_to(
            marker_cluster)

    slider_map_div.object = map_plot._repr_html_()

def update_heatmap(event):
    selected_era = king_selector_.value

    num = conquests[conquests.Era == selected_era].index[-1]
    subset = conquests.loc[:num, :]  # padişahları kümülatif almak için yaptık bunun yanında categorize da denenebilir ama bu daha kısa bi koddu

    map_plot = folium.Map(location=[subset["lat"].mean()-1, subset["lon"].mean()+5], zoom_start=5, width=800, height=600)

    heat_data = [[row["lat"], row["lon"]] for index, row in subset.iterrows()]
    HeatMap(heat_data).add_to(map_plot)

    #update


    heat_map_div.object = map_plot._repr_html_()

def update_slider_HeatMap(event):
    n = slider2.value
    subset = conquests.loc[0:n, :]


    map_plot = folium.Map(location=[subset["lat"].mean()-1, subset["lon"].mean()+5], zoom_start=5, width=800, height=600)
    heat_data = [[row["lat"], row["lon"]] for index, row in subset.iterrows()]
    HeatMap(heat_data).add_to(map_plot)

    slider2_map_div.object = map_plot._repr_html_()


pn.extension()

# Slider
slider = pn.widgets.IntSlider(value=0, start=0, end=228)
slider.param.watch(update_slider_map, "value")

slider_map_div = pn.pane.HTML(height = 600,width=800)

# King Selector
king_selector = pn.widgets.Select(options=conquests["Era"].unique().tolist())
king_selector.param.watch(update_map, "value")

map_div = pn.pane.HTML(height = 600,width=800)

#Heat Map

slider2 = pn.widgets.IntSlider(value=0, start=0, end=228)
slider2.param.watch(update_slider_HeatMap, "value")

slider2_map_div = pn.pane.HTML(height = 600,width=800)

#Heat Map Padisah

king_selector_ = pn.widgets.Select(options=conquests["Era"].unique().tolist())
king_selector_.param.watch(update_heatmap, "value")

heat_map_div = pn.pane.HTML(height = 600,width=800)

# Layout
slider_layout = pn.Row(slider, slider_map_div)
king_selector_layout = pn.Row(king_selector, map_div)
slider2_layout = pn.Row(slider2, slider2_map_div)
heat_map_layout = pn.Row(king_selector_, heat_map_div)

app_layout = pn.Column(slider_layout, king_selector_layout, slider2_layout, heat_map_layout, sizing_mode='stretch_both')
update_slider_map(None)
update_map(None)
update_slider_HeatMap(None)
update_heatmap(None)
app_layout.servable()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/maps")
def maps():
    return render_template("maps.html")

@app.route("/book")
def book():
    return render_template("book.html")


if __name__ == "__main__":
    panel_process = subprocess.Popen(['panel', 'serve', 'blog.py', '--allow-websocket-origin=*'])
    app.run(debug=True)
    panel_process.terminate()
