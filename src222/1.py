import sys
from dash import Dash, dcc, html, Input, Output, callback

from pages import home

# Initialize the Dash app
app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', pathname="/home", refresh=False),
    html.Div(id='page-content')
])

@callback(Output('page-content', 'children'),
          Input('url', 'pathname'))
def display_page(pathname): 
    if pathname in ['/', '/menu', '/home']:
        return home.layout
    else:
        return html.Div([
            html.H1('404 - Página no encontrada'),
            html.Div(f'La URL "{pathname}" no fue encontrada en el servidor.'),
            html.Li(html.A('Menu', href='/menu')),
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
