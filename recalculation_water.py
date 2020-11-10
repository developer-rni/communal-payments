# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cd_recalculation_water.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from water_recalc_error1 import Ui_Dialog_error1
from water_recalc_error2 import Ui_Dialog_error2
import sys, MainMenu

class Ui_Dialog(object):

    def OpenWindowError1(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_error1()
        self.ui.setupUi(self.window)
        self.window.show()
    def OpenWindowError2(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_error2()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 245)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 190, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 90, 341, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox.setMinimum(0.0)
        self.doubleSpinBox.setMaximum(10000.0)
        self.doubleSpinBox.setProperty("value", 1.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(90, 20, 101, 25))
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
        self.spinBox.setGeometry(QtCore.QRect(220, 20, 91, 26))
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
        Dialog.setWindowTitle(_translate("Dialog", "Перерасчет воды по счетчику"))
        self.label.setText(_translate("Dialog", "Введите показания счетчика"))
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
        month_addr = self.comboBox.currentText()
        year_addr = self.spinBox.value()
        water_recalc = self.doubleSpinBox.value()
        self.sqlite_update_db(month_addr, year_addr, water_recalc)
        self.close()
    
    def reject_data(self):
        self.close()

    def sqlite_update_db(self, month, year, water_rec):
        year_addr = str(year) + '_t13'
        year_addr_next = str(year + 1) + '_t13'

        payment_type1 = 'water_meter'
        payment_type2 = 'water_difference'
        payment_type3 = 'water_change_text'
        payment_type4 = 'water_to_pay'
        payment_type5 = 'water_unit_price'
        payment_type6 = 'total'

        if month == 'Январь':
            what_month = 'jan'
            what_month_next = 'feb'
        elif month == 'Февраль':
            what_month = 'feb'
            what_month_next = 'mar'
        elif month == 'Март':
            what_month = 'mar'
            what_month_next = 'apr'
        elif month == 'Апрель':
            what_month = 'apr'
            what_month_next = 'may'
        elif month == 'Май':
            what_month = 'may'
            what_month_next = 'jun'
        elif month == 'Июнь':
            what_month = 'jun'
            what_month_next = 'jul'
        elif month == 'Июль':
            what_month = 'jul'
            what_month_next = 'aug'
        elif month == 'Август':
            what_month = 'aug'
            what_month_next = 'sept'
        elif month == 'Сентябрь':
            what_month = 'sept'
            what_month_next = 'oct'
        elif month == 'Октябрь':
            what_month = 'oct'
            what_month_next = 'nov'
        elif month == 'Ноябрь':
            what_month = 'nov'
            what_month_next = 'dec'
        else:
            what_month = 'dec'
            what_month_next = 'jan'
        
        [real_water_meter], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type1, year_addr, what_month))

        if real_water_meter != None and real_water_meter != 0:

            if real_water_meter < water_rec:

                [difference_old], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type2, year_addr, what_month))

                difference_new = int(water_rec) - int(real_water_meter)
                difference_new = difference_new + difference_old
                MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type2, difference_new, what_month))

                MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type1, water_rec, what_month))

                if what_month != 'dec':
                    [difference_new_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type2, year_addr, what_month_next))
                    [water_to_pay_next_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type4, year_addr, what_month_next))
                    [total_next_month_old], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type6, year_addr, what_month_next))
                else:
                    [difference_new_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type2, year_addr_next, what_month_next))
                    [water_to_pay_next_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type4, year_addr_next, what_month_next))
                    [total_next_month_old], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type6, year_addr_next, what_month_next))

                if water_to_pay_next_month != None and water_to_pay_next_month != 0:
                    [water_unit_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type5, year_addr, what_month))
                    water_to_pay_new = difference_new * water_unit_price
                    water_meter_new_month = int(water_rec) + difference_new_month
                    total_next_month_new = (total_next_month_old - water_to_pay_next_month) + water_to_pay_new
                    if what_month != 'dec':
                        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type1, water_meter_new_month, what_month_next))
                        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type4, water_to_pay_new, what_month_next))
                        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type6, total_next_month_new, what_month_next))

                        # /запись в общий отчет двух таблиц/
                        # ---------------------------
                        year_addr_t13 = year_addr
                        year_addr_a61a = str(year) + '_a61a'
                        [result_t13], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type6, year_addr_t13, what_month_next))
                        [result_a61a], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type6, year_addr_a61a, what_month_next))
                        if result_t13 is None:
                            result_t13 = 0
                        if result_a61a is None:
                            result_a61a = 0
                        general_total_result = result_t13 + result_a61a
                        t_general_total_to_pay = 'general_total_to_pay'
                        t_general_month = what_month_next + '_general_total'
                        what_year = year
                        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE year="{}"'.format(t_general_total_to_pay, t_general_month, general_total_result, what_year))
                    else:
                        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr_next, payment_type1, water_meter_new_month, what_month_next))
                        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr_next, payment_type4, water_to_pay_new, what_month_next))
                        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr_next, payment_type6, total_next_month_new, what_month_next))

                        # /запись в общий отчет двух таблиц/
                        # ---------------------------
                        year_addr_t13 = year_addr
                        year_addr_a61a = str(year) + '_a61a'
                        [result_t13], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type6, year_addr_t13, what_month_next))
                        [result_a61a], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type6, year_addr_a61a, what_month_next))
                        if result_t13 is None:
                            result_t13 = 0
                        if result_a61a is None:
                            result_a61a = 0
                        general_total_result = result_t13 + result_a61a
                        t_general_total_to_pay = 'general_total_to_pay'
                        t_general_month = what_month_next + '_general_total'
                        what_year = year + 1
                        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE year="{}"'.format(t_general_total_to_pay, t_general_month, general_total_result, what_year))



                [water_change_text], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type3, year_addr, what_month))
                if water_change_text != None and water_change_text != ' *перерасчет':
                    water_change_text_new = water_change_text + ' *перерасчет'
                    MainMenu.cur.execute('UPDATE "{}" SET {} = "{}" WHERE month="{}"'.format(year_addr, payment_type3, water_change_text_new, what_month))
                elif water_change_text == None:
                    water_change_text_new = ' *перерасчет'
                    MainMenu.cur.execute('UPDATE "{}" SET {} = "{}" WHERE month="{}"'.format(year_addr, payment_type3, water_change_text_new, what_month))
                elif water_change_text == ' *перерасчет':
                    pass

            else:
                #pass # вывести ошибку что значение больше текущего
                self.OpenWindowError2()

        else:
            #pass # вывести ошибку что нужно сначало расчитать водоснабжение
            self.OpenWindowError1()

        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

