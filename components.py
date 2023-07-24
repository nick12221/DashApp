from config import *
from component_ids import *
from dash import Dash, html, dcc, no_update, dash_table as dt
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

# Components for api and excel functionality

# storage and loading components
store_movie_list = dcc.Store(id=imported_file_movie_list_id)

store_omdb_data = dcc.Store(id=imported_movie_data_id)

loading_excel_import = dcc.Loading(id=file_upload_loading_id)

loading_api_import = dcc.Loading(id=api_import_loading_id)

download_component = dcc.Download(id=results_download_id)

# The excel upload and import from OMDB api
upload_movie_button = dcc.Upload(
    id=upload_file_btn_id, children=html.Div([html.A(upload_file_message)])
)

import_movie_api_data_btn = html.Button(
    import_movie_api_message, id=api_import_btn_id, n_clicks=0
)

# Modal for messages that pops out after clicking the import api button
pull_movie_info_modal = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader(
                    dbc.ModalTitle(html.Div(id=api_import_modal_title_id)),
                    close_button=True,
                ),
                dbc.ModalBody(html.Div(id=api_import_modal_message_id)),
            ],
            id=api_import_modal_position_id,
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
                    dbc.ModalTitle(html.Div(id=file_upload_modal_title_id)),
                    close_button=True,
                ),
                dbc.ModalBody(html.Div(id=file_upload_modal_message_id)),
            ],
            id=file_upload_modal_position_id,
            centered=True,
            is_open=False,
        )
    ]
)

# App title form
app_title_form = dbc.Form(id=app_title_form_id, children=[welcome_message])


instructions_pulling_movies_form = dbc.Form(
    id=instructions_text_id,
    children=[
        dcc.Markdown(
            """
    ##### **Instructions and Overview**

    - This is a ML Application designed to pull movie data from the OMDB API and predict revenue.
    
    - Upload a CSV or Excel file with one column labeled "Title" and the list of movies to import.
    
    - Click the "Import" button to retrieve movie data from OMDB and see API query performance (Can only import 1,000/day).
    
    - Use "Run Model" button to make revenue predictions for the movies imported via the API.
    
    - Utilize the visuals to understand model composition and performance.
    
    ##### **Key Features**
    
    - Flexible file upload to provide target list of movies.
    
    - User-friendly interface and controls for accessing data from the OMDB API.
    
    - Full display of fitted model coefficients and statistical significance using my own statistical package.
    
    - Seamless experience to run model with data preprocessing handled by the app.
    
    - Just press "Predict" to predict movie revenue and then download results!
    """
        )
    ],
)

# Div components for the boxes showing time for api pull
total_time_box = html.Div(id=total_time_box_id, children=[default_total_time])
avg_time_box = html.Div(id=avg_time_box_id, children=[default_avg_time])

# Components for the model part of the app

# Buttons for running model and results
model_prediction_btn = html.Button(
    model_run_btn_text, id=model_prediction_btn_id, n_clicks=0
)

export_results_btn = html.Button(export_btn_text, id=export_results_btn_id, n_clicks=0)

model_coefficients_graph = dcc.Graph(
    id=model_coefs_div_id, config={"displayModeBar": False}
)

# Table with results
result_table = dt.DataTable(
    id=results_table_id,
    filter_action="native",
    page_action="none",
    filter_options={"case": "insensitive"},
    style_header={
        "backgroundColor": "#D4F1F4",
        "color": "black",
        "padding": ".5vh .3vw",
        "textAlign": "center",
        "fontSize": "2.5vh",
        "boxShadow": "0px 8px 20px rgba(0, 0, 0, 0.2)",
        "border": "1px solid #ddd",
    },
    columns=[
        {"name": file_title_column_name, "id": file_title_column_name},
        {"name": revenue_prediction_column, "id": revenue_prediction_column},
    ],
)


# Final structure to pass to app
components_div = dbc.Form(
    id=movie_file_and_api_form_id,
    children=[
        store_movie_list,
        store_omdb_data,
        html.Div(
            id=all_components_div_id,
            children=[
                html.Div(
                    id=instructions_div_id,
                    children=[instructions_pulling_movies_form],
                ),
                html.Div(
                    id=all_components_but_instructions_div_id,
                    children=[
                        html.Div(
                            id=api_pull_component_id,
                            children=[
                                html.Div(
                                    id=upload_and_api_div_id,
                                    children=[
                                        html.Label(
                                            id=button_labels_div_id,
                                            children=[button_controls_label],
                                        ),
                                        upload_movie_button,
                                        import_movie_api_data_btn,
                                        loading_excel_import,
                                        loading_api_import,
                                    ],
                                ),
                                html.Div(
                                    id=total_time_div_id,
                                    children=[
                                        html.Label(
                                            id=total_time_label_id,
                                            children=[total_time_label],
                                        ),
                                        total_time_box,
                                    ],
                                ),
                                html.Div(
                                    id=avg_time_div_id,
                                    children=[
                                        html.Label(
                                            id=avg_time_label_id,
                                            children=[avg_time_label],
                                        ),
                                        avg_time_box,
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            id=model_title_div_id,
                            children=[model_section_title],
                        ),
                        html.Div(
                            id=model_components_div_id,
                            children=[
                                html.Div(
                                    id=graph_div_id,
                                    children=[model_coefficients_graph],
                                ),
                                html.Div(
                                    id=run_model_div_id,
                                    children=[
                                        html.Div(
                                            id=model_btns_div_id,
                                            children=[
                                                html.Div(
                                                    id=predict_div_id,
                                                    children=[model_prediction_btn],
                                                ),
                                                html.Div(
                                                    id=export_div_id,
                                                    children=[
                                                        export_results_btn,
                                                        download_component,
                                                    ],
                                                ),
                                            ],
                                        ),
                                        html.Div(
                                            id=result_table_div_id,
                                            children=[result_table],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        pull_movie_info_modal,
        upload_excel_modal,
    ],
)
