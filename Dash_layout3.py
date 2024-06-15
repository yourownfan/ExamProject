from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {'background':'#111111', 'text':'#7FDBFF'}

app.layout = html.Div(children = [
    html.H1(children = 'Hello!', style ={'textAlign':'center',
                                         'color': colors['text']}),
    html.Div('Dash: Web Dashboards with Python'),
    dcc.Graph(id = 'example',
            figure ={'data': [{'x':[1,2,3],'y':[9,8,7], 'type':'bar', 'name': 'Company 1'},
                              {'x':[1,2,3],'y':[3,3,4], 'type':'bar', 'name': 'Company 2'}
                              ],
                    'layout': {
                                'plot_bgcolor':colors['background'],
                                'paper_bgcolor':colors['background'],
                                'font':{'color':colors['text']},
                                'title':'Data Vizualisation'
                               }})
], style = {'backgroundColor': colors['background']})

if __name__ == '__main__':
    app.run(debug = True)