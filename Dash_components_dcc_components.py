from dash import Dash, html, dcc
#import plotly.express as px
#import pandas as pd

app = Dash(__name__)

app.layout = html.Div([

            html.Label('Dropdown'),
            dcc.Dropdown(options = [{'label':'Microsoft',
                                    'value':'MSFT'},
                                    {'label':'Amazon',
                                     'value':'AMZN'}],
                         value = 'MSFT'),
            html.Label('Slider'),
            dcc.Slider(min =-10, max = 10, step = 0.5, value = 0),
            html.P('Radio Items'),
            dcc.RadioItems(options = [{'label':'Microsoft',
                                    'value':'MSFT'},
                                    {'label':'Amazon',
                                     'value':'AMZN'}],
                           value = 'MSFT')
])
# If elements are overlapping each other you can stick some of them into their oun Divs
# OR use html.P instead of html.Label
if __name__ == '__main__':
    app.run(debug=True)