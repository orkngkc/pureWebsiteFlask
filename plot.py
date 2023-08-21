import panel as pn
import pandas as pd
import plotly.express as px

pn.extension("plotly")
tipler = pd.read_csv("Tipler_csv.csv")

def update_plot(event):
    selected_king = king_selector.value
    subset = tipler[tipler["Padişah Dönemi"] == selected_king]["Sosyal Grup"].value_counts()
    fig = px.bar(subset, x=subset.index, y=subset.values, title="Sosyal Grup Sayıları")
    return fig




king_selector = pn.widgets.Select(options=tipler["Padişah Dönemi"].unique().tolist())
king_selector.param.watch(update_plot, "value")

zort = update_plot(None)

responsive = pn.pane.Plotly(zort)

lay = pn.Column(king_selector,responsive)
lay.servable()

