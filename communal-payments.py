# communal-payments Rybkin Nikita Igorevich
# v 0.1.2

import sys, MainMenu
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QGridLayout, QLabel, QApplication

"""Нужно добавить таблицы для андреевской и общего отчета(итого) через desiner"""

class ExampleApp(QtWidgets.QMainWindow, MainMenu.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле Main.py
        super(ExampleApp, self).__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        #------
        self.InitUI()


    def InitUI(self):
        self.action_2.triggered.connect(self.close)  # Закрыть программу при нажатии Файл->Выход
        self.action_3.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(1))  # Открыть окно "что платим" при нажатии на Толстого13->Рассчитать
        self.action_4.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(3))  # Открыть таблицу отчет при нажатии на Толстого13->Отчет
        self.action_5.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(2))  # Открыть окно "что платим" при нажатии на Андреевская61->Рассчитать
        self.action_6.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(3))  # Открыть таблицу отчет при нажатии на Андреевская61->Отчет



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

