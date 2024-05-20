from dash import dcc, html, Input, Output, callback

def read_file(filename):
    """Reads the content of the specified HTML file."""
    with open(filename, 'r') as file:
        return file.read()

# default_html = read_file('outputs/mapa_buenos_aires.html')  # Initial map
# preprocessed_html = read_file('outputs/mapa_buenos_aires_preba.html')  # Preprocessed map

layout = html.Div([
    html.Li(html.A('Menu', href='/menu')),
    html.Iframe(id='map', srcDoc="default_html", style={'border': 'none'}, width='100%', height='600px')
])


@callback(
    Output('map', 'srcDoc'),
    Input('aplicar', 'n_clicks')
)
def update_map(n_clicks):
    """Updates the map based on button clicks."""

    default_html = read_file('outputs/mapa_buenos_aires.html')  # Initial map
    preprocessed_html = read_file('outputs/mapa_buenos_aires_preba.html')  # Preprocessed map

    if n_clicks is None:  # Handle initial state (no clicks)
        return default_html
    else:
        return preprocessed_html
    