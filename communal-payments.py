# communal-payments Rybkin Nikita Igorevich

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Main import Ui_MainWindow

# Create application
app = QApplication(sys.argv)

# Create form and init UI
Form = QtGui.QWid
ui = Ui_MainWindow
ui.setupUi(Form)
Form.show()


# Hook logic



# Run main loop
sys.exit(app.exec_())


# from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QTextEdit
# from PyQt5 import uic, QtCore, QtGui, QtWidgets
# import sys
#
#
# class UI(QMainWindow):
#     def __init__(self):
#         super(UI, self).__init__()
#
#         uic.loadUi("ui/cd_MainMenu.ui", self)
#         # uic.loadUi("ui/cd_ElectricalEnergy.ui", self)
#         uic.loadUi("ui/cd_TypesOfPayments.ui", self)
#
#         self.show()
#
#
# app = QApplication(sys.argv)
# UIWindow = UI()
# app.exec_()