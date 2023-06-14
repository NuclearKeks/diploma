import sys
import os
import numpy as np
import pandas as pd
from typing import Optional
import PySide6.QtCore
import PySide6.QtWidgets
from PySide6.QtWidgets import QApplication, QFileDialog
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from interface import Ui_MainWindow
from scipy.optimize import minimize, Bounds
from matplotlib import pyplot as plt
from smoothing import simple_exp_smooth, kalman_filter
from grad_boost import gbm, gbm_test
from corr_rec import corr_res, corr_res_test
from vinsor_right import vins_right, vins_right_test
from vinsor_left import vins_left, vins_left_test
from linear_approx import linapprox, linapprox_test
from rss import rss, rss_test

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        super(MplCanvas, self).__init__(self.fig)


class Window(Ui_MainWindow):

    def __init__(self) -> None:
        pd.options.mode.chained_assignment = None
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Интерфейс')

        self.plot = MplCanvas(self, width=5, height=4, dpi=100)
        self.ui.graph_layout.addWidget(self.plot)

        self.ui.directory_select.clicked.connect(self.directory_select)
        self.ui.directory_select.clicked.connect(self.show_smooth_list)
        self.ui.directory_select.clicked.connect(self.show_cols)
        self.ui.draw_button.clicked.connect(self.algorithm_select)
        self.ui.clear_button.clicked.connect(self.clear_plot)
        self.switches = [self.ui.switches.itemAt(i).widget() for i in range(self.ui.switches.count())]
        self.efficiency = [self.ui.efficiency.itemAt(i).widget() for i in range(self.ui.efficiency.count())]
        for statement in self.efficiency:
            statement.setText('-')

    def directory_select(self):
        self.f_name = QFileDialog.getOpenFileName(self)[0]
        f_show = self.f_name.split('/')[-1]
        self.ui.filename.setText(f_show)
        self.data = pd.read_excel(self.f_name)
    
    def clear_plot(self):
        self.plot.ax.cla()
        self.plot.draw()

    def show_smooth_list(self):
        self.ui.smoothing.clear()
        items = ['Экспоненциальное', 'Фильтр Калмана']
        self.ui.smoothing.addItems(items)
    
    def show_cols(self):
        self.ui.column.clear()
        self.ui.column.addItems(self.data.columns[1:])

    def algorithm_select(self):
        self.algs = []
        self.testalgs = []
        self.algeff = []
        for switch in self.switches:
            if switch.isChecked():
                statement = '_'.join(switch.objectName().split('_')[:-1])
                self.algs.append(statement)
                self.testalgs.append(statement+'_test')
                self.algeff.append(statement+'_eff')
        self.data = pd.read_excel(self.f_name)
        results = []
        col = self.ui.column.currentText()
        if self.ui.smoothing.currentText() == 'Экспоненциальное':
            for column in self.data.columns:
                self.data[column] = simple_exp_smooth(self.data[column], column)
        elif self.ui.smoothing.currentText() == 'Фильтр Калмана':
                self.data = kalman_filter(self.data)

        for alg in self.algs:
            currentalg = globals()[alg]
            currentres = currentalg(self.data)
            currentres = currentres[col]
            results.append(currentres)

        f0 = self.data.dropna(axis=0)
        f0.reset_index(drop=True, inplace=True)

        tests = []
        for test in self.testalgs:
            currenttest = globals()[test]
            currenttest = currenttest[col]
            tests.append(currenttest)
        values = np.column_stack(tests)
        algnum = len(self.algs)
        bnds = []
        for i in range(algnum):
            bnds.append((0, 1))
        bnds = tuple(bnds)
        coefs = np.zeros((len(values), algnum))
        for x in range(len(tests[0])):
            def f(*args):
                return (np.sum(values[x, :]*args)-f0[x])**2
            Bounds(0, 1, keep_feasible=False)
            result = minimize(lambda coeffs: f(*coeffs),
                            x0=np.zeros(6), method='TNC', bounds=bnds)
            coefs[x] = result.x
        final_coefs = coefs.mean(axis=0)
        for i, statement in enumerate(self.algeff):
            for coef in self.efficiency:
                if coef.objectName() == statement:
                    coef.setText(str(np.round(final_coefs[i],3)))
        restored = np.zeros((len(self.data), 1))
        nans = []
        nans_indexes = []
        values = np.column_stack(results)
        for row in range(len(self.data)):
            if np.isnan(self.data[col][row]):
                nans_indexes.append(row)
                restored[row] = np.sum(values[row, :]*final_coefs)
                nans.append(restored[row])
            else:
                restored[row] = self.data[col][row]
        self.plot.ax.scatter(nans_indexes, nans, label='missings', c='r', s=10)
        self.plot.ax.plot(self.data.index, restored, label='restored', linewidth=2)
        self.plot.ax.set_title(col)
        self.plot.ax.legend()
        self.plot.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
