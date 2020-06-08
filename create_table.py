from PyQt5 import QtWidgets, QtCore
import MainMenu

class create_table_cl(object):

    def create_table_t13(self):
        year = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
        month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
        cloumn_c = 6
        row_c = 8

        for _year in year:
          for _month in month:
            exec('self.tab_%d = QtWidgets.QWidget()' % (_year))
            exec('self.tab_%d.setObjectName("tab_%d")' % (_year, _year))
            exec('self.tabWidget_%d_year = QtWidgets.QTabWidget(self.tab_%d)' % (_year, _year))
            exec('self.tabWidget_%d_year.setGeometry(QtCore.QRect(40, 40, 900, 300))' % (_year))
            exec('self.tabWidget_%d_year.setObjectName("tabWidget_%d_year")' % (_year, _year))
            exec('self.tab_%d_%s = QtWidgets.QWidget()' % (_year, _month))
            exec('self.tab_%d_%s.setObjectName("tab_%d_%s")' % (_year, _month, _year, _month))
            exec('self.tableWidget_%d_%s = QtWidgets.QTableWidget(self.tab_%d_%s)' % (_year, _month, _year, _month))
            exec('self.tableWidget_%d_%s.setGeometry(QtCore.QRect(0, 0, 900, 270))' % (_year, _month))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            exec('sizePolicy.setHeightForWidth(self.tableWidget_%d_%s.sizePolicy().hasHeightForWidth())' % (_year, _month))
            exec('self.tableWidget_%d_%s.setSizePolicy(sizePolicy)' % (_year, _month))
            exec('self.tableWidget_%d_%s.setMinimumSize(QtCore.QSize(100, 0))' % (_year, _month))
            exec('self.tableWidget_%d_%s.setObjectName("tableWidget_%d_%s")' % (_year, _month, _year, _month))
            exec('self.tableWidget_%d_%s.setColumnCount(%d)' % (_year, _month, cloumn_c))
            exec('self.tableWidget_%d_%s.setRowCount(%d)' % (_year, _month, row_c))
            for _row in range(0, row_c):
              item = QtWidgets.QTableWidgetItem()
              exec('self.tableWidget_%d_%s.setVerticalHeaderItem(%d, item)' % (_year, _month, _row))
            for _cloumn in range(0, cloumn_c):
              item = QtWidgets.QTableWidgetItem()
              exec('self.tableWidget_%d_%s.setHorizontalHeaderItem(%d, item)' % (_year, _month, _cloumn))
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(11)
            item.setFont(font)
            exec('self.tableWidget_%d_%s.setItem(0, 0, item)' % (_year, _month))
            exec('self.tabWidget_%d_year.addTab(self.tab_%d_%s, "")' % (_year, _year, _month))
          exec('self.label_%d = QtWidgets.QLabel(self.tab_%d)' % (_year, _year))
          exec('self.label_%d.setGeometry(QtCore.QRect(470, 5, 67, 31))' % (_year))
          exec('self.label_%d.setObjectName("label_%d")' % (_year, _year))
          exec('self.tabWidget.addTab(self.tab_%d, "")' % (_year))
    