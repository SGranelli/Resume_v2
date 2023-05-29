import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=3)


layout = html.Div([
    dcc.Markdown('**Soledad Granelli**  \n'
                 '#### Insights Consultant',
                 style={'textAlign': 'center',
                        'fontSize': '40px', 'line-height': '0.5', 'margin-top': '35px'}),

    dcc.Markdown('### Reach out @', style={'textAlign': 'center', 'margin-top': '40px','color':'gray'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('[Mobile] (https://api.whatsapp.com/send?phone=541136758004)', link_target='_blank', style={'textAlign': 'center'})
        ], width=4),
        dbc.Col([
            dcc.Markdown('[Email] (mailto://soledad.granelli@gmail.com)', link_target='_blank', style={'textAlign': 'center'},
                         className='ms-3'),
        ], width=4),
        dbc.Col([
            dcc.Markdown('[LinkedIn] (https://www.linkedin.com/in/soledad-granelli/)', link_target='_blank', style={'textAlign': 'center'})
        ], width=4),
    ], justify='center'),
])