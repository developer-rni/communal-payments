# communal-payments Rybkin Nikita Igorevich

import sys, Main, ElectricalEnergy, TypesOfPayments
from PyQt5 import QtWidgets

class ExampleApp(QtWidgets.QMainWindow, Main.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле Main.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        #------
        self.action_5.triggered.connect(self.close)  # Закрыть программу при нажатии толстого13->Выход
        #self.action.triggered.connect(TypesOfPayments.Ui_Form)  # Закрыть программу при нажатии толстого13->Выход






def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()