from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)
app.layout = html.Div(children = [
    html.H1(children = 'Hello!'),
    html.Div('Dash: Web Dashboards with Python'),
    dcc.Graph(id = 'example',
            figure ={'data': [{'x':[1,2,3],'y':[9,8,7], 'type':'bar', 'name': 'Company 1'},
                              {'x':[1,2,3],'y':[3,3,4], 'type':'bar', 'name': 'Company 2'}
                              ],
                    'layout': {'title':'Data Vizualisation'
                               }})
])

if __name__ == '__main__':
    app.run(debug = True)