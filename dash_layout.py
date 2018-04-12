# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 15:57:23 2018

@author: crist
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
import os
import pandas as pd
import numpy as np

import plotly.offline as py
import cufflinks as cf
import plotly.graph_objs as go
from dash.dependencies import Input, Output

from flask import send_from_directory


app=dash.Dash()
app.scripts.config.serve_locally=True
app.css.config.serve_locally=True
appDir = os.path.dirname(os.path.realpath(__file__))

clients = ['John', 'Sally', 'Cris']
portfolios = ['3401', '3403', '3404']
asset_classes = ['Equities', 'Fixed Income']
random_n = [5,3]

#base chart height and width, into a list and adjusted with slider
chartW = 600
chartH = 500
sizes = [chartW, chartH]


# App layout
app.layout = html.Div(children=[
                #stylesheets and general head
                html.Link(href='/static/style.css', rel='stylesheet'),
                html.Script(src='/static/javascript.js'),
                #LEFT
                html.Div(
                    children=[
                        #HEADER
                        html.Div(children=[
                            html.H2('Control Panel'),
                        ],
                        className = 'top-left'
                        ),
                        #LEFT NAV CONTENT
                        html.Div(
                            children=[
                                html.Label('Dropdown 1'),
                                dcc.Dropdown(
                                    id = 'dropdown-1',
                                    options = [{'label': i, 'value': i} for i in clients],
                                    multi = True,
                                    value = clients[0]
                                ),
                                html.Label('Dropdown 2'),
                                dcc.Dropdown(
                                    id = 'dropdown-2',
                                    options = [{'label': i, 'value': i} for i in portfolios],
                                    value = portfolios[0]
                                ),
                                html.Label('Radio Items 2'),
                                dcc.RadioItems(
                                    id = 'radio-1',
                                    options = [{'label': i, 'value': i} for i in portfolios],
                                    value = portfolios[0],
                                    labelStyle = {'display': 'inline-block'}
                                ),
                                html.Label('Chart size adjustment'),
                                dcc.Slider(
                                    id = 'size-slider',
                                    min = 0.9,
                                    max = 1.1,
                                    step = 0.01,
                                    value = 1
                                ),
                            ],
                            className = 'content'
                        ),     
                    ],
                    className = 'column left'
                ),
                #RIGHT
                html.Div(
                    children=[
                        #HEADER
                        html.Div(children=[
                            html.H2('Dashboard Layout'),
                        ],
                        className = 'top-right'
                        ),
                        #RIGHT MAIN CONTENT
                        html.Div(children=[
                            dcc.Graph(
                                id='graph-1',
                                ),
                            dcc.Graph(
                                id='graph-2',
                                ),
                            dcc.Graph(
                                id='graph-3',
                                ),
                            dcc.Graph(
                                id='graph-4',
                                ),
                            dcc.Graph(
                                id='graph-5',
                                ),
                            dcc.Graph(
                                id='graph-6',
                                ),
                            dcc.Graph(
                                id='graph-7',
                                ),
                            dcc.Graph(
                                id='graph-8',
                                ),    
                            ],
                            className='content'
                        ),
                ],
                className = 'column')
],
className='app-content'
)

@app.callback(Output('graph-1', 'figure'),
             [Input('size-slider', 'value')])
def update_chart(sizer):
    y = random_n
    x = asset_classes
    trace = go.Bar(
            x = x,
            y = y
    )
    
    data = [trace]
    
    layout = go.Layout(
            height = sizes[1]*sizer,
            width = sizes[0]*sizer
    )
    
    fig = go.Figure(data=data, layout=layout)

    return fig



#include static files (css and js)
@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(appDir, 'static')
    return send_from_directory(static_folder, path)
              
if __name__ == '__main__':
    app.run_server(debug=True)

                        

