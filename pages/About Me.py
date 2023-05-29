import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0)

# resume sample template from https://zety.com/
layout = html.Div([
    dcc.Markdown('**Soledad Granelli**  \n'
                 '#### Insights Consultant',
                 style={'textAlign': 'center',
                        'fontSize': '40px', 'line-height': '0.5', 'margin-top': '35px'}),

    dcc.Markdown('### Who I am', style={'textAlign': 'center', 'margin-top': '40px','color':'gray'}),
    html.Hr(),
    dcc.Markdown('+10 years consumer insights experience & +5 years media strategy experience.\n'
                 'Data wiz & storyteller. vlookup advocate.  \n'
                 '_"I have no special talent. I am only passionately curious"_ - A. Einstein\n',
                 style={'textAlign': 'center', 'white-space': 'pre'}),



    dcc.Markdown('### Work History', style={'textAlign': 'center', 'margin-top': '60px','color':'gray'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Independent Consultant**  \n'
                         '10/2021 to current',
                         style={'textAlign': 'left'}),
        ], width=3),
        dbc.Col([
            dcc.Markdown('**Insights Manager**  \n'
                         'US & UK',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Provide clients with data-driven insight and decision making at the key stages of Strategic Planning, KPI selection and target setting, measurement framework development and post-campaign evaluation.'),
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Wavemaker Argentina**  \n'
                         '06/2019 to 07/2021  \n',
                         style={'textAlign': 'left'})
        ], width=3),
        dbc.Col([
            dcc.Markdown('**Head of Business Planning & Strategy**  \n'
                         'Buenos Aires, AR',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Responsible for developing and executing communication strategies for new and existing clients, considering business, consumer, and competitive factors, as well as brand and product needs.'),
                html.Li(
                    'Conduct regular and ad-hoc analysis of market trends, consumer insights, media landscape, and competition using diverse sources, including syndicated data, third-party resources, proprietary tools, and desk research methods.'),
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Mindshare Argentina**  \n'
                         '03/2014 to 06/2019',
                         style={'textAlign': 'left'})
        ], width=3),
        dbc.Col([
            dcc.Markdown('**Business & Comms Planning Sr. Manager**  \n'
                         'Buenos Aires, AR',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Manage a team of up to 5 people, prioritizing career and talent growth.'),
                html.Li(
                    'Oversee end-to-end execution of qualitative and quantitative projects, from setup to presenting findings to steakholders.'),
                html.Li(
                    'Lead development of customized projects to gain deeper insights into consumer behavior, market dynamics, and media trends.'),
                html.Li(
                    'Collaborate with client leads to formulate effective communication strategies for new and existing clients.'),
            ]),

            dcc.Markdown('**Business Planning Coordinator**  \n'
                         'Buenos Aires, AR',
                         style={'white-space': 'pre'},
                         className='ms-3'),

            dcc.Markdown('**Business Planning Analyst**  \n'
                         'Buenos Aires, AR',
                         style={'white-space': 'pre'},
                         className='ms-3'),

        ], width=5),
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**VPM Vía Pública**  \n'
                         '01/2012 to 03/2014  \n',
                         style={'textAlign': 'left'}),
        ], width=3),
        dbc.Col([
            dcc.Markdown('**Commercial Assistant**  \n'
                         'Buenos Aires, AR',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Responsible for providing the commercial team with timely updates on industry trends, campaign insights, and performance reports.'),
                html.Li(
                    'Serve as a liaison between various departments to ensure seamless campaign execution and implementation.'),
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Zenith Media**  \n'
                         '12/2010 to 01/2012  \n',
                         style={'textAlign': 'left'})
        ], width=3),
        dbc.Col([
            dcc.Markdown('**Research Analyst**  \n'
                         'Buenos Aires, AR',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Conduct comprehensive consumer insights, competitive analysis, and industry research utilizing syndicated and proprietary tools. '),
                html.Li(
                    'Primarily focused on delivering analysis for the FMCG industry while maintaining versatility across other sectors.'),
            ])
        ], width=5)
    ], justify='center'),

    dcc.Markdown('### Education', style={'textAlign': 'center', 'margin-top': '60px','color':'gray'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Fundación de Altos Estudios**  \n'
                         '**en Ciencias Comerciales**  \n'
                         '2011',
                         style={'textAlign': 'left'})
        ], width=3),
        dbc.Col([
            dcc.Markdown('**Bachelor\'s Degree**    \n'
                         '**Advertising & Strategic Communication**  \n'
                         'Buenos Aires, AR',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
])