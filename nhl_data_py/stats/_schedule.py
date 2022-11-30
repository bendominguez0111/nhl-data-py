from nhl_data_py.stats import SCHEDULE_URL

import pandas as pd
import requests

def get_schedules() -> pd.DataFrame:
    return