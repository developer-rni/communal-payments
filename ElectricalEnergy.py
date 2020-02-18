# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cd_ElectricalEnergy.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import MainMenu, sqlite3

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(404, 290)
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
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox.setMaximum(99999)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.spinBox_2 = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox_2.setMaximum(999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.acept_data)
        self.buttonBox.rejected.connect(self.reject_data)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Расчет электроэнергии"))
        self.label.setText(_translate("Dialog", "Показания на этот месяц"))
        self.label_2.setText(_translate("Dialog", "Норма в этом месяце"))
        self.label_3.setText(_translate("Dialog", "Цена за поподание в норму"))
        self.label_4.setText(_translate("Dialog", "Цена за сверхнорму"))

    def acept_data(self):
        global energy_this_month
        global energy_unit_price
        global energy_price_per_norm
        global energy_excess_prise
        energy_this_month = self.spinBox.value()
        energy_unit_price = self.spinBox_2.value()
        energy_price_per_norm = self.doubleSpinBox.value()
        energy_excess_prise = self.doubleSpinBox_2.value()
        self.sqlite_update_db(energy_this_month, energy_unit_price, energy_price_per_norm, energy_excess_prise)
        self.close()
    def reject_data(self):
        self.close()

    def sqlite_update_db(self, nb1, nb2, nb3, nb4):

        year_addr = str(MainMenu.year_spin_t13) + '_t13'

        payment_type1 = 'energy_this_month'
        payment_type2 = 'energy_unit_price'
        payment_type3 = 'energy_price_per_norm'
        payment_type4 = 'energy_excess_price'

        number1 = nb1
        number2 = nb2
        number3 = nb3
        number4 = nb4

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
        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type2, number2, what_month))
        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type3, number3, what_month))
        MainMenu.cur.execute('UPDATE "{}" SET {} = {} WHERE month="{}"'.format(year_addr, payment_type4, number4, what_month))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

