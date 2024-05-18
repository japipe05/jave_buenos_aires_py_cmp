import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import base64

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Definir el layout de la aplicación
app.layout = html.Div([
    dcc.Upload(
        id='upload-html',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select an HTML file')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),
    html.Div(id='output-html')
])

# Callback para actualizar el contenido del HTML cargado
@app.callback(
    Output('output-html', 'children'),
    [Input('upload-html', 'contents')]
)
def display_html(contents):
    if contents is not None:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string).decode('utf-8')
        return html.Iframe(srcDoc=decoded, style={'width': '100%', 'height': '600px'})
    return html.Div([
        'No file uploaded yet.'
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
