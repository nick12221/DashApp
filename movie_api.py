import requests
import json
from config import *
from component_ids import *
import dash
from dash.dependencies import Input, Output, State
import time


class MovieRequests:
    """This class is for connecting to the OMDB API.

    Attributes
    ----------
    api_key : str
        The API key to connect to OMDB

    movie_info_list: list, dict
        list of dictionaries with movie information

    invalid_movies_list: list
        list of invalid movies

    Methods
    -------
    get_movie_data:
        Returns a list of dictionaries for the list of movie titles passed through the function.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the MovieRequests object.
        """

        self.api_key = "d5320d5f"  # for business would put this in an AWS Secrets manager or equivalent
        self.movie_info_list = []
        self.invalid_movies_list = []

    def get_movie_data(self, movie_title: str) -> None:
        """This function connects to the OMDB API and returns a list of dictionaries.

        Parameters:

        movie_title: str
            A list of movie titles whose data you want to get. Movie titles should be strings.

        Returns: None saves down two lists as attributes list of dictionaries with each movie's information and
                list of invalid movies.
        """

        movie_response = requests.get(
            f"http://www.omdbapi.com/?t={movie_title}&apikey={self.api_key}"
        )
        movie_json = movie_response.text
        movie_dict = json.loads(movie_json)
        if movie_dict["Response"] == "False":
            self.invalid_movies_list.append(movie_title)
        else:
            self.movie_info_list.append(movie_dict)

    def import_movie_data_app(self, app):
        @app.callback(
            Output(imported_movie_data_id, "data"),
            Output(api_import_modal_position_id, "is_open"),
            Output(api_import_modal_title_id, "children"),
            Output(api_import_modal_message_id, "children"),
            Output(total_time_box_id, "children"),
            Output(avg_time_box_id, "children"),
            Output(api_import_loading_id, "children"),
            State(imported_file_movie_list_id, "data"),
            Input(api_import_btn_id, "n_clicks"),
        )
        def nested_import_api_data(movie_list, api_btn_clicks):
            change_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
            if api_btn_clicks == 0:
                raise dash.exceptions.PreventUpdate()
            elif movie_list is None:
                raise dash.exceptions.PreventUpdate()
            elif api_import_btn_id in change_id:
                try:
                    start_time = time.time()

                    for i in movie_list:
                        self.get_movie_data(i)

                    end_time = time.time()
                    total_time = str(round(end_time - start_time, 2)) + " Sec(s)"
                    avg_time = (
                        str(round((end_time - start_time) / len(movie_list), 2))
                        + " S/Request"
                    )

                except Exception as e:
                    return (
                        None,
                        True,
                        error_title,
                        str(e),
                        default_total_time,
                        default_avg_time,
                        None,
                    )

                num_movies_imported = str(len(self.movie_info_list))

                if len(self.invalid_movies_list) > 0:
                    invalid_movies = ", ".join(self.invalid_movies_list)
                    return (
                        self.movie_info_list,
                        True,
                        success_title,
                        num_movies_imported
                        + modal_message_movies_imported
                        + modal_message_wrong_movies
                        + invalid_movies,
                        total_time,
                        avg_time,
                        None,
                    )
                else:
                    return (
                        self.movie_info_list,
                        True,
                        success_title,
                        num_movies_imported + modal_message_movies_imported,
                        total_time,
                        avg_time,
                        None,
                    )
            else:
                raise dash.exceptions.PreventUpdate()

        return nested_import_api_data
