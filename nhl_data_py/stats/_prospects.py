from nhl_data_py.stats import PROSPECTS_URL

import pandas as pd
import requests

def get_prospects() -> pd.DataFrame:
    return