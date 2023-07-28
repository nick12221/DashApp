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

    def __init__(self):
        """Initialization method for the class."""

        self.numeric_imputer = SimpleImputer(strategy="mean")

    def fit(self, X: pd.DataFrame) -> "FeatureTransformer":
        """Method to learn the parameters of the training dataset.

        Parameters:

        X: Pandas dataframe of the data to fit.

        Returns: Self."""

        X[runtime_column] = X[runtime_column].str.extract(r"(\d+)").astype(float)
        X[imdb_votes_column] = X[imdb_votes_column].str.extract(r"(\d+)").astype(float)
        X[awards_column] = X[awards_column].str.lower()
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

        X[model_numeric_columns] = self.numeric_imputer.transform(
            X[model_numeric_columns]
        )

        return X


class CustomPreprocessor:
    """Class for creating a model preprocessing pipeline and fitting and transforming data.

    Attributes:

    preprocessor: Use column transformer to create execution plan of preprocessing steps.

    training_df: pandas dataframe of training data

    Methods:

    fit: Get params of training data to use on the test dataset.

    Transform: perform the necessary transformations on the data."""

    def __init__(self, award_win_value, award_nom_value, award_no_award_value):
        """Method to initialize the class."""

        self.preprocessor = None
        self.award_true = (award_win_value,)
        self.nom_true = (award_nom_value,)
        self.no_award = (award_no_award_value,)

    def fit(self, initial_df: pd.DataFrame) -> None:
        """Method that creates the transformation pipeline and leverages the
        FeatureTransformer class."""

        self.preprocessor = ColumnTransformer(
            transformers=[
                (
                    "preprocessing",
                    FeatureTransformer(),
                    model_all_columns,
                ),
            ],
            verbose_feature_names_out=False,
        )

        self.preprocessor.fit(initial_df)

        return self

    def transform(self, new_data: pd.DataFrame) -> pd.DataFrame:
        """Method to transform the dataset based on learned parameters and additional
        transformation.

        Parameters:

        X: Pandas dataframe of data to transform.

        Returns: Transformed Pandas Dataframe."""

        X_new = new_data.copy()

        X = self.preprocessor.transform(X_new)
        X[created_award_status_column] = np.where(
            X[awards_column].str.contains(win_text_identifier) == True,
            self.award_true,
            np.where(
                X[awards_column].str.contains(nom_text_identifier) == True,
                self.nom_true,
                self.no_award,
            ),
        )

        X = pd.get_dummies(X, columns=[created_award_status_column])

        if award_status_reference_column in X.columns:
            X.drop([award_status_reference_column, awards_column], axis=1, inplace=True)
        else:
            s2 = [col for col in X.columns if created_award_status_column in col]
            X.drop([s2[0], awards_column], axis=1, inplace=True)

        return X

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
