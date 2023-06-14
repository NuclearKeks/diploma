import pandas as pd
import numpy as np


def corr_res(data: pd.DataFrame):
    r, c = np.where(data.isna())
    r, c = list(r), list(c)
    data_cleared = data.dropna(axis=0)
    cor = data_cleared.corr(method='pearson')
    means = [data_cleared[column].mean() for column in data_cleared.columns]
    cols = data_cleared.columns
    new_data = data.copy()
    for i, row in enumerate(r):
        num = c[i]
        r = np.delete(np.array(cor[cols[num]]), num)
        p = np.delete(np.array(new_data.iloc[row]), num)
        pm = np.delete(np.array(means), num)
        new_data[cols[num]][row] = means[num] + \
            sum(r*(p-pm))/sum([abs(_) for _ in cor[cols[num]]])
    return new_data


def corr_res_test(data: pd.DataFrame):
    pd.options.mode.chained_assignment = None
    data_df = data.dropna(axis=0)
    data_df.reset_index(drop=True, inplace=True)
    rows = len(data_df)
    cols = len(data_df.columns)
    ultranew_data = np.zeros((rows, cols))
    for col in range(cols):
        colname = data_df.columns[col]
        for row in range(rows):
            temp = data_df[colname][row]
            data_df[colname][row] = np.nan
            ultranew_data[row][col] = corr_res(data_df)[colname][row]
            data_df[colname][row] = temp
    ultranew_data = pd.DataFrame(ultranew_data, columns=data_df.columns)
    return ultranew_data
