from PyQt5 import QtWidgets, uic
import sys
import sqlite3

connection = sqlite3.connect("database/plane_db.db")
cursor = connection.cursor()
 
app = QtWidgets.QApplication([])
ui = uic.loadUi("ui_desingnes/ui_design_V_4.ui")

la = ui.tabWidget.currentIndex()

def checking_input(input_string):
    # function which checks the correctness of the inputы
    try:
        return float(input_string)
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
        # napisat` vivod oshibki
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
    # активируетс япри нажатии на кнопку найти
    # далее проверяется на какой странице (самолёты, вертолёты, все) была нажата кнопка
    button = QtWidgets.QApplication.instance().sender()
    exc = ""
    output = []
    if button == ui.pushButton_find_p:
        # finding planes
        exc = "SELECT * FROM aircrafts" + "\n"
        exc += """WHERE TYPE = "самолет"\n"""
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
        exc += gap_checking(ui.P_size_line_long_ot, ui.P_size_line_long_do, "HEIGTH")
        
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

        print(exc)
        cursor.execute(exc)
        output = cursor.fetchall()

    elif button == ui.pushButton_find_h:
        # finding helicopters
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
        exc += create_request_str(ui.H_wei_line_sob, "MASS_EMPTY")
        
        # checking mass normal
        exc += create_request_str(ui.H_wei_line_norm, "MASS_NORMAL")
        
        # checking mass max
        exc += create_request_str(ui.H_wei_line_max, "MASS_MAXIMAL")

        # checking size length
        exc += create_request_str(ui.H_size_line_long, "LEN")
        
        # checking size height
        exc += create_request_str(ui.H_size_line_high, "HEIGTH")
        
        # checking size main rotor
        exc += create_request_str(ui.H_size_line_Dnes, "DIAMETR_MAIN_ROTOR")
        
        # checking size tail rotor
        exc += create_request_str(ui.H_size_line_Drul, "DIAMETR_TAIL_ROTOR")
        
        # checking crew
        exc += create_request_str(ui.H_load_line_crew, "CREW")
        
        # checking armament
        exc += create_request_str(ui.H_load_line_comlo, "ARMAMENT")
        
        # checking passengers
        exc += create_request_str(ui.H_load_line_pascap, "PASSENGERS")
        
        # checking max load
        exc += create_request_str(ui.H_load_line_maxlo, "PAYLOAD")
        
        # checking fligth cruise speed
        exc += create_request_str(ui.H_fl_line_cruis, "SPEED_NORMAL")
        
        # checking fligth max speed
        exc += create_request_str(ui.H_fl_line_maxsp, "SPEED_MAX")
        
        # checking fligth range
        exc += create_request_str(ui.H_fl_line_range, "RANGE")
        
        # checking static ceiling
        exc += create_request_str(ui.H_fl_line_sthi, "STATIC_CEILING")
        
        # checking practice ceiling
        exc += create_request_str(ui.H_fl_line_sthi, "SERVICE_CEILING")

        print(exc)
        cursor.execute(exc)
        output = cursor.fetchall()
      
    elif button == ui.push_find_all:
        all_country_check = False
        all_country_array = []

        # Проверка флажков на странах всех ла

        if ui.checkBox_75.isChecked():
            all_country_check = True
            all_country_array.append("Россия")
        if ui.checkBox_76.isChecked():
            all_country_check = True
            all_country_array.append("СССР")
        if ui.checkBox_77.isChecked():
            all_country_check = True
            all_country_array.append("Америка")
        if ui.checkBox_78.isChecked():
            all_country_check = True
            all_country_array.append("Китай")
        if ui.checkBox_79.isChecked():
            all_country_check = True
            all_country_array.append("Великобритания")
        if ui.checkBox_80.isChecked():
            all_country_check = True
            all_country_array.append("Италия")
        if ui.checkBox_82.isChecked():
            all_country_check = True
            all_country_array.append("Франция")
        if ui.checkBox_82.isChecked():
            all_country_check = True
            all_country_array.append("Испания")
        
        # Проверка флажков на двигателх всех ла

        all_engine_check = False
        all_angine_array = []
        if ui.checkBox_91.isChecked():
            all_engine_check = True
            all_angine_array.append("ТРДД")
        if ui.checkBox_92.isChecked():
            all_engine_check = True
            all_angine_array.append("ТРД")
        if ui.checkBox_93.isChecked():
            all_engine_check = True
            all_angine_array.append("ТВД")
        if ui.checkBox_94.isChecked():
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
        exc += gap_checking(ui.lineEdit_31, ui.lineEdit_36, "YEAR")
        
        # checking mass empty
        mass_empty = checking_input(ui.lineEdit_83.text())
        if mass_empty != -1:
            exc += "AND MASS_EMPTY BETWEEN %s AND %s" % (str(mass_empty * 0.95), str(mass_empty * 1.05))
            exc += '\n'
        else:
            pass
        
        # checking mass normal
        mass_normal = checking_input(ui.lineEdit_85.text())
        if mass_normal != -1:
            exc += "AND MASS_NORMAL BETWEEN %s AND %s" % (str(mass_normal * 0.95), str(mass_normal * 1.05))
            exc += '\n'
        else:
            pass
        
        # checking mass max
        mass_max = checking_input(ui.lineEdit_84.text())
        if mass_max != -1:
            exc += "AND MASS_MAXIMAL BETWEEN %s AND %s" % (mass_max * 0.95, mass_max * 1.05)
            exc += '\n'
        else:
            pass

        # checking size length
        length = checking_input(ui.lineEdit_37.text())
        if length != -1:
            exc += "AND LEN BETWEEN %s AND %s" % (length * 0.95, length * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking size height
        high = checking_input(ui.lineEdit_38.text())
        if high != -1:
            exc += "AND HEIGTH BETWEEN %s AND %s" % (high * 0.95, high * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking crew
        crew = checking_input(ui.lineEdit_87.text())
        if crew != -1:
            exc += "AND CREW BETWEEN %s AND %s" % (crew * 0.95, crew * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking armament
        armament = checking_input(ui.lineEdit_88.text())
        if armament != -1:
            exc += "AND ARMAMENT BETWEEN %s AND %s" % (armament * 0.95, armament * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking passengers
        passengers = checking_input(ui.lineEdit_86.text())
        if passengers != -1:
            exc += "AND PASSENGERS BETWEEN %s AND %s" % (passengers * 0.95, passengers * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking max load
        max_load = checking_input(ui.lineEdit_89.text())
        if max_load != -1:
            exc += "AND PAYLOAD BETWEEN %s AND %s" % (max_load * 0.95, max_load * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking fligth cruise speed
        fl_cruise_speed = checking_input(ui.lineEdit_90.text())
        if fl_cruise_speed != -1:
            exc += "AND SPEED_NORMAL BETWEEN %s AND %s" % (fl_cruise_speed * 0.95, fl_cruise_speed * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking fligth max speed
        fl_max_speed = checking_input(ui.lineEdit_92.text())
        if fl_max_speed != -1:
            exc += "AND SPEED_MAX BETWEEN %s AND %s" % (fl_max_speed * 0.95, fl_max_speed * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking fligth range
        fl_range = checking_input(ui.lineEdit_91.text())
        if fl_range != -1:
            exc += "AND RANGE BETWEEN %s AND %s" % (fl_range * 0.95, fl_range * 1.05)
            exc += '\n'
        else:
            pass
        exc_1 = exc
        # checking static ceiling
        static_ceiling = checking_input(ui.lineEdit_93.text())
        if static_ceiling != -1:
            exc += "AND STATIC_CEILING BETWEEN %s AND %s" % (static_ceiling * 0.95, static_ceiling * 1.05)
            exc += '\n'
            exc_1 += "AND HEIGHT_MAX BETWEEN %s AND %s" % (static_ceiling * 0.95, static_ceiling * 1.05)
            exc_1 += '\n'
        else:
            pass
            
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
        # grusniy smalik
        pass

ui.pushButton_forward_p.clicked.connect(next_page_plane)
ui.pushButton_back_p.clicked.connect(prev_page_plane)
ui.pushButton_forward_h.clicked.connect(next_page_plane)
ui.pushButton_back_h.clicked.connect(prev_page_plane)
ui.push_forward_all.clicked.connect(next_page_plane)
ui.push_back_all.clicked.connect(prev_page_plane)
ui.push_find_all.clicked.connect(finding)
ui.pushButton_find_p.clicked.connect(finding)
ui.pushButton_find_h.clicked.connect(finding)


ui.show()
sys.exit(app.exec())
connection.close()
