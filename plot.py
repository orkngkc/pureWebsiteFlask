import plotly.express as px
import pandas as pd
import panel as pn

tipler = pd.read_excel("Tipler Revize.xlsx")
tipler["Padişah Dönemi"] = tipler["Padişah Dönemi"].str.strip()
sultan_list = tipler["Padişah Dönemi"].unique().tolist()

pn.extension("plotly")


def update_plot(selected_king):
    subset = tipler[tipler["Padişah Dönemi"] == selected_king]["Sosyal Grup"].value_counts()

    # Create a bar trace using go.Bar
    fig = px.bar(subset, x=subset.index, y=subset.values,
                 color='Sosyal Grup',
                 title=f"{selected_king} Dönemi Öncesi Sosyal Gruplar",
                 labels={'pop': 'Sosyal Gruplar', "y": "Count", "x": "Sosyal Gruplar"}, height=400)

    return fig


king_selector = pn.widgets.Select(options=sultan_list)
# Get the initial figure with data

initial_fig = update_plot(king_selector.value)

responsive = pn.pane.Plotly(initial_fig, height=600, width=800)  # Create the responsive pane with the initial figure


def selector_callback(event):
    selected_king = event.new
    updated_fig = update_plot(selected_king)
    responsive.object = updated_fig


king_selector.param.watch(selector_callback, "value")

lay = pn.Column(king_selector, responsive)
lay.servable()