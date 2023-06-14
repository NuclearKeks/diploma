# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'final_interfacegMTpAi.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(856, 605)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 160, 81, 20))
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setMargin(0)
        self.draw_button = QPushButton(self.centralwidget)
        self.draw_button.setObjectName(u"draw_button")
        self.draw_button.setGeometry(QRect(40, 520, 121, 61))
        self.clear_button = QPushButton(self.centralwidget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setGeometry(QRect(230, 520, 121, 61))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 100, 151, 16))
        self.label_8.setFrameShadow(QFrame.Plain)
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setMargin(0)
        self.column = QComboBox(self.centralwidget)
        self.column.setObjectName(u"column")
        self.column.setGeometry(QRect(40, 130, 151, 22))
        self.column.setEditable(False)
        self.column.setDuplicatesEnabled(False)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setGeometry(QRect(390, 20, 451, 581))
        self.verticalLayoutWidget = QWidget(self.widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 40, 431, 521))
        self.graph_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.graph_layout.setObjectName(u"graph_layout")
        self.graph_layout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 0, 91, 31))
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setMargin(0)
        self.graph_name = QLineEdit(self.centralwidget)
        self.graph_name.setObjectName(u"graph_name")
        self.graph_name.setGeometry(QRect(130, 490, 221, 22))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 490, 80, 20))
        self.label_9.setFrameShadow(QFrame.Plain)
        self.label_9.setTextFormat(Qt.AutoText)
        self.label_9.setMargin(0)
        self.filename = QLabel(self.centralwidget)
        self.filename.setObjectName(u"filename")
        self.filename.setGeometry(QRect(40, 60, 301, 31))
        font = QFont()
        font.setPointSize(10)
        self.filename.setFont(font)
        self.directory_select = QPushButton(self.centralwidget)
        self.directory_select.setObjectName(u"directory_select")
        self.directory_select.setGeometry(QRect(40, 10, 301, 41))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(18)
        self.directory_select.setFont(font1)
        self.directory_select.setIconSize(QSize(16, 16))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 80, 391, 20))
        self.line.setStyleSheet(u"")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(380, -10, 20, 751))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 160, 91, 20))
        self.label_4.setFrameShadow(QFrame.Plain)
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setMargin(0)
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(40, 180, 212, 191))
        self.switches = QVBoxLayout(self.verticalLayoutWidget_2)
        self.switches.setObjectName(u"switches")
        self.switches.setContentsMargins(0, 0, 0, 0)
        self.vins_left_switch = QCheckBox(self.verticalLayoutWidget_2)
        self.vins_left_switch.setObjectName(u"vins_left_switch")
        self.vins_left_switch.setChecked(True)

        self.switches.addWidget(self.vins_left_switch)

        self.vins_right_switch = QCheckBox(self.verticalLayoutWidget_2)
        self.vins_right_switch.setObjectName(u"vins_right_switch")
        self.vins_right_switch.setChecked(True)

        self.switches.addWidget(self.vins_right_switch)

        self.linapprox_sqitch = QCheckBox(self.verticalLayoutWidget_2)
        self.linapprox_sqitch.setObjectName(u"linapprox_sqitch")
        self.linapprox_sqitch.setChecked(True)

        self.switches.addWidget(self.linapprox_sqitch)

        self.rss_switch = QCheckBox(self.verticalLayoutWidget_2)
        self.rss_switch.setObjectName(u"rss_switch")
        self.rss_switch.setChecked(True)

        self.switches.addWidget(self.rss_switch)

        self.corr_res_switch = QCheckBox(self.verticalLayoutWidget_2)
        self.corr_res_switch.setObjectName(u"corr_res_switch")
        self.corr_res_switch.setChecked(True)

        self.switches.addWidget(self.corr_res_switch)

        self.gbm_switch = QCheckBox(self.verticalLayoutWidget_2)
        self.gbm_switch.setObjectName(u"gbm_switch")
        self.gbm_switch.setEnabled(True)
        self.gbm_switch.setChecked(True)

        self.switches.addWidget(self.gbm_switch)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(270, 180, 111, 191))
        self.efficiency = QVBoxLayout(self.verticalLayoutWidget_3)
        self.efficiency.setObjectName(u"efficiency")
        self.efficiency.setContentsMargins(0, 0, 0, 0)
        self.vins_left_eff = QLabel(self.verticalLayoutWidget_3)
        self.vins_left_eff.setObjectName(u"vins_left_eff")
        self.vins_left_eff.setFrameShadow(QFrame.Plain)
        self.vins_left_eff.setTextFormat(Qt.AutoText)
        self.vins_left_eff.setMargin(0)

        self.efficiency.addWidget(self.vins_left_eff)

        self.vins_right_eff = QLabel(self.verticalLayoutWidget_3)
        self.vins_right_eff.setObjectName(u"vins_right_eff")
        self.vins_right_eff.setFrameShadow(QFrame.Plain)
        self.vins_right_eff.setTextFormat(Qt.AutoText)
        self.vins_right_eff.setMargin(0)

        self.efficiency.addWidget(self.vins_right_eff)

        self.linapprox_eff = QLabel(self.verticalLayoutWidget_3)
        self.linapprox_eff.setObjectName(u"linapprox_eff")
        self.linapprox_eff.setFrameShadow(QFrame.Plain)
        self.linapprox_eff.setTextFormat(Qt.AutoText)
        self.linapprox_eff.setMargin(0)

        self.efficiency.addWidget(self.linapprox_eff)

        self.rss_eff = QLabel(self.verticalLayoutWidget_3)
        self.rss_eff.setObjectName(u"rss_eff")
        self.rss_eff.setFrameShadow(QFrame.Plain)
        self.rss_eff.setTextFormat(Qt.AutoText)
        self.rss_eff.setMargin(0)

        self.efficiency.addWidget(self.rss_eff)

        self.corr_res_eff = QLabel(self.verticalLayoutWidget_3)
        self.corr_res_eff.setObjectName(u"corr_res_eff")
        self.corr_res_eff.setFrameShadow(QFrame.Plain)
        self.corr_res_eff.setTextFormat(Qt.AutoText)
        self.corr_res_eff.setMargin(0)

        self.efficiency.addWidget(self.corr_res_eff)

        self.gbm_eff = QLabel(self.verticalLayoutWidget_3)
        self.gbm_eff.setObjectName(u"gbm_eff")
        self.gbm_eff.setEnabled(True)
        self.gbm_eff.setFrameShadow(QFrame.Plain)
        self.gbm_eff.setTextFormat(Qt.AutoText)
        self.gbm_eff.setMargin(0)

        self.efficiency.addWidget(self.gbm_eff)

        self.smoothing = QComboBox(self.centralwidget)
        self.smoothing.setObjectName(u"smoothing")
        self.smoothing.setGeometry(QRect(200, 130, 151, 22))
        self.smoothing.setEditable(False)
        self.smoothing.setDuplicatesEnabled(False)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(200, 100, 161, 16))
        self.label_10.setFrameShadow(QFrame.Plain)
        self.label_10.setTextFormat(Qt.AutoText)
        self.label_10.setMargin(0)
        self.gbm_switch_2 = QCheckBox(self.centralwidget)
        self.gbm_switch_2.setObjectName(u"gbm_switch_2")
        self.gbm_switch_2.setEnabled(True)
        self.gbm_switch_2.setGeometry(QRect(40, 380, 210, 20))
        self.gbm_switch_2.setChecked(False)
        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(40, 409, 311, 71))
        self.dop_params = QVBoxLayout(self.verticalLayoutWidget_4)
        self.dop_params.setObjectName(u"dop_params")
        self.dop_params.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(False)
        self.label_5.setFrameShadow(QFrame.Plain)
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setMargin(0)

        self.dop_params.addWidget(self.label_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.verticalLayoutWidget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(False)
        self.label_6.setFrameShadow(QFrame.Plain)
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setMargin(0)

        self.horizontalLayout.addWidget(self.label_6)

        self.left_border = QLineEdit(self.verticalLayoutWidget_4)
        self.left_border.setObjectName(u"left_border")
        self.left_border.setEnabled(False)

        self.horizontalLayout.addWidget(self.left_border)

        self.label_7 = QLabel(self.verticalLayoutWidget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(False)
        self.label_7.setFrameShadow(QFrame.Plain)
        self.label_7.setTextFormat(Qt.AutoText)
        self.label_7.setMargin(0)

        self.horizontalLayout.addWidget(self.label_7)

        self.right_border = QLineEdit(self.verticalLayoutWidget_4)
        self.right_border.setObjectName(u"right_border")
        self.right_border.setEnabled(False)

        self.horizontalLayout.addWidget(self.right_border)

        self.label_16 = QLabel(self.verticalLayoutWidget_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setEnabled(False)
        self.label_16.setFrameShadow(QFrame.Plain)
        self.label_16.setTextFormat(Qt.AutoText)
        self.label_16.setMargin(0)

        self.horizontalLayout.addWidget(self.label_16)

        self.step = QLineEdit(self.verticalLayoutWidget_4)
        self.step.setObjectName(u"step")
        self.step.setEnabled(False)

        self.horizontalLayout.addWidget(self.step)


        self.dop_params.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u044b:", None))
        self.draw_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043b\u0438\u0441\u0442", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0442\u043e\u043b\u0431\u0435\u0446:", None))
        self.column.setCurrentText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">\u0413\u0440\u0430\u0444\u0438\u043a</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430:", None))
        self.filename.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.directory_select.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b", None))
