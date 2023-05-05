from config import *
import dash
from dash import Dash, html, dcc, no_update, dash_table as dt
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc


instructions_pulling_movies_form = dbc.Form(id='instructions-for-cluster-tab-id',
                                children=[
                                    dcc.Markdown('''
                                    * Configure K Means Clustering algorithm using the variable selection and number of clusters options below. Click the "Run" button to get results.

                                    * Analyze the types of clusters in the data table and use the charts to evaluate the algorithm.
                                    ''')
                                ])

cluster_options_dropdown = dcc.Dropdown(id = 'cluster-options-dropdown-id',
                            placeholder="Select variables for K Means Clustering")

num_clusters_input = dcc.Input(id='num-cluster-input-id',
                            type='number',
                            placeholder='Please enter number of clusters',
                            min=0)


run_cluster_algorithm = html.Button(run_cluster_message,
                                        id='run-cluster-btn-id',
                                        n_clicks=0)

export_clusters_btn = html.Button(export_cluster_table_message,
                                        id='export-cluster-table-btn-id',
                                        n_clicks=0)


configure_cluster_algorithm = html.Div(id='configure-div-id', children=[
                                dbc.Row([
                                    html.Div(id='variable-dropdown-div-id', children=[
                                        dbc.Col([
                                            cluster_options_dropdown
                                        ])
                                    ]),
                                    html.Div(id='num_cluster_input-div-id', children=[
                                        dbc.Col([
                                            num_clusters_input
                                        ])
                                    ]),
                                    html.Div(id='run-cluster-div-id', children=[
                                        dbc.Col([
                                            run_cluster_algorithm
                                        ])
                                    ]),
                                    html.Div(id='export-div-id', children=[
                                        dbc.Col([
                                            export_clusters_btn
                                        ])
                                    ])
                                ])
                            ])

cluster_result_table = dt.DataTable(id='cluster-table-id',
                                        filter_action='native',
                                        sort_action='native',
                                        style_header={'backgroundColor':'#ACC0C4',
                                                    'fontWeight':'bold'}
                                        )

elbow_graph = dcc.Graph(id='elbow-graph-id')

silhoutte_graph = dcc.Graph(id='silhouette-graph-id')

results_section = html.Div(id='all-result-div-id',children = [
    dbc.Row([
        html.Div(id='result-table-div-id', children=[
            dbc.Col([
                cluster_result_table
            ])
        ]),
        html.Div(id='evaluation-div-id',children=[
                dbc.Col([
                    html.Div(id='elbow-div-id', children=[
                        dbc.Row([
                            elbow_graph
                        ])
                    ]),
                    html.Div(id='silhouette-div-id', children=[
                        dbc.Row([
                            silhoutte_graph
                        ])
                    ])
                ])
            ])
        ])
    ])