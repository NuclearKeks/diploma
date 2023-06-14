from linear_approx import linapprox
from vinsor_left import vins_left
from vinsor_right import vins_right
from rss import rss
from corr_rec import corr_res
from grad_boost import gbm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_original = pd.read_excel('train_data_no_missings.xlsx')
# data_test = pd.read_excel('nan_in_every_row.xlsx').replace(np.nan, None)
data_test = pd.read_excel('nan_200.xlsx')
data_test = data_test[data_test.columns[1:]]
# print(data_test.head())
# print(data_test[data_test.columns[1]][0:10])
data_cleared = data_test.dropna(axis=0)

fig, ax = plt.subplots(2,3)
# LEN = 100
# LEN = 100
cols = data_test.columns
col = cols[0]
# x = data_test[data_test.columns[0]][0:LEN]

for i in range(2):
    for j in range(3):
        ax[i,j].plot(data_original.index, data_original[col], c='#ab1b1b', label='orig')
y1 = vins_left(data_test)
y2 = vins_right(data_test)
y3 = linapprox(data_test)
y4 = rss(data_test)
y5 = corr_res(data_test)
y6 = gbm(data_test)[0]
ax[0,0].plot(y1.index, y1[col], c='#18b842', label='vins left') #vins left
ax[0,1].plot(y2.index, y2[col], c='#8c8c08', label='vins right') #vins right
ax[0,2].plot(y3.index, y3[col], c='#960b88', label='linapprox') #linapprox
ax[1,0].plot(y4.index, y4[col], c='#18b842', label='rss') #rss
ax[1,1].plot(y5.index, y5[col], c='#8c8c08', label='korr res') #korr res
ax[1,2].plot(y6.index, y6[col], c='#960b88', label='gbm') #gbm
for i in range(2):
    for j in range(3):
        ax[i,j].plot(data_cleared.index, data_cleared[col], c='#000000', label='cleared')
for i in range(2):
    for j in range(3):
        ax[i,j].legend(loc='lower right')

plt.show()