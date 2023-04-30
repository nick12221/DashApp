import base64
import io
import pandas as pd
from config import *


class CSVImportExport:
    '''Class for reading and writing csv files.
    
    Attributes
    ----------
    imported_movie_list : list
        List of movies (string values) that were uploaded from csv.

    Methods
    -------
    parse_csv_contents:
        Saves down list of movie titles from the uploaded csv..
    '''

    def __init__(self):
        '''
        Constructs all the necessary attributes for the CSVImportExport object.
        '''
        self.imported_movie_list = None

    def parse_csv_contents(self, contents, filename):
        '''This function reads in a csv file into the dash app.
        
        Parameters:
        
        contents: 
            Contents of the csv file that was uploaded.

        filename: str
            Name of the csv file that was uploaded.
            
        Returns: 
            Does not return anything. Saves down movies as list attribute to the CSVImportExport object.
        '''
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)

        try:
            if 'csv' in filename:
                movie_df = pd.read_csv(io.BytesIO(decoded))
                self.imported_movie_list = movie_df.iloc[:,0]
            else:
                raise Exception(csv_import_error_message)
        except Exception as e:
            raise str(e)