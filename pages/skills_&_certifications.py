import dash
import os
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=1)

image_path = os.path.join("assets", "Certificado.jpg")

layout = html.Div([
    dcc.Markdown('**Soledad Granelli**  \n'
                 '#### Insights Consultant',
                 style={'textAlign': 'center',
                        'fontSize': '40px', 'line-height': '0.5', 'margin-top': '35px'}),

    dcc.Markdown('### Skills', style={'textAlign': 'center', 'margin-top': '40px','color':'gray'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Programming & visualization**  \n',
                         style={'textAlign': 'left'}),
        ], width=3),
        dbc.Col([
            dcc.Markdown('* Python  \n'
                         '* Tableau  \n'
                         '* SQL  \n'
                         '* Power BI  \n'
                         '* Advanced Excel  \n',
                         style={'white-space': 'pre'},
                         className='ms-3')
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Market & consumer insights**  \n',
                         style={'textAlign': 'left'}),
        ], width=3),
        dbc.Col([
            dcc.Markdown('* Kantar Suite  \n'
                         '* Euromonitor  \n'
                         '* GWI / TGI  \n'
                         '* Survey Monkey  \n'
                         '* Social Listening tools: Infegy, Meltwater, Sysomos  \n',
                         style={'white-space': 'pre'},
                         className='ms-3')
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Measurement & performance**  \n',
                         style={'textAlign': 'left'}),
        ], width=3),
        dbc.Col([
            dcc.Markdown('* Google & Meta Ads   \n'
                         '* Empflifi (Social Bakers) / Sprout Social  \n'
                         '* Comscore / Similar Web  \n'
                         '* Adcuality / Admetricks  \n'
                         '* Exolyt  \n',
                         style={'white-space': 'pre'},
                         className='ms-3')
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Soft skills**  \n',
                         style={'textAlign': 'left'}),
        ], width=3),
        dbc.Col([
            dcc.Markdown('* Team & project management   \n'
                         '* Data management & visualization  \n'
                         '* Strategic thinking  \n'
                         '* Presentation to stakeholders  \n'
                         '* Proactive, methodical, and practical approach  \n',
                         style={'white-space': 'pre'},
                         className='ms-3')
        ], width=5)
    ], justify='center'),

    dcc.Markdown('### Certifications', style={'textAlign': 'center', 'margin-top': '40px', 'color': 'gray'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Centro REDES**  \n'
                         '2021',
                         style={'textAlign': 'left'}),
        ], width=3),
        dbc.Col([
            dcc.Markdown('**Python Programming**  \n'
                         'Buenos Aires, AR  \n'
                         'Grade: 10/10  \n'
                         '[See certificate]({})'.format(image_path),
                         style={'white-space': 'pre'},
                         className='ms-3')
        ], width=5)
    ], justify='center'),
])