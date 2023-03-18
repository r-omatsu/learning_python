# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_Pityna.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(855, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidgetLog = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetLog.setGeometry(QtCore.QRect(5, 0, 340, 500))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidgetLog.setFont(font)
        self.listWidgetLog.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidgetLog.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidgetLog.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidgetLog.setObjectName("listWidgetLog")
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setGeometry(QtCore.QRect(30, 510, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(200, 510, 130, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(5, 540, 680, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.buttonTalk = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTalk.setGeometry(QtCore.QRect(690, 540, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonTalk.setFont(font)
        self.buttonTalk.setObjectName("buttonTalk")
        self.labelResponse = QtWidgets.QLabel(self.centralwidget)
        self.labelResponse.setGeometry(QtCore.QRect(350, 300, 500, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelResponse.setFont(font)
        self.labelResponse.setFrameShape(QtWidgets.QFrame.Box)
        self.labelResponse.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelResponse.setText("")
        self.labelResponse.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResponse.setObjectName("labelResponse")
        self.labelShowing = QtWidgets.QLabel(self.centralwidget)
        self.labelShowing.setGeometry(QtCore.QRect(350, 0, 500, 295))
        self.labelShowing.setText("")
        self.labelShowing.setPixmap(QtGui.QPixmap(":/re/img1.gif"))
        self.labelShowing.setScaledContents(True)
        self.labelShowing.setObjectName("labelShowing")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 855, 36))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.menuClose = QtWidgets.QAction(MainWindow)
        self.menuClose.setObjectName("menuClose")
        self.menu.addAction(self.menuClose)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.buttonTalk.clicked.connect(MainWindow.buttonTalkSlot)  # type: ignore
        self.radioButton_1.clicked.connect(MainWindow.showResponderName)  # type: ignore
        self.radioButton_2.clicked.connect(MainWindow.hiddenResponderName)  # type: ignore
        self.menuClose.triggered.connect(MainWindow.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton_1.setText(_translate("MainWindow", "Responderを表示"))
        self.radioButton_2.setText(_translate("MainWindow", "Responderを非表示"))
        self.buttonTalk.setText(_translate("MainWindow", "話す"))
        self.menu.setTitle(_translate("MainWindow", "ファイル"))
        self.menuClose.setText(_translate("MainWindow", "閉じる"))


# import qt_resource_rc
