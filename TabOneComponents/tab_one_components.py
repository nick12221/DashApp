from config import *
import dash
from dash import Dash, html, dcc, no_update, dash_table as dt
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

store_movie_list = dcc.Store(id='store-movie-list-id')

store_omdb_data = dcc.Store(id='store-movie-data-id')

loading_api_pull = dcc.Loading(id='loading-pulling-down-movie-info-id',
                               type="circle")

upload_movie_button= dcc.Upload(id='upload-movie-list-btn-id', children=html.Div([
                                html.A(upload_file_message)
                                ])
                            )

import_movie_api_data_btn = html.Button(import_movie_api_message,
                                        id='import-movies-api-btn-id',
                                        n_clicks=0)

pull_movie_info_modal = html.Div([
                            dbc.Modal(
                                [
                                    dbc.ModalHeader(dbc.ModalTitle(html.Div(id = 'pull-movie-modal-title-id')), close_button=True),
                                    dbc.ModalBody(html.Div(id='pull-movie-modal-message-id'))
                                ],
                                id='pull-movie-modal-position-id',
                                centered=True,
                                is_open=False
                            )
                        ])



welcome_form = dbc.Form(
    id='welcome-message-form-id',
    children=[
        welcome_message
    ]
)



instructions_pulling_movies_form = dbc.Form(id='instructions-for-app-id',
                                            children=[
                                                dcc.Markdown('''
                                                * Please upload a CSV or excel with one column for the movies you want to pull from the OMDB API. App only allows for pulling 1,000 movies per day. Please click the "import" button to pull the data into the app.

                                                * The second tab performs segmentation using K Means Clustering.

                                                * The third tab is responsible for statistical learning, where the user can build their own linear regression model.

                                                * The fourth tab you can upload your own description for a movie and it will make a prediction for what genre(s) it could belong to.
                                            ''')
                                            ])

capabilities_form = dbc.Form(id='capabilities-for-app-id',
                                            children=[
                                                dcc.Markdown('''
                                                * Pull any movie info through the app. 
                                        
                                                * Rich functionality for clustering and visualizing data.
                                         
                                                * Suite of statistical testing and modelling movie characteristics.
                                                
                                                * Predict movie genre for custom/new movie descriptions.
                                            ''')
                                            ])

instruction_capabilities_forms = dbc.Row([
                                    html.Div(id='instructions-form-id', children=[
                                        dbc.Col([
                                            instructions_pulling_movies_form
                                        ])
                                    ]),
                                    html.Div(id='capabilities-form-id', children=[
                                        dbc.Col([
                                            capabilities_form
                                        ])
                                    ])
                                ])

confirm_movies_form = dbc.Form(id='choose-movies-form-id',
                        children=[
                            store_movie_list,
                            store_omdb_data,
                            dbc.Label(id = 'choose-movie-label-id', children=[
                                enter_movie_instruction_label
                            ]),
                            html.Br(),
                            html.Br(),
                            dbc.Row([
                                html.Div(id='upload-csv-container-id', children=[
                                    dbc.Col([
                                        upload_movie_button
                                    ])
                                ]),
                                html.Div(id='import-movie-data-container-id', children=[
                                    dbc.Col([
                                        import_movie_api_data_btn
                                    ])
                                ])
                            ]),
                            loading_api_pull,
                            pull_movie_info_modal,
                        ])