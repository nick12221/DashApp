from config import *
import dash
from dash import Dash, html, dcc, no_update, dash_table as dt
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc


predictions__choies = dcc.RadioItems(['Use Imported Data', 'Build Own Prediction'], 'Use Imported Data')

instructions_running_predictions = dbc.Form(id='instructions-for-model-id',
                                            children=[
                                                dcc.Markdown('''
                                                * Please upload a CSV or excel with one column for the movies you want to pull from the OMDB API. App only allows for pulling 1,000 movies per day. Please click the "import" button to pull the data into the app.

                                                * The second tab performs segmentation using K Means Clustering.

                                                * The third tab is responsible for statistical learning, where the user can build their own linear regression model.

                                                * The fourth tab you can upload your own description for a movie and it will make a prediction for what genre(s) it could belong to.
                                            ''')
                                            ])

