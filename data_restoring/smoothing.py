import numpy as np
import pandas as pd
from filterpy.kalman import KalmanFilter


def simple_exp_smooth(d, colname, extra_periods=1, alpha=0.4,):
    d = np.array(d)
    cols = len(d)
    d = np.append(d, [np.nan]*extra_periods)
    f = np.full(cols+extra_periods, np.nan)
    f[1] = d[0]
    for t in range(2, cols+1):
        f[t] = alpha*d[t-1]+(1-alpha)*f[t-1]
    f[cols+1:] = f[t]
    df = pd.DataFrame.from_dict(
        {colname: f})
    return df


def kalman_filter(df):
    new_data = np.zeros((len(df), len(df.columns)))
    for x in range(len(df.columns)):
        colname = df.columns[x]
        col = df[colname]
        f = KalmanFilter(dim_x=1, dim_z=1)
        f.x = np.array([[col[0]]])
        f.F = np.array([[1]])
        f.H = np.array([[1]])
        estimates = []
        for n in range(len(col)):
            f.predict()
            f.update(col[n])
            new_data[n][x] = f.x[0]
        estimates.append(f.x[0])
        new_data.append(estimates)
        estimates = np.array(estimates)
        return estimates
