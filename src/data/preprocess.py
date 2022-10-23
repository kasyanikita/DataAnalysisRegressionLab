import pandas as pd
import numpy as np
import sys
import os
from typing import Tuple

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import src.config as cfg

def drop_cols(df : pd.DataFrame, cols : list) -> pd.DataFrame:
    for col in cols:
        if col in df.columns:
           df =  df.drop(col, axis=1)
    return df


def cast_types(df: pd.DataFrame) -> pd.DataFrame:
    df[cfg.CAT_COLS] = df[cfg.CAT_COLS].astype('string')

    df[cfg.INT_COLS] = df[cfg.INT_COLS].astype(np.int64)

    df[cfg.REAL_COLS] = df[cfg.REAL_COLS].astype(np.float64)

    return df


def set_idx(df: pd.DataFrame, idx_col: str) -> pd.DataFrame:
    df = df.set_index(idx_col)
    return df

def fill_cat_na(df: pd.DataFrame) -> pd.DataFrame:
    for cat in cfg.CAT_COLS:
        df[cat] = df[cat].fillna('')
    return df


def fill_int_na(df: pd.DataFrame) -> pd.DataFrame:
    for col in cfg.INT_COLS:
        df[col] = df[col].fillna(0)
    return df
    

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = set_idx(df, cfg.ID_COL)
    df = drop_cols(df, cfg.UNNECESSARY_COLS)
    df = fill_int_na(df)
    df = cast_types(df)
    df = fill_cat_na(df)
    return df


def preprocess_target(df: pd.DataFrame) -> pd.DataFrame:
    df = df.astype(np.int64)
    return df


def extract_target(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    df, target = df.drop(cfg.TARGET_COL, axis=1), df[cfg.TARGET_COL].copy()
    return df, target
