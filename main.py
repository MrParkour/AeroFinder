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
        float(input_string)
        return float(input_string)
    except Exception:
        return -1

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
        # если флажок россия стоит то в вида строки добавить россия
        plans_country_check = False
        plane_country_array = []
        if ui.P_coun_cb_Rus.isChecked():
            plans_country_check = True
            plane_country_array.append("Россия")
        if ui.P_coun_cb_USSR.isChecked():
            plans_country_check = True
            plane_country_array.append("СССР")
        
    

    elif button == ui.pushButton_find_h:
        # finding helicopters
        exc = "SELECT * FROM aircrafts" + "\n"
        exc += """WHERE TYPE = "вертолет"\n"""
        # checking year
        year_from = checking_input(ui.H_year_line_ot.text())
        year_to = checking_input(ui.H_year_line_do.text())
        if year_from != -1 and year_to != -1:
            exc += "AND YEAR BETWEEN %s AND %s" % (str(year_from), str(year_to))
            exc += "\n"
        elif year_from == -1 and year_to != -1:
            exc += "AND YEAR <= %s" % (str(year_to))
            exc += "\n"
        elif year_from != -1 and year_to == -1:
            exc += "AND YEAR >= %s" % (str(year_from))
            exc += "\n"
        else:
            pass
        
        # checking mass empty
        mass_empty = checking_input(ui.H_wei_line_sob.text())
        if mass_empty != -1:
            exc += "AND MASS_EMPTY BETWEEN %s AND %s" % (str(mass_empty * 0.95), str(mass_empty * 1.05))
            exc += '\n'
        else:
            pass
        
        # checking mass normal
        mass_normal = checking_input(ui.H_wei_line_norm.text())
        if mass_normal != -1:
            exc += "AND MASS_NORMAL BETWEEN %s AND %s" % (str(mass_normal * 0.95), str(mass_normal * 1.05))
            exc += '\n'
        else:
            pass
        
        # checking mass max
        mass_max = checking_input(ui.H_wei_line_max.text())
        if mass_max != -1:
            exc += "AND MASS_MAXIMAL BETWEEN %s AND %s" % (mass_max * 0.95, mass_max * 1.05)
            exc += '\n'
        else:
            pass

        # checking size length
        length = checking_input(ui.H_size_line_long.text())
        if length != -1:
            exc += "AND LEN BETWEEN %s AND %s" % (length * 0.95, length * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking size height
        high = checking_input(ui.H_size_line_high.text())
        if high != -1:
            exc += "AND HEIGTH BETWEEN %s AND %s" % (high * 0.95, high * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking size main rotor
        diameter_main_rotor = checking_input(ui.H_size_line_Dnes.text())
        if diameter_main_rotor != -1:
            exc += "AND DIAMETR_MAIN_ROTOR BETWEEN %s AND %s" % (diameter_main_rotor * 0.95, diameter_main_rotor * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking size tail rotor
        diameter_tail_rotor = checking_input(ui.H_size_line_Drul.text())
        if diameter_tail_rotor != -1:
            exc += "AND DIAMETR_TAIL_ROTOR BETWEEN %s AND %s" % (diameter_tail_rotor * 0.95, diameter_tail_rotor * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking crew
        crew = checking_input(ui.H_load_line_crew.text())
        if crew != -1:
            exc += "AND CREW BETWEEN %s AND %s" % (crew * 0.95, crew * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking armament
        armament = checking_input(ui.H_load_line_comlo.text())
        if armament != -1:
            exc += "AND ARMAMENT BETWEEN %s AND %s" % (armament * 0.95, armament * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking passengers
        passengers = checking_input(ui.H_load_line_pascap.text())
        if passengers != -1:
            exc += "AND PASSENGERS BETWEEN %s AND %s" % (passengers * 0.95, passengers * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking max load
        max_load = checking_input(ui.H_load_line_maxlo.text())
        if max_load != -1:
            exc += "AND PAYLOAD BETWEEN %s AND %s" % (max_load * 0.95, max_load * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking fligth cruise speed
        fl_cruise_speed = checking_input(ui.H_fl_line_cruis.text())
        if fl_cruise_speed != -1:
            exc += "AND SPEED_NORMAL BETWEEN %s AND %s" % (fl_cruise_speed * 0.95, fl_cruise_speed * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking fligth max speed
        fl_max_speed = checking_input(ui.H_fl_line_maxsp.text())
        if fl_max_speed != -1:
            exc += "AND SPEED_MAX BETWEEN %s AND %s" % (fl_max_speed * 0.95, fl_max_speed * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking fligth range
        fl_range = checking_input(ui.H_fl_line_range.text())
        if fl_range != -1:
            exc += "AND RANGE BETWEEN %s AND %s" % (fl_range * 0.95, fl_range * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking static ceiling
        static_ceiling = checking_input(ui.H_fl_line_sthi.text())
        if static_ceiling != -1:
            exc += "AND STATIC_CEILING BETWEEN %s AND %s" % (static_ceiling * 0.95, static_ceiling * 1.05)
            exc += '\n'
        else:
            pass
        
        # checking practice ceiling
        practice_ceiling = checking_input(ui.H_fl_line_sthi.text())
        if practice_ceiling != -1:
            exc += "AND SERVICE_CEILING BETWEEN %s AND %s" % (practice_ceiling * 0.95, practice_ceiling * 1.05)
            exc += '\n'
        else:
            pass
        print(exc)
        cursor.execute(exc)
        output = cursor.fetchall()
      
    elif button == ui.push_find_all:
        # finding all

        exc = "SELECT * FROM aircrafts" + "\n"
        exc += """WHERE TYPE in ("вертолет", "самолет")\n"""

        # checking year
        year_from = checking_input(ui.lineEdit_31.text())
        year_to = checking_input(ui.lineEdit_36.text())
        if year_from != -1 and year_to != -1:
            exc += "AND YEAR BETWEEN %s AND %s" % (str(year_from), str(year_to))
            exc += "\n"
        elif year_from == -1 and year_to != -1:
            exc += "AND YEAR <= %s" % (str(year_to))
            exc += "\n"
        elif year_from != -1 and year_to == -1:
            exc += "AND YEAR >= %s" % (str(year_from))
            exc += "\n"
        else:
            pass
        
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
        
        # checking static ceiling
        static_ceiling = checking_input(ui.lineEdit_93.text())
        if static_ceiling != -1:
            exc += "AND STATIC_CEILING BETWEEN %s AND %s" % (static_ceiling * 0.95, static_ceiling * 1.05)
            exc += '\n'
            exc_1 += "AND HEIGTH_MAX BETWEEN %s AND %s" % (static_ceiling * 0.95, static_ceiling * 1.05)
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
