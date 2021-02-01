# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import MainMenu


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
        self.doubleSpinBox.setMaximum(9999.99)
        self.doubleSpinBox.setProperty("value", 0.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.acept_data)
        self.buttonBox.rejected.connect(self.reject_data)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Расчет мусора Толстого 13"))
        self.label.setText(_translate("Dialog", "Цена за месяц"))

    def acept_data(self):
        global trash_price

        trash_price = self.doubleSpinBox.value()

        self.sqlite_update_db(trash_price)
        self.close()

    def reject_data(self):
        self.close()

    def sqlite_update_db(self, nb1):

        year_addr = str(MainMenu.year_spin_t13) + '_t13'

        payment_type1 = 'trash_price'
        payment_type2 = 'trash_to_pay'

        number1 = nb1

        if MainMenu.month_combo_t13 == 'Январь':
            what_month = 'jan'
        elif MainMenu.month_combo_t13 == 'Февраль':
            what_month = 'feb'
        elif MainMenu.month_combo_t13 == 'Март':
            what_month = 'mar'
        elif MainMenu.month_combo_t13 == 'Апрель':
            what_month = 'apr'
        elif MainMenu.month_combo_t13 == 'Май':
            what_month = 'may'
        elif MainMenu.month_combo_t13 == 'Июнь':
            what_month = 'jun'
        elif MainMenu.month_combo_t13 == 'Июль':
            what_month = 'jul'
        elif MainMenu.month_combo_t13 == 'Август':
            what_month = 'aug'
        elif MainMenu.month_combo_t13 == 'Сентябрь':
            what_month = 'sept'
        elif MainMenu.month_combo_t13 == 'Октябрь':
            what_month = 'oct'
        elif MainMenu.month_combo_t13 == 'Ноябрь':
            what_month = 'nov'
        else:
            what_month = 'dec'

        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type1, number1, what_month))
        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type2, number1, what_month))

        # /запись итого в данную таблицу/
        # ---------------------------

        payment_water_pay = 'water_to_pay'
        payment_energy_pay = 'energy_to_pay'
        payment_gas_pay = 'gas_to_pay'
        payment_trash_pay = 'trash_to_pay'
        payment_internet_pay = 'internet_to_pay'
        payment_phone_to_pay = 'phone_to_pay'
        [water_result], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_water_pay, year_addr, what_month))
        [energy_result], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_energy_pay, year_addr, what_month))
        [gas_result], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_gas_pay, year_addr, what_month))
        [trash_result], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_trash_pay, year_addr, what_month))
        [internet_result], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_internet_pay, year_addr, what_month))
        [phone_result], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_phone_to_pay, year_addr, what_month))

        spisok = [water_result, energy_result, gas_result, trash_result, internet_result, phone_result]

        i = 0
        for element in spisok:
            if element is None:
                spisok[i] = 0
            i += 1

        total_result = round(sum(spisok), 2)

        payment_total = 'total'
        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_total, total_result, what_month))

        # /запись в общий отчет двух таблиц/
        # ---------------------------

        year_addr_t13 = year_addr
        year_addr_a61a = str(MainMenu.year_spin_t13) + '_a61a'

        [result_t13], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_total, year_addr_t13, what_month))
        [result_a61a], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_total, year_addr_a61a, what_month))

        if result_t13 is None:
            result_t13 = 0
        if result_a61a is None:
            result_a61a = 0

        general_total_result = result_t13 + result_a61a

        t_general_total_to_pay = 'general_total_to_pay'
        t_general_month = what_month + '_general_total'
        what_year = MainMenu.year_spin_t13
        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE year="{}"'.format(t_general_total_to_pay, t_general_month, general_total_result, what_year))
