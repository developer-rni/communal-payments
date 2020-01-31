# communal-payments Rybkin Nikita Igorevich

import sys, MainMenu, ElectricalEnergy, TypesOfPayments, Table_t13
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QGridLayout, QLabel, QApplication

class ExampleApp(QtWidgets.QMainWindow, MainMenu.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле Main.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        #------
        self.typofpay = typofpay()
        self.table_t13 = table_t13()


        self.action_5.triggered.connect(self.close)  # Закрыть программу при нажатии Файл->Выход
        self.action.triggered.connect(self.show_typofpay)  # Открыть окно "что платим" при нажатии на Толстого13->Рассчитать
        self.action_6.triggered.connect(self.show_typofpay)  # Открыть окно "что платим" при нажатии на Андреевская61->Рассчитать
        self.action_2.triggered.connect(self.show_table_t13)  #


    def show_typofpay(self):
        self.setCentralWidget(self.typofpay)
    def show_table_t13(self):
        self.setCentralWidget(self.table_t13)

class typofpay(QtWidgets.QWidget, TypesOfPayments.Ui_Form):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле Main.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.ElectEn = ElectEn()

        self.pushButton.clicked.connect(self.show_ElectEn)

    def show_ElectEn(self):
        self.ElectEn.show()

class table_t13(QtWidgets.QTabWidget, Table_t13.Ui_TabWidget):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле Main.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

class ElectEn(QtWidgets.QDialog, ElectricalEnergy.Ui_Dialog):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле Main.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

