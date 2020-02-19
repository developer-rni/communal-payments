# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cd_phone.ui'
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
        self.doubleSpinBox.setMaximum(9999.99)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.acept_data)
        self.buttonBox.rejected.connect(self.reject_data)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Расчет телефона Толстого 13"))
        self.label.setText(_translate("Dialog", "Цена за месяц"))

    def acept_data(self):
        global phone_price

        phone_price = self.doubleSpinBox.value()

        self.sqlite_update_db(phone_price)
        self.close()
    def reject_data(self):
        self.close()

    def sqlite_update_db(self, nb1):

        year_addr = str(MainMenu.year_spin_t13) + '_t13'

        payment_type1 = 'phone_price'

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

