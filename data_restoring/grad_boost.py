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
            # gпредсказание
            rowpred = data_array[row]
            rowpred = np.delete(rowpred, i)
            rowpred = asarray(rowpred).reshape((1, len(rowpred)))
            ynew = model.predict(rowpred)
            ultranew_data[row][i] = ynew
            data_array[row][i] = temp
    ultranew_data = pd.DataFrame(ultranew_data, columns=data_df.columns)
    return ultranew_data


# TODO - check performance of xgboost & lgbm
# TODO - CatBoost
if __name__ == '__main__':
    # data_orig = pd.read_excel('train_data_no_missings.xlsx')
    data_orig = pd.read_excel('kalmanK1.xlsx')
    data_orig = data_orig[data_orig.columns[1:]]
    data = pd.read_excel('nan_200.xlsx')
    # data = pd.read_excel('kalmanK1.xlsx')
    data = data[data.columns[1:]]
    cols = data.columns
    MARKER_SIZE = 5
    COL = cols[1]

    # real example
    data_restored = gbm(data)
    # plt.plot(data_restored.index,
    #          data_restored[cols[0]], c='#b521b8', label='0')
    # plt.plot(data_restored.index,
    #          data_restored[cols[1]], c='#595323', label='1')
    # plt.plot(data_restored.index,
    #          data_restored[cols[2]], c='#1cb83d', label='2')
    plt.scatter(data_orig.index,
                data_orig[COL], s=MARKER_SIZE, c='#de2c1f', label='original')
    plt.scatter(data_restored.index,
                data_restored[COL], s=MARKER_SIZE, c='#32a852', label='restored')
    plt.scatter(data.index, data[COL], s=MARKER_SIZE, label='missing')
    # plt.plot(data_restored.index, data_restored[COL], c='#32a852', label= 'restored normal')
    # plt.plot(data_cleared.index, data_cleared[COL], label='missing')
    plt.legend()
    plt.show()

    # # # preparation for combination
    # prep_data = gbm_test(data)
    # # gbm_test(data)
    # prep_data[0].to_excel('prep_gbm.xlsx')
    # plt.plot(prep_data[0].index, prep_data[0]
    #          [COL], c='#2ec720', label='prepared')
    # plt.plot(prep_data[1].index, prep_data[1]
    #          [COL], c='#2118d9', label='original')
    # # plt.plot(prep_data[0].index, prep_data[0][cols[0]], c='#b521b8', label= '0')
    # # plt.plot(prep_data[0].index, prep_data[0][cols[1]], c='#595323', label= '1')
    # # plt.plot(prep_data[0].index, prep_data[0][cols[2]], c='#1cb83d', label= '2')
    # plt.legend()
    # plt.show()

# #errors
#     nans1 = []
#     nans_indexes1 = []
#     print(len(data))
#     print(len(data.dropna()))
#     for column in data.columns:
#         nancol = []
#         nancol_indexes = []
#         for row in range(len(data)):
#             s = data[column][row]
#             if np.isnan(s):
#                 nancol.append(data_restored[column][row])
#                 nancol_indexes.append(row)
#         nans1.append(nancol)
#         nans_indexes1.append(nancol_indexes)

#     errors = []
#     for x in range(len(data_restored.columns)):
#         col = data_orig.columns[x]
#         nans = nans1[x]
#         nans_indexes = nans_indexes1[x]
#         errors1 = []
#         # print()
#         for i, v in enumerate(nans):
#             ss = nans_indexes[i]
#             orig = data_orig[col][ss]
#             diapason = np.max(data_orig[col]) - np.min(data_orig[col])
#             errors1.append(abs(v-orig)/diapason)
#         errors.append(np.mean(errors1))
#     print(errors)
#     print(f'Error_cool:{np.mean(errors)}')
