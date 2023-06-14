import numpy as np
import pandas as pd
from scipy.optimize import minimize


def rss_for_col(data: pd.Series):
    y = data.dropna()
    x = np.arange(len(y))
    def f(x, a, b): return a * x + b
    def to_minimise(x, y, a, b): return np.sum((y-f(x, a, b))**2)
    res = minimize(lambda coeffs: to_minimise(x, y, *coeffs), x0=np.zeros(2))
    x = np.arange(len(data))
    for i, v in enumerate(data):
        if np.isnan(v):
            data[i] = res.x[1]+res.x[0]*x[i]
    return data


def rss(data: pd.DataFrame):
    new_data = data.copy()
    cols = new_data.columns
    new_columns = []
    for col in cols:
        col = new_data[col]
        col = rss_for_col(col)
        new_columns.append(col)
    np.array(new_columns)
    new_columns = np.rot90(new_columns, k=1, axes=(0, 1))
    new_data = pd.DataFrame(new_columns, columns=cols)
    new_data = new_data.iloc[::-1]
    new_data.reset_index(drop=True, inplace=True)
    return new_data


def rss_test(data: pd.DataFrame):
    pd.options.mode.chained_assignment = None
    data_df = data.dropna(axis=0)
    data_df.reset_index(drop=True, inplace=True)
    rows = len(data_df)
    cols = len(data_df.columns)
    ultranew_data = np.zeros((rows, cols))
    for col in range(cols):
        colname = data_df.columns[col]
        for row in range(0, rows):
            column = data_df[colname]
            column[row] = np.nan
            ultranew_data[row][col] = rss_for_col(column)[row]
    ultranew_data = pd.DataFrame(ultranew_data, columns=data_df.columns)
    ultranew_data = ultranew_data.loc[(ultranew_data != 0).any(axis=1)]
    return ultranew_data
