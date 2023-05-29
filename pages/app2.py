import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from .side_bar import sidebar

dash.register_page(__name__, title='Surveys & Focus groups projects', order=3)

file1_url = "https://drive.google.com/file/d/1LYMRQRl38U7eU47UPWJ4SmVPJe6ix684/view?usp=sharing"
file2_url = "https://drive.google.com/file/d/1prJgFoLeaVZi4C-WH3jWQnOnf_nJbsXF/view?usp=sharing"

def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [dcc.Markdown('#### **Survey & Focus group project samples**',
                              style={'textAlign': 'center',
                                     'fontSize': '40px', 'line-height': '0.5', 'margin-top': '35px'}),
                    html.Hr(),
                    dbc.Row([
                        dbc.Col([
                            dcc.Markdown('**Surveys**  \n',
                                         style={'textAlign': 'left'})
                        ], width=4),
                        dbc.Col([
                            dcc.Markdown('**Awareness Study**    \n'
                                         'A survey that reveals brand awareness, purchase intent, and brand image   \n'
                                         'across the fragrance & make-up industry  \n'
                                         'Mar 2019  \n',
                                         style={'white-space': 'pre'},
                                         className='ms-3'),
                            html.A('See analysis', href=file1_url, target='_blank', className='ms-3'),
                        ], width=5)
                    ], justify='center', style={'margin-top': '25px'}),
                 dbc.Row([
                     dbc.Col([
                         dcc.Markdown('**Focus group**  \n',
                                      style={'textAlign': 'left', 'margin-top': '15px'})
                     ], width=4),
                     dbc.Col([
                         dcc.Markdown('**Product & creative test**    \n'
                                      'The purpose of the study was to test the concept of a new product for a cinema brand  \n'
                                      'and to evaluate the TVC created to promote it  \n'
                                      'Jul 2017  \n',
                                      style={'white-space': 'pre'},
                                      className='ms-3'),
                         html.A('See analysis', href=file2_url, target='_blank', className='ms-3'),
                     ], width=5)
                 ], justify='center', style={'margin-top': '25px'}),
                 ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])