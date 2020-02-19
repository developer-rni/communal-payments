# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cd_ElectricalEnegry_a61a.ui'
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
        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox.setMaximum(99999)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.acept_data)
        self.buttonBox.rejected.connect(self.reject_data)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Расчет электроэнергии Андреевская 61А"))
        self.label.setText(_translate("Dialog", "Сумма к оплате"))

    def acept_data(self):
        global energy_unit_price

        energy_unit_price = self.spinBox.value()

        self.sqlite_update_db(energy_unit_price)
        self.close()
    def reject_data(self):
        self.close()

    def sqlite_update_db(self, nb1):

        year_addr = str(MainMenu.year_spin_a61a) + '_a61a'

        payment_type1 = 'energy_unit_price'

        number1 = nb1

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

