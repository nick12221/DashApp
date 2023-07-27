import pandas as pd
import numpy as np
from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import joblib
from sklearn import set_config
from config import *

set_config(transform_output="pandas")


class FeatureTransformer(BaseEstimator, TransformerMixin):
    """Class for creating custom fit and transform method for feature transformation.
    Inherits from the BaseEstimator and TransformerMixin classes of scikit-learn.

    Attributes:

    nomination_condition: Condition to indicate whether a movie was nominated for an award.

    award_condition: Condition to indicate whether a movie won an award.

    award_true: Value if the movie did win an award.

    nom_true: Value if the movie was nominated for an award.

    no_award: Value if the movie did not win an award.

    numeric_imputer: The imputer to use for missing numeric values.

    Methods:

    fit: Get params of training data to use on the test dataset.

    Transform: perform the necessary transformations on the data."""

    def __init__(
        self,
        nomination_condition,
        award_condition,
        award_true: str,
        nom_true: str,
        no_award: str,
    ):
        """Initialization method for the class."""

        self.nomination_condition = nomination_condition
        self.award_condition = award_condition
        self.award_true = award_true
        self.nom_true = nom_true
        self.no_award = no_award
        self.numeric_imputer = SimpleImputer(strategy="mean")

    def fit(self, X: pd.DataFrame) -> "FeatureTransformer":
        """Method to learn the parameters of the training dataset.

        Parameters:

        X: Pandas dataframe of the data to fit.

        Returns: Self."""

        X[runtime_column] = X[runtime_column].str.extract(r"(\d+)").astype(float)
        X[imdb_votes_column] = X[imdb_votes_column].str.extract(r"(\d+)").astype(float)
        self.numeric_imputer.fit(X[model_numeric_columns])
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """Method to transform the dataset based on learned parameters and additional transformation.

        Parameters:

        X: Pandas dataframe of data to transform.

        Returns: Transformed Pandas Dataframe."""

        if pd.api.types.is_numeric_dtype(X[runtime_column]) == True:
            pass
        else:
            X[runtime_column] = X[runtime_column].str.extract(r"(\d+)").astype(float)

        if pd.api.types.is_numeric_dtype(X[imdb_votes_column]) == True:
            pass
        else:
            X[imdb_votes_column] = (
                X[imdb_votes_column].str.extract(r"(\d+)").astype(float)
            )

        X[awards_column] = X[awards_column].str.lower()
        X[created_award_status_column] = np.where(
            self.award_condition,
            self.award_true,
            np.where(self.nomination_condition, self.nom_true, self.no_award),
        )
        X[model_numeric_columns] = self.numeric_imputer.transform(
            X[model_numeric_columns]
        )
        X = pd.get_dummies(X, columns=[created_award_status_column])
        X.drop([award_status_reference_column, awards_column], axis=1, inplace=True)

        return X


class CustomPreprocessor:
    """Class for creating a model preprocessing pipeline and fitting and transforming data.

    Attributes:

    preprocessor: Use column transformer to create execution plan of preprocessing steps.

    training_df: pandas dataframe of training data

    Methods:

    fit: Get params of training data to use on the test dataset.

    Transform: perform the necessary transformations on the data."""

    def __init__(self, training_data: pd.DataFrame):
        """Method to initialize the class."""

        self.preprocessor = None
        self.training_df = training_data

    def fit(self):
        """Method that creates the transformation pipeline and leverages the
        FeatureTransformer class."""

        self.preprocessor = ColumnTransformer(
            transformers=[
                (
                    "preprocessing",
                    FeatureTransformer(
                        award_condition=self.training_df[awards_column].str.contains(
                            win_text_identifier
                        )
                        == True,
                        award_true=award_win_value,
                        nomination_condition=self.training_df[
                            awards_column
                        ].str.contains(nom_text_identifier)
                        == True,
                        nom_true=award_nom_value,
                        no_award=award_no_award_value,
                    ),
                    model_all_columns,
                ),
            ],
            verbose_feature_names_out=False,
        )

        self.preprocessor.fit(self.training_df)

        return self

    def transform(self, new_data: pd.DataFrame) -> pd.DataFrame:
        """Method to transform the dataset based on learned parameters and additional
        transformation.

        Parameters:

        X: Pandas dataframe of data to transform.

        Returns: Transformed Pandas Dataframe."""

        X_new = new_data.copy()

        X_new_preprocessed = self.preprocessor.transform(X_new)
        return X_new_preprocessed

    def save(self, filepath: str) -> None:
        """Method to save down the preprocessor attribute.

        Parameters:

        filepath: string of the filepath to save down.

        Returns: None, saves down object."""

        joblib.dump(self.preprocessor, filepath)

    def load(self, filepath: str) -> None:
        """Method to read the saved preprocessor attribute.

        Parameters:

        filepath: string of the filepath to save down.

        Returns: None, Saves down as preprocessor attribute"""
        self.preprocessor = joblib.load(filepath)
