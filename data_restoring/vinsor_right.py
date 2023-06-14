import pandas as pd
import numpy as np


def vins_right(data: pd.DataFrame):
    new_data = data.copy()
    cols = new_data.columns
    new_columns = []
    for col in cols:
        col = np.asarray(new_data[col])
        for i in range(len(col)-1, -1, -1):
            if np.isnan(col[i]) and i < len(col)-1:
                col[i] = col[i+1]
        new_columns.append(col.tolist())
    np.array(new_columns)
    new_columns = np.rot90(new_columns, k=1, axes=(0, 1))
    new_data = pd.DataFrame(new_columns, columns=cols)
    new_data = new_data.iloc[::-1]
    new_data.reset_index(drop=True, inplace=True)
    return new_data


def vins_right_test(data: pd.DataFrame):
    data_df = data.dropna(axis=0)
    data_df.reset_index(drop=True, inplace=True)
    rows = len(data_df)
    cols = len(data_df.columns)
    ultranew_data = np.zeros((rows, cols))
    for col in range(cols):
        colname = data_df.columns[col]
        column = np.asarray(data_df[colname])
        for row in range(0, rows-1):
            ultranew_data[row][col] = column[row+1]
    ultranew_data = pd.DataFrame(ultranew_data, columns=data_df.columns)
    return [ultranew_data, data_df]
