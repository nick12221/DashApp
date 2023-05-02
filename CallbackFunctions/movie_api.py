import requests
import json

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
            