from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
import numpy as np

app = Dash(__name__)

#Creating data
np.random.seed(80)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

# We call
app.layout = html.Div([dcc.Graph(id = 'scatterplot',
                                 figure = {'data': [go.Scatter(x=random_x,
                                                               y=random_y,
                                                               mode='markers',
                                                               marker={
                                                                   'size': 13,
                                                                   'color': 'deeppink',
                                                                   'symbol':'star',
                                                                   'line':{'width': 2}
                                                               }
                                                               )],

                                           'layout':go.Layout(title='My Scatterplot')}
                                 ),
                       dcc.Graph(id = 'scatterplot2',
                                 figure = {'data': [go.Scatter(x=random_x,
                                                               y=random_y,
                                                               mode='markers',
                                                               marker={
                                                                   'size': 13,
                                                                   'color': 'rgb(130,79,199)',
                                                                   'symbol':'pentagon',
                                                                   'line':{'width': 1}
                                                               }
                                                               )],

                                           'layout':go.Layout(title='My Scatterplot')}
                                 )])

if __name__ == '__main__':
    app.run(debug = True)