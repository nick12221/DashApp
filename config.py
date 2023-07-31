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

default_total_time = "0 Seconds"

default_avg_time = "0 S/Request"

movie_id_column = "imdbID"

# -----------------------------Model Section Variables---------------------------#

model_section_title = "Model Summary and Prediction"

feature_importance_header = "Feature Importance"

model_run_btn_text = "Predict"

export_btn_text = "Export Results"

revenue_prediction_column = "Revenue Prediction"

runtime_column = "Runtime"

imdb_votes_column = "imdbVotes"

metascore_column = "Metascore"

imdb_rating_column = "imdbRating"

awards_column = "Awards"

created_award_status_column = "Award Status"

award_status_reference_column = "Award Status_No Award or Nomination"

award_win_value = "Win"

award_nom_value = "Nominated"

award_no_award_value = "No Award or Nomination"

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

top_genre_column = "FirstGrenre"

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
    imdb_rating_column,
    awards_column,
    genre_column,
]

model_numeric_columns = [
    runtime_column,
    imdb_votes_column,
    metascore_column,
    imdb_rating_column,
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
            "Variables": "Const",
            "Coefficients": 1.601803946142876,
            "Coef Std. Errors": 0.4162082836343957,
            "T Stat": 3.8485633494741474,
            "Statistically Significant": "Significant",
            "Model Variables": "Intercept",
            "Model Coefficients": 1.6,
        },
        {
            "Variables": "Runtime",
            "Coefficients": 0.0017131149639807,
            "Coef Std. Errors": 0.0023839557857945,
            "T Stat": 0.7186018189552016,
            "Statistically Significant": "Not Significant",
            "Model Variables": "Runtime",
            "Model Coefficients": 0.17,
        },
        {
            "Variables": "Imdbvotes",
            "Coefficients": 0.0012989822527303,
            "Coef Std. Errors": 0.0002595763990365,
            "T Stat": 5.004238665578968,
            "Statistically Significant": "Significant",
            "Model Variables": "Imdbvotes",
            "Model Coefficients": 0.13,
        },
        {
            "Variables": "Metascore",
            "Coefficients": 0.0010573445418105,
            "Coef Std. Errors": 0.0037789309656513,
            "T Stat": 0.2797999093979966,
            "Statistically Significant": "Not Significant",
            "Model Variables": "Metascore",
            "Model Coefficients": 0.11,
        },
        {
            "Variables": "Imdbrating",
            "Coefficients": 0.2503866032167136,
            "Coef Std. Errors": 0.0671451709342137,
            "T Stat": 3.729033670374193,
            "Statistically Significant": "Significant",
            "Model Variables": "Imdbrating",
            "Model Coefficients": 25.04,
        },
        {
            "Variables": "Award Status_Nominated",
            "Coefficients": -0.0466171599530549,
            "Coef Std. Errors": 0.1431552082232534,
            "T Stat": -0.3256406842030822,
            "Statistically Significant": "Not Significant",
            "Model Variables": "Award Status_Nominated",
            "Model Coefficients": -4.66,
        },
        {
            "Variables": "Award Status_Oscar Nom",
            "Coefficients": 0.0854481517482054,
            "Coef Std. Errors": 0.1880317611859768,
            "T Stat": 0.4544346721493033,
            "Statistically Significant": "Not Significant",
            "Model Variables": "Award Status_Oscar Nom",
            "Model Coefficients": 8.54,
        },
        {
            "Variables": "Award Status_Oscar Win",
            "Coefficients": 0.6190942540249608,
            "Coef Std. Errors": 0.2191627227338449,
            "T Stat": 2.824815490072186,
            "Statistically Significant": "Significant",
            "Model Variables": "Award Status_Oscar Win",
            "Model Coefficients": 61.91,
        },
        {
            "Variables": "Award Status_Win",
            "Coefficients": 0.0295613415490763,
            "Coef Std. Errors": 0.1305522639401608,
            "T Stat": 0.2264330058851056,
            "Statistically Significant": "Not Significant",
            "Model Variables": "Award Status_Win",
            "Model Coefficients": 2.96,
        },
        {
            "Variables": "Genre Group_Action/Adventure",
            "Coefficients": 0.5663531735422882,
            "Coef Std. Errors": 0.136541031384468,
            "T Stat": 4.147860667227337,
            "Statistically Significant": "Significant",
            "Model Variables": "Genre Group_Action/Adventure",
            "Model Coefficients": 56.64,
        },
        {
            "Variables": "Genre Group_Animation",
            "Coefficients": 1.112744304017152,
            "Coef Std. Errors": 0.2704939826622058,
            "T Stat": 4.113748827480396,
            "Statistically Significant": "Significant",
            "Model Variables": "Genre Group_Animation",
            "Model Coefficients": 111.27,
        },
        {
            "Variables": "Genre Group_Comedy",
            "Coefficients": 0.4285182903033628,
            "Coef Std. Errors": 0.1276356031275182,
            "T Stat": 3.357357036776318,
            "Statistically Significant": "Significant",
            "Model Variables": "Genre Group_Comedy",
            "Model Coefficients": 42.85,
        },
        {
            "Variables": "Genre Group_Drama/Thriller",
            "Coefficients": 0.3621901081985116,
            "Coef Std. Errors": 0.1370862921941632,
            "T Stat": 2.6420592635587576,
            "Statistically Significant": "Significant",
            "Model Variables": "Genre Group_Drama/Thriller",
            "Model Coefficients": 36.22,
        },
        {
            "Variables": "Genre Group_Horror",
            "Coefficients": -0.0060434995219333,
            "Coef Std. Errors": 0.2858471390285781,
            "T Stat": -0.02114241738599,
            "Statistically Significant": "Not Significant",
            "Model Variables": "Genre Group_Horror",
            "Model Coefficients": -0.6,
        },
    ]
)
