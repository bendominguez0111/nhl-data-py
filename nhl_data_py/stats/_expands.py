from nhl_data_py.stats import EXPANDS_URL

import pandas as pd
import requests

def get_expands() -> pd.DataFrame:
    return