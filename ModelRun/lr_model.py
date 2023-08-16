import MASA
import pandas as pd
import numpy as np
from model_preprocessing import CustomPreprocessor
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import joblib
from config import *

moviedata_df = pd.read_csv(
    r"C:\Users\nickp\movies.csv",
    converters={
        "Metascore": str,
        "imdbRating": str,
        "imdbVotes": str,
        "BoxOffice": str,
        "Runtime": str,
    },
)
moviedata_df["BoxOffice"] = (
    moviedata_df["BoxOffice"]
    .str.replace(",", "", regex=True)
    .str.extract(r"(\d+)")
    .astype(float)
)

# Remove no box office data
good_revenue_df = moviedata_df.loc[moviedata_df["BoxOffice"].notnull()].copy()
good_revenue_df["Year"] = good_revenue_df["Year"].astype(int)
good_revenue_df["CPI"] = good_revenue_df["Year"].map(cpi_dict)

good_revenue_df = good_revenue_df.loc[good_revenue_df["CPI"].notnull()]
good_revenue_df["CY CPI"] = cpi_dict[2023]
good_revenue_df["BoxOfficeIn2023Dollars"] = good_revenue_df["BoxOffice"] * (
    good_revenue_df["CY CPI"] / good_revenue_df["CPI"]
)

# Create X and Y variables
y = np.log(good_revenue_df[["BoxOfficeIn2023Dollars"]])

x = good_revenue_df.copy()

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=14
)

DataPreprocessor = CustomPreprocessor()

DataPreprocessor.fit(x_train)
x_train = DataPreprocessor.transform(x_train)
x_test = DataPreprocessor.transform(x_test)
DataPreprocessor.save("fitted_preprocessor.pkl")
x_train.to_csv(r"train data.csv")

# Run model
modelnick = MASA.OLSSuite()

modelnick.GetOLSResults(y_train.values, x_train.values, list(x_train.columns))
print(modelnick.Metrics)
joblib.dump(modelnick, "fitted_model.pkl")


print(MASA.GetVif(x_train.values))
pd.DataFrame(modelnick.OLSResults).to_csv(r"model results.csv")


test_predictions = modelnick.GetPredictions(x_test.values)

# print MSE Value and R2 value to compare

print(MASA.GetMSE(y_test.values, test_predictions))
print(MASA.GetR2(y_test.values, test_predictions))
