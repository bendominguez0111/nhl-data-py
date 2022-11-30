from nhl_data_py.stats import PERFORMER_TYPES_URL

import pandas as pd
import requests

def get_performer_types() -> pd.DataFrame:
    return