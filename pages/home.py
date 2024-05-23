from dash import dcc, html, Input, Output, callback

layout = html.Div([

    html.H1('Menú'),
    html.Br(),
    dcc.Link('Go to Page map', href='/maps'),

    html.H1("Filtrar Dataset"),
    html.Label("Selecciona un rango de edad:"),
    dcc.RangeSlider(
        id='age_range',
        min=15,
        max=60,
        step=1,
        marks={i: str(i) for i in range(15, 60)},
        value=[15, 60]
    ),
    html.Br(),
    html.Label("Selecciona un género:"),
    dcc.Dropdown(
        id='gender',
        options=[
            {'label': 'Masculino', 'value': 1},
            {'label': 'Femenino', 'value': 0}
        ],
        value=[0,1],
        multi=True
    ),
    html.Br(),
    html.Label("Selecciona un barrio:"),
    dcc.Dropdown(
        id='barrio',
        options=[
            {'label': 'Agronomia', 'value': 'Agronomia'},
            {'label': 'Almagro', 'value': 'Almagro'},
            {'label': 'Todos', 'value': 'todos'}
        ],
        value=['Almagro'],
        multi=True
    ),
    html.Br(),
    html.Label("Selecciona un color:"),
    dcc.Dropdown(
        id='color',
        options=[
            {'label': 'Azul', 'value': 1},
            {'label': 'Rojo', 'value': 0}
        ],
        value=[1],
        multi=True
    ),

    html.Button('Aplicar', id='aplicar', n_clicks=0),

    html.Div(id="message"),

])






import pandas as pd
import geopandas as gpd
from keplergl import KeplerGl
import plotly.express as px
from dash import dcc, html, Input, Output, callback, State
import dash_bootstrap_components as dbc

df_clientes = pd.read_parquet('D:\Workspace_git\Javeriana\Maestria\Top Avan Bases datos\jave_buenos_aires_py_cmp\insumos\df_clientes.parquet.gzip')
df_ba = gpd.read_file("D:\Workspace_git\Javeriana\Maestria\Top Avan Bases datos\jave_buenos_aires_py_cmp\insumos\RMBA.geojson")

# Ejecutar creacion de los html
# Define the callback function

@callback(
    Output('message', 'children'),
    Input('age_range', 'value'),
    Input('gender', 'value'),
    Input('barrio', 'value'),
    Input('aplicar', "n_clicks"),
)
def update_html_and_message(age_range, gender, barrio, aplicar):
    if aplicar:

        print(age_range, gender, barrio)

        filtered_data = df_clientes[(df_clientes["sexo"].isin(gender)) & 
                                    (df_clientes["edad"] >= age_range[0]) & 
                                    (df_clientes["edad"] <= age_range[1])]
        
        if barrio[0] == 'todos':
            filtered_data2 = df_ba.copy()
        else:
            filtered_data2 = df_ba[(df_ba["barrios"].isin(barrio))]

        ## Save  CSV file
        # filtered_data.to_csv("filtered_data.csv", index=False)
        # filtered_data2.to_file('filtered_data2.geojson', driver='GeoJSON') 

        # Generador de mapa
        mapa_buenos_aires = KeplerGl(height=500, data={"df_ba": filtered_data2})
        config_mapa_buenos_aires = mapa_buenos_aires.config
        mapa_buenos_aires.save_to_html(data={'Comunas y barrios de Buenos Aires': filtered_data2}, config=config_mapa_buenos_aires, file_name='outputs/filtro_mapa_buenos_aires_prueba.html')




        # import os

        # def guardar_mapa_buenos_aires(data, config, file_name):
        #     # Verificar si el archivo existe
        #     if os.path.exists(file_name):
        #         # Eliminar el archivo existente
        #         os.remove(file_name)

        #     # Generar y guardar el mapa
        #     mapa_buenos_aires.save_to_html(data, config, file_name)

        # # Guardar el mapa
        # guardar_mapa_buenos_aires(data={'df_ba': filtered_data2}, config=config_mapa_buenos_aires, file_name='outputs/mapa_buenos_aires_preba.html')

        # with open("outputs/mapa_buenos_aires_preba.html", 'w') as f:
        #     f.save_to_html(data={'df_ba': filtered_data2}, config=config_mapa_buenos_aires, f='outputs/mapa_buenos_aires_preba.html')





        # Create message
        return html.Div(children="Todo Ok", style={"color": "green"})

    else:
        return html.Div(children="Dale al boton", style={"color": "green"})
