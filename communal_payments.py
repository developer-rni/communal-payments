#!/usr/bin/python3
# communal_payments Rybkin Nikita Igorevich
# v 1.7.3

import sys, MainMenu, save, exitM, upload_gd, upload_error, upload_success, change, change_a61a, recalculation_water
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QGridLayout, QLabel, QApplication


class ExampleApp(QtWidgets.QMainWindow, MainMenu.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле Main.py
        super(ExampleApp, self).__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        #------
        self.InitUI()
        self.save = save()
        self.exitM = exitM()
        self.upload_success = upload_success()
        self.upload_error = upload_error()
        self.change = change()
        self.change_a61a = change_a61a()
        self.recalculation_water = recalculation_water()


    def InitUI(self):
        self.action_save.triggered.connect(self.show_save_db)  # Вывести окно и сохранить данные в бд при нажатии Файл -> сохронить
        self.action_download_GD.triggered.connect(self.upload_BD)  # Загрузить БД в Google Drive при нажатии Файл -> Залить в облако (google drive)
        self.action_exit.triggered.connect(self.show_exitM)  # Закрыть программу при нажатии Файл -> Выход

        self.action_t13_calculate.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(1))  # Открыть окно "что платим" при нажатии на Толстого13 -> Рассчитать
        self.action_t13_report.triggered.connect(self.show_report_t13)  # Открыть таблицу отчет при нажатии на Толстого13 -> Отчет
        self.action_t13_change.triggered.connect(self.show_change_t13) # Вывести окно изменение платежей Толстого 13
        self.action_t13_recalculation_water.triggered.connect(self.show_recalculation_water_t13) # Вывести окно пересчет водоснабжения Толстого 13
        
        self.action_a61a_calculate.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(2))  # Открыть окно "что платим" при нажатии на Андреевская 61а -> Рассчитать
        self.action_a61a_report.triggered.connect(self.show_report_a61a)  # Открыть таблицу отчет при нажатии на Андреевская 61а -> Отчет
        self.action_a61a_change.triggered.connect(self.show_change_a61a) # Вывести окно изменение платежей Андреевская 61а

        self.action_generalreport.triggered.connect(self.show_general_report)  # Откртыть Итого -> Общий отчет

    def show_save_db(self):
        MainMenu.con.commit()
        self.save.show()

    def show_exitM(self):
        self.exitM.show()

    def show_report_t13(self):
        MainMenu.Ui_MainWindow.data_update_t13(self)
        self.stackedWidget.setCurrentIndex(3)

    def show_report_a61a(self):
        MainMenu.Ui_MainWindow.data_update_a61a(self)
        self.stackedWidget.setCurrentIndex(4)

    def show_general_report(self):
        MainMenu.Ui_MainWindow.data_update_general_total(self)
        self.stackedWidget.setCurrentIndex(5)
        
    def upload_BD(self):
        result_upload = upload_gd.upload_file.upload_f(self)
        if result_upload == True:
            self.upload_success.show()
        elif result_upload == False:
            self.upload_error.show()

    def show_change_t13(self):
        self.change.show()
    
    def show_change_a61a(self):
        self.change_a61a.show()
    
    def show_recalculation_water_t13(self):
        self.recalculation_water.show()



class save(QtWidgets.QDialog, save.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

class exitM(QtWidgets.QDialog, exitM.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

class upload_success(QtWidgets.QDialog, upload_success.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

class upload_error(QtWidgets.QDialog, upload_error.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

class change(QtWidgets.QDialog, change.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

class change_a61a(QtWidgets.QDialog, change_a61a.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

class recalculation_water(QtWidgets.QDialog, recalculation_water.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

