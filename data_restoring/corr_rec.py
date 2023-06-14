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


if __name__ == '__main__':
    from matplotlib import pyplot as plt
    # data_test = pd.read_excel('nan_200.xlsx').replace(np.nan, None)
    # data = pd.read_excel('nan_200_climat.xlsx')
    data = pd.read_excel('nan_200.xlsx')
    data_orig = pd.read_excel('kalmanK1.xlsx')
    data_orig = data_orig[data_orig.columns[1:]]
    data = data[data.columns[1:]]
    COL = data.columns[2]
    MARKER_SIZE = 5

    # df = pd.read_excel('K1Work.xls')
    # #заголовочная строка
    # x = 1
    # df.columns = df.iloc[x]
    # df = df.drop(list(range(x+1)))
    # df = df.loc[:, df.columns.notna()]

    # real example
    new_data = corr_res(data)
    # new_data = corr_res(df)
    # COL = df.columns[1]
    plt.plot(new_data.index, new_data[COL],  c='#32a852', label='restored')
    plt.plot(data.index, data[COL],  label='original')
    # plt.plot(df.index, df[COL],  label='original')
    plt.legend()
    plt.show()

    # # preparation for combination
    # prep_data = corr_res_test(data)
    # prep_data[0].to_excel('prep_corr.xlsx')
    # plt.plot(prep_data[0].index, prep_data[0]
    #          [COL], c='#2ec720', label='prepared')
    # plt.plot(prep_data[1].index, prep_data[1]
    #          [COL], c='#2118d9', label='original')
    # plt.legend()
    # plt.show()


# # errors
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
#                 nancol.append(new_data[column][row])
#                 nancol_indexes.append(row)
#         nans1.append(nancol)
#         nans_indexes1.append(nancol_indexes)

#     errors = []
#     for x in range(len(new_data.columns)):
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
