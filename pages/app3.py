import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from .side_bar import sidebar

dash.register_page(__name__, title='Data Viz projects', order=4)

tableau_dashboard_url1 = "https://public.tableau.com/app/profile/soledad.granelli/viz/Campaignanalysis_16229294927900/CampaignPerformance"
tableau_dashboard_url2 = "https://github.com/SGranelli/Newsroom_project.git"

def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [dcc.Markdown('#### **Data Viz project samples**',
                              style={'textAlign': 'center',
                                     'fontSize': '40px', 'line-height': '0.5', 'margin-top': '35px'}),
                 html.Hr(),

                 dbc.Row([
                     dbc.Col([
                         dcc.Markdown('**Tableau**  \n',
                                      style={'textAlign': 'left'})
                     ], width=4),
                     dbc.Col([
                         dcc.Markdown('**Digital campaign performance**    \n'
                                     'A dashboard that analyzes campaign performance, fetching data from Google Ads,   \n'
                                     'Facebook Ads and Programmatic. The tool allows us to visualize key metrics per source,   \n'
                                     'and by campaign and type of audience.   \n'
                                     'Jul 2021  \n',
                                      style={'white-space': 'pre'},
                                      className='ms-3'),
                         html.A('See dashboard', href=tableau_dashboard_url2, target='_blank', className='ms-3'),
                     ], width=5)
                 ], justify='center', style={'margin-top': '25px'}),

                 dbc.Row([
                     dbc.Col([
                         dcc.Markdown('**Python**  \n',
                                      style={'textAlign': 'left'})
                     ], width=4),
                     dbc.Col([
                         dcc.Markdown('**Newsroom**    \n'
                                      'A Python project to collect news from Google from up to 5 search terms.   \n'
                                      'Collect, visualize and download data to a CSV   \n'
                                      'Jun 2021',
                                      style={'white-space': 'pre'},
                                      className='ms-3'),
                         html.A('See dashboard', href=tableau_dashboard_url2, target='_blank', className='ms-3'),
                     ], width=5)
                 ], justify='center', style={'margin-top': '25px'})

                 ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10
            )
        ]
    )
])