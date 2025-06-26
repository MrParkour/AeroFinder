from PyQt5 import QtWidgets, uic
import sys
import sqlite3

connection = sqlite3.connect("database/plane_db.db")
cursor = connection.cursor()
 
app = QtWidgets.QApplication([])
ui = uic.loadUi("ui_designes/ui_design_V_5.ui")

la = ui.tabWidget.currentIndex()

def checking_input(input_string):
    # function which checks the correctness of the inputы
    try:
        if float(input_string) >= 0:
            return float(input_string)
        else:
            QtWidgets.QMessageBox.information(None, "Ошибка", "Введите число больше 0")
            return -1
    except Exception:
        return -1

def create_request_str(obj_name, collumn_name):
    num = checking_input(obj_name.text())
    if num > 0:
        return "AND %s BETWEEN %s AND %s\n" % (collumn_name, num * 0.95, num * 1.05)
    elif num == -1:
        # вывести сообщения с ошибкой
        return ""
    else:
        return ""

# функция возвращает строку для запроса в sql проверяю промежуток от до
# на вход принимает два объекта lineEdit под (first, second), соответсвенно там где "от" и "до"
# name это название столюца в базе данныз sql
def gap_checking(first, second, name):
    checked_from = checking_input(first.text())
    checked_to = checking_input(second.text())
    if checked_from < checked_to:
        if checked_from != -1 and checked_to != -1:
            return "AND %s BETWEEN %s AND %s\n" % (name, str(checked_from), str(checked_to))
        elif checked_from == -1 and checked_to != -1:
            return "AND %s <= %s\n" % (name, str(checked_to))
        elif checked_from != -1 and checked_to == -1:
            return "AND %s >= %s\n" % (name, str(checked_from))
        else:
            return ""
    else:
        if checked_from != -1 and checked_to != -1:
            if name == "YEAR":
                QtWidgets.QMessageBox.information(None, "Ошибка", "Проверьте, чтобы значение 'от' было меньше, чем 'до' в поле 'Год выпуска'")
            elif name == "MASS_EMPTY":
                QtWidgets.QMessageBox.information(None, "Ошибка", "Проверьте, чтобы значение 'от' было меньше, чем 'до' в поле 'Масса пустого'")
            elif name == "MASS_NORMAL":
                QtWidgets.QMessageBox.information(None, "Ошибка", "Проверьте, чтобы значение 'от' было меньше, чем 'до' в поле 'Нормальная масса")
            elif name == "MASS_MAXIMAL":
                QtWidgets.QMessageBox.information(None, "Ошибка", "Проверьте, чтобы значение 'от' было меньше, чем 'до' в поле 'Максимальная взлётная масса'")
            elif name == "LEN":
                QtWidgets.QMessageBox.information(None, "Ошибка", "Проверьте, чтобы значение 'от' было меньше, чем 'до' в поле 'Длина'")
            elif name == "HEIGTH":
                QtWidgets.QMessageBox.information(None, "Ошибка", "Проверьте, чтобы значение 'от' было меньше, чем 'до' в поле 'Высота'")
            elif name == "WING_SPAN":
                QtWidgets.QMessageBox.information(None, "Ошибка", "Проверьте, чтобы значение 'от' было меньше, чем 'до' в поле 'Размах крыла'")
            elif name == "WING_AREA":
                QtWidgets.QMessageBox.information(None, "Ошибка", "Проверьте, чтобы значение 'от' было меньше, чем 'до' в поле 'Площадь крыла'")
            elif name == "WING_SWEEP":
                QtWidgets.QMessageBox.information(None, "Ошибка", "Проверьте, чтобы значение 'от' было меньше, чем 'до' в поле 'Стреловидность крыла'")
            elif name == "CREW":
                QtWidgets.QMessageBox.information(None, "Ошибка", "Проверьте, чтобы значение 'от' было меньше, чем 'до' в поле 'Экипаж'")
            elif name == "ARMAMENT":
                QtWidgets.QMessageBox.information(None, "Ошибка", "Проверьте, чтобы значение 'от' было меньше, чем 'до' в поле 'Боевая нагрузка'")
            elif name == "PASSENGERS":
                QtWidgets.QMessageBox.information(None, "Ошибка", "Проверьте, чтобы значение 'от' было меньше, чем 'до' в поле 'Пассажировместимость'")
            elif name == "PAYLOAD":
                QtWidgets.QMessageBox.information(None, "Ошибка", "Проверьте, чтобы значение 'от' было меньше, чем 'до' в поле 'Максимальная нагрузка'")
            elif name == "SPEED_NORMAL":
                QtWidgets.QMessageBox.information(None, "Ошибка", "Проверьте, чтобы значение 'от' было меньше, чем 'до' в поле 'Крейсерская скорость'")
            elif name == "SPEED_MAX":
                QtWidgets.QMessageBox.information(None, "Ошибка", "Проверьте, чтобы значение 'от' было меньше, чем 'до' в поле 'Максимальная скорость'")
            elif name == "RANGE":
                QtWidgets.QMessageBox.information(None, "Ошибка", "Проверьте, чтобы значение 'от' было меньше, чем 'до' в поле 'Дальность полёта'")
            elif name == "HEIGHT_MAX":
                QtWidgets.QMessageBox.information(None, "Ошибка", "Проверьте, чтобы значение 'от' было меньше, чем 'до' в поле 'Максимальная высота полёта'")
        else:
            return ""

def next_page_plane():
    button = QtWidgets.QApplication.instance().sender()
    if button == ui.pushButton_forward_p:
        obj = ui.stackedWidget_plane
    elif button == ui.pushButton_forward_h:
        obj = ui.stackedWidget_heli
    elif button == ui.push_forward_all:
        obj = ui.stackedWidget_all

    if obj.currentIndex() == (obj.count() - 1):
        obj.setCurrentIndex(0)
    else:
        obj.setCurrentIndex(obj.currentIndex() + 1)

def prev_page_plane():
    button = QtWidgets.QApplication.instance().sender()
    if button == ui.pushButton_back_p:
        obj = ui.stackedWidget_plane
    elif button == ui.pushButton_back_h:
        obj = ui.stackedWidget_heli
    elif button == ui.push_back_all:
        obj = ui.stackedWidget_all

    if obj.currentIndex() == 0:
        obj.setCurrentIndex(obj.count() - 1)
    else:
        obj.setCurrentIndex(obj.currentIndex() - 1)


def finding():
    try:
        button = QtWidgets.QApplication.instance().sender()
        exc = ""
        output = []
        if button == ui.pushButton_find_p:
            # finding planes
            exc = "SELECT * FROM aircrafts" + "\n"
            exc += """WHERE TYPE = "Самолёт"\n"""
            plans_country_check = False
            plane_country_array = []

            # Проверка флажков у стран самолётов
            if ui.P_coun_cb_Rus.isChecked():
                plans_country_check = True
                plane_country_array.append("Россия")
            if ui.P_coun_cb_USSR.isChecked():
                plans_country_check = True
                plane_country_array.append("СССР")
            if ui.P_coun_cb_Amer.isChecked():
                plans_country_check = True
                plane_country_array.append("Америка")
            if ui.P_coun_cb_Chinazes.isChecked():
                plans_country_check = True
                plane_country_array.append("Китай")
            if ui.P_coun_cb_GBrit.isChecked():
                plans_country_check = True
                plane_country_array.append("Великобритания")
            if ui.P_coun_cb_Iatli.isChecked():
                plans_country_check = True
                plane_country_array.append("Италия")
            if ui.P_coun_cb_Fran.isChecked():
                plans_country_check = True
                plane_country_array.append("Франция")
            if ui.P_coun_cb_Spain.isChecked():
                plans_country_check = True
                plane_country_array.append("Испания")

            # Прверка флажков у двигателей самолётов
            plans_engine_check = False
            plane_engine_array = []
            if ui.P_eng_type_cb_TRDD.isChecked():
                plans_engine_check = True
                plane_engine_array.append("ТРДД")
            if ui.P_eng_type_cb_TVD.isChecked():
                plans_engine_check = True
                plane_engine_array.append("ТВД")
            if ui.P_eng_type_cb_PD.isChecked():
                plans_engine_check = True
                plane_engine_array.append("ПД")
            if ui.P_eng_type_cb_TRD.isChecked():
                plans_engine_check = True
                plane_engine_array.append("ТРД")

            if plans_engine_check:
                exc += """AND ENGINE_TYPE IN ('%s')\n""" % ("""', '""".join(plane_engine_array))
            if plans_country_check:
                exc += """AND COUNTRY IN ('%s')\n""" % ("""', '""".join(plane_country_array))

            # оставлено на всякий случай
            # year_from = checking_input(ui.P_year_line_ot.text())
            # year_to = checking_input(ui.P_year_line_do.text())
            # if year_from != -1 and year_to != -1:
            #     exc += "AND YEAR BETWEEN %s AND %s" % (str(year_from), str(year_to))
            #     exc += "\n"
            # elif year_from == -1 and year_to != -1:
            #     exc += "AND YEAR <= %s" % (str(year_to))
            #     exc += "\n"
            # elif year_from != -1 and year_to == -1:
            #     exc += "AND YEAR >= %s" % (str(year_from))
            #     exc += "\n"
            # else:
            #     pass

            exc += gap_checking(ui.P_year_line_ot, ui.P_year_line_do, 'YEAR')

            # checking mass empty
            exc += gap_checking(ui.P_wei_line_sob_ot, ui.P_wei_line_sob_do, 'MASS_EMPTY')

            # checking mass normal
            exc += gap_checking(ui.P_wei_line_norm_ot, ui.P_wei_line_norm_do, "MASS_NORMAL")

            # checking max mass
            exc += gap_checking(ui.P_wei_line_max_ot, ui.P_wei_line_max_do, "MASS_MAXIMAL")

            # checking size length
            exc += gap_checking(ui.P_size_line_long_ot, ui.P_size_line_long_do, "LEN")

            # checking size heigth
            exc += gap_checking(ui.P_size_line_high_ot, ui.P_size_line_high_do, "HEIGTH")

            # checking wing span
            exc += gap_checking(ui.P_size_line_razmax_ot, ui.P_size_line_rasmax_do, "WING_SPAN")

            # checking wing area
            exc += gap_checking(ui.P_size_line_plosh_ot, ui.P_size_line_plosh_do, "WING_AREA")

            # checking wing sweep
            exc += gap_checking(ui.P_size_line_strel_ot, ui.P_size_line_strel_do, "WING_SWEEP")

            # checking crew
            exc += gap_checking(ui.P_load_line_crew_ot, ui.P_load_line_crew_do, "CREW")

            # checking armament
            exc += gap_checking(ui.P_load_line_comlo_ot, ui.P_load_line_comlo_do, "ARMAMENT")

            # checking passengers capacity
            exc += gap_checking(ui.P_load_line_pascap_ot, ui.P_load_line_pascap_do, "PASSENGERS")

            # checking payload
            exc += gap_checking(ui.P_load_line_maxlo_ot, ui.lineEdit_12, "PAYLOAD")

            # checking flight cruise speed
            exc += gap_checking(ui.P_fl_line_cruis_ot, ui.P_fl_line_cruis_do, "SPEED_NORMAL")

            # checking flight max speed
            exc += gap_checking(ui.P_fl_line_maxsp_ot, ui.P_fl_line_maxsp_do, "SPEED_MAX")

            # checking flight range
            exc += gap_checking(ui.P_fl_line_rang_ot, ui.P_fl_line_rang_do, "RANGE")

            # checking flight max heigth
            exc += gap_checking(ui.P_fl_line_maxhi_ot, ui.P_fl_line_maxhi_do, "HEIGHT_MAX")

            cursor.execute(exc)
            output = cursor.fetchall()

        elif button == ui.pushButton_find_h:
            heli_country_check = False
            heli_country_array = []

            # Проверка флажков у стран вертолётов
            if ui.H_co_cb_Rus.isChecked():
                heli_country_check = True
                heli_country_array.append("Россия")
            if ui.H_coun_cb_USSR.isChecked():
                heli_country_check = True
                heli_country_array.append("СССР")
            if ui.H_coun_cb_Amer.isChecked():
                heli_country_check = True
                heli_country_array.append("Америка")
            if ui.H_coun_cb_Chinazes.isChecked():
                heli_country_check = True
                heli_country_array.append("Китай")
            if ui.H_coun_cb_GBrit.isChecked():
                heli_country_check = True
                heli_country_array.append("Великобритания")
            if ui.H_coun_cb_Itali.isChecked():
                heli_country_check = True
                heli_country_array.append("Италия")
            if ui.h_coun_cb_Fran.isChecked():
                heli_country_check = True
                heli_country_array.append("Франция")
            if ui.H_coun_cb_Spain.isChecked():
                heli_country_check = True
                heli_country_array.append("Испания")
            # Провекрка флажков двигателей вертолётов
            heli_engine_check = False
            heli_engine_array = []
            if ui.H_eng_type_cb_TRDD.isChecked():
                heli_engine_check = True
                heli_engine_array.append("ТРДД")
            if ui.H_eng_type_cb_TRD.isChecked():
                heli_engine_check = True
                heli_engine_array.append("ТРД")
            if ui.H_eng_type_cb_TVD.isChecked():
                heli_engine_check = True
                heli_engine_array.append("ТВД")
            if ui.checkBox_74.isChecked():
                heli_engine_check = True
                heli_engine_array.append("ПД")

            # finding helicopters

            exc = "SELECT * FROM aircrafts" + "\n"
            exc += """WHERE TYPE = "вертолет"\n"""
            # creating exc for country and engine type

            if heli_engine_check:
                exc += """AND ENGINE_TYPE IN ('%s')\n""" % ("""', '""".join(heli_engine_array))
            if heli_country_check:
                exc += """AND COUNTRY IN ('%s')\n""" % ("""', '""".join(heli_country_array))

            # checking year
            exc += gap_checking(ui.H_year_line_ot, ui.H_year_line_do, "YEAR")
            
            # checking mass empty
            exc += gap_checking(ui.H_wei_line_sob_ot, ui.H_wei_line_sob_do, "MASS_EMPTY")

            # checking mass normal
            exc += gap_checking(ui.H_wei_line_norm_ot, ui.H_wei_line_norm_do, "MASS_NORMAL")

            # checking mass max
            exc += gap_checking(ui.H_wei_line_max_ot, ui.H_wei_line_max_do, "MASS_MAXIMAL")

            # checking size length
            exc += gap_checking(ui.H_size_line_long_ot, ui.H_size_line_long_do, "LEN")

            # checking size height
            exc += gap_checking(ui.H_size_line_high_ot, ui.H_size_line_high_do, "HEIGTH")
            # checking size main rotor
            exc += gap_checking(ui.H_size_line_diamnes_ot, ui.H_size_line_diamnes_do, "DIAMETR_MAIN_ROTOR")

            # checking size tail rotor
            exc += gap_checking(ui.H_size_line_diamrul_ot, ui.H_size_line_diamrul_do, "DIAMETR_TAIL_ROTOR")

            # checking crew
            exc += gap_checking(ui.H_load_line_crew_ot, ui.H_load_line_crew_do, "CREW")

            # checking armament
            exc += gap_checking(ui.H_load_line_comlo_ot, ui.H_load_line_comlo_do, "ARMAMENT")

            # checking passengers
            exc += gap_checking(ui.H_load_line_pascap_ot, ui.H_load_line_pascap_do, "PASSENGERS")

            # checking max load
            exc += gap_checking(ui.H_load_line_maxlo_ot, ui.H_load_line_maxlo_do, "PAYLOAD")

            # checking fligth cruise speed
            exc += gap_checking(ui.H_fl_line_cruis_ot, ui.H_fl_line_cruis_do, "SPEED_NORMAL")

            # checking fligth max speed
            exc += gap_checking(ui.H_fl_line_maxsp_ot, ui.H_fl_line_maxsp_do, "SPEED_MAX")

            # checking fligth range
            exc += gap_checking(ui.H_fl_line_rang_ot, ui.H_fl_line_rang_do, "RANGE")

            # checking static ceiling
            exc += gap_checking(ui.H_fl_line_sthi_ot, ui.H_fl_line_sthi_do, "STATIC_CEILING")

            # checking practice ceiling
            exc += gap_checking(ui.H_fl_line_prhi_ot, ui.H_fl_line_prhi_do, "SERVICE_CEILING")

            cursor.execute(exc)
            output = cursor.fetchall()

        elif button == ui.push_find_all:
            all_country_check = False
            all_country_array = []
            print(1)

            # Проверка флажков на странах всех ла

            if ui.ALL_coun_cb_Rus.isChecked():
                all_country_check = True
                all_country_array.append("Россия")
            if ui.ALL_coun_cb_USSR.isChecked():
                all_country_check = True
                all_country_array.append("СССР")
            if ui.ALL_coun_cb_Amer.isChecked():
                all_country_check = True
                all_country_array.append("Америка")
            if ui.ALL_coun_cb_Chinazes.isChecked():
                all_country_check = True
                all_country_array.append("Китай")
            if ui.ALL_coun_cb_GBrit.isChecked():
                all_country_check = True
                all_country_array.append("Великобритания")
            if ui.ALL_coun_cb_Itali.isChecked():
                all_country_check = True
                all_country_array.append("Италия")
            if ui.ALL_coun_cb_Fran.isChecked():
                all_country_check = True
                all_country_array.append("Франция")
            if ui.ALL_coun_cb_Spain.isChecked():
                all_country_check = True
                all_country_array.append("Испания")

            # Проверка флажков на двигателх всех ла

            all_engine_check = False
            all_angine_array = []
            if ui.P_eng_type_cb_TRDD_2.isChecked():
                all_engine_check = True
                all_angine_array.append("ТРДД")
            if ui.checkBox_92.isChecked():
                all_engine_check = True
                all_angine_array.append("ТРД")
            if ui.P_eng_type_cb_TVD_2.isChecked():
                all_engine_check = True
                all_angine_array.append("ТВД")
            if ui.P_eng_type_cb_PD_2.isChecked():
                all_engine_check = True
                all_angine_array.append("ПД")
            # finding all

            exc = "SELECT * FROM aircrafts" + "\n"
            exc += """WHERE TYPE in ("вертолет", "самолет")\n"""

            # exc for engine type and country
            if all_engine_check:
                exc += """AND ENGINE_TYPE IN ('%s')\n""" % ("""', '""".join(all_angine_array))
            if all_country_check:
                exc += """AND COUNTRY IN ('%s')\n""" % ("""', '""".join(all_country_array))

            # checking year
            print(0)
            exc += gap_checking(ui.ALL_year_line_ot, ui.ALL_year_line_do, "YEAR")   
            print(1)
            # checking mass empty
            exc += gap_checking(ui.ALL_wei_line_sob_ot, ui.ALL_wei_line_sob_do, "MASS_EMPTY")
            print(2)
            # checking mass normal
            exc += gap_checking(ui.ALL_wei_line_norm_ot, ui.ALL_wei_line_norm_do, "MASS_NORMAL")
            print(3)
            # checking mass max
            exc += gap_checking(ui.ALL_wei_line_max_ot, ui.ALL_wei_line_max_do, "MASS_MAXIMAL")
            print(4)
            # checking size length
            exc += gap_checking(ui.ALL_size_line_long_ot, ui.ALL_size_line_long_do, "LEN")
            print(5)
            # checking size height
            exc += gap_checking(ui.ALL_size_line_high_ot, ui.ALL_size_line_high_do, "HEIGTH")
            print(6)
            # checking crew
            exc += gap_checking(ui.ALL_load_line_crew_ot, ui.ALL_load_line_crew_do, "CREW")
            print(7)
            # checking armament
            exc += gap_checking(ui.ALL_load_line_comlo_ot, ui.ALL_load_line_comlo_do, "ARMAMENT")
            print(8)
            # checking passengers
            exc += gap_checking(ui.ALL_load_line_pascap_ot, ui.ALL_load_line_pascap_do, "PASSENGERS")
            print(9)
            # checking max load
            exc += gap_checking(ui.ALL_load_line_maxlo_ot, ui.ALL_load_line_maxlo_do, "PAYLOAD")
            print(10)
            # checking fligth cruise speed
            exc += gap_checking(ui.ALL_fl_line_cruise_ot, ui.ALL_fl_line_cruise_do, "SPEED_NORMAL")
            print(11)
            # checking fligth max speed
            exc += gap_checking(ui.ALL_fl_line_maxsp_ot, ui.ALL_fl_line_maxsp_do, "SPEED_MAX")
            print(12)
            # checking fligth range
            exc += gap_checking(ui.ALL_fl_line_rang_ot, ui.ALL_fl_line_rang_do, "RANGE")
            print(13)
            exc_1 = exc
            exc += gap_checking(ui.ALL_fl_line_maxhi_ot, ui.ALL_fl_line_maxhi_do, "STATIC_CEILING")
            exc_1 += gap_checking(ui.ALL_fl_line_maxhi_ot, ui.ALL_fl_line_maxhi_do, "HEIGHT_MAX")
            print(exc)
            cursor.execute(exc)
            output_plane = cursor.fetchall()
            cursor.execute(exc_1)
            output_heli = cursor.fetchall()
            output = output_heli + output_plane

        # сделать проверку на флажки
        # записать итог в строку вида "спортивный, перехватчик, истребитель"
        # добавить переменную bool которая показывается есть ли чтото или нет

        if output != []:
            # vivod
            pass
        else:
            msg_box = QtWidgets.QMessageBox.information(None, "Ошибка", "К сожаления ни одного летательного аппарата с такими техническими характеристиками не было найдено. Измените критерии поиска и попробуйте еще раз.")
            msg_box.setIcon(QtWidgets.QMessageBox.warning)
    except Exception:
        pass

def clear():
    # прверить на какой стр нажата кнопка, затем очистить все лайны и боксы на этой стр
    button = QtWidgets.QApplication.instance().sender()
    if button == ui.pushButton_clear_plane:
        # очистка всех лайнов в самолётах
        ui.P_year_line_ot.clear()
        ui.P_year_line_do.clear()

        ui.P_wei_line_sob_ot.clear()
        ui.P_wei_line_sob_do.clear()
        ui.P_wei_line_norm_ot.clear()
        ui.P_wei_line_norm_do.clear()
        ui.P_wei_line_max_ot.clear()
        ui.P_wei_line_max_do.clear()

        ui.P_size_line_long_ot.clear()
        ui.P_size_line_long_do.clear()
        ui.P_size_line_high_ot.clear()
        ui.P_size_line_high_do.clear()
        ui.P_size_line_razmax_ot.clear()
        ui.P_size_line_razmax_do.clear()
        ui.P_size_line_plosh_ot.clear()
        ui.P_size_line_plosh_do.clear()
        ui.P_size_line_strel_ot.clear()
        ui.P_size_line_strel_do.clear()

        ui.P_load_line_crew_ot.clear()
        ui.P_load_line_crew_do.clear()
        ui.P_load_line_comlo_ot.clear()
        ui.P_load_line_comlo_do.clear()
        ui.P_load_line_pascap_ot.clear()
        ui.P_load_line_pascap_do.clear()
        ui.P_load_line_maxlo_ot.clear()
        ui.P_load_line_maxlo_do.clear()

        ui.P_fl_line_cruis_ot.clear()
        ui.P_fl_line_cruis_do.clear()
        ui.P_fl_line_maxsp_ot.clear()
        ui.P_fl_line_maxsp_do.clear()
        ui.P_fl_line_rang_ot.clear()
        ui.P_fl_line_range_do.clear()
        ui.P_fl_line_maxhi_ot.clear()
        ui.P_fl_line_maxhi_do.clear()

        # очистка всех чекбоксов в сомолётах
        ui.P_coun_cb_Rus.setChecking(False)
        ui.P_coun_cb_Amer.setChecking(False)
        ui.P_coun_cb_GBrit.setChecking(False)
        ui.P_coun_cb_Fran.setChecking(False)
        ui.P_coun_cb_USSR.setChecking(False)
        ui.P_coun_cb_Chinazes.setChecking(False)
        ui.P_coun_cb_Itali.setChecking(False)
        ui.P_coun_cb_Spain.setChecking(False)

        ui.P_eng_type_cb_TRDD.setChecking(False)
        ui.P_eng_type_cb_TVD.setChecking(False)
        ui.P_eng_type_cb_PD.setChecking(False)
        ui.P_eng_type_cb_TRD.setChecking(False)

    if button == ui.pushButton_clear_heli:
        # очистка всех лайнов в вертолётах
        ui.H_year_line_ot.clear()
        ui.H_yaer_line_do.clear()

        ui.H_wei_line_sob_ot.clear()
        ui.H_wei_line_norm_ot.clear()
        ui.H_wei_line_max_ot.clear()
        ui.H_wei_line_sob_do.clear()
        ui.H_wei_line_norm_do.clear()
        ui.H_wei_line_max_do.clear()

        ui.H_size_line_long_ot.clear()
        ui.H_size_line_high_ot.clear()
        ui.H_size_line_Dnes_ot.clear()
        ui.H_size_line_Dru_ot.clear()
        ui.H_size_line_long_do.clear()
        ui.H_size_line_high_do.clear()
        ui.H_size_line_Dnes_do.clear()
        ui.H_size_line_Dru_do.clear()

        ui.H_load_line_crew_ot.clear()
        ui.H_load_line_comlo_ot.clear()
        ui.H_load_line_pascap_ot.clear()
        ui.H_load_line_maxlo_ot.clear()
        ui.H_load_line_crew_do.clear()
        ui.H_load_line_comlo_do.clear()
        ui.H_load_line_pascap_do.clear()
        ui.H_load_line_maxlo_do.clear()

        ui.H_fl_line_cruis_ot.clear()
        ui.H_fl_line_maxsp_ot.clear()
        ui.H_fl_line_range_ot.clear()
        ui.H_fl_line_sthi_ot.clear()
        ui.H_fl_line_prhi_ot.clear()
        ui.H_fl_line_cruis_do.clear()
        ui.H_fl_line_maxsp_do.clear()
        ui.H_fl_line_range_do.clear()
        ui.H_fl_line_sthi_do.clear()
        ui.H_fl_line_prhi_do.clear()

        # очистка всех боксов в вертолётах
        ui.H_coun_cb_Rus.setCheking(False)
        ui.H_coun_cb_Amer.setCheckng(False)
        ui.H_coun_cb_GBrit.setCheckng(False)
        ui.H_coun_cb_Fran.setCheckng(False)
        ui.H_coun_cb_USSR.setCheckng(False)
        ui.H_coun_cb_Chinazes.setCheckng(False)
        ui.H_coun_cb_Itali.setCheckng(False)
        ui.H_coun_cb_Spain.setCheckng(False)

        ui.H_eng_type_cb_TRDD.setChecking(False)
        ui.H_eng_type_cb_TVD.setChecking(False)
        ui.H_eng_type_cb_PD.setChecking(False)
        ui.H_eng_type_cb_TRD.setChecking(False)

    if button == ui.pushButton_clear_all:
        # очистка всех лайнов в алл
        ui.ALL_year_line_ot.clear()
        ui.ALL_year_line_do.clear()

        ui.ALL_wei_line_sob_ot.clear()
        ui.ALL_wei_line_sob_do.clear()
        ui.ALL_wei_line_norm_ot.clear()
        ui.ALL_wei_line_norm_do.clear()
        ui.ALL_wei_line_max_ot.clear()
        ui.ALL_wei_line_max_do.clear()

        ui.ALL_size_line_long_ot.clear()
        ui.ALL_size_line_long_do.clear()
        ui.ALL_size_line_high_ot.clear()
        ui.ALL_size_line_high_do.clear()

        ui.ALL_load_line_crew_ot.clear()
        ui.ALL_load_line_crew_do.clear()
        ui.ALL_load_line_comlo_ot.clear()
        ui.ALL_load_line_comlo_do.clear()
        ui.ALL_load_line_pascap_ot.clear()
        ui.ALL_load_line_pascap_do.clear()
        ui.ALL_load_line_maxlo_ot.clear()
        ui.ALL_load_line_maxlo_do.clear()

        ui.ALL_fl_line_cruis_ot.clear()
        ui.ALL_fl_line_cruis_do.clear()
        ui.ALL_fl_line_maxsp_ot.clear()
        ui.ALL_fl_line_maxsp_do.clear()
        ui.ALL_fl_line_rang_ot.clear()
        ui.ALL_fl_line_range_do.clear()
        ui.ALL_fl_line_maxhi_ot.clear()
        ui.ALL_fl_line_maxhi_do.clear()

        # очистка всех чекбоксов в вертолётах
        ui.ALL_coun_cb_Rus.setChecking(False)
        ui.ALL_coun_cb_Amer.setChecking(False)
        ui.ALL_coun_cb_GBrit.setChecking(False)
        ui.ALL_coun_cb_Fran.setChecking(False)
        ui.ALL_coun_cb_USSR.setChecking(False)
        ui.ALL_coun_cb_Chinazes.setChecking(False)
        ui.ALL_coun_cb_Itali.setChecking(False)
        ui.ALL_coun_cb_Spain.setChecking(False)

        ui.P_eng_type_cb_TRDD.setChecking(False)
        ui.P_eng_type_cb_TVD.setChecking(False)
        ui.P_eng_type_cb_PD.setChecking(False)
        ui.P_eng_type_cb_TRD.setChecking(False)


ui.push_find_all.clicked.connect(finding)
ui.pushButton_find_p.clicked.connect(finding)
ui.pushButton_find_h.clicked.connect(finding)

# функции очистки
ui.pushButton_clear_plane.clicked.connect(clear)
ui.pushButton_clear_heli.clicked.connect(clear)
ui.pushButton_clear_all.clicked.connect(clear)

ui.show()
sys.exit(app.exec())
connection.close()
