from dash import Dash, dcc, html, Input, Output, callback
# import plotly.graph_objs as go
# import base64
# import pandas as pd
from pages import home, maps#, maps2, #map3

## Inicializar la aplicación Dash
app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    # data_store,
    dcc.Location(id='url', pathname="/", refresh=False),
    html.Div(id='page-content')
])

@callback(Output('page-content', 'children'),
          Input('url', 'pathname'),
          )
def display_page(pathname): 
    if (pathname == '/') | (pathname == '/menu') | (pathname == '/home'):
        return home.layout
    elif (pathname == '/maps'):
        return maps.layout
    else:
        return html.Div([
            html.H1('404 - Página no encontrada'),
            html.Div('La URL "{}" no fue encontrada en el servidor.'.format(pathname)),
            html.Li(html.A('Menu', href='/menu')),
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
