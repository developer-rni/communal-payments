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

        payment_type1 = 'water_meter'
        payment_type2 = 'water_difference'
        payment_type3 = 'water_change_text'

        if month == 'Январь':
            what_month = 'jan'
        elif month == 'Февраль':
            what_month = 'feb'
        elif month == 'Март':
            what_month = 'mar'
        elif month == 'Апрель':
            what_month = 'apr'
        elif month == 'Май':
            what_month = 'may'
        elif month == 'Июнь':
            what_month = 'jun'
        elif month == 'Июль':
            what_month = 'jul'
        elif month == 'Август':
            what_month = 'aug'
        elif month == 'Сентябрь':
            what_month = 'sept'
        elif month == 'Октябрь':
            what_month = 'oct'
        elif month == 'Ноябрь':
            what_month = 'nov'
        else:
            what_month = 'dec'
        
        [real_water_meter], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type1, year_addr, what_month))


        if real_water_meter != None and real_water_meter != 0:

            if real_water_meter < water_rec:

                [difference_old], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format(payment_type2, year_addr, what_month))

                difference_new = int(water_rec) - int(real_water_meter)
                difference_new = difference_new + difference_old
                MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type2, difference_new, what_month))

                MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type1, water_rec, what_month))

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

