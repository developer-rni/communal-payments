# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cd_trash_a61a.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, MainMenu

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 341, 171))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox.setDecimals(2)
        self.doubleSpinBox.setMaximum(999.99)
        self.doubleSpinBox.setProperty("value", 0.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox.setMaximum(10)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.acept_data)
        self.buttonBox.rejected.connect(self.reject_data)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Расчет мусора Андреевская 61А"))
        self.label.setText(_translate("Dialog", "Цена за 1 человека"))
        self.label_2.setText(_translate("Dialog", "Кол-во человеков"))

    def acept_data(self):
        global trash_unit_price
        global trash_amount

        trash_unit_price = self.doubleSpinBox.value()
        trash_amount = self.spinBox.value()

        self.sqlite_update_db(trash_unit_price, trash_amount)
        self.close()
    def reject_data(self):
        self.close()

    def sqlite_update_db(self, nb1, nb2):

        year_addr = str(MainMenu.year_spin_a61a) + '_a61a'

        payment_type1 = 'trash_unit_price'
        payment_type2 = 'trash_amount'

        number1 = nb1
        number2 = nb2

        if MainMenu.month_combo_a61a == 'Январь':
            what_month = 'jan'
        elif MainMenu.month_combo_a61a == 'Февраль':
            what_month = 'feb'
        elif MainMenu.month_combo_a61a == 'Март':
            what_month = 'mar'
        elif MainMenu.month_combo_a61a == 'Апрель':
            what_month = 'apr'
        elif MainMenu.month_combo_a61a == 'Май':
            what_month = 'may'
        elif MainMenu.month_combo_a61a == 'Июнь':
            what_month = 'jun'
        elif MainMenu.month_combo_a61a == 'Июль':
            what_month = 'jul'
        elif MainMenu.month_combo_a61a == 'Август':
            what_month = 'aug'
        elif MainMenu.month_combo_a61a == 'Сентябрь':
            what_month = 'sept'
        elif MainMenu.month_combo_a61a == 'Октябрь':
            what_month = 'oct'
        elif MainMenu.month_combo_a61a == 'Ноябрь':
            what_month = 'nov'
        else:
            what_month = 'dec'

        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type1, number1, what_month))
        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type2, number2, what_month))

        trash_to_pay = number1 * number2
        payment_type3 = 'trash_to_pay'

        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type3, trash_to_pay, what_month))


        # /запись итого в данную таблицу/
        # --------------------------------

        payment_energy_pay = 'energy_to_pay'
        payment_gas_pay = 'gas_to_pay'
        payment_trash_pay = 'trash_to_pay'

        [energy_result], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_energy_pay, year_addr, what_month))
        [gas_result], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_gas_pay, year_addr, what_month))
        [trash_result], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_trash_pay, year_addr, what_month))

        spisok = [energy_result, gas_result, trash_result]

        i = 0
        for element in spisok:
            if element is None:
                spisok[i] = 0
            i += 1

        total_result = spisok[0] + spisok[1] + spisok[2]

        payment_total = 'total'

        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_total, total_result, what_month))



        # /запись в общий отчет двух таблиц/
        # ---------------------------

        year_addr_t13 = str(MainMenu.year_spin_a61a) + '_t13'
        year_addr_a61a = year_addr

        [result_t13], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_total, year_addr_t13, what_month))
        [result_a61a], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_total, year_addr_a61a, what_month))

        if result_t13 is None:
            result_t13 = 0
        if result_a61a is None:
            result_a61a = 0

        general_total_result = result_t13 + result_a61a

        t_general_total_to_pay = 'general_total_to_pay'
        t_general_month = what_month + '_general_total'
        what_year = MainMenu.year_spin_a61a
        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE year="{}"'.format(t_general_total_to_pay, t_general_month, general_total_result, what_year))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

