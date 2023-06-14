from scipy.optimize import minimize, Bounds
from grad_boost import gbm, gbm_test
from corr_rec import corr_res, corr_res_test
from vinsor_right import vins_right, vins_right_test
from vinsor_left import vins_left, vins_left_test
from linear_approx import linapprox, linapprox_test
from rss import rss, rss_test
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None

col = 9
data = pd.read_excel('nan_200.xlsx')
data_orig = pd.read_excel('kalmanK1.xlsx')
data_orig = data_orig[data_orig.columns[col]]
f0 = data.dropna(axis=0)
f0.reset_index(drop=True, inplace=True)
f1 = pd.read_excel('prep_vinsleft.xlsx')
f2 = pd.read_excel('prep_vinsright.xlsx')
f3 = pd.read_excel('prep_linapprox.xlsx')
f4 = pd.read_excel('prep_rss.xlsx')
f5 = pd.read_excel('prep_corr.xlsx')
f6 = pd.read_excel('prep_gbm.xlsx')
# f1 = vins_left_test(data)
# f2 = vins_right_test(data)
# f3 = linapprox_test(data)
# f4 = rss_test(data)
# f5 = corr_res_test(data)
# f6 = gbm_test(data)
f0 = f0[f0.columns[col]]
f1 = f1[f1.columns[col]]
f2 = f2[f2.columns[col]]
f3 = f3[f3.columns[col]]
f4 = f4[f4.columns[col]]
f5 = f5[f5.columns[col]]
f6 = f6[f6.columns[col]]
# print(f1)
f4 = f3
f5 = f3


y1 = vins_left(data)
y2 = vins_right(data)
y3 = linapprox(data)
y4 = rss(data)
y5 = corr_res(data)
y6 = gbm(data)
y1 = y1[y1.columns[col]]
y2 = y2[y2.columns[col]]
y3 = y3[y3.columns[col]]
y4 = y4[y4.columns[col]]
y5 = y5[y5.columns[col]]
y6 = y6[y6.columns[col]]

y4 = y3
y5 = y3

algorithms = (y1, y2, y3, y4, y5, y6)
values = np.column_stack((f1, f2, f3, f4, f5, f6))
algnum = len(algorithms)
bnds = []
for i in range(algnum):
    bnds.append((0, 1))
bnds = tuple(bnds)
coefs_scipy = np.zeros((len(f0), algnum))
for x in range(len(f1)):
    def f(*args):
        return (np.sum(values[x, :]*args)-f0[x])**2
    Bounds(0, 1, keep_feasible=False)
    result = minimize(lambda coeffs: f(*coeffs),
                      x0=np.zeros(6), method='TNC', bounds=bnds)
    # print(result.x)
    if x % 100 == 0:
        print(x)
    coefs_scipy[x] = result.x
coefs = coefs_scipy  # ssss
values_table = pd.DataFrame(values)
coefs_table = pd.DataFrame(coefs)
# print(coefs_table)
# print('-----------------------')
final_coefs = coefs.mean(axis=0)
# print(pd.DataFrame(final_coefs))

# restored = np.sum(final_coefs*values, axis=1)
# res = pd.DataFrame(restored)

# ///////////////////////////
values = np.column_stack(algorithms)
restored = np.zeros((len(data), 1))
nans = []
nans_indexes = []
for row in range(len(data)):
    if np.isnan(data[data.columns[col]][row]):
        nans_indexes.append(row)
        restored[row] = np.sum(values[row, :]*final_coefs)
        nans.append(restored[row])
    else:
        restored[row] = data[data.columns[col]][row]

plt.plot(data.index, restored, label='restored', linewidth=2)
plt.plot(data_orig.index, data_orig, label='original', linewidth=1)
plt.scatter(nans_indexes, nans, label='missings', c='r', s=10)
plt.title(data.columns[col])
plt.legend()
plt.show()

errors = []
errors1 = []
for i, v in enumerate(nans):
    orig = data_orig[nans_indexes[i]]
    diapason = np.max(data_orig)-np.min(data_orig)
    errors.append(abs(v-orig)/orig)
    errors1.append(abs(v-orig)/diapason)
print(f"Error:{np.mean(errors)} ")
print(f'Error_cool:{np.mean(errors1)}')
