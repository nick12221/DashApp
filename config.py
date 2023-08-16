# ------------------------------Variables for API and Excel Upload------------------------#
import re
import pandas as pd

tab_one_label = "Import Movie Data"

upload_file_message = "Upload CSV or Excel"

file_import_error_message = "Can only upload a CSV or Excel file."

no_title_column_message = 'First column must be called "Title".'

file_title_column_name = "Title"

import_movie_api_message = "Import from OMDB API"

button_controls_label = "Import Controls"

welcome_message = "CinSights: A Movie Analytics Platform"

success_title = "Success"

error_title = "Error"

excel_movie_titles_uploaded_message = " movie titles were uploaded by the user."

modal_message_movies_imported = " movies were imported from the OMDB API."

modal_message_wrong_movies = " The following movies were not found: "

total_time_label = "Total Time for API Pull"

avg_time_label = "Avg. Time Per API Request"

default_total_time = "0 Sec(s)"

default_avg_time = "0 S/Request"

movie_id_column = "imdbID"

# -----------------------------Model Section Variables---------------------------#

model_section_title = "Model Summary and Prediction"

feature_importance_header = "Feature Importance"

model_run_btn_text = "Predict"

export_btn_text = "Export Results"

movie_title_column = "Title"

revenue_prediction_column = "Revenue Prediction"

runtime_column = "Runtime"

imdb_votes_column = "imdbVotes"

metascore_column = "Metascore"

imdb_rating_column = "imdbRating"

awards_column = "Awards"

created_award_status_column = "Award Status"

award_status_reference_column = "Award Status_No Award Or Nomination"

award_win_value = "Other Win"

award_nom_value = "Other Nom"

award_no_award_value = "No Award Or Nomination"

win_text_identifier = "win"

nom_text_identifier = "nom"

oscar_win_value = "Oscar Win"

oscar_nom_value = "Oscar Nom"

nom_keyword = "nom"
won_keyword = "won"
oscar_keyword = "oscar"

oscar_win_regex = rf"{re.escape(won_keyword)}.*{re.escape(oscar_keyword)}|{re.escape(oscar_keyword)}.*{re.escape(won_keyword)}"

oscar_nom_regex = rf"{re.escape(nom_keyword)}.*{re.escape(oscar_keyword)}|{re.escape(oscar_keyword)}.*{re.escape(nom_keyword)}"

genre_column = "Genre"

top_genre_column = "First_Genre"

created_genre_column = "Genre Group"

action_value = "action"
adventure_value = "adventure"
comedy_value = "comedy"
horror_value = "horror"
animation_value = "animation"
drama_value = "drama"
thriller_value = "thriller"

action_adv_value = "Action/Adventure"
drama_thriller_value = "Drama/Thriller"
other_genre_value = "Other"

genre_reference_column = "Genre Group_Other"

model_all_columns = [
    runtime_column,
    imdb_votes_column,
    metascore_column,
    awards_column,
    genre_column,
]

model_numeric_columns = [
    runtime_column,
    imdb_votes_column,
    metascore_column,
]

cpi_dict = {
    1913: 9.9,
    1914: 10,
    1915: 10.1,
    1916: 10.9,
    1917: 12.8,
    1918: 15,
    1919: 17.3,
    1920: 20,
    1921: 17.9,
    1922: 16.8,
    1923: 17.1,
    1924: 17.1,
    1925: 17.5,
    1926: 17.7,
    1927: 17.4,
    1928: 17.2,
    1929: 17.2,
    1930: 16.7,
    1931: 15.2,
    1932: 13.6,
    1933: 12.9,
    1934: 13.4,
    1935: 13.7,
    1936: 13.9,
    1937: 14.4,
    1938: 14.1,
    1939: 13.9,
    1940: 14,
    1941: 14.7,
    1942: 16.3,
    1943: 17.3,
    1944: 17.6,
    1945: 18,
    1946: 19.5,
    1947: 22.3,
    1948: 24,
    1949: 23.8,
    1950: 24.1,
    1951: 26,
    1952: 26.6,
    1953: 26.8,
    1954: 26.9,
    1955: 26.8,
    1956: 27.2,
    1957: 28.1,
    1958: 28.9,
    1959: 29.2,
    1960: 29.6,
    1961: 29.9,
    1962: 30.3,
    1963: 30.6,
    1964: 31,
    1965: 31.5,
    1966: 32.5,
    1967: 33.4,
    1968: 34.8,
    1969: 36.7,
    1970: 38.8,
    1971: 40.5,
    1972: 41.8,
    1973: 44.4,
    1974: 49.3,
    1975: 53.8,
    1976: 56.9,
    1977: 60.6,
    1978: 65.2,
    1979: 72.6,
    1980: 82.4,
    1981: 90.9,
    1982: 96.5,
    1983: 99.6,
    1984: 103.9,
    1985: 107.6,
    1986: 109.6,
    1987: 113.6,
    1988: 118.3,
    1989: 124,
    1990: 130.7,
    1991: 136.2,
    1992: 140.3,
    1993: 144.5,
    1994: 148.2,
    1995: 152.4,
    1996: 156.9,
    1997: 160.5,
    1998: 163,
    1999: 166.6,
    2000: 172.2,
    2001: 177.1,
    2002: 179.9,
    2003: 184,
    2004: 188.9,
    2005: 195.3,
    2006: 201.6,
    2007: 207.3,
    2008: 215.3,
    2009: 214.5,
    2010: 218.1,
    2011: 224.9,
    2012: 229.6,
    2013: 233,
    2014: 236.7,
    2015: 237,
    2016: 240,
    2017: 245.1,
    2018: 251.1,
    2019: 255.7,
    2020: 258.8,
    2021: 271,
    2022: 292.7,
    2023: 309.6,
}

