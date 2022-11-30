from nhl_data_py.stats import CONFERENCES_URL

import pandas as pd
import requests

def get_conferences() -> pd.DataFrame:
    return