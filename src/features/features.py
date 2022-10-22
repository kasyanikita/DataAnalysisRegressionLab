import pandas as pd
import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import src.config as cfg

def feature_gen(df : pd.DataFrame) -> pd.DataFrame:
    
    return df