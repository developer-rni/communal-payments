from PyQt5 import QtWidgets, QtCore
import MainMenu

class upd_table_cl(object):

    def upd_t_t13(self):
        year = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
        month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
        for _year in year:
            for _month in month:
                _year_ = str(_year) + '_t13'
                # water
                [water_meter], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_meter', _year_, _month))
                [water_this_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_this_month', _year_, _month))
                [water_last_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_last_month', _year_, _month))
                [water_difference], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_difference', _year_, _month))
                [water_unit_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_unit_price', _year_, _month))
                [water_change], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_change', _year_, _month))
                [water_change_text], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_change_text', _year_, _month))
                [water_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_to_pay', _year_, _month))
                wm = water_meter
                wtm = water_this_month
                wlm = water_last_month
                wd = water_difference
                wup = water_unit_price
                wch = water_change
                wcht = water_change_text
                wtp = water_to_pay
        
                # energy
                [energy_this_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_this_month', _year_, _month))
                [energy_last_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_last_month', _year_, _month))
                [energy_difference], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_difference', _year_, _month))
                [energy_unit_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_unit_price', _year_, _month))
                [energy_price_per_norm], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_price_per_norm', _year_, _month))
                [energy_excess_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_excess_price', _year_, _month))
                [energy_change], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_change', _year_, _month))
                [energy_change_text], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_change_text', _year_, _month))
                [energy_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_to_pay', _year_, _month))
                etm = energy_this_month
                elm = energy_last_month
                ed = energy_difference
                eup = energy_unit_price
                eppn = energy_price_per_norm
                eep = energy_excess_price
                ech = energy_change
                echt = energy_change_text
                etp = energy_to_pay
        
                # gas
                [gas_this_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_this_month', _year_, _month))
                [gas_last_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_last_month', _year_, _month))
                [gas_difference], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_difference', _year_, _month))
                [gas_unit_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_unit_price', _year_, _month))
                [gas_coefficient], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_coefficient', _year_, _month))
                [gas_vdgo], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_vdgo', _year_, _month))
                [gas_change], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_change', _year_, _month))
                [gas_change_text], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_change_text', _year_, _month))
                [gas_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_to_pay', _year_, _month))
                gtm = gas_this_month
                glm = gas_last_month
                gd = gas_difference
                gup = gas_unit_price
                gc = gas_coefficient
                gv = gas_vdgo
                gch = gas_change
                gcht = gas_change_text
                gtp = gas_to_pay
        
                # trash
                [trash_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('trash_price', _year_, _month))
                [trash_change], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('trash_change', _year_, _month))
                [trash_change_text], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('trash_change_text', _year_, _month))
                [trash_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('trash_to_pay', _year_, _month))
                tp = trash_price
                tch = trash_change
                tcht = trash_change_text
                if trash_to_pay is not None:
                    ttp = round(trash_to_pay, 2)
                else:
                    ttp = trash_to_pay
        
                # internet
                [internet_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('internet_price', _year_, _month))
                [internet_change], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('internet_change', _year_, _month))
                [internet_change_text], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('internet_change_text', _year_, _month))
                [internet_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('internet_to_pay', _year_, _month))
                internet_p = internet_price
                ich = internet_change
                icht = internet_change_text
                itp = internet_to_pay
        
                # phone
                [phone_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('phone_price', _year_, _month))
                [phone_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('phone_to_pay', _year_, _month))
                # [phone_change], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('phone_change', _year_, _month))
                # [phone_change_text], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('phone_change_text', _year_, _month))
                phone_p = phone_price
                # phone_ch = phone_change
                # phone_cht = phone_change_text
                phone_tp = phone_to_pay
        
                # total
                [total_t13], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('total', _year_, _month))
                total = total_t13
        
                #Вода
                item = QtWidgets.QTableWidgetItem(str(wtm))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(0, 0, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(wlm))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(1, 0, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(wd))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(2, 0, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(wup))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(3, 0, item)' % (_year, _month))

                item = QtWidgets.QTableWidgetItem(str(wm))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(4, 0, item)' % (_year, _month))

                item = QtWidgets.QTableWidgetItem(str(wch))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(6, 0, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(wcht))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(7, 0, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(wtp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(8, 0, item)' % (_year, _month))
        
                #Свет
                item = QtWidgets.QTableWidgetItem(str(etm))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(0, 1, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(elm))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(1, 1, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(ed))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(2, 1, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(eup))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(3, 1, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(eppn))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(4, 1, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(eep))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(5, 1, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(ech))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(6, 1, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(echt))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(7, 1, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(etp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(8, 1, item)' % (_year, _month))
        
                #Газ
                item = QtWidgets.QTableWidgetItem(str(gtm))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(0, 2, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(glm))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(1, 2, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(gd))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(2, 2, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(gup))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(3, 2, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(gc))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(4, 2, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(gv))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(5, 2, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(gch))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(6, 2, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(gcht))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(7, 2, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(gtp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(8, 2, item)' % (_year, _month))
        
                #Мусор
                item = QtWidgets.QTableWidgetItem(str(tp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(3, 3, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(tch))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(6, 3, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(tcht))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(7, 3, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(ttp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(8, 3, item)' % (_year, _month))
        
                #Интернет
                item = QtWidgets.QTableWidgetItem(str(internet_p))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(3, 4, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(ich))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(6, 4, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(icht))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(7, 4, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(itp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(8, 4, item)' % (_year, _month))
        
                #Телефон
                item = QtWidgets.QTableWidgetItem(str(phone_p))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(3, 5, item)' % (_year, _month))
                # item = QtWidgets.QTableWidgetItem(str(phone_ch))
                # item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                # exec('self.tableWidget_%d_%s.setItem(6, 5, item)' % (_year, _month))
                # item = QtWidgets.QTableWidgetItem(str(phone_cht))
                # item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                # exec('self.tableWidget_%d_%s.setItem(7, 5, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(phone_tp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(8, 5, item)' % (_year, _month))
        
                #Итого
                exec('self.tableWidget_%d_%s.setSpan(9, 0, 1, 6)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(total))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(9, 0, item)' % (_year, _month))


    def upd_t_a61a(self):
        year = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
        month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
        for _year in year:
            for _month in month:
                _year_ = str(_year) + '_a61a'
                # energy
                [energy_unit_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_unit_price', _year_, _month))
                [energy_change], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_change', _year_, _month))
                [energy_change_text], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_change_text', _year_, _month))
                [energy_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_to_pay', _year_, _month))
                eup = energy_unit_price
                ec = energy_change
                ect = energy_change_text
                etp = energy_to_pay

                # gas
                [gas_this_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_this_month', _year_, _month))
                [gas_last_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_last_month', _year_, _month))
                [gas_difference], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_difference', _year_, _month))
                [gas_unit_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_unit_price', _year_, _month))
                [gas_coefficient], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_coefficient', _year_, _month))
                [gas_vdgo], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_vdgo', _year_, _month))
                [gas_change], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_change', _year_, _month))
                [gas_change_text], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_change_text', _year_, _month))
                [gas_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_to_pay', _year_, _month))
                gtm = gas_this_month
                glm = gas_last_month
                gd = gas_difference
                gup = gas_unit_price
                gc = gas_coefficient
                gvdgo = gas_vdgo
                gch = gas_change
                gcht = gas_change_text
                gtp = gas_to_pay

                # trash
                [trash_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('trash_price', _year_, _month))
                [trash_change], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('trash_change', _year_, _month))
                [trash_change_text], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('trash_change_text', _year_, _month))
                [trash_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('trash_to_pay', _year_, _month))
                tp = trash_price
                tc = trash_change
                tct = trash_change_text
                if trash_to_pay is not None:
                    ttp = round(trash_to_pay, 2)
                else:
                    ttp = trash_to_pay

                # total
                [total_a61a], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('total', _year_, _month))
                if total_a61a is not None:
                    total = round(total_a61a, 2)
                else:
                    total = total_a61a

                #Свет
                item = QtWidgets.QTableWidgetItem(str(eup))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(3, 0, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(ec))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(6, 0, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(ect))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(7, 0, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(etp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(8, 0, item)' % (_year, _month))

                #Газ
                item = QtWidgets.QTableWidgetItem(str(gtm))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(0, 1, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(glm))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(1, 1, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(gd))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(2, 1, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(gup))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(3, 1, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(gc))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(4, 1, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(gvdgo))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(5, 1, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(gch))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(6, 1, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(gcht))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(7, 1, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(gtp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(8, 1, item)' % (_year, _month))

                #Мусор
                item = QtWidgets.QTableWidgetItem(str(tp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(3, 2, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(tc))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(6, 2, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(tct))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(7, 2, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(ttp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(8, 2, item)' % (_year, _month))

                #Итого
                exec('self.tableWidget_%d_%s_2.setSpan(9, 0, 1, 4)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(total))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(9, 0, item)' % (_year, _month))


    def upd_general_total(self):
        year = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
        month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
        for _year in year:
            for _month in month:
                _month_ = _month + '_general_total'
                [general_total_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE year="{}"'.format(_month_, 'general_total_to_pay', _year))
                if general_total_to_pay is not None:
                    gttp = round(general_total_to_pay, 2)
                else:
                    gttp = general_total_to_pay

                item = QtWidgets.QTableWidgetItem(str(gttp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_3.setItem(0, 0, item)' % (_year, _month))