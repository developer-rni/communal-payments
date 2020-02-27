from PyQt5 import QtWidgets, QtCore
import MainMenu

class upd_table_cl(object):
    def table_extract_t13(self):

        #water
        [water_this_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_this_month', '2020_t13', 'jan'))
        [water_last_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_last_month', '2020_t13', 'jan'))
        [water_difference], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_difference', '2020_t13', 'jan'))
        [water_unit_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_unit_price', '2020_t13', 'jan'))
        [water_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_to_pay', '2020_t13', 'jan'))
        global wtm
        global wlm
        global wd
        global wup
        global wtp
        wtm = water_this_month
        wlm = water_last_month
        wd = water_difference
        wup = water_unit_price
        wtp = water_to_pay

        #energy
        [energy_this_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_this_month', '2020_t13', 'jan'))
        [energy_last_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_last_month', '2020_t13', 'jan'))
        [energy_difference], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_difference', '2020_t13', 'jan'))
        [energy_unit_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_unit_price', '2020_t13', 'jan'))
        [energy_price_per_norm], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_price_per_norm', '2020_t13', 'jan'))
        [energy_excess_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_excess_price', '2020_t13', 'jan'))
        [energy_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_to_pay', '2020_t13', 'jan'))
        global etm
        global elm
        global ed
        global eup
        global eppn
        global eep
        global etp
        etm = energy_this_month
        elm = energy_last_month
        ed = energy_difference
        eup = energy_unit_price
        eppn = energy_price_per_norm
        eep = energy_excess_price
        etp = energy_to_pay

        #gas
        [gas_this_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_this_month', '2020_t13', 'jan'))
        [gas_last_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_last_month', '2020_t13', 'jan'))
        [gas_difference], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_difference', '2020_t13', 'jan'))
        [gas_unit_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_unit_price', '2020_t13', 'jan'))
        [gas_coefficient], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_coefficient', '2020_t13', 'jan'))
        [gas_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_to_pay', '2020_t13', 'jan'))
        global gtm
        global glm
        global gd
        global gup
        global gc
        global gtp
        gtm = gas_this_month
        glm = gas_last_month
        gd = gas_difference
        gup = gas_unit_price
        gc = gas_coefficient
        gtp = gas_to_pay

        #trash
        [trash_unit_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('trash_unit_price', '2020_t13', 'jan'))
        [trash_amount], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('trash_amount', '2020_t13', 'jan'))
        [trash_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('trash_to_pay', '2020_t13', 'jan'))
        global tup
        global ta
        global ttp
        tup = trash_unit_price
        ta = trash_amount
        ttp = round(trash_to_pay, 2)

        #internet
        [internet_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('internet_price', '2020_t13', 'jan'))
        [internet_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('internet_to_pay', '2020_t13', 'jan'))
        global internet_p
        global itp
        internet_p = internet_price
        itp = internet_to_pay

        #phone
        [phone_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('phone_price', '2020_t13', 'jan'))
        [phone_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('phone_to_pay', '2020_t13', 'jan'))
        global phone_p
        global phone_tp
        phone_p = phone_price
        phone_tp = phone_to_pay

        #total
        [total_t13], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('total', '2020_t13', 'jan'))
        global total
        total = total_t13

    def table_extract_a61a(self):
        pass

    def upd_t_t13(self):
        upd_table_cl.table_extract_t13(self)

        #Вода
        item = QtWidgets.QTableWidgetItem(str(wtm))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem(str(wlm))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem(str(wd))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem(str(wup))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem(str(wtp))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(6, 0, item)

        #Свет
        item = QtWidgets.QTableWidgetItem(str(etm))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem(str(elm))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem(str(ed))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem(str(eup))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem(str(eppn))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem(str(eep))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem(str(etp))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(6, 1, item)

        #Газ
        item = QtWidgets.QTableWidgetItem(str(gtm))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem(str(glm))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem(str(gd))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem(str(gup))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem(str(gc))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem(str(gtp))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(6, 2, item)

        #Мусор
        item = QtWidgets.QTableWidgetItem(str(tup))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem(str(ta))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem(str(ttp))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(6, 3, item)

        #Интернет
        item = QtWidgets.QTableWidgetItem(str(internet_p))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem(str(itp))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(6, 4, item)

        #Телефон
        item = QtWidgets.QTableWidgetItem(str(phone_p))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem(str(phone_tp))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(6, 5, item)

        #Итого
        self.tableWidget_2020_jan.setSpan(7, 0, 1, 6) #объединение ячеек итого
        item = QtWidgets.QTableWidgetItem(str(total))
        item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.tableWidget_2020_jan.setItem(7, 0, item)

    def upd_t_a61a(self):
        upd_table_cl.table_extract_a61a(self)