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
                return pd.read_csv(io.BytesIO(decoded))  
            elif "xls" in filename:
                return pd.read_excel(io.BytesIO(decoded))   
            else:
                raise Exception(file_import_error_message)
        except Exception as e:
            raise str(e)

    def app_upload_file(self, app):
        @app.callback(
            Output("store-movie-list-id", "data"),
            Output("upload-movie-title-excel-modal-position-id", "is_open"),
            Output("upload-movie-title-excel-id", "children"),
            Output("upload-movie-title-excel-modal-message-id", "children"),
            Output("loading-excel-id", "children"),
            State("upload-movie-list-btn-id", "filename"),
            Input("upload-movie-list-btn-id", "contents"),
        )
        def nested_upload(names, contents):
            change_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
            if contents is None:
                raise dash.exceptions.PreventUpdate()
            elif "upload-movie-list-btn-id" in change_id:
                try:
                    movie_df = self.parse_file_contents(contents, names)
                except:
                    return None, True, error_title, file_import_error_message, None
                
                if list(movie_df.columns)[0] == 'Title':
                    self.uploaded_movie_list = movie_df.iloc[:, 0]
                else:
                    return None, True, error_title, no_title_column_message, None

                import_success_message = (
                    str(len(self.uploaded_movie_list))
                    + excel_movie_titles_uploaded_message
                )
                return (
                    self.uploaded_movie_list,
                    True,
                    success_title,
                    import_success_message,
                    None,
                )
            else:
                raise dash.exceptions.PreventUpdate()

        return nested_upload
