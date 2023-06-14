import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy import asarray
from xgboost import XGBRegressor


def gbm(data: pd.DataFrame):
    r, c = np.where(data.isna())
    r, c = list(r), list(c)
    data_cleared = data.dropna(axis=0)
    data_array = asarray(data)
    data_new = data.copy()
    for i, col in enumerate(data.columns):
        x = asarray(data_cleared.drop(col, axis=1))
        y = asarray(data_cleared[col])
        model = XGBRegressor(objective='reg:squarederror',
                             n_estimators=100,
                             tree_method='exact')
        model.fit(x, y)
        for j, row_to_predict in enumerate(r):
            if i == c[j]:
                row = data_array[row_to_predict]
                row = np.delete(row, i)
                row = asarray(row).reshape((1, len(row)))
                ynew = model.predict(row)
                data_new[col][row_to_predict] = ynew
    return data_new


def gbm_test(data: pd.DataFrame):
    pd.options.mode.chained_assignment = None
    data_df = data.dropna(axis=0)
    data_df.reset_index(drop=True, inplace=True)
    data_array = asarray(data)
    rows = len(data_df)
    cols = len(data_df.columns)
    ultranew_data = np.zeros((rows, cols))
    for i, col in enumerate(data_df.columns):
        x = asarray(data_df.drop(col, axis=1))
        y = asarray(data_df[col])
        model = XGBRegressor(objective='reg:squarederror',
                             n_estimators=100,
                             tree_method='exact')
        model.fit(x, y)
        colname = data_df.columns[i]
        for row in range(rows):
            temp = data_array[row][i]
            data_array[row][i] = np.nan
            rowpred = data_array[row]
            rowpred = np.delete(rowpred, i)
            rowpred = asarray(rowpred).reshape((1, len(rowpred)))
            ynew = model.predict(rowpred)
            ultranew_data[row][i] = ynew
            data_array[row][i] = temp
    ultranew_data = pd.DataFrame(ultranew_data, columns=data_df.columns)
    return ultranew_data
