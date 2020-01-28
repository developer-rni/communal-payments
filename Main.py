# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cd_MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu_61 = QtWidgets.QMenu(self.menubar)
        self.menu_61.setObjectName("menu_61")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_13 = QtWidgets.QMenu(self.menubar)
        self.menu_13.setObjectName("menu_13")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.menu_61.addAction(self.action_6)
        self.menu_61.addAction(self.action_7)
        self.menu.addAction(self.action_8)
        self.menu_13.addAction(self.action)
        self.menu_13.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_5)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_13.menuAction())
        self.menubar.addAction(self.menu_61.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Коммунальные платежи"))
        self.menu_61.setTitle(_translate("MainWindow", "Андреевская 61А"))
        self.menu.setTitle(_translate("MainWindow", "ИТОГО"))
        self.menu_13.setTitle(_translate("MainWindow", "Толстого 13"))
        self.menu_2.setTitle(_translate("MainWindow", "Файл"))
        self.action.setText(_translate("MainWindow", "Рассчитать"))
        self.action_2.setText(_translate("MainWindow", "Отчет"))
        self.action_3.setText(_translate("MainWindow", "Сохранить"))
        self.action_5.setText(_translate("MainWindow", "Выход"))
        self.action_6.setText(_translate("MainWindow", "Рассчитать"))
        self.action_7.setText(_translate("MainWindow", "Отчет"))
        self.action_8.setText(_translate("MainWindow", "Общий отчет"))

