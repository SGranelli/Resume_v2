import dash
import os
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .side_bar import sidebar

dash.register_page(__name__, title='Research projects', order=2)

file1_url = "https://drive.google.com/file/d/1-S0puoVfWgVanKbEC4OGtFmG4Rj93ssk/view?usp=share_link"
file2_url = "https://drive.google.com/file/d/1wXb3GH1081GobsVBLTZHX2pFIdqUdrIg/view?usp=sharing"
file3_url = "https://drive.google.com/file/d/15flVZvBHcmM9Kxtbw2YWyJYL9ZuzX6Z0/view?usp=sharing"
file4_url = "https://drive.google.com/file/d/1l6V7mYNOVpCKzHDK7KRx6wcJj2pxA3Gl/view?usp=sharing"
file5_url = "https://drive.google.com/file/d/1lWZD1WwqBfDjnkVAI7vvdSc9XHjeAsid/view?usp=sharing"

def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [dcc.Markdown('#### **Research project samples**',
                              style={'textAlign': 'center',
                                     'fontSize': '40px', 'line-height': '0.5', 'margin-top': '35px'}),
                    html.Hr(),
                    dbc.Row([
                        dbc.Col([
                            dcc.Markdown('**Market Research**  \n',
                                         style={'textAlign': 'left'})
                        ], width=4),
                        dbc.Col([
                            dcc.Markdown('**AR Country review**    \n'
                                         'A snapshot of the Argentinean market and future perspectives  \n'
                                         'July 2020  \n',
                                         style={'white-space': 'pre'},
                                         className='ms-3'),
                         html.A('See analysis', href=file1_url, target='_blank', className='ms-3'),
                        ], width=5)
                    ], justify='center', style={'margin-top': '25px'}),
                 dbc.Row([
                     dbc.Col([
                         dcc.Markdown('**Industry Research**  \n',
                                      style={'textAlign': 'left'})
                     ], width=4),
                     dbc.Col([
                         dcc.Markdown('**Wine Industry Analysis**    \n'
                                      'Analysis for a wine brand, including a market & competitive deep dive  \n'
                                      'May 2021  \n',
                                      style={'white-space': 'pre'},
                                      className='ms-3'),
                         html.A('See analysis', href=file2_url, target='_blank', className='ms-3'),
                     ], width=5)
                 ], justify='center', style={'margin-top': '25px'}),
                 dbc.Row([
                     dbc.Col([
                         dcc.Markdown('**Industry Research**  \n',
                                      style={'textAlign': 'left'})
                     ], width=4),
                     dbc.Col([
                         dcc.Markdown('**VOD Industry Analysis**    \n'
                                      'Market, competitive, and consumer analysis for a VOD brand  \n'
                                      'Jul 2019  \n',
                                      style={'white-space': 'pre'},
                                      className='ms-3'),
                         html.A('See analysis', href=file3_url, target='_blank', className='ms-3'),
                     ], width=5)
                 ], justify='center', style={'margin-top': '25px'}),
                 dbc.Row([
                     dbc.Col([
                         dcc.Markdown('**Social Listening**  \n',
                                      style={'textAlign': 'left'})
                     ], width=4),
                     dbc.Col([
                         dcc.Markdown('**GRAMMYs & Oscars 2022**    \n'
                                      'A social listening report about the 2022 edition of GRAMMYs & Oscars,   \n'
                                      'identifying volumes, demographics, and main conversation drivers   \n'
                                      'Mar 2022  \n',
                                      style={'white-space': 'pre'},
                                      className='ms-3'),
                         html.A('See analysis', href=file4_url, target='_blank', className='ms-3'),
                     ], width=5)
                 ], justify='center', style={'margin-top': '25px'}),
                 dbc.Row([
                     dbc.Col([
                         dcc.Markdown('**Social Listening**  \n',
                                      style={'textAlign': 'left'})
                     ], width=4),
                     dbc.Col([
                         dcc.Markdown('**Burger week 2020**    \n'
                                      'An analysis of the conversations about Burger Week, to identify   \n'
                                      'key conversation drivers, sentiment, and future implications   \n'
                                      'Jun 2020  \n',
                                      style={'white-space': 'pre'},
                                      className='ms-3'),
                         html.A('See analysis', href=file5_url, target='_blank', className='ms-3'),
                     ], width=5)
                 ], justify='center', style={'margin-top': '25px'}),

                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])
