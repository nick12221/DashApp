import base64
import io
import pandas as pd
import dash
from dash.dependencies import Input, Output, State
from config import *
from component_ids import *


class FileImportExport:
    """Class for reading and writing csv files.

    Attributes
    ----------
    uploaded_movie_list : list
        List of movies (string values) that were uploaded from csv or excel.

    Methods
    -------
    parse_file_contents:
        Returns dataframe of movie titles from the uploaded file.
    """

    def __init__(self):
        self.uploaded_movie_list = None

    def parse_file_contents(self, file_contents: str, filename: str) -> pd.DataFrame:
        """Method to read in csv or excel file.

        Parameters:

        file_contents: str:
            Contents of the csv file that was uploaded.

        filename: str
            Name of the csv file that was uploaded.

        Returns:
            Pandas dataframe.
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
            Output(imported_file_movie_list_id, "data"),
            Output(file_upload_modal_position_id, "is_open"),
            Output(file_upload_modal_title_id, "children"),
            Output(file_upload_modal_message_id, "children"),
            Output(file_upload_loading_id, "children"),
            State(upload_file_btn_id, "filename"),
            Input(upload_file_btn_id, "contents"),
        )
        def nested_upload(names, contents):
            change_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
            if contents is None:
                raise dash.exceptions.PreventUpdate()
            elif upload_file_btn_id in change_id:
                try:
                    movie_df = self.parse_file_contents(contents, names)
                except:
                    return None, True, error_title, file_import_error_message, None

                if list(movie_df.columns)[0] == file_title_column_name:
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
