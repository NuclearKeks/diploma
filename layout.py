# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layoutgrvbDj.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(856, 648)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 10, 101, 20))
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setMargin(0)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 230, 121, 21))
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setMargin(0)
        self.other_params = QComboBox(self.centralwidget)
        self.other_params.setObjectName(u"other_params")
        self.other_params.setGeometry(QRect(40, 260, 71, 22))
        self.other_params.setEditable(False)
        self.parameters = QLineEdit(self.centralwidget)
        self.parameters.setObjectName(u"parameters")
        self.parameters.setGeometry(QRect(110, 260, 61, 22))
        self.expression = QLineEdit(self.centralwidget)
        self.expression.setObjectName(u"expression")
        self.expression.setGeometry(QRect(40, 40, 311, 22))
        self.output_expression = QTextBrowser(self.centralwidget)
        self.output_expression.setObjectName(u"output_expression")
        self.output_expression.setGeometry(QRect(40, 320, 321, 61))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 300, 121, 16))
        self.left_border = QLineEdit(self.centralwidget)
        self.left_border.setObjectName(u"left_border")
        self.left_border.setGeometry(QRect(70, 440, 51, 22))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 390, 211, 21))
        self.label_5.setFrameShadow(QFrame.Plain)
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setMargin(0)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 440, 21, 20))
        self.label_6.setFrameShadow(QFrame.Plain)
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setMargin(0)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 470, 21, 20))
        self.label_7.setFrameShadow(QFrame.Plain)
        self.label_7.setTextFormat(Qt.AutoText)
        self.label_7.setMargin(0)
        self.right_border = QLineEdit(self.centralwidget)
        self.right_border.setObjectName(u"right_border")
        self.right_border.setGeometry(QRect(70, 470, 51, 22))
        self.draw_button = QPushButton(self.centralwidget)
        self.draw_button.setObjectName(u"draw_button")
        self.draw_button.setGeometry(QRect(60, 560, 121, 61))
        self.clear_button = QPushButton(self.centralwidget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setGeometry(QRect(210, 560, 121, 61))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 170, 151, 16))
        self.label_8.setFrameShadow(QFrame.Plain)
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setMargin(0)
        self.x_param = QComboBox(self.centralwidget)
        self.x_param.setObjectName(u"x_param")
        self.x_param.setGeometry(QRect(40, 200, 71, 22))
        self.x_param.setEditable(False)
        self.x_param.setDuplicatesEnabled(False)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setGeometry(QRect(390, 20, 451, 581))
        self.verticalLayoutWidget = QWidget(self.widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 50, 431, 521))
        self.graph_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.graph_layout.setObjectName(u"graph_layout")
        self.graph_layout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 9, 41, 16))
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setMargin(0)
        self.graph_name = QLineEdit(self.centralwidget)
        self.graph_name.setObjectName(u"graph_name")
        self.graph_name.setGeometry(QRect(130, 530, 200, 22))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(50, 530, 80, 20))
        self.label_9.setFrameShadow(QFrame.Plain)
        self.label_9.setTextFormat(Qt.AutoText)
        self.label_9.setMargin(0)
        self.param1name = QLabel(self.centralwidget)
        self.param1name.setObjectName(u"param1name")
        self.param1name.setGeometry(QRect(70, 410, 31, 21))
        self.param1name.setFrameShadow(QFrame.Plain)
        self.param1name.setTextFormat(Qt.AutoText)
        self.param1name.setMargin(0)
        self.graph3d_widgets = QWidget(self.centralwidget)
        self.graph3d_widgets.setObjectName(u"graph3d_widgets")
        self.graph3d_widgets.setEnabled(False)
        self.graph3d_widgets.setGeometry(QRect(199, 169, 151, 361))
        self.grapg3d_label = QLabel(self.graph3d_widgets)
        self.grapg3d_label.setObjectName(u"grapg3d_label")
        self.grapg3d_label.setEnabled(False)
        self.grapg3d_label.setGeometry(QRect(2, 0, 151, 16))
        self.grapg3d_label.setFrameShadow(QFrame.Plain)
        self.grapg3d_label.setTextFormat(Qt.AutoText)
        self.grapg3d_label.setMargin(0)
        self.x_param_2 = QComboBox(self.graph3d_widgets)
        self.x_param_2.setObjectName(u"x_param_2")
        self.x_param_2.setEnabled(False)
        self.x_param_2.setGeometry(QRect(10, 30, 71, 22))
        self.x_param_2.setEditable(False)
        self.x_param_2.setDuplicatesEnabled(False)
        self.label_12 = QLabel(self.graph3d_widgets)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setEnabled(False)
        self.label_12.setGeometry(QRect(20, 270, 21, 20))
        self.label_12.setFrameShadow(QFrame.Plain)
        self.label_12.setTextFormat(Qt.AutoText)
        self.label_12.setMargin(0)
        self.param2name = QLabel(self.graph3d_widgets)
        self.param2name.setObjectName(u"param2name")
        self.param2name.setEnabled(False)
        self.param2name.setGeometry(QRect(20, 240, 31, 21))
        self.param2name.setFrameShadow(QFrame.Plain)
        self.param2name.setTextFormat(Qt.AutoText)
        self.param2name.setMargin(0)
        self.label_13 = QLabel(self.graph3d_widgets)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setEnabled(False)
        self.label_13.setGeometry(QRect(20, 300, 21, 20))
        self.label_13.setFrameShadow(QFrame.Plain)
        self.label_13.setTextFormat(Qt.AutoText)
        self.label_13.setMargin(0)
        self.left_border_2 = QLineEdit(self.graph3d_widgets)
        self.left_border_2.setObjectName(u"left_border_2")
        self.left_border_2.setEnabled(False)
        self.left_border_2.setGeometry(QRect(40, 270, 51, 22))
        self.right_border_2 = QLineEdit(self.graph3d_widgets)
        self.right_border_2.setObjectName(u"right_border_2")
        self.right_border_2.setEnabled(False)
        self.right_border_2.setGeometry(QRect(40, 300, 51, 22))
        self.label_15 = QLabel(self.graph3d_widgets)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 330, 30, 20))
        self.label_15.setFrameShadow(QFrame.Plain)
        self.label_15.setTextFormat(Qt.AutoText)
        self.label_15.setMargin(0)
        self.step_2 = QLineEdit(self.graph3d_widgets)
        self.step_2.setObjectName(u"step_2")
        self.step_2.setGeometry(QRect(40, 330, 51, 22))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 80, 301, 22))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.graph2d = QRadioButton(self.layoutWidget)
        self.graph2d.setObjectName(u"graph2d")
        self.graph2d.setChecked(True)

        self.horizontalLayout.addWidget(self.graph2d)

        self.graph3d = QRadioButton(self.layoutWidget)
        self.graph3d.setObjectName(u"graph3d")

        self.horizontalLayout.addWidget(self.graph3d)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 40, 21, 21))
        self.params_3d = QWidget(self.centralwidget)
        self.params_3d.setObjectName(u"params_3d")
        self.params_3d.setEnabled(False)
        self.params_3d.setGeometry(QRect(20, 110, 331, 61))
        self.expression_3 = QLineEdit(self.params_3d)
        self.expression_3.setObjectName(u"expression_3")
        self.expression_3.setGeometry(QRect(20, 30, 311, 22))
        self.label_11 = QLabel(self.params_3d)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 0, 21, 21))
        self.expression_2 = QLineEdit(self.params_3d)
        self.expression_2.setObjectName(u"expression_2")
        self.expression_2.setGeometry(QRect(20, 0, 311, 22))
        self.label_14 = QLabel(self.params_3d)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 30, 21, 21))
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(40, 500, 30, 20))
        self.label_16.setFrameShadow(QFrame.Plain)
        self.label_16.setTextFormat(Qt.AutoText)
        self.label_16.setMargin(0)
        self.step = QLineEdit(self.centralwidget)
        self.step.setObjectName(u"step")
        self.step.setGeometry(QRect(70, 500, 51, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.params_3d.raise_()
        self.graph3d_widgets.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.other_params.raise_()
        self.parameters.raise_()
        self.expression.raise_()
        self.output_expression.raise_()
        self.label_4.raise_()
        self.left_border.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.right_border.raise_()
        self.draw_button.raise_()
        self.clear_button.raise_()
        self.label_8.raise_()
        self.x_param.raise_()
        self.widget.raise_()
        self.graph_name.raise_()
        self.label_9.raise_()
        self.param1name.raise_()
        self.layoutWidget.raise_()
        self.label_10.raise_()
        self.label_16.raise_()
        self.step.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 856, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0447\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b:", None))
        self.other_params.setCurrentText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u043e\u0432\u043e\u0435 \u0412\u044b\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u044b \u0438\u0441\u0441\u043b\u0435\u0434\u0443\u0435\u043c\u044b\u0445 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e:", None))
        self.draw_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043b\u0438\u0441\u0442", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0441\u043b\u0435\u0434\u0443\u0435\u043c\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 1:", None))
        self.x_param.setCurrentText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430:", None))
        self.param1name.setText("")
        self.grapg3d_label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0441\u043b\u0435\u0434\u0443\u0435\u043c\u044b\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 2:", None))
        self.x_param_2.setCurrentText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442:", None))
        self.param2name.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433:", None))
        self.graph2d.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0432\u0443\u0445\u043c\u0435\u0440\u043d\u044b\u0439 \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.graph3d.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0451\u0445\u043c\u0435\u0440\u043d\u044b\u0439 \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"y=", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"x=", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"z=", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433:", None))
    # retranslateUi

