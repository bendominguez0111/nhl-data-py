from nhl_data_py.stats import SEASONS_URL

import pandas as pd
import requests

def get_seasons() -> pd.DataFrame:
    return