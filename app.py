import dash
import sys
import webbrowser
from threading import Timer
from dash import Dash, html, dcc, no_update, dash_table as dt
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from CallbackFunctions.file_import_export import *
from TabOneComponents.tab_one_components import *

FileImportExport = FileImportExport()

#Initialize app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(id='dash-app-id', children=[
    dcc.Tabs([
        dcc.Tab(label=tab_one_label, id='tab-one-id', children=[
            html.Div(id='title-page-id', children=[
                welcome_form,
                instruction_capabilities_forms,
                html.Div(id='import-movie-data-row-id', children=[
                    confirm_movies_form
                ])
            ])  
        ]),
        dcc.Tab(label=tab_two_label, id='tab-two-id', children=[
        ])  
    ])
])


FileImportExport.app_upload_file(app)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')

if __name__ == '__main__':
    Timer(1, open_browser).start();
    app.run_server(debug=True, use_reloader=False)