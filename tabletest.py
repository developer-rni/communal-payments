try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *

except:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *


import sqlite3


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Table')

        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)

    def fill(self):
        self.table_widget.clear()

        labels = ['Вода в текущем месяце', 'Вода в предыдущем месяце', 'Потрачено воды', 'Цена за 1', 'К оплате']

        self.table_widget.setColumnCount(len(labels))
        self.table_widget.setHorizontalHeaderLabels(labels)

        with sqlite3.connect('data/data_cp.db') as connect:
            for water_this_month, water_last_month, water_difference, water_unit_price, water_to_pay in connect.execute("SELECT water_this_month, water_last_month, water_difference, water_unit_price, water_to_pay FROM '2020_t13'"):
                row = self.table_widget.rowCount()
                self.table_widget.setRowCount(row + 1)

                self.table_widget.setItem(row, 0, QTableWidgetItem(str(water_this_month)))
                self.table_widget.setItem(row, 1, QTableWidgetItem(str(water_last_month)))
                self.table_widget.setItem(row, 2, QTableWidgetItem(str(water_difference)))
                self.table_widget.setItem(row, 3, QTableWidgetItem(str(water_unit_price)))
                self.table_widget.setItem(row, 4, QTableWidgetItem(str(water_to_pay)))


if __name__ == '__main__':
    app = QApplication([])

    w = Widget()
    w.show()
    w.fill()

    app.exec()