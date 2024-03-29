import pandas as pd
import numpy as np
from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import statsmodels.api as sm
import joblib
from sklearn import set_config
from config import *

set_config(transform_output="pandas")


class FeatureTransformer(BaseEstimator, TransformerMixin):
    """Class for creating custom fit and transform method for feature transformation.
    Inherits from the BaseEstimator and TransformerMixin classes of scikit-learn.

    Attributes
    ----------

    numeric_imputer: The imputer to use for missing numeric values.

    Methods
    ---------

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

        for i in model_numeric_columns:
            X[i] = (
                X[i]
                .str.replace(",", "", regex=True)
                .str.extract(r"(\d+)")
                .astype(float)
            )

        self.numeric_imputer.fit(X[model_numeric_columns])
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """Method to transform the dataset based on learned parameters and additional transformation.

        Parameters:

        X: Pandas dataframe of data to transform.

        Returns: Transformed Pandas Dataframe."""

        if pd.api.types.is_numeric_dtype(X[runtime_column]) == False:
            X[runtime_column] = (
                X[runtime_column]
                .str.replace(",", "", regex=True)
                .str.extract(r"(\d+)")
                .astype(float)
            )
        else:
            pass

        if pd.api.types.is_numeric_dtype(X[imdb_votes_column]) == False:
            X[imdb_votes_column] = (
                X[imdb_votes_column]
                .str.replace(",", "", regex=True)
                .str.extract(r"(\d+)")
                .astype(float)
            )
        else:
            pass

        if pd.api.types.is_numeric_dtype(X[metascore_column]) == False:
            X[metascore_column] = (
                X[metascore_column]
                .str.replace(",", "", regex=True)
                .str.extract(r"(\d+)")
                .astype(float)
            )
        else:
            pass

        X[model_numeric_columns] = self.numeric_imputer.transform(
            X[model_numeric_columns]
        )

        X[awards_column] = X[awards_column].str.lower()
        X[awards_column] = X[awards_column].fillna(award_status_reference_column)
        X[top_genre_column] = X[genre_column].str.split(",").str[0].str.lower()

        return X


class CustomPreprocessor:
    """Class for creating a model preprocessing pipeline and fitting and transforming data.

    Attributes
    ----------

    oscar_win: value for indicating oscar win.

    oscar_nom: Value for indicating oscar nomination.

    award_true: Value if the movie did win an award.

    nom_true: Value if the movie was nominated for an award.

    no_award: Value if the movie did not win an award.

    preprocessor: Use column transformer to create execution plan of preprocessing steps.

    Methods
    -------

    fit: Get params of training data to use on the test dataset.

    Transform: perform the necessary transformations on the data."""

    def __init__(
        self,
        preprocessor=None,
    ):
        """Method to initialize the class."""

        self.preprocessor = preprocessor
        self.oscar_win = oscar_win_value
        self.oscar_nom = oscar_nom_value
        self.award_true = award_win_value
        self.nom_true = award_nom_value
        self.no_award = award_no_award_value
        self.action_adventure = action_adv_value
        self.drama_thriller = drama_thriller_value
        self.comedy = comedy_value
        self.horror = horror_value
        self.animation = animation_value
        self.other_genre = other_genre_value

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
            X[awards_column].str.contains(oscar_win_regex, regex=True),
            self.oscar_win,
            np.where(
                X[awards_column].str.contains(oscar_nom_regex, regex=True),
                self.oscar_nom,
                np.where(
                    X[awards_column].str.contains(win_text_identifier) == True,
                    self.award_true,
                    np.where(
                        X[awards_column].str.contains(nom_text_identifier) == True,
                        self.nom_true,
                        self.no_award,
                    ),
                ),
            ),
        )  # Create award status column

        X[created_genre_column] = np.where(
            X[top_genre_column].str.contains(
                f"{action_value}|{adventure_value}", regex=True
            ),
            self.action_adventure,
            np.where(
                X[top_genre_column].str.contains(
                    f"{drama_value}|{thriller_value}", regex=True
                ),
                self.drama_thriller,
                np.where(
                    X[top_genre_column].str.contains(comedy_value),
                    self.comedy,
                    np.where(
                        X[top_genre_column].str.contains(horror_value) == True,
                        self.horror,
                        np.where(
                            X[top_genre_column].str.contains(animation_value) == True,
                            self.animation,
                            self.other_genre,
                        ),
                    ),
                ),
            ),
        )  # Create Grouped Genre column

        X = sm.add_constant(X)
        X = pd.get_dummies(
            X, columns=[created_award_status_column, created_genre_column]
        )

        X.columns = [col.title() for col in X.columns]

        missing_columns = list(set(all_columns) - set(X.columns))

        if len(missing_columns) == 0:
            pass
        else:
            X.loc[:, missing_columns] = 0

        X.drop(
            [
                award_status_reference_column,
                awards_column,
                genre_reference_column,
                genre_column,
                top_genre_column,
            ],
            axis=1,
            inplace=True,
        )

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
