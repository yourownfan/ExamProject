from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import yfinance as yf
from datetime import datetime
import pandas as pd
import dash_auth

USERNAME_PASSWORD_PAIRS=[['username', 'password'], ['Login_ne_bezopasen', 'Parol_bezopasen']]
app = Dash(__name__)
dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)
server = app.server


nsdq = pd.read_csv('NASDAQcompanylist.csv')
nsdq.set_index('Symbol', inplace = True)
options = []
for tic in nsdq.index:
    mydict = {}
    mydict['label'] = nsdq.loc[tic]['Name']+''+tic
    mydict['value'] = tic
    options.append(mydict)

app.layout = html.Div([
            html.H1('Stock Ticker Dashboard'),
            html.Div([html.H3('Enter a stock symbol:', style = {'paddingRight':'30px'}),
            dcc.Dropdown(id = 'my_ticker_symbol',
                         options = options,
                         value = ['MSFT'],
                         multi = True)], style = {'display':'iline-block', 'verticalAlign':'top', 'width':'40%'}),

            html.Div([html.H3('Select a start and end date:'),
                      dcc.DatePickerRange(id = 'my_date_picker',
                                          initial_visible_month=datetime.today(),
                                          min_date_allowed='2015-1-1',
                                          max_date_allowed=datetime.today(),
                                          start_date='2020-1-1',
                                          end_date=datetime.today(),
                                          with_portal=True
                                          )
                      ], style = {'display':'inline-block'}),
            html.Div([
                    html.Button(id = 'submit-button',
                                          n_clicks = 0,
                                          children = 'Submit',
                                          style = {'fontSize': 24, 'marginLeft': '30px'}
                                          )
                      ]),
                      dcc.Graph(id = 'my_graph',
                                figure = {'data':[
                                    {'x':[1,2], 'y':[3,1]}
                        ], 'layout': {'title':'Default Title'}})])

@app.callback(Output('my_graph', 'figure'),
              [Input('submit-button', 'n_clicks')],
              [State('my_ticker_symbol', 'value'),
               State('my_date_picker','start_date'),
               State('my_date_picker','end_date')
            ])

def update_graph(n_clicks, stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')

    traces = []
    for tic in stock_ticker:
        data = yf.download(tic, start, end)
        traces.append({'x': data.index,'y': data['Close'], 'name': tic})
    fig = {
        'data': traces,
        'layout': {'title': stock_ticker}
    }
    return fig

if __name__ == '__main__':
    app.run(debug = True)