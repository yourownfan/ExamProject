from dash import Dash, html, dcc
#import plotly.express as px
#import pandas as pd

app = Dash(__name__)

app.layout = html.Div(['This is my Div!',
                      html.Div(['This is an inner division'],
                      style = {'color':'red', 'border':'2px red solid'}),
                      html.Div(['Second inner division'],
                      style = {'color': 'blue', 'border': '3px blue solid'})],
                    style = {'color': 'green', 'border':'2px green solid'}
                      )
if __name__ == '__main__':
    app.run(debug=True)