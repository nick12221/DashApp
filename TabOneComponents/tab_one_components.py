from config import *
import dash
from dash import Dash, html, dcc, no_update, dash_table as dt
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

store_movie_data = dcc.Store(id='store-movie-data-id')

movie_selection_dropdown = dcc.Dropdown(id='movie-selection-dropdown-id',
                                        options = top_1000_movies_list,
                                        optionHeight=65,
                                        placeholder = movie_selection_dropdown_placeholder,
                                        multi=True)

upload_movie_button= dcc.Upload(id='upload-excel-movie-list-id', children=html.Div([
                                html.A(upload_excel_message)
                                ])
                            )

import_dropdown_movies_button = html.Button(id='import-dropdown-movies-id',
                                            n_clicks=0)

import_csv_movies_button = html.Button(id='import-csv-movies-id',
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

                                            ])

capabilities_form = dbc.Form(id='capabilities-for-app-id',
                                            children=[
                                                
                                            ])



confirm_movies_form = dbc.Form(id='choose-movies-form-id',
                        children=[
                            store_movie_data,
                            dbc.Label(id = 'choose-movie-label-id', children=[
                                enter_movie_instruction_label
                            ]),
                            html.Br(),
                            html.Br(),
                            dbc.Row([
                                html.Div(id='movie-dropdown-container-id', children=[
                                    dbc.Col([
                                        movie_selection_dropdown
                                    ])
                                ]),
                                html.Div(id='upload-csv-container-id', children=[
                                    dbc.Col([
                                        upload_movie_button
                                    ])
                                ])
                            ]),
                            dcc.Loading(id='loading-pulling-down-movie-info-id'),
                            pull_movie_info_modal
                        ])