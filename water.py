# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import MainMenu


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 291)
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
        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox.setMaximum(99999)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.acept_data)
        self.buttonBox.rejected.connect(self.reject_data)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Расчет водоснабжения Толстого 13"))
        self.label.setText(_translate("Dialog", "Показания на этот месяц"))
        self.label_2.setText(_translate("Dialog", "Цена за водоснабжение"))
        self.label_3.setText(_translate("Dialog", "Цена за водоотведение"))

    def acept_data(self):
        global water_this_month
        global water_unit_price

        water_this_month = self.spinBox.value()
        water_supply = self.doubleSpinBox.value()
        water_drain = self.doubleSpinBox_2.value()

        water_unit_price = round((float(water_supply) + float(water_drain)), 2)

        self.sqlite_update_db(water_this_month, water_unit_price)
        self.close()

    def reject_data(self):
        self.close()

    def sqlite_update_db(self, nb1, nb2):

        year_addr = str(MainMenu.year_spin_t13) + '_t13'

        payment_type1 = 'water_this_month'
        payment_type2 = 'water_unit_price'

        number1 = nb1
        number2 = nb2

        if MainMenu.month_combo_t13 == 'Январь':
            what_month = 'jan'
            what_month_old = 'dec'
        elif MainMenu.month_combo_t13 == 'Февраль':
            what_month = 'feb'
            what_month_old = 'jan'
        elif MainMenu.month_combo_t13 == 'Март':
            what_month = 'mar'
            what_month_old = 'feb'
        elif MainMenu.month_combo_t13 == 'Апрель':
            what_month = 'apr'
            what_month_old = 'mar'
        elif MainMenu.month_combo_t13 == 'Май':
            what_month = 'may'
            what_month_old = 'apr'
        elif MainMenu.month_combo_t13 == 'Июнь':
            what_month = 'jun'
            what_month_old = 'may'
        elif MainMenu.month_combo_t13 == 'Июль':
            what_month = 'jul'
            what_month_old = 'jun'
        elif MainMenu.month_combo_t13 == 'Август':
            what_month = 'aug'
            what_month_old = 'jul'
        elif MainMenu.month_combo_t13 == 'Сентябрь':
            what_month = 'sept'
            what_month_old = 'aug'
        elif MainMenu.month_combo_t13 == 'Октябрь':
            what_month = 'oct'
            what_month_old = 'sept'
        elif MainMenu.month_combo_t13 == 'Ноябрь':
            what_month = 'nov'
            what_month_old = 'oct'
        else:
            what_month = 'dec'
            what_month_old = 'nov'

        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type1, number1, what_month))
        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type2, number2, what_month))

        year_addr_prev = MainMenu.year_spin_t13 - 1
        year_addr_previous = str(year_addr_prev) + '_t13'

        if what_month == 'jan':
            year_addr_old = year_addr_previous
        else:
            year_addr_old = year_addr

        payment_type_old = 'water_this_month'

        payment_type3 = 'water_last_month'

        [water_last_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type_old, year_addr_old, what_month_old))
        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type3, water_last_month, what_month))

        water_difference = water_this_month - water_last_month
        payment_type4 = 'water_difference'
        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type4, water_difference, what_month))

        payment_type_old2 = 'water_difference'
        payment_type_old3 = 'water_unit_price'

        [water_difference_old], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type_old2, year_addr_old, what_month_old))
        [water_unit_price_old], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type_old3, year_addr_old, what_month_old))
        # water_unit_price_old = water_unit_price_old.replace(',', '.')
        water_to_pay = round((float(water_difference_old) * float(water_unit_price_old)), 2)

        payment_type5 = 'water_to_pay'

        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type5, water_to_pay, what_month))

        payment_type6 = 'water_meter'
        [water_meter_old], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type6, year_addr_old, what_month_old))
        water_meter_new = water_meter_old + water_difference
        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type6, water_meter_new, what_month))

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
