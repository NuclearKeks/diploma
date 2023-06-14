import pandas as pd
import numpy as np


def vins_left_col(data1: list):
    data = data1.copy()
    for i, v in enumerate(data):
        if np.isnan(v) and i > 0:
            data[i] = data[i-1]
    return data


def vins_left(data: pd.DataFrame):
    new_data = data.copy()
    cols = new_data.columns
    new_columns = []
    for col in cols:
        col = np.asarray(new_data[col])
        for i, v in enumerate(col):
            if np.isnan(v) and i > 0:
                col[i] = col[i-1]
        new_columns.append(col.tolist())
    np.array(new_columns)
    new_columns = np.rot90(new_columns, k=1, axes=(0, 1))
    new_data = pd.DataFrame(new_columns, columns=cols)
    new_data = new_data.iloc[::-1]
    new_data.reset_index(drop=True, inplace=True)
    return new_data


def vins_left_test(data: pd.DataFrame):
    data_df = data.dropna(axis=0)
    data_df.reset_index(drop=True, inplace=True)
    rows = len(data_df)
    cols = len(data_df.columns)
    ultranew_data = np.zeros((rows, cols))
    for col in range(cols):
        colname = data_df.columns[col]
        column = np.asarray(data_df[colname])
        for row in range(1, rows):
            ultranew_data[row][col] = column[row-1]
    ultranew_data = pd.DataFrame(ultranew_data, columns=data_df.columns)
    return [ultranew_data, data_df]


if __name__ == '__main__':
    from matplotlib import pyplot as plt
    data = pd.read_excel('nan_200.xlsx')
    data_orig = pd.read_excel('kalmanK1.xlsx')
    data = data[data.columns[1:]]
    x = 1
    COL = data.columns[x]
    MARKER_SIZE = 5

    # real example
    # data_after = vins_left(data)
    # new_data = data_after[0]
    new_data = vins_left(data)
    # print(nans, nans_indexes, sep='\n')
    plt.scatter(new_data.index, new_data[COL],
                s=MARKER_SIZE, c='#2ec720', label='restored')
    plt.scatter(data.index, data[COL], s=MARKER_SIZE,
                c='#2118d9', label='original')
    plt.legend()
    plt.show()

    # #error_count
    # errors = []
    # for x in range(len(new_data.columns)):
    #     nans = data_after[1][x]
    #     nans_indexes = data_after[2][x]
    #     errors1 = []
    #     for i, v in enumerate(nans):
    #         orig = data_orig[data.columns[x]][nans_indexes[i]]
    #         # print(orig, v)
    #         diapason = np.max(data_orig[data.columns[x]]) - \
    #             np.min(data_orig[data.columns[x]])
    #         errors1.append(abs(v-orig)/diapason)
    #     errors.append(np.mean(errors1))
    # print(f'Error_cool:{np.mean(errors)}')

    # # preparation for combination
    # prep_data = vins_left_test(data)
    # prep_data[0].to_excel('prep_vinsleft.xlsx')
    # plt.scatter(prep_data[0].index, prep_data[0][COL],
    #             s=MARKER_SIZE, c='#2ec720', label='prepared')
    # plt.scatter(prep_data[1].index, prep_data[1][COL],
    #             s=MARKER_SIZE, c='#2118d9', label='original')
    # plt.legend()
    # plt.show()