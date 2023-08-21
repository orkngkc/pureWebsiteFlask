import plotly.express as px
import pandas as pd
import panel as pn
from pandas.api.types import CategoricalDtype

tipler = pd.read_excel("Tipler Revize.xlsx")
tipler["Padişah Dönemi"] = tipler["Padişah Dönemi"].str.strip()
sultan_list = tipler["Padişah Dönemi"].unique().tolist()
sultan_list.insert(1, 'Ertuğrul Gazi')
sultan_list.pop()
cat_dtype = CategoricalDtype(categories = sultan_list, ordered = True)
tipler["Padişah Dönemi"] = tipler["Padişah Dönemi"].astype(cat_dtype)

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

cross = pd.crosstab(tipler['Sosyal Grup'], tipler["Sıfat Değeri"])
cross['total'] = cross['-'] + cross['Nötr'] + cross['nötr'] + cross['Olumlu'] + cross['Olumsuz'] + cross['n']
cross['percentage'] = (cross["Olumlu"] / cross["total"]) * 100
percentage_subset = cross[cross.total >= 3].iloc[1:, 7:]
percentage_subset.index.name = None
percentage_subset.columns.name = None
percentage_subset = percentage_subset["percentage"].squeeze()

subset1 = tipler[tipler["Padişah Dönemi"] < 'Murad II']["Sosyal Grup"].value_counts()
subset1 = subset1[subset1.values >=3]
fig1 = px.bar(subset1, x=subset1.index, y=subset1.values,
             color='Sosyal Grup',
             title = f"Murad II Dönemi Öncesi Sosyal Gruplar",
             labels={'pop':'Sosyal Gruplar', "y": "Count", "x":"Sosyal Gruplar"}, height=400,width=600)
subset = tipler[tipler["Padişah Dönemi"] >= 'Murad II']["Sosyal Grup"].value_counts()
subset = subset[subset.values >=3]
fig = px.bar(subset, x=subset.index, y=subset.values,
             color='Sosyal Grup',
             title = f"Murad II Dönemi ve Sonrası Sosyal Gruplar",
             labels={'pop':'Sosyal Gruplar', "y": "Count", "x":"Sosyal Gruplar"}, height=400,width=600)

percFig = px.bar(percentage_subset, x=percentage_subset.index, y=percentage_subset.values,
             color = "percentage",
             title = f"Sosyal Grupların Olumlu Anılma Yüzdeleri",
             labels={'pop':'Sosyal Gruplar', "y": "Count", "x":"Sıfat Değerleri"}, height=600,width=1050)
king_selector.param.watch(selector_callback, "value")



lay = pn.Column(king_selector, responsive)
lay2 = pn.Column(percFig)
lay3 = pn.Row(fig1,fig)
tabs = pn.Tabs(
    ("Sıfat Dağılımı Padişaha Göre",lay),
    ("Sıfatların Olumlu Geçme Yüzdesi", lay2),
    ("Murad II Öncesi ve Sonrası Sıfatların Karşılaştırması",lay3)
)

tabs.servable()