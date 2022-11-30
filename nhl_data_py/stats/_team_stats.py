from nhl_data_py.stats import TEAM_STATS_URL

import pandas as pd
import requests

def get_team_stats() -> pd.DataFrame:
    return