model_variables_column = "Model Variables"
model_coef_column = "Model Coefficients"
model_sig_col = "Statistically Significant"

model_result_df = pd.DataFrame(
    [
        {
            "Variables": "const",
            "Coefficients": 11.328452815404646,
            "Coef Std. Errors": 0.4726887805166729,
            "T Stat": 23.965986252142624,
            "Statistical Significance": "Significant",
            "Model Variables": "Const",
            "Model Coefficients": 11.328,
        },
        {
            "Variables": "Runtime",
            "Coefficients": 0.0309157858245032,
            "Coef Std. Errors": 0.0035509725752136,
            "T Stat": 8.706286846679777,
            "Statistical Significance": "Significant",
            "Model Variables": "Runtime",
            "Model Coefficients": 0.031,
        },
        {
            "Variables": "imdbVotes",
            "Coefficients": 3.037860474400006e-06,
            "Coef Std. Errors": 3.552023828123152e-07,
            "T Stat": 8.552477746201316,
            "Statistical Significance": "Significant",
            "Model Variables": "Imdbvotes",
            "Model Coefficients": 0.0,
        },
        {
            "Variables": "Metascore",
            "Coefficients": -0.0163840939750329,
            "Coef Std. Errors": 0.004453505029385,
            "T Stat": -3.6789211793694183,
            "Statistical Significance": "Significant",
            "Model Variables": "Metascore",
            "Model Coefficients": -0.016,
        },
        {
            "Variables": "Award Status_Nominated",
            "Coefficients": 0.8876116237866021,
            "Coef Std. Errors": 0.1998641345294214,
            "T Stat": 4.441075062699353,
            "Statistical Significance": "Significant",
            "Model Variables": "Award Status_Other Nom",
            "Model Coefficients": 0.888,
        },
        {
            "Variables": "Award Status_Oscar Nom",
            "Coefficients": 2.304281457633836,
            "Coef Std. Errors": 0.2568369472850357,
            "T Stat": 8.971767816086686,
            "Statistical Significance": "Significant",
            "Model Variables": "Award Status_Oscar Nom",
            "Model Coefficients": 2.304,
        },
        {
            "Variables": "Award Status_Oscar Win",
            "Coefficients": 2.493833705931512,
            "Coef Std. Errors": 0.3128062407868569,
            "T Stat": 7.972455088038941,
            "Statistical Significance": "Significant",
            "Model Variables": "Award Status_Oscar Win",
            "Model Coefficients": 2.494,
        },
        {
            "Variables": "Award Status_Win",
            "Coefficients": 0.8627530673029853,
            "Coef Std. Errors": 0.1773186898582524,
            "T Stat": 4.86555065341767,
            "Statistical Significance": "Significant",
            "Model Variables": "Award Status_Other Win",
            "Model Coefficients": 0.863,
        },
        {
            "Variables": "Genre Group_Action/Adventure",
            "Coefficients": 2.037700024384578,
            "Coef Std. Errors": 0.1887661496931849,
            "T Stat": 10.79483809833806,
            "Statistical Significance": "Significant",
            "Model Variables": "Genre Group_Action/Adventure",
            "Model Coefficients": 2.038,
        },
        {
            "Variables": "Genre Group_Drama/Thriller",
            "Coefficients": -0.0251200885711694,
            "Coef Std. Errors": 0.1892306616500462,
            "T Stat": -0.132748511008355,
            "Statistical Significance": "Not Significant",
            "Model Variables": "Genre Group_Drama/Thriller",
            "Model Coefficients": -0.025,
        },
        {
            "Variables": "Genre Group_animation",
            "Coefficients": 2.4233068004757667,
            "Coef Std. Errors": 0.3645497079286936,
            "T Stat": 6.64739745436792,
            "Statistical Significance": "Significant",
            "Model Variables": "Genre Group_Animation",
            "Model Coefficients": 2.423,
        },
        {
            "Variables": "Genre Group_comedy",
            "Coefficients": 1.3165391681216243,
            "Coef Std. Errors": 0.1757574406688302,
            "T Stat": 7.490659644972323,
            "Statistical Significance": "Significant",
            "Model Variables": "Genre Group_Comedy",
            "Model Coefficients": 1.317,
        },
        {
            "Variables": "Genre Group_horror",
            "Coefficients": 1.5903217558689529,
            "Coef Std. Errors": 0.3855366221349809,
            "T Stat": 4.12495639729956,
            "Statistical Significance": "Significant",
            "Model Variables": "Genre Group_Horror",
            "Model Coefficients": 1.59,
        },
    ]
)

desired_result_col_order = [
    "Const",
    "Runtime",
    "Imdbvotes",
    "Metascore",
    "Award Status_Other Nom",
    "Award Status_Other Win",
    "Award Status_Oscar Nom",
    "Award Status_Oscar Win",
    "Genre Group_Action/Adventure",
    "Genre Group_Animation",
    "Genre Group_Comedy",
    "Genre Group_Drama/Thriller",
    "Genre Group_Horror",
]

all_columns = desired_result_col_order + [
    genre_reference_column,
    award_status_reference_column,
]
