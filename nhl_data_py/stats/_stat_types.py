from nhl_data_py.stats import STAT_TYPES_URL

import pandas as pd
import requests

def get_stat_types() -> pd.DataFrame():
    return