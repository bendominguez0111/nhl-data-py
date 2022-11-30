from nhl_data_py.stats import PLATFORMS_URL

import pandas as pd
import requests

def get_platforms() -> pd.DataFrame:
    return