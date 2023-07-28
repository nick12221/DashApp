import MASA
import pandas as pd
import numpy as np
from model_preprocessing import CustomPreprocessor
from sklearn.model_selection import train_test_split
import statsmodels.api as sm


moviedata_df = pd.read_csv(r"C:\Users\nickp\movies.csv")
moviedata_df["BoxOffice"] = (
    moviedata_df["BoxOffice"].str.extract(r"(\d+)").astype(float)
)


# Remove no box office data
good_revenue_df = moviedata_df.loc[moviedata_df["BoxOffice"].notnull()]

# Create X and Y variables
y = np.log(good_revenue_df[["BoxOffice"]])

x = good_revenue_df.copy()

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=14)

DataPreprocessor = CustomPreprocessor(
    award_win_value="Win",
    award_nom_value="Nominated",
    award_no_award_value="No Award or Nomination",
)

DataPreprocessor.fit(x_train)
x_train = DataPreprocessor.transform(x_train)
x_test = DataPreprocessor.transform(x_test)

# Run model
modelnick = MASA.OLSSuite()

modelnick.GetOLSResults(y_train.values, x_train.values, list(x_train.columns))
pd.DataFrame(modelnick.OLSResults).to_csv(r"model results.csv")


test_predictions = modelnick.predict(x_test.values)

# print MSE Value and R2 value to compare
