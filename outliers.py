import pandas as pd

def get_lower_and_upper_bounds(x, multiplier):
    q1 = x.quantile(0.25)
    q3 = x.quantile(0.75)
    iqr = q3 - q1
    lower_fence = q1 - multiplier*iqr
    upper_fence = q3 + multiplier*iqr
    lower_outliers = x[x <= lower_fence]
    upper_outliers = x[x >= upper_fence]
    return lower_outliers, upper_outliers


def emp_rule(x, sigma):
    zscores = (x - x.mean()) / x.std()
    df = pd.DataFrame()
    df["x"] = x
    df["zscore"] = abs(zscores)
    outliers = df[zscores >= sigma]
    return outliers

