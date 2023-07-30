import dash
import webbrowser
from dash import html, dcc, no_update, dash_table as dt
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from movie_api import MovieRequests
from file_import_export import FileImportExport
from components import *
from component_ids import *


class DashApp:
    def __init__(self):
        self.app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.app.layout = html.Div(
            id=dash_app_id,
            children=[
                dcc.Tab(
                    label=tab_one_label,
                    id=tab_one_id,
                    children=[
                        html.Div(
                            id=title_page_id,
                            children=[
                                app_title_form,
                                components_div,
                            ],
                        )
                    ],
                ),
            ],
        )

        self.APIRequests = MovieRequests()
        self.ExcelImportExport = FileImportExport()

        self.ExcelImportExport.app_upload_file(self.app)
        self.APIRequests.import_movie_data_app(self.app)
        self.ExcelImportExport.app_model_result_export(self.app)

    def run(self):
        webbrowser.open_new("http://127.0.0.1:8050/")
        self.app.run_server(debug=True, use_reloader=True)


if __name__ == "__main__":
    app = DashApp()
    app.run()