#if QT_CONFIG(tooltip)
        self.line.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.line.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u042d\u0444\u0444\u0435\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c", None))
        self.vins_left_switch.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u043d\u0437\u043e\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 (\u043b\u0435\u0432\u043e\u0435)", None))
        self.vins_right_switch.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u043d\u0437\u043e\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435(\u043f\u0440\u0430\u0432\u043e\u0435)", None))
        self.linapprox_sqitch.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u043d\u0435\u0439\u043d\u0430\u044f \u0430\u043f\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446\u0438\u044f", None))
        self.rss_switch.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u043d\u0430\u0438\u043c\u0435\u043d\u044c\u0448\u0438\u0445 \u043a\u0432\u0430\u0434\u0440\u0430\u0442\u043e\u0432", None))
        self.corr_res_switch.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u043e\u043d\u043d\u043e\u0435 \u0432\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.gbm_switch.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0434\u0438\u0435\u043d\u0442\u043d\u044b\u0439 \u0431\u0443\u0441\u0442\u0438\u043d\u0433", None))
        self.vins_left_eff.setText(QCoreApplication.translate("MainWindow", u"0.191", None))
        self.vins_right_eff.setText(QCoreApplication.translate("MainWindow", u"0.181", None))
        self.linapprox_eff.setText(QCoreApplication.translate("MainWindow", u"0.185", None))
        self.rss_eff.setText(QCoreApplication.translate("MainWindow", u"0.084", None))
        self.corr_res_eff.setText(QCoreApplication.translate("MainWindow", u"0.157", None))
        self.gbm_eff.setText(QCoreApplication.translate("MainWindow", u"0.15", None))
        self.smoothing.setCurrentText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0438\u043f \u0441\u0433\u043b\u0430\u0436\u0438\u0432\u0430\u043d\u0438\u044f:", None))
        self.gbm_switch_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043d\u043a\u0430\u044f \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0430", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u044b \u0440\u0430\u0441\u0441\u043c\u0430\u0442\u0440\u0438\u0432\u0430\u0435\u043c\u044b\u0445 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433:", None))
    # retranslateUi

