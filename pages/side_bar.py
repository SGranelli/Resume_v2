import dash
from dash import html
import dash_bootstrap_components as dbc

def sidebar():
    nav_links = []
    for page in dash.page_registry.values():
        if page["path"].startswith("/app"):
            nav_links.append(
                dbc.NavLink(
                    [
                        html.Div(page["title"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            )
        elif page["path"]=="/portfolio":
            nav_links.append(
                dbc.NavLink(
                    [
                        html.Div("Research projects", className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            )
    return dbc.Nav(children=nav_links,
                   vertical=True,
                   pills=True,
                   className="bg-dark")