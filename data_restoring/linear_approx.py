# import random
# from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def linapprox_for_col(data1: list):
    data = data1.copy()
    borders = []
    for ranges in [range(len(data)), reversed(range(len(data)))]:
        for i in ranges:
            if not np.isnan(data[i]):
                borders.append(i)
                break
    leftborder, rightborder = borders[0], borders[1]
    body = range(leftborder, rightborder)
    for i, v in enumerate(data):
        if i in body and np.isnan(v):
            y1 = data[i-1]
            for j in range(i+1, len(data)):
                if not np.isnan(data[j]):
                    y2 = data[j]
                    break
            for k in range(i, j):
                data[k] = (k-i+1)*(y2-y1)/(j-i+1)+y1
    flag = 1
    for interval in [reversed(range(0, leftborder)), range(rightborder, len(data))]:
        for k in interval:
            if np.isnan(data[k]):
                i = k+flag*2
                j = k+flag*1
                data[k] = 2*data[j]-data[i]
        flag -= 2
    return data


def linapprox(data: pd.DataFrame):
    cols = data.columns
    new_columns = []
    for col in cols:
        col = np.asarray(data[col]).tolist()
        col = linapprox_for_col(col)
        new_columns.append(col)
    new_columns = np.array(new_columns)
    new_columns = np.rot90(new_columns, k=1, axes=(0, 1))
    new_data = pd.DataFrame(new_columns, columns=cols)
    new_data = new_data.iloc[::-1]
    new_data.reset_index(drop=True, inplace=True)
    return new_data


def linapprox_test(data: pd.DataFrame):
    data_df = data.dropna(axis=0)
    data_df.reset_index(drop=True, inplace=True)
    rows = len(data_df)
    cols = len(data_df.columns)
    ultranew_data = np.zeros((rows, cols))
    for col in range(cols):
        colname = data_df.columns[col]
        for row in range(rows):
            column = list(data_df[colname])
            column[row] = np.nan
            if row == 0:
                x = 0
                column = column[:3]
                ultranew_data[row][col] = column[1]-column[2] + column[1]
            elif row == rows-1:
                x = 2
                column = column[:rows-4:-1]
                column.reverse()
                ultranew_data[row][col] = 2*(column[0]-column[1]) + column[1]
            else:
                x = 1
                column = column[row-1:row+2]
                ultranew_data[row][col] = (column[2] - column[0])/2 + column[0]
    ultranew_data = pd.DataFrame(ultranew_data, columns=data_df.columns)
    return [ultranew_data, data_df]


if __name__ == '__main__':
    from matplotlib import pyplot as plt
    data = pd.read_excel('nan_200.xlsx')
    data_orig = pd.read_excel('kalmanK1.xlsx')
    data = data[data.columns[1:]]
    COL = data.columns[0]
    MARKER_SIZE = 5

    # real example
    # new_data = linapprox(data)
    # data_after = linapprox(data)
    # new_data = data_after[0]
    new_data = linapprox(data)
    plt.scatter(new_data.index, new_data[COL],
                s=MARKER_SIZE, c='#2ec720', label='restored')
    plt.scatter(data.index, data[COL], s=MARKER_SIZE,
                c='#2118d9', label='original')
    plt.legend()
    plt.show()

    # # preparation for combination
    # prep_data = linapprox_test(data)
    # prep_data[0].to_excel('prep_linapprox.xlsx')
    # plt.plot(prep_data[1].index, prep_data[1]
    #          [COL], c='#2118d9', label='original')
    # plt.plot(prep_data[0].index, prep_data[0]
    #          [COL], c='#2ec720', label='prepared')
    # plt.legend()
    # plt.show()

    # #errors
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
