import dash
import webbrowser
import numpy as np
import pandas as pd
from dash import html, dcc, no_update, dash_table as dt
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import joblib
from movie_api import MovieRequests
from file_import_export import FileImportExport
from run_model import ModelPrediction
from components import *
from component_ids import *


class DashApp:
    """Class for the dash app

    Attributes
    ----------

    app: The model app

    model: The pretrained model to load

    preprocessor: The pretrained pipeline

    app layout: The layout of the application

    APIRequests: Loaded class for api request

    ExcelImportExport: Loaded class for importing/exporting csv files

    modelPrediction: Loaded class for model predictions

    Methods
    -------

    run: Run the dash app
    """

    def __init__(self):
        self.app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.model = joblib.load("fitted_model.pkl")
        self.preprocessor = joblib.load("fitted_preprocessor.pkl")
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
        self.ModelPrediction = ModelPrediction(preprocessor=self.preprocessor)

        self.ExcelImportExport.app_upload_file(self.app)
        self.APIRequests.import_movie_data_app(self.app)
        self.ExcelImportExport.app_model_result_export(self.app)
        self.ModelPrediction.model_predictions(self.app, self.model)

    def run(self):
        webbrowser.open_new("http://127.0.0.1:8050/")
        self.app.run_server(debug=True, use_reloader=False)


if __name__ == "__main__":
    app = DashApp()
    app.run()
