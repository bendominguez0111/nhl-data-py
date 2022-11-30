from nhl_data_py.stats import CONFIGURATIONS_URL

import pandas as pd
import requests

def get_configurations() -> pd.DataFrame:
    return