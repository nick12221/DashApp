from config import *
import dash
from dash import Dash, html, dcc, no_update, dash_table as dt
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# storage and loading components used on the first tab
store_movie_list = dcc.Store(id="store-movie-list-id")

store_omdb_data = dcc.Store(id="store-movie-data-id")

loading_excel_import = dcc.Loading(id="loading-excel-id", type="circle")

loading_api_pull = dcc.Loading(id="loading-pulling-down-movie-info-id", type="circle")

# The excel upload and import from OMDB api
upload_movie_button = dcc.Upload(
    id="upload-movie-list-btn-id", children=html.Div([html.A(upload_file_message)])
)

import_movie_api_data_btn = html.Button(
    import_movie_api_message, id="import-movies-api-btn-id", n_clicks=0
)

# Modal for messages that pops out after clicking the import api button
pull_movie_info_modal = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader(
                    dbc.ModalTitle(html.Div(id="pull-movie-modal-title-id")),
                    close_button=True,
                ),
                dbc.ModalBody(html.Div(id="pull-movie-modal-message-id")),
            ],
            id="pull-movie-modal-position-id",
            centered=True,
            is_open=False,
        )
    ]
)

# Modal for messages that pops out after clicking the excel upload button
upload_excel_modal = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader(
                    dbc.ModalTitle(html.Div(id="upload-movie-title-excel-id")),
                    close_button=True,
                ),
                dbc.ModalBody(html.Div(id="upload-movie-title-excel-modal-message-id")),
            ],
            id="upload-movie-title-excel-modal-position-id",
            centered=True,
            is_open=False,
        )
    ]
)


welcome_form = dbc.Form(id="welcome-message-form-id", children=[welcome_message])


instructions_pulling_movies_form = dbc.Form(
    id="instructions-for-app-id",
    children=[
        dcc.Markdown(
            """
    ##### **Instructions and Overview**

    - This is a ML Application designed to pull movie data from the OMDB API and predict revenue.
    
    - Upload a CSV or Excel file with one column labeled "Title" and the list of movies to import.
    
    - Click the "Import" button to retrieve movie data from OMDB (Can only import 1,000/day).
    
    - Use the second tab for making revenue predictions on the movies imported on the first tab.
    
    - Utilize the visuals to understand model composition and performance.
    
    ##### **Key Features**
    
    - Flexible file upload to provide target list of movies.
    
    - User-friendly interface for accessing data from OMDB API.
    
    - Comprehensive suite of metrics displayed for the pretrained ML Model.
    
    - Seamless experience to run model with data preprocessing handled by the app.
    
    - Easy to run and download results for any movie.
    """
        )
    ],
)

movie_instructions_and_functionality = dbc.Form(
    id="choose-movies-form-id",
    children=[
        store_movie_list,
        store_omdb_data,
        dbc.Row(
            [
                html.Div(
                    id="instructions-form-id",
                    children=[instructions_pulling_movies_form],
                ),
                html.Div(
                    id="tab-one-buttons-id",
                    children=[
                        html.Label(
                            id="buttons-label-id", children=[button_controls_label]
                        ),
                        upload_movie_button,
                        import_movie_api_data_btn,
                    ],
                ),
            ],
        ),
        loading_api_pull,
        loading_excel_import,
        pull_movie_info_modal,
        upload_excel_modal,
    ],
)
