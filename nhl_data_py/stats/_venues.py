from nhl_data_py.stats import VENUES_URL

import pandas as pd
import requests

def get_venues() -> pd.DataFrame():
    return