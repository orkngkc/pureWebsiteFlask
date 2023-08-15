from blog import *

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
                    Sene: {row['Sene'][-4:]}   <br>
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
                    Sene: {row['Sene'][-4:]}   <br>
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


slider = pn.widgets.IntSlider(value=0, start=0, end=228)
slider.param.watch(update_slider_map, "value")

slider_map_div = pn.pane.HTML(height = 600,width=800)

# King Selector
king_selector = pn.widgets.Select(options=conquests["Era"].unique().tolist())
king_selector.param.watch(update_map, "value")

map_div = pn.pane.HTML(height = 600,width=800)

slider_layout = pn.Row(slider, slider_map_div)
king_selector_layout = pn.Row(king_selector, map_div)

maps_layout = pn.Column(slider_layout, king_selector_layout)

update_slider_map(None)
update_map(None)

maps_layout.servable()