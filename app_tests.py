import pytest
from unittest.mock import patch, MagicMock
from file_import_export import FileImportExport
from movie_api import MovieRequests
from app import DashApp
import pandas as pd

correct_excel_template_df = pd.DataFrame({"Title": ["Batman", "Superman"]})

incorrect_excel_template_df = pd.DataFrame({"fds": ["Batman", "Superman"]})


@patch(
    "file_import_export.FileImportExport.parse_file_contents",
    return_value=correct_excel_template_df,
)
def test_excel_title_column_correct():
    app = DashApp()
    APIConnector = MovieRequests()
