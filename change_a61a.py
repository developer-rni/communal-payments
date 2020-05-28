# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cd_change_a61a.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, MainMenu

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(634, 242)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(280, 190, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(140, 20, 101, 25))
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
        self.spinBox.setGeometry(QtCore.QRect(40, 20, 91, 26))
        self.spinBox.setPrefix("")
        self.spinBox.setMinimum(2020)
        self.spinBox.setMaximum(2030)
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(440, 20, 90, 17))
        self.label_4.setObjectName("label_4")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 50, 581, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox.setMinimum(-9999.99)
        self.doubleSpinBox.setMaximum(9999.99)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_2.setMinimum(-9999.99)
        self.doubleSpinBox_2.setMaximum(9999.99)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_3.setMinimum(-9999.99)
        self.doubleSpinBox_3.setMaximum(9999.99)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout.addWidget(self.doubleSpinBox_3, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.acept_data)
        self.buttonBox.rejected.connect(self.reject_data)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Изменение показаний по видам платежей Андреевская 61А"))
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
        self.label_4.setText(_translate("Dialog", "Примечание"))
        self.label_3.setText(_translate("Dialog", "Изменение масора"))
        self.label.setText(_translate("Dialog", "Изменение электроэнергии"))
        self.label_2.setText(_translate("Dialog", "Изменение газоснабжения"))

    def acept_data(self):
        global energy_change
        global energy_change_text
        global gas_change
        global gas_change_text
        global trash_change
        global trash_change_text

        global year_change
        global month_change

        energy_change = self.doubleSpinBox.value()
        energy_change_text = self.lineEdit.text()
        gas_change = self.doubleSpinBox_2.value()
        gas_change_text = self.lineEdit_2.text()
        trash_change = self.doubleSpinBox_3.value()
        trash_change_text = self.lineEdit_3.text()

        year_change = self.spinBox.value()
        month_change = self.comboBox.currentText()

        self.sqlite_update_db_change(energy_change, energy_change_text, gas_change, gas_change_text, trash_change, trash_change_text, year_change, month_change)

        self.close()

    def reject_data(self):
        self.close()

    def sqlite_update_db_change(self, nb1, tx1, nb2, tx2, nb3, tx3, year, month):
        year_addr_change = str(year) + '_a61a'

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
        
        #print ("nb1 = " + str(nb1), "tx1 = " + str(tx1), "nb2 = " + str(nb2), "tx2 = " + str(tx2), "nb3 = " + str(nb3), "tx3 = " + str(tx3), year_addr_change, month_change)
        
        cloumn_name_1 = 'energy_change'
        cloumn_name_2 = 'energy_change_text'
        cloumn_name_3 = 'gas_change'
        cloumn_name_4 = 'gas_change_text'
        cloumn_name_5 = 'trash_change'
        cloumn_name_6 = 'trash_change_text'

        cloumn_name_total = 'total'

        [energy_change_slots], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(cloumn_name_1, year_addr_change, what_month_change))
        [gas_change_slots], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(cloumn_name_3, year_addr_change, what_month_change))
        [trash_change_slots], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(cloumn_name_5, year_addr_change, what_month_change))

        [total], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(cloumn_name_total, year_addr_change, what_month_change))

        if energy_change_slots is None:
            MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr_change, cloumn_name_1, nb1, what_month_change))
            total = total + nb1
        else:
            if nb1 > energy_change_slots:
                energy_change_difference = nb1 - energy_change_slots
                total = total + energy_change_difference
                MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr_change, cloumn_name_1, nb1, what_month_change))
            elif nb1 < energy_change_slots:
                energy_change_difference = energy_change_slots - nb1
                total = total - energy_change_difference
                MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr_change, cloumn_name_1, nb1, what_month_change))
            else:
                pass

        if tx1:
            MainMenu.cur.execute('UPDATE "{}" SET {} = "{}" WHERE month="{}"'.format(year_addr_change, cloumn_name_2, tx1, what_month_change))

        if gas_change_slots is None:
            MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr_change, cloumn_name_3, nb2, what_month_change))
            total = total + nb2
        else:
            if nb2 > gas_change_slots:
                gas_change_difference = nb2 - gas_change_slots
                total = total + gas_change_difference
                MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr_change, cloumn_name_3, nb2, what_month_change))
            elif nb2 < gas_change_slots:
                gas_change_difference = gas_change_slots - nb2
                total = total - gas_change_difference
                MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr_change, cloumn_name_3, nb2, what_month_change))
            else:
                pass
        
        if tx2:
            MainMenu.cur.execute('UPDATE "{}" SET {} = "{}" WHERE month="{}"'.format(year_addr_change, cloumn_name_4, tx2, what_month_change))

        if trash_change_slots is None:
            MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr_change, cloumn_name_5, nb3, what_month_change))
            total = total + nb3
        else:
            if nb3 > trash_change_slots:
                trash_change_difference = nb3 - trash_change_slots
                total = total + trash_change_difference
                MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr_change, cloumn_name_5, nb3, what_month_change))
            elif nb3 < trash_change_slots:
                trash_change_difference = trash_change_slots - nb3
                total = total - trash_change_difference
                MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr_change, cloumn_name_5, nb3, what_month_change))
            else:
                pass

        if tx3:
            MainMenu.cur.execute('UPDATE "{}" SET {} = "{}" WHERE month="{}"'.format(year_addr_change, cloumn_name_6, tx3, what_month_change))


        MainMenu.cur.execute('UPDATE "{}" SET {} = "{}" WHERE month="{}"'.format(year_addr_change, cloumn_name_total, total, what_month_change))

        # /запись в общий отчет двух таблиц/
        # ---------------------------

        year_addr_change_t13 = year_addr_change
        year_addr_change_a61a = str(year) + '_a61a'

        [result_total_change_t13], = MainMenu.cur.execute('SELECT total FROM "{}" WHERE month="{}"'.format(year_addr_change_t13, what_month_change))
        [result_total_change_a61a], = MainMenu.cur.execute('SELECT total FROM "{}" WHERE month="{}"'.format(year_addr_change_a61a, what_month_change))

        if result_total_change_t13 is None:
            result_total_change_t13 = 0
        if result_total_change_a61a is None:
            result_total_change_a61a = 0

        general_total_result_change = result_total_change_t13 + result_total_change_a61a

        t_general_total_to_pay = 'general_total_to_pay'
        t_general_month = what_month_change + '_general_total'
        what_year_generaltotal_change = year
        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE year="{}"'.format(t_general_total_to_pay, t_general_month, general_total_result_change, what_year_generaltotal_change))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())