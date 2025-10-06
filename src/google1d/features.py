import pandas as pd
import numpy as np

def add_engagement_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if {"likes","views"}.issubset(out.columns):
        out["like_ratio"] = out["likes"] / out["views"].replace({0: np.nan})
    if "comment_count" in out.columns and "views" in out.columns:
        out["comment_ratio"] = out["comment_count"] / out["views"].replace({0: np.nan})
    elif "comments" in out.columns and "views" in out.columns:
        out["comment_ratio"] = out["comments"] / out["views"].replace({0: np.nan})
    return out
