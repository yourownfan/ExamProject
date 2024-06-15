from dash import Dash, html, dcc
import plotly.graph_objs as go
import numpy as np

app = Dash(__name__)

app.layout=html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(options=[{'label':'Microsoft', 'value':'MSFT'},
                          {'label':'Amazon','value':'AMZN'}],
                 value = 'MSFT')
])

if __name__ == '__main__':
    app.run(debug = True)