# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cd_change.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, MainMenu

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(628, 290)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 230, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 581, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_5.setMinimum(-9999.99)
        self.doubleSpinBox_5.setMaximum(9999.99)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout.addWidget(self.doubleSpinBox_5, 4, 1, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_2.setMinimum(-9999.99)
        self.doubleSpinBox_2.setMaximum(9999.99)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 1, 1, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_4.setMinimum(-9999.99)
        self.doubleSpinBox_4.setMaximum(9999.99)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout.addWidget(self.doubleSpinBox_4, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox.setDecimals(2)
        self.doubleSpinBox.setMinimum(-9999.99)
        self.doubleSpinBox.setMaximum(9999.99)
        self.doubleSpinBox.setProperty("value", 0.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 0, 1, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_3.setMinimum(-9999.99)
        self.doubleSpinBox_3.setMaximum(9999.99)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout.addWidget(self.doubleSpinBox_3, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 2, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(410, 10, 90, 17))
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(110, 10, 101, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(10, 10, 91, 26))
        self.spinBox.setPrefix("")
        self.spinBox.setMinimum(2020)
        self.spinBox.setMaximum(2030)
        self.spinBox.setObjectName("spinBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.acept_data)
        self.buttonBox.rejected.connect(self.reject_data)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Изменение показаний по видам платежей Толстого 13"))
        self.label_4.setText(_translate("Dialog", "Изменение масора"))
        self.label_3.setText(_translate("Dialog", "Изменение газоснабжения"))
        self.label_5.setText(_translate("Dialog", "Изменение интернета"))
        self.label_2.setText(_translate("Dialog", "Изменение электроэнергии"))
        self.label.setText(_translate("Dialog", "Изменение воды"))
        self.label_6.setText(_translate("Dialog", "Примечание"))
        self.comboBox.setItemText(0, _translate("Dialog", "Январь"))
        self.comboBox.setItemText(1, _translate("Dialog", "Февраль"))
        self.comboBox.setItemText(2, _translate("Dialog", "Март"))
        self.comboBox.setItemText(3, _translate("Dialog", "Апрель"))
        self.comboBox.setItemText(4, _translate("Dialog", "Май"))
        self.comboBox.setItemText(5, _translate("Dialog", "Июнь"))
        self.comboBox.setItemText(6, _translate("Dialog", "Июль"))
        self.comboBox.setItemText(7, _translate("Dialog", "Август"))
        self.comboBox.setItemText(8, _translate("Dialog", "Сентябрь"))
        self.comboBox.setItemText(9, _translate("Dialog", "Октябрь"))
        self.comboBox.setItemText(10, _translate("Dialog", "Ноябрь"))
        self.comboBox.setItemText(11, _translate("Dialog", "Декабрь"))
        self.spinBox.setSuffix(_translate("Dialog", " год"))
    
    def acept_data(self):
        global water_change
        global water_change_text
        global energy_change
        global energy_change_text
        global gas_change
        global gas_change_text
        global trash_change
        global trash_change_text
        global internet_change
        global internet_change_text

        global year_change
        global month_change

        water_change = self.doubleSpinBox.value()
        water_change_text = self.lineEdit.text()
        energy_change = self.doubleSpinBox_2.value()
        energy_change_text = self.lineEdit_2.text()
        gas_change = self.doubleSpinBox_3.value()
        gas_change_text = self.lineEdit_3.text()
        trash_change = self.doubleSpinBox_4.value()
        trash_change_text = self.lineEdit_4.text()
        internet_change = self.doubleSpinBox_5.value()
        internet_change_text = self.lineEdit_5.text()

        year_change = self.spinBox.value()
        month_change = self.comboBox.currentText()

        self.sqlite_update_db_change(water_change, water_change_text, energy_change, energy_change_text, gas_change, gas_change_text, trash_change, trash_change_text, internet_change, internet_change_text, year_change, month_change)

        self.close()

    def reject_data(self):
        self.close()

    def sqlite_update_db_change(self, nb1, tx1, nb2, tx2, nb3, tx3, nb4, tx4, nb5, tx5, year, month):
        year_addr_change = str(year) + '_t13'

        if month == 'Январь':
            what_month_change = 'jan'
        elif month == 'Февраль':
            what_month_change = 'feb'
        elif month == 'Март':
            what_month_change = 'mar'
        elif month == 'Апрель':
            what_month_change = 'apr'
        elif month == 'Май':
            what_month_change = 'may'
        elif month == 'Июнь':
            what_month_change = 'jun'
        elif month == 'Июль':
            what_month_change = 'jul'
        elif month == 'Август':
            what_month_change = 'aug'
        elif month == 'Сентябрь':
            what_month_change = 'sept'
        elif month == 'Октябрь':
            what_month_change = 'oct'
        elif month == 'Ноябрь':
            what_month_change = 'nov'
        else:
            what_month_change = 'dec'
        
        print ("nb1 = " + str(nb1), "tx1 = " + str(tx1), "nb2 = " + str(nb2), "tx2 = " + str(tx2), "nb3 = " + str(nb3), "tx3 = " + str(tx3), "nb4 = " + str(nb4), "tx4 = " + str(tx4), "nb5 = " + str(nb5), "tx5 = " + str(tx5), year_addr_change, month_change)
        
        cloumn_name_1 = 'water_change'
        cloumn_name_2 = 'water_change_text'
        cloumn_name_3 = 'energy_change'
        cloumn_name_4 = 'energy_change_text'
        cloumn_name_5 = 'gas_change'
        cloumn_name_6 = 'gas_change_text'
        cloumn_name_7 = 'trash_change'
        cloumn_name_8 = 'trash_change_text'
        cloumn_name_9 = 'internet_change'
        cloumn_name_10 = 'internet_change_text'

  #      if not tx1:
  #          tx1 = NULL
  #      if tx2 == '':
  #          tx2 = NULL
  #      if tx3 == '':
  #          tx3 = NULL
  #      if tx4 == '':
  #          tx4 = NULL
  #      if tx5 == '':
  #          tx5 = NULL

        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr_change, cloumn_name_1, nb1, what_month_change))
        if tx1:
            MainMenu.cur.execute('UPDATE "{}" SET {} = "{}" WHERE month="{}"'.format(year_addr_change, cloumn_name_2, tx1, what_month_change))
        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr_change, cloumn_name_3, nb2, what_month_change))
        if tx2:
            MainMenu.cur.execute('UPDATE "{}" SET {} = "{}" WHERE month="{}"'.format(year_addr_change, cloumn_name_4, tx2, what_month_change))
        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr_change, cloumn_name_5, nb3, what_month_change))
        if tx3:
            MainMenu.cur.execute('UPDATE "{}" SET {} = "{}" WHERE month="{}"'.format(year_addr_change, cloumn_name_6, tx3, what_month_change))
        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr_change, cloumn_name_7, nb4, what_month_change))
        if tx4:
            MainMenu.cur.execute('UPDATE "{}" SET {} = "{}" WHERE month="{}"'.format(year_addr_change, cloumn_name_8, tx4, what_month_change))
        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr_change, cloumn_name_9, nb5, what_month_change))
        if tx5:
            MainMenu.cur.execute('UPDATE "{}" SET {} = "{}" WHERE month="{}"'.format(year_addr_change, cloumn_name_10, tx5, what_month_change))
        #UPDATE "2020_a61a" SET 'gas_vdgo' = 50.5 WHERE month="jun"

        [total_result_old], = MainMenu.cur.execute('SELECT total FROM "{}" WHERE month="{}"'.format(year_addr_change, what_month_change))

        print (total_result_old)

        total_result_change = nb1 + nb2 + nb3 + nb4 + nb5 + total_result_old
        MainMenu.cur.execute('UPDATE "{}" SET total = "{}" WHERE month="{}"'.format(year_addr_change, total_result_change, what_month_change))

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())