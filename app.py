import dash
import webbrowser
from dash import Dash, html, dcc, no_update, dash_table as dt
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from movie_api import MovieRequests
from file_import_export import FileImportExport
from tab_one_components import *
from tab_two_components import *


# Initialize app
class DashApp:
    def __init__(self):
        self.app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.app.layout = html.Div(
            id="dash-app-id",
            children=[
                dcc.Tabs(
                    [
                        dcc.Tab(
                            label=tab_one_label,
                            id="tab-one-id",
                            children=[
                                html.Div(
                                    id="title-page-id",
                                    children=[
                                        welcome_form,
                                        instruction_capabilities_forms,
                                        html.Div(
                                            id="import-movie-data-row-id",
                                            children=[confirm_movies_form],
                                        ),
                                    ],
                                )
                            ],
                        ),
                    ]
                )
            ],
        )
        self.APIRequests = MovieRequests()
        self.ExcelImportExport = FileImportExport()

        self.ExcelImportExport.app_upload_file(self.app)
        self.APIRequests.import_movie_data_app(self.app)

    def run(self):
        webbrowser.open_new("http://127.0.0.1:8050/")
        self.app.run_server(debug=True, use_reloader=False)


if __name__ == "__main__":
    app = DashApp()
    app.run()
