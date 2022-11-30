from nhl_data_py.stats import EVENT_TYPES_URL

import pandas as pd
import requests

def get_event_types() -> pd.DataFrame:
    return