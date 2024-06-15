from dash import Dash, html, dcc
import plotly.graph_objs as go
import numpy as np

app = Dash(__name__)

np.random.seed(88)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1,101, 100)

app.layout = html.Div([dcc.Graph(id = 'scatterplot',
                                 figure = {'data': [go.Scatter(
                                     x =random_x,
                                     y = random_y,
                                     mode = 'markers',
                                     marker ={'size': 12,
                                               'color': 'deeppink',
                                               'symbol': 'star',
                                               'line': {'width':1}}

                                 )],
                                   'layout': go.Layout(title='My Scatterplot',
                                                       xaxis={'title':'Some data'})

                                 }
                                 )])

if __name__ == '__main__':
    app.run(debug = True)