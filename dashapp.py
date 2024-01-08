#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import dash
from dash import Dash,dcc,html,Input,Output,State,callback
import plotly.graph_objs as go
import plotly.express as px
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('airlines_data.csv')


# In[ ]:





# In[50]:


app = dash.Dash(__name__)
server = app.server

# In[51]:


import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Prepare the options for the dropdowns
year_options = [2015,2016]
month_options = [{'label': month, 'value': month} for month in df.MONTH.unique()]

app.layout = html.Div([
    html.H1(children ="Overview of Airline Industry OF INDIA",style={'textAlign': 'center','margin':'10px'}),
    html.Br(),
    html.Br(),
    html.Div([
        html.H3(children ="Graph of Passengers to India",style={'margin':'10px'}),
        dcc.Dropdown(options=year_options, id='dropdown-year-p2i',value = 2015),
        dcc.Dropdown(options=month_options, id='dropdown-month-p2i',value = "JAN"),
        dcc.Graph(id='graph-p2i')
    ]),
    html.Br(),
    html.Br(),
    html.Div([
        html.H3(children ="Graph of Passengers from India",style={'margin':'10px'}),
        dcc.Dropdown(options=year_options, id='dropdown-year-pfi',value= 2015),
        dcc.Dropdown(options=month_options, id='dropdown-month-pfi',value= "JAN"),
        dcc.Graph(id='graph-pfi')
    ]),
    html.Br(),
    html.Br(),
    html.Div([
        html.H3(children ="Graph of Frieght to India",style={'margin':'10px'}),
        dcc.Dropdown(options=year_options, id='dropdown-year-f2i',value= 2015),
        dcc.Dropdown(options=month_options, id='dropdown-month-f2i',value= "JAN"),
        dcc.Graph(id='graph-f2i')
    ]),
    html.Br(),
    html.Br(),
    html.Div([
        html.H3(children ="Graph of Frieght from India",style={'margin':'10px'}),
        dcc.Dropdown(options=year_options, id='dropdown-year-ffi',value= 2015),
        dcc.Dropdown(options=month_options, id='dropdown-month-ffi',value= "JAN"),
        dcc.Graph(id='graph-ffi')
    ]),
    html.Br(),
    html.Br(),
    html.Div([
    html.Div([
        html.H3(children="PI chart Passengers to India", style={'margin':'10px'}),
        dcc.Dropdown(options=year_options, id='dropdown-year-p2ip', value=2015),
        dcc.Dropdown(options=month_options, id='dropdown-month-p2ip', value="JAN"),
        dcc.Graph(id='graph-p2ip')
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([
        html.H3(children="PI chart Passengers from India", style={'margin':'10px'}),
        dcc.Dropdown(options=year_options, id='dropdown-year-pfip', value=2015),
        dcc.Dropdown(options=month_options, id='dropdown-month-pfip', value="JAN"),
        dcc.Graph(id='graph-pfip')
    ], style={'width': '50%', 'display': 'inline-block'})
]),
    html.Br(),
    html.Br(),
    html.Div([
    html.Div([
        html.H3(children="PI chart Frieght to India", style={'margin':'10px'}),
        dcc.Dropdown(options=year_options, id='dropdown-year-f2ip', value=2015),
        dcc.Dropdown(options=month_options, id='dropdown-month-f2ip', value="JAN"),
        dcc.Graph(id='graph-f2ip')
    ], style={'width': '50%', 'display': 'inline-block'}),

    html.Div([
        html.H3(children="PI chart Frieght from India", style={'margin':'10px'}),
        dcc.Dropdown(options=year_options, id='dropdown-year-ffip', value=2015),
        dcc.Dropdown(options=month_options, id='dropdown-month-ffip', value="JAN"),
        dcc.Graph(id='graph-ffip')
    ], style={'width': '50%', 'display': 'inline-block'})
]),
],style = {
    'backgroundColor':'#DCF2F1'})

@app.callback(
    Output('graph-p2i', 'figure'),
    [Input('dropdown-year-p2i', 'value'),
     Input('dropdown-month-p2i', 'value')]
)
def update_graph(year_value, month_value):
    dff = df[df.YEAR == year_value]
    dff1 = dff[dff.MONTH == month_value]
    fig = px.treemap(dff1, path=["CARRIER TYPE", "AIRLINE NAME"], values="PASSENGERS TO INDIA", color="CARRIER TYPE", hover_data=["PASSENGERS TO INDIA"])
    return fig  # return the figure

@app.callback(
    Output('graph-pfi', 'figure'),
    [Input('dropdown-year-pfi', 'value'),
     Input('dropdown-month-pfi', 'value')]
)
def update_graph(year_value, month_value):
    dff = df[df.YEAR == year_value]
    dff1 = dff[dff.MONTH == month_value]
    fig = px.treemap(dff1, path=["CARRIER TYPE", "AIRLINE NAME"], values="PASSENGERS FROM INDIA", color="CARRIER TYPE", hover_data=["PASSENGERS FROM INDIA"])
    return fig  # return the figure

@app.callback(
    Output('graph-f2i', 'figure'),
    [Input('dropdown-year-f2i', 'value'),
     Input('dropdown-month-f2i', 'value')]
)
def update_graph(year_value, month_value):
    dff = df[df.YEAR == year_value]
    dff1 = dff[dff.MONTH == month_value]
    fig = px.treemap(dff1, path=["CARRIER TYPE", "AIRLINE NAME"], values="FREIGHT TO INDIA", color="CARRIER TYPE", hover_data=["FREIGHT TO INDIA"])
    return fig  # return the figure

@app.callback(
    Output('graph-ffi', 'figure'),
    [Input('dropdown-year-ffi', 'value'),
     Input('dropdown-month-ffi', 'value')]
)
def update_graph(year_value, month_value):
    dff = df[df.YEAR == year_value]
    dff1 = dff[dff.MONTH == month_value]
    fig = px.treemap(dff1, path=["CARRIER TYPE", "AIRLINE NAME"], values="FREIGHT FROM INDIA", color="CARRIER TYPE", hover_data=["FREIGHT FROM INDIA"])
    return fig  # return the figure

@app.callback(
    Output('graph-p2ip', 'figure'),
    [Input('dropdown-year-p2ip', 'value'),
     Input('dropdown-month-p2ip', 'value')]
)
def update_graph(year_value, month_value):
    dff = df[df.YEAR == year_value]
    dff1 = dff[dff.MONTH == month_value]
    fig = px.pie(dff1,values = 'PASSENGERS FROM INDIA',names = 'CARRIER TYPE')
    return fig  # return the figure

@app.callback(
    Output('graph-pfip', 'figure'),
    [Input('dropdown-year-pfip', 'value'),
     Input('dropdown-month-pfip', 'value')]
)
def update_graph(year_value, month_value):
    dff = df[df.YEAR == year_value]
    dff1 = dff[dff.MONTH == month_value]
    fig = px.pie(dff1,values = 'PASSENGERS TO INDIA',names = 'CARRIER TYPE')
    return fig  # return the figure

@app.callback(
    Output('graph-ffip', 'figure'),
    [Input('dropdown-year-ffip', 'value'),
     Input('dropdown-month-ffip', 'value')]
)
def update_graph(year_value, month_value):
    dff = df[df.YEAR == year_value]
    dff1 = dff[dff.MONTH == month_value]
    fig = px.pie(dff1,values = 'FREIGHT FROM INDIA',names = 'CARRIER TYPE')
    return fig  # return the figure

@app.callback(
    Output('graph-f2ip', 'figure'),
    [Input('dropdown-year-f2ip', 'value'),
     Input('dropdown-month-f2ip', 'value')]
)
def update_graph(year_value, month_value):
    dff = df[df.YEAR == year_value]
    dff1 = dff[dff.MONTH == month_value]
    fig = px.pie(dff1,values = 'FREIGHT TO INDIA',names = 'CARRIER TYPE')
    return fig  # return the figure

if __name__ == '__main__':
    app.run_server(debug=False)


# In[ ]:





# In[ ]:




