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
                [water_this_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_this_month', _year_, _month))
                [water_last_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_last_month', _year_, _month))
                [water_difference], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_difference', _year_, _month))
                [water_unit_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_unit_price', _year_, _month))
                [water_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('water_to_pay', _year_, _month))
                wtm = water_this_month
                wlm = water_last_month
                wd = water_difference
                wup = water_unit_price
                wtp = water_to_pay
        
                # energy
                [energy_this_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_this_month', _year_, _month))
                [energy_last_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_last_month', _year_, _month))
                [energy_difference], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_difference', _year_, _month))
                [energy_unit_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_unit_price', _year_, _month))
                [energy_price_per_norm], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_price_per_norm', _year_, _month))
                [energy_excess_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_excess_price', _year_, _month))
                [energy_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_to_pay', _year_, _month))
                etm = energy_this_month
                elm = energy_last_month
                ed = energy_difference
                eup = energy_unit_price
                eppn = energy_price_per_norm
                eep = energy_excess_price
                etp = energy_to_pay
        
                # gas
                [gas_this_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_this_month', _year_, _month))
                [gas_last_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_last_month', _year_, _month))
                [gas_difference], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_difference', _year_, _month))
                [gas_unit_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_unit_price', _year_, _month))
                [gas_coefficient], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_coefficient', _year_, _month))
                [gas_vdgo], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_vdgo', _year_, _month))
                [gas_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_to_pay', _year_, _month))
                gtm = gas_this_month
                glm = gas_last_month
                gd = gas_difference
                gup = gas_unit_price
                gc = gas_coefficient
                gv = gas_vdgo
                gtp = gas_to_pay
        
                # trash
                [trash_unit_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('trash_unit_price', _year_, _month))
                [trash_amount], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('trash_amount', _year_, _month))
                [trash_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('trash_to_pay', _year_, _month))
                tup = trash_unit_price
                ta = trash_amount
                if trash_to_pay is not None:
                    ttp = round(trash_to_pay, 2)
                else:
                    ttp = trash_to_pay
        
                # internet
                [internet_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('internet_price', _year_, _month))
                [internet_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('internet_to_pay', _year_, _month))
                internet_p = internet_price
                itp = internet_to_pay
        
                # phone
                [phone_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('phone_price', _year_, _month))
                [phone_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('phone_to_pay', _year_, _month))
                phone_p = phone_price
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
                item = QtWidgets.QTableWidgetItem(str(wtp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(6, 0, item)' % (_year, _month))
        
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
                item = QtWidgets.QTableWidgetItem(str(etp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(6, 1, item)' % (_year, _month))
        
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

                item = QtWidgets.QTableWidgetItem(str(gtp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(6, 2, item)' % (_year, _month))
        
                #Мусор
                item = QtWidgets.QTableWidgetItem(str(tup))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(3, 3, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(ta))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(4, 3, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(ttp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(6, 3, item)' % (_year, _month))
        
                #Интернет
                item = QtWidgets.QTableWidgetItem(str(internet_p))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(3, 4, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(itp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(6, 4, item)' % (_year, _month))
        
                #Телефон
                item = QtWidgets.QTableWidgetItem(str(phone_p))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(3, 5, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(phone_tp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(6, 5, item)' % (_year, _month))
        
                #Итого
                exec('self.tableWidget_%d_%s.setSpan(7, 0, 1, 6)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(total))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s.setItem(7, 0, item)' % (_year, _month))

        # #test
        # year = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
        # month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
        # for _year in year:
        #     for _month in month:
        #         # total
        #         _year_ = str(_year) + '_t13'
        #         [total_t13], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('total', _year_, _month))
        #         total = total_t13
        # 
        #         #Итого
        #         exec('self.tableWidget_%d_%s.setSpan(7, 0, 1, 6)' % (_year, _month))
        #         # self.tableWidget_2020_jan.setSpan(7, 0, 1, 6) #объединение ячеек итого
        #         item = QtWidgets.QTableWidgetItem(str(total))
        #         item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        #         exec('self.tableWidget_%d_%s.setItem(7, 0, item)' % (_year, _month))
        #         # self.tableWidget_2020_jan.setItem(7, 0, item)

    def upd_t_a61a(self):
        year = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
        month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
        for _year in year:
            for _month in month:
                _year_ = str(_year) + '_a61a'
                # energy
                [energy_unit_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_unit_price', _year_, _month))
                [energy_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('energy_to_pay', _year_, _month))
                eup = energy_unit_price
                etp = energy_to_pay

                # gas
                [gas_this_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_this_month', _year_, _month))
                [gas_last_month], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_last_month', _year_, _month))
                [gas_difference], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_difference', _year_, _month))
                [gas_unit_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_unit_price', _year_, _month))
                [gas_coefficient], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_coefficient', _year_, _month))
                [gas_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('gas_to_pay', _year_, _month))
                gtm = gas_this_month
                glm = gas_last_month
                gd = gas_difference
                gup = gas_unit_price
                gc = gas_coefficient
                gtp = gas_to_pay

                # trash
                [trash_unit_price], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('trash_unit_price', _year_, _month))
                [trash_amount], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('trash_amount', _year_, _month))
                [trash_to_pay], = MainMenu.cur.execute('SELECT {} FROM "{}" WHERE month="{}"'.format('trash_to_pay', _year_, _month))
                tup = trash_unit_price
                ta = trash_amount
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
                item = QtWidgets.QTableWidgetItem(str(etp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(5, 0, item)' % (_year, _month))

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
                item = QtWidgets.QTableWidgetItem(str(gtp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(5, 1, item)' % (_year, _month))

                #Мусор
                item = QtWidgets.QTableWidgetItem(str(tup))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(3, 2, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(ta))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(4, 2, item)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(ttp))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(5, 2, item)' % (_year, _month))

                #Итого
                exec('self.tableWidget_%d_%s_2.setSpan(6, 0, 1, 4)' % (_year, _month))
                item = QtWidgets.QTableWidgetItem(str(total))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                exec('self.tableWidget_%d_%s_2.setItem(6, 0, item)' % (_year, _month))


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