import pandas as pd
import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import src.config as cfg

def is_garage(arr) -> list:
    ans = []
    for i in arr:
        if i:
            ans.append(1)
        else:
            ans.append(0)
    return ans

def add_garage_avail(df : pd.DataFrame) -> pd.DataFrame:
    df['GarageAvail'] = is_garage(df['GarageArea'])
    df['GarageAvail'] = df['GarageAvail'].astype(np.int8)
    return df

def add_garage_qual_ord(df : pd.DataFrame) -> pd.DataFrame:
    qualities = {'Po': 1, 'Fa': 2,'TA': 3, 'Gd': 4, 'Ex': 5}
    df['GarageQualOrd'] = df['GarageQual'].astype('string').map(qualities)
    df['GarageQualOrd'] = df['GarageQualOrd'].fillna(value=0)
    df['GarageQualOrd'] =  df['GarageQualOrd'].astype(np.int8)
    return df

def add_util_ord(df : pd.DataFrame) -> pd.DataFrame:
    utilities = {'ELO': 1, 'NoSeWa': 2, 'NoSewr': 3,'AllPub': 4}
    df['UtilsOrd'] = df['Utilities'].astype('string').map(utilities)
    df['UtilsOrd'] =  df['UtilsOrd'].astype(np.int8)
    return df

def feature_gen(df : pd.DataFrame) -> pd.DataFrame:
    df = add_garage_avail(df)
    df = add_garage_qual_ord(df)
    df = add_util_ord(df)
    return df