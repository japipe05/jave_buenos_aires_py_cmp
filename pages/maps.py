from dash import dcc, html, Input, Output, callback

# Función para leer el archivo ab.html
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Leer el archivo ab.html al inicio
initial_html = read_file('outputs/mapa_buenos_aires_preba.html')

layout = html.Div([

    html.Li(html.A('Menu', href='/menu')),
    html.Iframe(srcDoc=initial_html, style={'width': '100%', 'height': '600px'})

])
