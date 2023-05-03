import requests
import json
from config import *
import dash
from dash.dependencies import Input, Output, State

class MovieRequests:
    '''This class is for connecting to the OMDB API.
    
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
    '''

    def __init__(self):
        '''
        Constructs all the necessary attributes for the MovieRequests object.
        '''

        self.api_key = 'd5320d5f' #for business would put this in an AWS Secrets manager or equivalent
        self.movie_info_list = []
        self.invalid_movies_list = []


    def get_movie_data(self, movie_title_list):
        '''This function connects to the OMDB API and returns a list of dictionaries.
        
        Parameters:
        
        movie_title_list: list, str
            A list of movie titles whose data you want to get. Movie titles should be strings.
            
        Returns: Does not return a value, saves down two lists as attributes
            List of dictionaries with each movie's information. List of invalid movies.
        '''
        
        for i in movie_title_list:
            movie_response = requests.get(f'http://www.omdbapi.com/?t={i}&apikey={self.api_key}')
            movie_json = movie_response.text
            movie_dict = json.loads(movie_json)
            if movie_dict['Response'] == 'False':
                self.invalid_movies_list.append(i)
            else:
                self.movie_info_list.append(movie_dict)

    def import_movie_data_app(self, app):
        @app.callback(Output('store-movie-data-id', 'data'),
            Output('pull-movie-modal-position-id', 'is_open'),
            Output('pull-movie-modal-title-id', 'children'),
            Output('pull-movie-modal-message-id', 'children'),
            Output('loading-pulling-down-movie-info-id', 'children'),
            State('store-movie-list-id', 'data'),
            Input('import-movies-api-btn-id', 'n_clicks'))
        
        def nested_import_api_data(movie_list, api_btn_clicks):
            change_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
            if api_btn_clicks == 0:
                raise dash.exceptions.PreventUpdate()
            elif 'import-movies-api-btn-id' in change_id:
                try:
                    self.get_movie_data(movie_list)
                except Exception as e:
                    return None, True, error_title, str(e)

                if len(self.invalid_movies_list) > 0:
                    invalid_movies = ', '.join(self.invalid_movies_list)
                    num_movies_imported = str(len(self.movie_info_list))
                    return self.movie_info_list, True, success_title, num_movies_imported+modal_message_movies_imported+modal_message_wrong_movies+invalid_movies, None
                else:
                    return self.movie_info_list, True, success_title, num_movies_imported+modal_message_movies_imported, None
