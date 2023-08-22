import plotly.express as px
import pandas as pd
import panel as pn

tipler = pd.read_excel("Tipler Revize.xlsx")
tipler["Padişah Dönemi"] = tipler["Padişah Dönemi"].str.strip()
sultan_list = tipler["Padişah Dönemi"].unique().tolist()
sultan_list.insert(1, 'Ertuğrul Gazi')
sultan_list.pop()
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

######################################
dataset = pd.read_csv("nesneler.csv")
Nitelikler = dataset[['Sultan', 'Nitelik']]
Eylemler = dataset[['Sultan', 'Eylem']]
sultan_list2 = Nitelikler["Sultan"].unique().tolist()

def update_objects_plot1(selected_king2):
    filtered_data = Nitelikler[Nitelikler["Sultan"] == selected_king2]
    value_counts = filtered_data["Nitelik"].value_counts()

    fig = px.bar(value_counts, x=value_counts.index, y=value_counts.values,
                 color='Nitelik',
                 title=f"{selected_king2} Dönemi Öncesi Elden Ele Geçen Nesneler (Niteliklerine Göre)",
                 labels={'value_counts': 'Nesneler', "y": "Count", "x": "Nesneler"}, height=400)

    return fig

king_selector2 = pn.widgets.Select(options=sultan_list2)
initial_fig2 = update_objects_plot1(king_selector2.value)
responsive2 = pn.pane.Plotly(initial_fig2, height=600, width=800)

def selector_callback2(event):
    selected_king2 = event.new
    updated_fig = update_objects_plot1(selected_king2)
    responsive2.object = updated_fig  # Fixed: Use responsive2 instead of responsive

king_selector2.param.watch(selector_callback2, "value")
lay2 = pn.Column(king_selector2, responsive2)

########################################################

def update_objects_plot2(selected_king3):
    filtered_data = Eylemler[Eylemler["Sultan"] == selected_king3]
    value_counts = filtered_data["Eylem"].value_counts()

    fig = px.bar(value_counts, x=value_counts.index, y=value_counts.values,
                 color='Eylem',
                 title=f"{selected_king3} Dönemi Öncesi Elden Ele Geçen Nesneler (Eylemlere Göre)",
                 labels={'value_counts': 'Nesneler', "y": "Count", "x": "Nesneler"}, height=400)

    return fig

king_selector3 = pn.widgets.Select(options=sultan_list2)
initial_fig3 = update_objects_plot2(king_selector3.value)
responsive3 = pn.pane.Plotly(initial_fig3, height=600, width=800)

def selector_callback3(event):
    selected_king3 = event.new
    updated_fig = update_objects_plot2(selected_king3)
    responsive3.object = updated_fig

king_selector3.param.watch(selector_callback3, "value")
lay3 = pn.Column(king_selector3, responsive3)

########################################################

def update_objects_pie(selectedEylem):
    filtered_data = Eylemler[Eylemler["Eylem"] == selectedEylem]
    value_counts = filtered_data["Sultan"].value_counts()

    fig = px.pie(value_counts, names=value_counts.index, values=value_counts.values,
                 color='Sultan',
                 title=f"{selectedEylem} Eylemine Bağlı Nesnelerin Ait Olduğu Padişah Dağılımı",
                 labels={'value_counts': 'Sultan', "y": "Count", "x": "Sultan"}, height=400)

    return fig

_eylemler = ["Sahiplik", "İsâr", "Ganimet", "Gönderme", "Harac"]
eylemSelector = pn.widgets.Select(options=_eylemler)
initial_fig4 = update_objects_pie(eylemSelector.value)
responsive4 = pn.pane.Plotly(initial_fig4, height=600, width=800)

def selector_callback4(event):
    selected_eylem = event.new
    updated_fig = update_objects_pie(selected_eylem)
    responsive4.object = updated_fig

eylemSelector.param.watch(selector_callback4, "value")
lay4 = pn.Column(eylemSelector, responsive4)

###########################################################################

def update_objects_pie2(selectedNitelik):
    filtered_data = Nitelikler[Nitelikler["Nitelik"] == selectedNitelik]
    value_counts = filtered_data["Sultan"].value_counts()

    fig = px.pie(value_counts, names=value_counts.index, values=value_counts.values,
                 color='Sultan',
                 title=f"{selectedNitelik} Niteliğine Bağlı Nesnelerin Ait Olduğu Padişah Dağılımı",
                 labels={'value_counts': 'Sultan', "y": "Count", "x": "Sultan"}, height=400)

    return fig

_nitelikler = ["Kâlâ", "Taşınılmaz / Toprak", "Seyfiye", "İktidar", "Binek Hayvan", "Deniz Taşıtı", "İş Gücü", "Erzak", "İletişim", "Dini"]
nitelikSelector = pn.widgets.Select(options=_nitelikler)
initial_fig5 = update_objects_pie2(nitelikSelector.value)
responsive5 = pn.pane.Plotly(initial_fig5, height=600, width=800)

def selector_callback5(event):
    selected_nitelik = event.new
    updated_fig = update_objects_pie2(selected_nitelik)
    responsive5.object = updated_fig

nitelikSelector.param.watch(selector_callback5, "value")
lay5 = pn.Column(nitelikSelector, responsive5)

niteliktab = pn.Tabs(
    ("Nitelik Dağılımı", lay2),
    ("Padişah Dağılımı", lay5)
)

eylemtab = pn.Tabs(
    ("Eylem Dağılımı", lay3),
    ("Padişah Dağılımı", lay4)
)

subtab = pn.Tabs(
    ("Eyleme Göre", eylemtab),
    ("Niteliğe Göre", niteliktab)
)

tabs = pn.Tabs(
    ("Tipler", lay),
    ("Nesneler", subtab)
)

tabs.servable()
