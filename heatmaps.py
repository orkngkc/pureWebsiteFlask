from main import *
import folium
from folium.plugins import MarkerCluster, HeatMap
import panel as pn
def update_heatmap(event):
    selected_era = king_selector_.value

    num = conquests[conquests.Era == selected_era].index[-1]
    subset = conquests.loc[:num, :]  # padişahları kümülatif almak için yaptık bunun yanında categorize da denenebilir ama bu daha kısa bi koddu

    map_plot = folium.Map(location=[subset["lat"].mean()-1, subset["lon"].mean()+5], zoom_start=5, width=800, height=600, control_scale=True, tiles="Stamen Terrain")

    heat_data = [[row["lat"], row["lon"]] for index, row in subset.iterrows()]
    HeatMap(heat_data).add_to(map_plot)

    #update


    heat_map_div.object = map_plot._repr_html_()


def update_slider_HeatMap(event):
    n = slider2.value
    subset = conquests.loc[0:n, :]


    map_plot = folium.Map(location=[subset["lat"].mean()-1, subset["lon"].mean()+5], zoom_start=5, width=800, height=600, control_scale=True, tiles="Stamen Terrain")


    heat_data = [[row["lat"], row["lon"]] for index, row in subset.iterrows()]
    HeatMap(heat_data).add_to(map_plot)

    slider2_map_div.object = map_plot._repr_html_()


king_selector_ = pn.widgets.Select(options=conquests["Era"].unique().tolist())
king_selector_.param.watch(update_heatmap, "value")

heat_map_div = pn.pane.HTML(height = 600,width=800)

slider2 = pn.widgets.IntSlider(value=0, start=0, end=228)
slider2.param.watch(update_slider_HeatMap, "value")

slider2_map_div = pn.pane.HTML(height = 600,width=800)
update_slider_HeatMap(None)
update_heatmap(None)
heatmap_tab = pn.Column(king_selector_, heat_map_div)

# Create a tab for the second heatmap and slider
slider_tab = pn.Column(slider2, slider2_map_div)

# Create a Tabs widget with the two tabs
tabs = pn.Tabs(
    ("King Selector Heatmap", heatmap_tab),
    ("Slider Heatmap", slider_tab)
)


tabs.servable()
