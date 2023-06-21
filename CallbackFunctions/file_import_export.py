import base64
import io
import pandas as pd
import dash
from dash.dependencies import Input, Output, State
from config import *


class FileImportExport:
    """Class for reading and writing csv files.

    Attributes
    ----------
    uploaded_movie_list : list
        List of movies (string values) that were uploaded from csv.

    Methods
    -------
    parse_csv_contents:
        Saves down list of movie titles from the uploaded csv..
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the CSVImportExport object.
        """
        self.uploaded_movie_list = None

    def parse_file_contents(self, file_contents, filename):
        """This function reads in a csv file into the dash app.

        Parameters:

        contents:
            Contents of the csv file that was uploaded.

        filename: str
            Name of the csv file that was uploaded.

        Returns:
            Does not return anything. Saves down movies as list attribute to the CSVImportExport object.
        """
        content_type, content_string = file_contents.split(",")
        decoded = base64.b64decode(content_string)

        try:
            if "csv" in filename:
                movie_df = pd.read_csv(io.BytesIO(decoded))
                self.uploaded_movie_list = movie_df.iloc[:, 0]
            elif "xls" in filename:
                movie_df = pd.read_excel(io.BytesIO(decoded))
                self.uploaded_movie_list = movie_df.iloc[:, 0]
            else:
                raise Exception(file_import_error_message)
        except Exception as e:
            raise str(e)

    def app_upload_file(self, app):
        @app.callback(
            Output("store-movie-list-id", "data"),
            State("upload-movie-list-btn-id", "filename"),
            Input("upload-movie-list-btn-id", "contents"),
        )
        def nested_upload(names, contents):
            change_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
            if contents is None:
                raise dash.exceptions.PreventUpdate()
            elif "upload-movie-list-btn-id" in change_id:
                self.parse_file_contents(contents, names)
                return self.uploaded_movie_list
            else:
                raise dash.exceptions.PreventUpdate()

        return nested_upload
