from nhl_data_py.stats import DIVISIONS_URL

import pandas as pd
import requests

def get_divisions() -> pd.DataFrame:
    return