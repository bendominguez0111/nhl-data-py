from nhl_data_py.stats import AWARDS_URL
from nhl_data_py.utils import build_endpoint

import pandas as pd
import requests

def get_awards() -> pd.DataFrame:
    """

    Get all NHL Awards.

        Parameters:
            none

        Returns:
            df (pd.DataFrame): Pandas DataFrame containing awards data

    """
    res = requests.get(AWARDS_URL)
    json = res.json()['awards']
    df = pd.json_normalize(json)    

    return df

def get_award_by_id(id: str) -> pd.Series:
    """

    Get NHL Award by ID.
        
        Parameters:
            id (str): Award id
        
        Returns:
            s (pd.Series): Pandas Series containing individual award data

    """
    if type(id) == int:
        id = str(id)

    URL = build_endpoint(id, [AWARDS_URL])
    res = requests.get(URL)
    json = res.json()['awards'][0]
    s = pd.Series(json)

    return s