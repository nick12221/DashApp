from config import *
import dash
from dash import Dash, html, dcc, no_update, dash_table as dt
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc


predictions_choices = dcc.RadioItems(
    ["Use Imported Data", "Build Own Prediction"], "Use Imported Data"
)
