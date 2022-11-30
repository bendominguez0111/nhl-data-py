from nhl_data_py.stats import LANGUAGES_URL

import pandas as pd
import requests

def get_languages() -> pd.DataFrame:
    return