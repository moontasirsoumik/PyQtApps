# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fourth_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 650)
        MainWindow.setMinimumSize(QtCore.QSize(470, 650))
        MainWindow.setMaximumSize(QtCore.QSize(470, 650))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMaximumSize(QtCore.QSize(550, 620))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_24 = QtWidgets.QLabel(self.page)
        self.label_24.setMinimumSize(QtCore.QSize(50, 50))
        self.label_24.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setText("")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 4, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.page)
        self.label_19.setMinimumSize(QtCore.QSize(50, 50))
        self.label_19.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setText("")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 3, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setMinimumSize(QtCore.QSize(50, 50))
        self.label_8.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setText("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.page)
        self.label_15.setMinimumSize(QtCore.QSize(50, 50))
        self.label_15.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setText("")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 2, 4, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.page)
        self.label_20.setMinimumSize(QtCore.QSize(50, 50))
        self.label_20.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setText("")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 3, 4, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.page)
        self.label_29.setMinimumSize(QtCore.QSize(50, 50))
        self.label_29.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setText("")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 5, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setMinimumSize(QtCore.QSize(50, 50))
        self.label_16.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setText("")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 3, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.page)
        self.label_21.setMinimumSize(QtCore.QSize(50, 50))
        self.label_21.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setText("")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 4, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.page)
        self.label_26.setMinimumSize(QtCore.QSize(50, 50))
        self.label_26.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setText("")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 5, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.page)
        self.label_30.setMinimumSize(QtCore.QSize(50, 50))
        self.label_30.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_30.setFont(font)
        self.label_30.setText("")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 5, 4, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setMinimumSize(QtCore.QSize(50, 50))
        self.label_17.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setText("")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setMinimumSize(QtCore.QSize(50, 50))
        self.label_12.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setText("")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.page)
        self.label_28.setMinimumSize(QtCore.QSize(50, 50))
        self.label_28.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setText("")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 5, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.page)
        self.label_18.setMinimumSize(QtCore.QSize(50, 50))
        self.label_18.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setText("")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setMinimumSize(QtCore.QSize(50, 50))
        self.label_4.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setMinimumSize(QtCore.QSize(50, 50))
        self.label_5.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 4, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.page)
        self.label_25.setMinimumSize(QtCore.QSize(50, 50))
        self.label_25.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setText("")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 4, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.page)
        self.label_13.setMinimumSize(QtCore.QSize(50, 50))
        self.label_13.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setText("")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 2, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.page)
        self.label_22.setMinimumSize(QtCore.QSize(50, 50))
        self.label_22.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setText("")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setMinimumSize(QtCore.QSize(50, 50))
        self.label_6.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.page)
        self.label_7.setMinimumSize(QtCore.QSize(50, 50))
        self.label_7.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.page)
        self.label_9.setMinimumSize(QtCore.QSize(50, 50))
        self.label_9.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setMinimumSize(QtCore.QSize(50, 50))
        self.label_3.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.page)
        self.label_1.setMinimumSize(QtCore.QSize(50, 50))
        self.label_1.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_1.setFont(font)
        self.label_1.setText("")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.gridLayout_2.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.label_2.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.page)
        self.label_23.setMinimumSize(QtCore.QSize(50, 50))
        self.label_23.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setText("")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 4, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setMinimumSize(QtCore.QSize(50, 50))
        self.label_10.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 4, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.page)
        self.label_27.setMinimumSize(QtCore.QSize(50, 50))
        self.label_27.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setText("")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 5, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setMinimumSize(QtCore.QSize(50, 50))
        self.label_11.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setText("")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.page)
        self.label_14.setMinimumSize(QtCore.QSize(50, 50))
        self.label_14.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setText("")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 3, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_1.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_1.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout_2.addWidget(self.lineEdit_1, 6, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 6, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 6, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 6, 3, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(50, 50))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 6, 4, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.label_info = QtWidgets.QLabel(self.page)
        self.label_info.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_info.setFont(font)
        self.label_info.setText("")
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.gridLayout_3.addWidget(self.label_info, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_retry = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_retry.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_retry.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_retry.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("retry.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_retry.setIcon(icon)
        self.pushButton_retry.setObjectName("pushButton_retry")
        self.horizontalLayout_4.addWidget(self.pushButton_retry)
        self.pushButton_enter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_enter.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_enter.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_enter.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("enter.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_enter.setIcon(icon1)
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.horizontalLayout_4.addWidget(self.pushButton_enter)
        self.pushButton_hint = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_hint.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_hint.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_hint.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_hint.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            "hint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_hint.setIcon(icon2)
        self.pushButton_hint.setObjectName("pushButton_hint")
        self.horizontalLayout_4.addWidget(self.pushButton_hint)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wordle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())