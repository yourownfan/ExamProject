from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
app = Dash(__name__)
colors = {'background': '#111111', 'text': '#7FDBFF'}

app.layout = html.Div(children=[
    html.H1(children='Your information for today!', style={'textAlign': 'center', 'color':colors['text']}),
    dcc.Graph(id='example-graph',
              figure={'data': [{'x':[2021,2022,2023],'y':[4,1,2], 'type':'bar', 'name':'COMP1 return,%'},
                               {'x':[2021,2022,2023], 'y':[2,4,5], 'type':'bar', 'name':'COMP2 return,%' }],
              'layout':{'plot_bgcolor': colors['background'],
                        'paper_bgcolor': colors['background'],
                        'font': {'color': colors['text']},
                        'title':'Returns Dynamics'}})
], style={'backgroundColor':colors['background']})
if __name__ == '__main__':
    app.run(debug=True)