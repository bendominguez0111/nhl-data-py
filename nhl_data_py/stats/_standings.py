from nhl_data_py.stats import STANDINGS, STANDINGS_TYPES_URL

import pandas as pd
import requests

def get_standings() -> pd.DataFrame:
    return