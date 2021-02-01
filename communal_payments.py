#!/usr/bin/python3
# communal_payments Rybkin Nikita Igorevich
# v 1.7.4

import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import MainMenu
import save
import exitM
import upload_gd
import upload_error
import upload_success
import change
import change_a61a
import recalculation_water


class ExampleApp(QtWidgets.QMainWindow, MainMenu.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле Main.py
        super(ExampleApp, self).__init__()
        self.setupUi(self)
        # ------
        self.InitUI()
        self.save = Save()
        self.exitM = ExitM()
        self.upload_success = UploadSuccess()
        self.upload_error = UploadError()
        self.change = Change()
        self.change_a61a = ChangeA61A()
        self.recalculation_water = RecalculationWater()

    def InitUI(self):
        self.action_save.triggered.connect(self.show_save_db)  # Вывести окно и сохранить данные в бд при нажатии Файл -> сохранить
        self.action_download_GD.triggered.connect(self.upload_BD)  # Загрузить БД в Google Drive при нажатии Файл -> Залить в облако (google drive)
        self.action_exit.triggered.connect(self.show_exitM)  # Закрыть программу при нажатии Файл -> Выход

        self.action_t13_calculate.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(1))  # Открыть окно "что платим" при нажатии на Толстого13 -> Рассчитать
        self.action_t13_report.triggered.connect(self.show_report_t13)  # Открыть таблицу отчет при нажатии на Толстого13 -> Отчет
        self.action_t13_change.triggered.connect(self.show_change_t13)  # Вывести окно изменение платежей Толстого 13
        self.action_t13_recalculation_water.triggered.connect(self.show_recalculation_water_t13)    # Вывести окно пересчет водоснабжения Толстого 13

        self.action_a61a_calculate.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(2))  # Открыть окно "что платим" при нажатии на Андреевская 61а -> Рассчитать
        self.action_a61a_report.triggered.connect(self.show_report_a61a)  # Открыть таблицу отчет при нажатии на Андреевская 61а -> Отчет
        self.action_a61a_change.triggered.connect(self.show_change_a61a)    # Вывести окно изменение платежей Андреевская 61а

        self.action_generalreport.triggered.connect(self.show_general_report)  # Открыть Итого -> Общий отчет

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
        if result_upload:
            self.upload_success.show()
        elif result_upload:
            self.upload_error.show()

    def show_change_t13(self):
        self.change.show()

    def show_change_a61a(self):
        self.change_a61a.show()

    def show_recalculation_water_t13(self):
        self.recalculation_water.show()


class Save(QtWidgets.QDialog, save.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ExitM(QtWidgets.QDialog, exitM.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class UploadSuccess(QtWidgets.QDialog, upload_success.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class UploadError(QtWidgets.QDialog, upload_error.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Change(QtWidgets.QDialog, change.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ChangeA61A(QtWidgets.QDialog, change_a61a.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class RecalculationWater(QtWidgets.QDialog, recalculation_water.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
