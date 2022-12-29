import sys
from PySide6.QtWidgets import QApplication
from layout import Ui_MainWindow
import math
from math import * 
from numpy import arange
from helpers import multiple_replace
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        super(MplCanvas, self).__init__(self.fig)

class MplCanvas3d(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_axes([0.05, 0.05, 0.85, 0.85],projection='3d')
        super(MplCanvas3d, self).__init__(fig)

class Window(Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Построение графиков")
        self.expression = None
        self.plot2d = MplCanvas(self, width=5, height=4, dpi=100)
        self.plot3d = MplCanvas3d(self, width=5, height=4, dpi=100)
        self.plot = self.plot2d
        self.ui.graph_layout.addWidget(self.plot)
        self.reserved_statements = dir(math)
        self.ui.left_border.setText('0')
        self.ui.right_border.setText('100')
        self.ui.step.setText('1')
        self.params = []
        self.values = []
        self.ui.expression.textChanged.connect(self.expression_convert)
        self.ui.expression_2.textChanged.connect(self.expression_convert)
        self.ui.expression_3.textChanged.connect(self.expression_convert)
        self.ui.expression.textChanged.connect(self.param_select)
        self.ui.expression_2.textChanged.connect(self.param_select)
        self.ui.expression_3.textChanged.connect(self.param_select)
        self.ui.expression.textChanged.connect(self.second_param_select)
        self.ui.expression_2.textChanged.connect(self.second_param_select)
        self.ui.expression_3.textChanged.connect(self.second_param_select)
        self.ui.x_param.textActivated.connect(self.second_param_select)
        self.ui.graph3d.toggled.connect(self.second_param_select)
        self.ui.graph3d.toggled.connect(self.other_params_select)
        self.ui.expression.textChanged.connect(self.other_params_select)
        self.ui.expression_2.textChanged.connect(self.other_params_select)
        self.ui.expression_3.textChanged.connect(self.other_params_select)
        self.ui.x_param.textActivated.connect(self.other_params_select)
        self.ui.x_param_2.textActivated.connect(self.other_params_select)
        self.ui.other_params.textActivated.connect(self.clear_edit)
        self.ui.parameters.textEdited.connect(self.edit_params)
        self.ui.draw_button.clicked.connect(self.draw_plot)
        self.ui.clear_button.clicked.connect(self.clear_plot)
        self.ui.graph3d.toggled.connect(lambda:self.toggle_3d(self.ui.graph3d))
        self.ui.graph2d.toggled.connect(lambda:self.toggle_3d(self.ui.graph2d))

    def expression_convert(self):
        baka = f'{self.ui.expression.text()}\n{self.ui.expression_2.text()}\n{self.ui.expression_3.text()}'
        baka = baka.replace('^', '**')
        if baka.count('|') == 2:
            baka = baka.replace('|', 'abs(', 1)
            baka = baka.replace('|', ')', 1)
        self.ui.output_expression.append(baka)
        self.expression = baka
        self.buffer = baka
        self.ui.parameters.clear()

    def toggle_3d(self,b):
        self.ui.expression.clear()
        self.ui.expression_2.clear()
        self.ui.expression_3.clear()
        if b.text() == self.ui.graph3d.text():
            if self.ui.graph3d.isChecked():
                self.ui.params_3d.setEnabled(True)
                self.ui.graph3d_widgets.setEnabled(True)
                for widget in self.ui.graph3d_widgets.children():
                    widget.setEnabled(True)
                self.ui.left_border_2.setText('0')
                self.ui.right_border_2.setText('100')
                self.ui.step_2.setText('1')
                self.ui.graph_layout.itemAt(0).widget().setParent(None)
                self.plot = self.plot3d
                self.ui.graph_layout.addWidget(self.plot)
        if b.text() == self.ui.graph2d.text():
            if self.ui.graph2d.isChecked():
                self.ui.params_3d.setEnabled(False)
                self.ui.graph3d_widgets.setEnabled(True)
                self.ui.x_param_2.clear()
                for widget in self.ui.graph3d_widgets.children():
                    widget.setEnabled(False)
                self.ui.left_border_2.clear()
                self.ui.right_border_2.clear()
                self.ui.graph_layout.itemAt(0).widget().setParent(None)
                self.plot = self.plot2d
                self.ui.graph_layout.addWidget(self.plot)

    def draw_plot(self):
        x_param = self.ui.x_param.currentText()
        x_param_2 = self.ui.x_param_2.currentText()
        exp = self.buffer.split('\n')
        py = exp[0]
        y = []
        range1 = arange(eval(self.ui.left_border.text()),\
                        eval(self.ui.right_border.text()),\
                        eval(self.ui.step.text()))
        if self.ui.graph3d.isChecked():
            range2 = arange(eval(self.ui.left_border_2.text()),\
                            eval(self.ui.right_border_2.text()),\
                            eval(self.ui.step_2.text()))
            px = exp[1]
            pz = exp[2]
            x = []
            z = []
            for i in range1:
                for j in range2:
                    x.append(eval(px.replace(x_param,str(i)).replace(x_param_2,str(j))))
                    y.append(eval(py.replace(x_param,str(i)).replace(x_param_2,str(j))))
                    z.append(eval(pz.replace(x_param,str(i)).replace(x_param_2,str(j))))

            self.plot.ax.plot(x, y, z, label=self.ui.graph_name.text())
        else:
            x = range1
            y = [eval(py.replace(x_param, str(i))) for i in range1]
            self.plot.ax.plot(range1, y, label=self.ui.graph_name.text())
        self.plot.ax.legend()
        self.plot.draw()

    def clear_plot(self):
        self.plot.ax.cla()
        self.plot.draw()
        self.params.clear()
        self.values.clear()

    def text_prepare(self):
        text = self.ui.expression.text()+ '+' + self.ui.expression_2.text() + '+' + self.ui.expression_3.text()
        for letter in text:
            if not letter.isalpha():
                text = text.replace(letter, ' ')   
        text = text.split()
        return text

    def param_select(self):
        self.ui.x_param.clear()
        self.ui.other_params.clear()
        text = self.text_prepare()
        for word in text:
            items = [self.ui.x_param.itemText(i) for i in range(self.ui.x_param.count())]
            if word not in self.reserved_statements and word not in items:
                self.ui.x_param.addItem(word)
    
    def second_param_select(self):
        if self.ui.graph3d.isChecked():
            self.ui.x_param_2.clear()
            text = self.text_prepare()
            for word in text:
                items = [self.ui.x_param_2.itemText(i) for i in range(self.ui.x_param_2.count())]
                if word not in self.reserved_statements and word != self.ui.x_param.currentText() and word not in items:
                    self.ui.x_param_2.addItem(word)

    def other_params_select(self):
        self.ui.other_params.clear()
        text = self.text_prepare()
        for word in text:
            items = [self.ui.other_params.itemText(i) for i in range(self.ui.other_params.count())]
            if word not in self.reserved_statements \
            and word not in (self.ui.x_param.currentText(), self.ui.x_param_2.currentText())\
            and word not in items:
                        self.ui.other_params.addItem(word)
        self.ui.output_expression.setText(self.expression)
        self.params.clear()
        self.values.clear()
        self.ui.parameters.clear()
        self.ui.param1name.setText(self.ui.x_param.currentText())
        self.ui.param2name.setText(self.ui.x_param_2.currentText())

    def edit_params(self):
        param = self.ui.other_params.currentText() 
        text = self.ui.parameters.text() 
        if param not in self.params:
            self.params.append(param)
            self.values.append(text)
        self.values[self.params.index(param)] = text
        replacements = {self.params[i]:self.values[i] for i in range(len(self.params))}
        self.buffer = multiple_replace(replacements,self.expression)
        self.ui.output_expression.setText(self.buffer)
    
    def clear_edit(self):
        self.ui.parameters.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    

    window.show()
    sys.exit(app.exec())