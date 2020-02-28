# communal_payments Rybkin Nikita Igorevich
# v 0.7

import sys, MainMenu, save, exitM
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QGridLayout, QLabel, QApplication

#Сделать формулы и заполнить бпустые ячейки в БД

# MainMenu.month_combo_t13 #глобальная переменная с месяцем платежа Толстого 13
# MainMenu.month_combo_a61a #глобальная переменная с месяцем платежа Андреевская 61А
# MainMenu.year_spin_t13 #глобальная переменная с годом платежа Толстого 13
# MainMenu.year_spin_a61a #глобальная переменная с годом платежа Андреевская 61А


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


    def InitUI(self):
        self.action_save.triggered.connect(self.show_save_db)  # Вывести окно и сохранить данные в бд при нажатии Файл -> сохронить
        # self.action_download_GD.triggered.connect(self.)  # Закрыть программу при нажатии Файл -> Залить в облако (google drive)
        self.action_exit.triggered.connect(self.show_exitM)  # Закрыть программу при нажатии Файл -> Выход
        self.action_t13_calculate.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(1))  # Открыть окно "что платим" при нажатии на Толстого13 -> Рассчитать
        self.action_t13_report.triggered.connect(self.show_report_t13)  # Открыть таблицу отчет при нажатии на Толстого13 -> Отчет
        self.action_a61a_calculate.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(2))  # Открыть окно "что платим" при нажатии на Андреевская61 -> Рассчитать
        self.action_a61a_report.triggered.connect(self.show_report_a61a)  # Открыть таблицу отчет при нажатии на Андреевская61 -> Отчет
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


class save(QtWidgets.QDialog, save.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

class exitM(QtWidgets.QDialog, exitM.Ui_Dialog):
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

