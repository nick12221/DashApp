from model_preprocessing import CustomPreprocessor
import dash
import numpy as np
from components import *
from config import *
import pandas as pd
from sklearn import set_config


class ModelPrediction(CustomPreprocessor):
    """Class for executing the pretrained model. Child class of CustomPreprocessor.

    Attributes
    ---------

    Inherits all attributes from parent class CustomProcessor.

    Methods
    -------

    model_prediction: Method to run the model predictions"""

    def model_predictions(self, app, model):
        """Method for executing the prediction callback"""

        @app.callback(
            Output(results_table_id, "data"),
            Output(prediction_loading_id, "children"),
            State(store_omdb_data, "data"),
            Input(model_prediction_btn_id, "n_clicks"),
        )
        def run_model(input_data, clicks):
            set_config(transform_output="pandas")
            change_id = [p["prop_id"] for p in dash.callback_context.triggered][0]

            if clicks == 0:
                raise dash.exceptions.PreventUpdate()
            elif input_data is None:
                raise dash.exceptions.PreventUpdate()
            elif model_prediction_btn_id in change_id:
                input_df = pd.DataFrame(input_data)

                preprocessed_df = self.transform(input_df)
                movie_titles = input_df[movie_title_column].to_list()
                test_predictions = model.GetPredictions(
                    preprocessed_df.values
                ).flatten()
                pred_exp_df = np.exp(test_predictions)
                table_results = pd.DataFrame(
                    list(zip(movie_titles, pred_exp_df)),
                    columns=[file_title_column_name, revenue_prediction_column],
                )
                table_results[revenue_prediction_column] = table_results[
                    revenue_prediction_column
                ].apply(lambda x: f"${x:,.2f}")

                return table_results.to_dict("records"), None
            else:
                raise dash.exceptions.PreventUpdate()

        return run_model
