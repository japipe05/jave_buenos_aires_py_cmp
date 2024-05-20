from dash import dcc, html, Input, Output, callback

# Función para leer el archivo ab.html
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Leer el archivo ab.html al inicio
initial_html = read_file('outputs/mapa_buenos_aires_preba.html')

layout = html.Div([

    html.Li(html.A('Menu', href='/menu')),
    html.Iframe(
        id='iframe_content',
        srcDoc=initial_html,
        style={'width': '100%', 'height': '600px'}  # Adjusted height
    )
    # html.Iframe(id='map', srcDoc=initial_html, style={'border': 'none'}, width='100%', height='600px')

])


@callback(
    Output('iframe_content', 'srcDoc'),
    Input('aplicar', 'n_clicks')
)
def update_iframe(aplicar):
    if aplicar:
        iframe_content = read_file('outputs/mapa_buenos_aires_preba.html')
        return iframe_content
    else:
        iframe_content = read_file('outputs/mapa_buenos_aires.html')
        return iframe_content



# ## Callback for timeseries price
# @callback(
#         Output('map', 'srcDoc'),
#         Input('aplicar', 'n_clicks')
#         )
# def update_map(aplicar):
#     if aplicar:
#         return read_file('outputs/mapa_buenos_aires_preba.html')
#     else:
#         return read_file('outputs/mapa_buenos_aires.html')
    