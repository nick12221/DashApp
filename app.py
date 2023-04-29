import dash
from dash import Dash, html, dcc, no_update, dash_table as dt
from dash.dependecies import Input, Output, State
import dash_bootstrap_components as dbc


#Initialize app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div()