from PyQt5 import QtWidgets, uic
import sys
import sqlite3

connection = sqlite3.connect("database/plane_db.db")
cursor = connection.cursor()
 
app = QtWidgets.QApplication([])
ui = uic.loadUi("ui_designes/ui_design_V_6.ui")

la = ui.tabWidget.currentIndex()

# output_labels = []
# for i in range(0, 100):
#     output_labels.append(QtWidgets.QLabel())
#     output_labels[i].setText(str(i))
# for i in range(0, 100):
#     ui.gridPlanes.addWidget(output_labels[i], 0, i)

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
    # try:
    button = QtWidgets.QApplication.instance().sender()
    exc = ""
    output = []
    if button == ui.pushButton_find_p:
        # finding planes
        exc = "SELECT * FROM aircrafts_2" + "\n"
        exc += """WHERE TYPE = "Самолет"\n"""

        plans_obl_check = False
        plans_obl_array = []

        # Проверка флажков у обл римененния
        if ui.P_sport.isChecked():
            plans_obl_check = True
            plans_obl_array.append("Спортивный")
        if ui.P_med.isChecked():
            plans_obl_check = True
            plans_obl_array.append("Медицинский")
        if ui.P_lab.isChecked():
            plans_obl_check = True
            plans_obl_array.append("Лаборатория")
        if ui.P_gra.isChecked():
            plans_obl_check = True
            plans_obl_array.append("Гражданский")
        if ui.P_paj.isChecked():
            plans_obl_check = True
            plans_obl_array.append("Пажарный")
        if ui.P_milit.isChecked():
            plans_obl_check = True
            plans_obl_array.append("Военный")
        if ui.P_agro.isChecked():
            plans_obl_check = True
            plans_obl_array.append("Сельскохозяйственный")
        if ui.P_ycheb.isChecked():
            plans_obl_check = True
            plans_obl_array.append("Учебный")
        if ui.P_pro.isChecked():
            plans_obl_check = True
            plans_obl_array.append("Проект")
        # Проверка флажков у назначения

        plane_naz_check = False
        plane_naz_array = []
        if ui.P_pere.isChecked():
            plane_naz_check = True
            plane_naz_array.append("Перехватчик")
        if ui.P_bomb.isChecked():
            plane_naz_check = True
            plane_naz_array.append("Бомбардировщик")
        if ui.P_evak.isChecked():
            plane_naz_check = True
            plane_naz_array.append("Эвакуационный")
        if ui.P_istreb.isChecked():
            plane_naz_check = True
            plane_naz_array.append("Истребитель")
        if ui.P_trans.isChecked():
            plane_naz_check = True
            plane_naz_array.append("Транспортный")
        if ui.P_pas.isChecked():
            plane_naz_check = True
            plane_naz_array.append("Пассажирский")
        if ui.P_strat.isChecked():
            plane_naz_check = True
            plane_naz_array.append("Стратегический")
        if ui.P_gruz.isChecked():
            plane_naz_check = True
            plane_naz_array.append("Грузовой")
        if ui.P_shturm.isChecked():
            plane_naz_check = True
            plane_naz_array.append("Штурмовик")
        if ui.P_razv.isChecked():
            plane_naz_check = True
            plane_naz_array.append("Разведка")

        plans_country_check = False
        plane_country_array = []
        # Проверка флажков у стран самолётов
        if ui.P_coun_cb_Rus.isChecked():
            plans_country_check = True
            plane_country_array.append("РФ")
        if ui.P_coun_cb_USSR.isChecked():
            plans_country_check = True
            plane_country_array.append("СССР")
        if ui.P_coun_cb_Amer.isChecked():
            plans_country_check = True
            plane_country_array.append("США")
        if ui.P_coun_cb_Chinazes.isChecked():
            plans_country_check = True
            plane_country_array.append("Китай")
        if ui.P_coun_cb_GBrit.isChecked():
            plans_country_check = True
            plane_country_array.append("Европа")
        if ui.P_coun_cb_Itali.isChecked():
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
        if plans_obl_check:
            exc += """AND APPLICATION IN ('%s')\n""" % ("""', '""".join(plans_obl_array))
        if plane_naz_check:
            exc += """AND PURPROSE IN ('%s')\n""" % ("""', '""".join(plane_naz_array))

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
        exc += gap_checking(ui.P_size_line_razmax_ot, ui.P_size_line_razmax_do, "WING_SPAN_MAX")

        # checking wing area
        exc += gap_checking(ui.P_size_line_plosh_ot, ui.P_size_line_plosh_do, "WING_AREA")

        # checking wing sweep
        exc += gap_checking(ui.P_size_line_strel_ot, ui.P_size_line_strel_do, "WING_SWEEP_MAX")

        # checking crew
        exc += gap_checking(ui.P_load_line_crew_ot, ui.P_load_line_crew_do, "CREW")

        # checking armament
        exc += gap_checking(ui.P_load_line_comlo_ot, ui.P_load_line_comlo_do, "ARMAMENT")

        # checking passengers capacity
        exc += gap_checking(ui.P_load_line_pascap_ot, ui.P_load_line_pascap_do, "PASSENGERS")

        # checking payload
        exc += gap_checking(ui.P_load_line_maxlo_ot, ui.P_load_line_maxlo_do, "PAYLOAD")

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
        # Провекрка флажков у обл применения верт
        heli_obl_check = False
        heli_obl_array = []
        if ui.H_sport.isChecked():
            heli_obl_check = True
            heli_obl_array.append("Спортивный")
        if ui.H_med.isChecked():
            heli_obl_check = True
            heli_obl_array.append("Мудицинский")
        if ui.H_lab.isChecked():
            heli_obl_check = True
            heli_obl_array.append("Лаборатория")
        if ui.H_gra.isChecked():
            heli_obl_check = True
            heli_obl_array.append("Гражданский")
        if ui.H_milit.isChecked():
            heli_obl_check = True
            heli_obl_array.append("Военный")
        if ui.H_paj.isChecked():
            heli_obl_check = True
            heli_obl_array.append("Пожарный")
        if ui.H_ycheb.isChecked():
            heli_obl_check = True
            heli_obl_array.append("Учебный")
        if ui.H_pro.isChecked():
            heli_obl_check = True
            heli_obl_array.append("Проект")

        # Проверка флажков у назначения верт
        heli_naz_check = False
        heli_naz_array = []
        if ui.H_shturm.isChecked():
            heli_naz_check = True
            heli_naz_array.append("Штурмовик")
        if ui.H_gruz.isChecked():
            heli_naz_check = True
            heli_naz_array.append("Грузовой")
        if ui.H_pas.isChecked():
            heli_naz_check = True
            heli_naz_array.append("Пассажирский")
        if ui.H_ydar.isChecked():
            heli_naz_check = True
            heli_naz_array.append("Ударный")
        if ui.H_evak.isChecked():
            heli_naz_check = True
            heli_naz_array.append("Эвакуационный")



        # Проверка флажков у стран вертолётов
        heli_country_check = False
        heli_country_array = []
        if ui.H_coun_cb_Rus.isChecked():
            heli_country_check = True
            heli_country_array.append("РФ")
        if ui.H_coun_cb_USSR.isChecked():
            heli_country_check = True
            heli_country_array.append("СССР")
        if ui.H_coun_cb_Amer.isChecked():
            heli_country_check = True
            heli_country_array.append("США")
        if ui.H_coun_cb_Chinazes.isChecked():
            heli_country_check = True
            heli_country_array.append("Китай")
        if ui.H_coun_cb_GBrit.isChecked():
            heli_country_check = True
            heli_country_array.append("Европа")
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
        if ui.H_eng_type_cb_PD.isChecked():
            heli_engine_check = True
            heli_engine_array.append("ПД")

        # finding helicopters
        exc = "SELECT * FROM aircrafts_2" + "\n"
        exc += """WHERE TYPE = "Вертолет"\n"""
        # creating exc for country and engine type

        if heli_engine_check:
            exc += """AND ENGINE_TYPE IN ('%s')\n""" % ("""', '""".join(heli_engine_array))
        if heli_country_check:
            exc += """AND COUNTRY IN ('%s')\n""" % ("""', '""".join(heli_country_array))
        if heli_naz_check:
            exc += """AND PURPROSE IN ('%s')\n""" % ("""', '""".join(heli_naz_array))
        if heli_obl_check:
            exc += """AND APPLICATION IN ('%s')\n""" % ("""', '""".join(heli_obl_array))

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
        exc += gap_checking(ui.H_load_line_maxlo_ot, ui.H_load_line_maxlo_ot, "PAYLOAD")

        # checking fligth cruise speed
        exc += gap_checking(ui.H_fl_line_cruis_ot, ui.H_fl_line_cruis_ot, "SPEED_NORMAL")

        # checking fligth max speed
        exc += gap_checking(ui.H_fl_line_maxsp_ot, ui.H_fl_line_maxsp_do, "SPEED_MAX")

        # checking fligth range
        exc += gap_checking(ui.H_fl_line_rang_ot, ui.H_fl_line_rang_do, "RANGE")

        # checking static ceiling
        exc += gap_checking(ui.H_fl_line_sthi_ot, ui.H_fl_line_sthi_do, "STATIC_CEILING")

        # checking practice ceiling
        exc += gap_checking(ui.H_taga_ot, ui.H_taga_do, "ENGINE_ROD")
        exc += gap_checking(ui.H_fl_line_prhi_ot, ui.H_fl_line_prhi_do, "SERVICE_CEILING")
        exc += gap_checking(ui.H_rash_ot, ui.H_rash_do, "ENGINE_CONSUMPTION")

        print(exc)
        cursor.execute(exc)
        output = cursor.fetchall()

    elif button == ui.push_find_all:

        # Проверка флажков у обл римененния
        all_obl_check = False
        all_obl_array = []
        if ui.ALL_sport.isChecked():
            all_obl_check = True
            all_obl_array.append("Спортивный")
        if ui.ALL_med.isChecked():
            all_obl_check = True
            all_obl_array.append("Медицинский")
        if ui.ALL_lab.isChecked():
            all_obl_check = True
            all_obl_array.append("Лаборатория")
        if ui.ALL_gra.isChecked():
            all_obl_check = True
            all_obl_array.append("Гражданский")
        if ui.ALL_paj.isChecked():
            all_obl_check = True
            all_obl_array.append("Пожарный")
        if ui.ALL_milit.isChecked():
            all_obl_check = True
            all_obl_array.append("Военный")
        if ui.ALL_agro.isChecked():
            all_obl_check = True
            all_obl_array.append("Сельскохозяйственный")
        if ui.ALL_ycheb.isChecked():
            all_obl_check = True
            all_obl_array.append("Учебный")
        if ui.ALL_pro.isChecked():
            all_obl_check = True
            all_obl_array.append("Проект")

        # Проверка флажков у назначения
        all_naz_check = False
        all_naz_array = []
        if ui.ALL_pere.isChecked():
            all_naz_check = True
            all_naz_array.append("Перехватчик")
        if ui.ALL_bomb.isChecked():
            all_naz_check = True
            all_naz_array.append("Бомбардировщик")
        if ui.ALL_evak.isChecked():
            all_naz_check = True
            all_naz_array.append("Эвакуационный")
        if ui.ALL_istreb.isChecked():
            all_naz_check = True
            all_naz_array.append("Истребитель")
        if ui.ALL_trans.isChecked():
            all_naz_check = True
            all_naz_array.append("Транспортный")
        if ui.ALL_pas.isChecked():
            all_naz_check = True
            all_naz_array.append("Пассажирский")
        if ui.ALL_strat.isChecked():
            all_naz_check = True
            all_naz_array.append("Стратегический")
        if ui.ALL_gruz.isChecked():
            all_naz_check = True
            all_naz_array.append("Грузовой")
        if ui.ALL_shturm.isChecked():
            all_naz_check = True
            all_naz_array.append("Штурмовик")
        if ui.ALL_razv.isChecked():
            all_naz_check = True
            all_naz_array.append("Разведка")
        if ui.ALL_ydar.isChecked():
            all_naz_check = True
            all_naz_array.append("Ударный")

        # Проверка флажков на странах всех ла
        all_country_check = False
        all_country_array = []
        if ui.ALL_coun_cb_Rus.isChecked():
            all_country_check = True
            all_country_array.append("РФ")
        if ui.ALL_coun_cb_USSR.isChecked():
            all_country_check = True
            all_country_array.append("СССР")
        if ui.ALL_coun_cb_Amer.isChecked():
            all_country_check = True
            all_country_array.append("США")
        if ui.ALL_coun_cb_Chinazes.isChecked():
            all_country_check = True
            all_country_array.append("Китай")
        if ui.ALL_coun_cb_GBrit.isChecked():
            all_country_check = True
            all_country_array.append("Европа")
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
        if ui.ALL_eng_type_cb_TRDD.isChecked():
            all_engine_check = True
            all_angine_array.append("ТРДД")
        if ui.ALL_eng_type_cb_TRD.isChecked():
            all_engine_check = True
            all_angine_array.append("ТРД")
        if ui.ALL_eng_type_cb_TVD.isChecked():
            all_engine_check = True
            all_angine_array.append("ТВД")
        if ui.ALL_eng_type_cb_PD.isChecked():
            all_engine_check = True
            all_angine_array.append("ПД")
        if ui.ALL_eng_type_cb_GTD.isChecked():
            all_engine_check = True
            all_angine_array.append("ГТД")
        # finding all

        exc = "SELECT * FROM aircrafts_2" + "\n"
        exc += """WHERE TYPE in ("Вертолет", "Самолет")\n"""

        # exc for engine type and country
        if all_engine_check:
            exc += """AND ENGINE_TYPE IN ('%s')\n""" % ("""', '""".join(all_angine_array))
        if all_country_check:
            exc += """AND COUNTRY IN ('%s')\n""" % ("""', '""".join(all_country_array))
        if all_obl_check:
            exc += """AND APPLICATION IN ('%s')\n""" % ("""', '""".join(all_obl_array))
        if all_naz_check:
            exc += """AND PURPROSE IN ('%s')\n""" % ("""', '""".join(all_naz_array))

        # checking year
        exc += gap_checking(ui.ALL_year_line_ot, ui.ALL_year_line_do, "YEAR")   

        # checking mass empty
        exc += gap_checking(ui.ALL_wei_line_sob_ot, ui.ALL_wei_line_sob_do, "MASS_EMPTY")

        # checking mass normal
        exc += gap_checking(ui.ALL_wei_line_norm_ot, ui.ALL_wei_line_norm_do, "MASS_NORMAL")

        # checking mass max
        exc += gap_checking(ui.ALL_wei_line_max_ot, ui.ALL_wei_line_max_do, "MASS_MAXIMAL")

        # checking size length
        exc += gap_checking(ui.ALL_size_line_long_ot, ui.ALL_size_line_long_do, "LEN")

        # checking size height
        exc += gap_checking(ui.ALL_size_line_high_ot, ui.ALL_size_line_high_do, "HEIGTH")

        # checking crew
        exc += gap_checking(ui.ALL_load_line_crew_ot, ui.ALL_load_line_crew_do, "CREW")

        # checking armament
        exc += gap_checking(ui.ALL_load_line_comlo_ot, ui.ALL_load_line_comlo_do, "ARMAMENT")

        # checking passengers
        exc += gap_checking(ui.ALL_load_line_pascap_ot, ui.ALL_load_line_pascap_do, "PASSENGERS")

        # checking max load
        exc += gap_checking(ui.ALL_load_line_maxlo_ot, ui.ALL_load_line_maxlo_do, "PAYLOAD")

        # checking fligth cruise speed
        exc += gap_checking(ui.ALL_fl_line_cruis_ot, ui.ALL_fl_line_cruis_do, "SPEED_NORMAL")

        # checking fligth max speed
        exc += gap_checking(ui.ALL_fl_line_maxsp_ot, ui.ALL_fl_line_maxsp_do, "SPEED_MAX")

        # checking fligth range
        exc += gap_checking(ui.ALL_fl_line_rang_ot, ui.ALL_fl_line_rang_do, "RANGE")

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

    print(output)
    output_labels_names = []
    
    output_labels_tech = []
    for i in range(len(output)):
        output_labels_names.append(QtWidgets.QLabel())
        output_labels_names[i].setText(output[i][1])
    for i in range(len(output)):
        output_labels_tech.append(QtWidgets.QLabel())
        output_string = '\n'.join([str(x) for x in output[i][2:]])
        output_labels_tech[i].setText(output_string)
    if output != []:
        if button == ui.pushButton_find_p:
            for i in reversed(range(ui.gridPlanes.count())): 
                ui.gridPlanes.itemAt(i).widget().setParent(None)
            for i in range(len(output_labels_names)):
                    ui.gridPlanes.addWidget(output_labels_names[i], 0, i)
                    ui.gridPlanes.addWidget(output_labels_tech[i], 1, i)
        elif button == ui.pushButton_find_h:
            for i in reversed(range(ui.gridHeli.count())): 
                ui.gridHeli.itemAt(i).widget().setParent(None)
            for i in range(len(output_labels_names)):
                    ui.gridHeli.addWidget(output_labels_names[i], 0, i)
                    ui.gridHeli.addWidget(output_labels_tech[i], 1, i)
        elif button == ui.push_find_all:
            for i in reversed(range(ui.gridAll.count())): 
                ui.gridAll.itemAt(i).widget().setParent(None)
            for i in range(len(output_labels_names)):
                    ui.gridAll.addWidget(output_labels_names[i], 0, i)
                    ui.gridAll.addWidget(output_labels_tech[i], 1, i)
    else:
        msg_box = QtWidgets.QMessageBox.information(None, "Ошибка", "К сожаления ни одного летательного аппарата с такими техническими характеристиками не было найдено. Измените критерии поиска и попробуйте еще раз.")
    # except Exception:
    #     print("type error")
    #     pass
    # except Exception:
    #     print('Error')

def clear():
    # прверить на какой стр нажата кнопка, затем очистить все лайны и боксы на этой стр
    button = QtWidgets.QApplication.instance().sender()
    
    if button == ui.pushButton_clear_plane:
        for i in reversed(range(ui.gridPlanes.count())): 
            ui.gridPlanes.itemAt(i).widget().setParent(None)
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
        ui.P_fl_line_rang_do.clear()
        ui.P_fl_line_maxhi_ot.clear()
        ui.P_fl_line_maxhi_do.clear()

        ui.P_taga_ot.clear()
        ui.P_taga_do.clear()
        ui.P_rash_ot.clear()
        ui.P_rash_do.clear()

        # очистка всех чекбоксов в сомолётах
        ui.P_gra.setChecked(False)
        ui.P_med.setChecked(False)
        ui.P_lab.setChecked(False)
        ui.P_sport.setChecked(False)
        ui.P_paj.setChecked(False)
        ui.P_milit.setChecked(False)
        ui.P_agro.setChecked(False)
        ui.P_ycheb.setChecked(False)
        ui.P_pro.setChecked(False)

        ui.P_pere.setChecked(False)
        ui.P_istreb.setChecked(False)
        ui.P_bomb.setChecked(False)
        ui.P_trans.setChecked(False)
        ui.P_pas.setChecked(False)
        ui.P_strat.setChecked(False)
        ui.P_evak.setChecked(False)
        ui.P_gruz.setChecked(False)
        ui.P_shturm.setChecked(False)
        ui.P_razv.setChecked(False)

        ui.P_coun_cb_Rus.setChecked(False)
        ui.P_coun_cb_Amer.setChecked(False)
        ui.P_coun_cb_GBrit.setChecked(False)
        ui.P_coun_cb_Fran.setChecked(False)
        ui.P_coun_cb_USSR.setChecked(False)
        ui.P_coun_cb_Chinazes.setChecked(False)
        ui.P_coun_cb_Itali.setChecked(False)
        ui.P_coun_cb_Spain.setChecked(False)

        ui.P_eng_type_cb_TRDD.setChecked(False)
        ui.P_eng_type_cb_TVD.setChecked(False)
        ui.P_eng_type_cb_PD.setChecked(False)
        ui.P_eng_type_cb_TRD.setChecked(False)
        ui.P_eng_type_cb_GTD.setChecked(False)

        ui.P_sport.setChecked(False)
        ui.P_agro.setChecked(False)
        ui.P_gra.setChecked(False)
        ui.P_lab.setChecked(False)
        ui.P_med.setChecked(False)
        ui.P_milit.setChecked(False)
        ui.P_paj.setChecked(False)
        ui.P_pro.setChecked(False)
        ui.P_ycheb.setChecked(False)

        ui.P_bomb.setChecked(False)
        ui.P_evak.setChecked(False)
        ui.P_gruz.setChecked(False)
        ui.P_istreb.setChecked(False)
        ui.P_pas.setChecked(False)
        ui.P_pere.setChecked(False)
        ui.P_razv.setChecked(False)
        ui.P_shturm.setChecked(False)
        ui.P_strat.setChecked(False)
        ui.P_trans.setChecked(False)

    if button == ui.pushButton_clear_heli:
        # очистка всех лайнов в вертолётах
        for i in reversed(range(ui.gridHeli.count())): 
            ui.gridHeli.itemAt(i).widget().setParent(None)
        ui.H_year_line_ot.clear()
        ui.H_year_line_do.clear()

        ui.H_wei_line_sob_ot.clear()
        ui.H_wei_line_norm_ot.clear()
        ui.H_wei_line_max_ot.clear()
        ui.H_wei_line_sob_do.clear()
        ui.H_wei_line_norm_do.clear()
        ui.H_wei_line_max_do.clear()

        ui.H_size_line_long_ot.clear()
        ui.H_size_line_high_ot.clear()
        ui.H_size_line_diamnes_ot.clear()
        ui.H_size_line_diamrul_ot.clear()
        ui.H_size_line_long_do.clear()
        ui.H_size_line_high_do.clear()
        ui.H_size_line_diamnes_do.clear()
        ui.H_size_line_diamrul_do.clear()

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
        ui.H_fl_line_rang_ot.clear()
        ui.H_fl_line_sthi_ot.clear()
        ui.H_fl_line_prhi_ot.clear()
        ui.H_fl_line_cruis_do.clear()
        ui.H_fl_line_maxsp_do.clear()
        ui.H_fl_line_rang_do.clear()
        ui.H_fl_line_sthi_do.clear()
        ui.H_fl_line_prhi_do.clear()

        ui.H_taga_ot.clear()
        ui.H_taga_do.clear()
        ui.H_rash_ot.clear()
        ui.H_rash_do.clear()

        # очистка всех боксов в вертолётах
        ui.H_gra.setChecked(False)
        ui.H_med.setChecked(False)
        ui.H_lab.setChecked(False)
        ui.H_sport.setChecked(False)
        ui.H_paj.setChecked(False)
        ui.H_milit.setChecked(False)
        ui.H_ycheb.setChecked(False)
        ui.H_pro.setChecked(False)

        ui.H_trans.setChecked(False)
        ui.H_pas.setChecked(False)
        ui.H_ydar.setChecked(False)
        ui.H_evak.setChecked(False)
        ui.H_gruz.setChecked(False)
        ui.H_shturm.setChecked(False)
        ui.H_razv.setChecked(False)

        ui.H_coun_cb_Rus.setChecked(False)
        ui.H_coun_cb_Amer.setChecked(False)
        ui.H_coun_cb_GBrit.setChecked(False)
        ui.h_coun_cb_Fran.setChecked(False)
        ui.H_coun_cb_USSR.setChecked(False)
        ui.H_coun_cb_Chinazes.setChecked(False)
        ui.H_coun_cb_Itali.setChecked(False)
        ui.H_coun_cb_Spain.setChecked(False)

        ui.H_eng_type_cb_TRDD.setChecked(False)
        ui.H_eng_type_cb_TVD.setChecked(False)
        ui.H_eng_type_cb_PD.setChecked(False)
        ui.H_eng_type_cb_TRD.setChecked(False)
        ui.H_eng_type_cb_GTD.setChecked(False)

        ui.H_gra.setChecked(False)
        ui.H_lab.setChecked(False)
        ui.H_med.setChecked(False)
        ui.H_milit.setChecked(False)
        ui.H_paj.setChecked(False)
        ui.H_pro.setChecked(False)
        ui.H_sport.setChecked(False)
        ui.H_ycheb.setChecked(False)

        ui.H_shturm.setChecked(False)
        ui.H_gruz.setChecked(False)
        ui.H_ydar.setChecked(False)

    if button == ui.pushButton_clear_all:
        # очистка всех лайнов в алл
        for i in reversed(range(ui.gridAll.count())): 
            ui.gridAll.itemAt(i).widget().setParent(None)
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
        ui.ALL_fl_line_rang_do.clear()
        ui.ALL_fl_line_maxhi_ot.clear()
        ui.ALL_fl_line_maxhi_do.clear()

        ui.ALL_taga_ot.clear()
        ui.ALL_taga_do.clear()
        ui.ALL_rash_ot.clear()
        ui.ALL_rash_do.clear()

        # очистка всех чекбоксов в вертолётах
        ui.ALL_gra.setChecked(False)
        ui.ALL_med.setChecked(False)
        ui.ALL_lab.setChecked(False)
        ui.ALL_sport.setChecked(False)
        ui.ALL_paj.setChecked(False)
        ui.ALL_milit.setChecked(False)
        ui.ALL_agro.setChecked(False)
        ui.ALL_ycheb.setChecked(False)
        ui.ALL_pro.setChecked(False)

        ui.ALL_pere.setChecked(False)
        ui.ALL_istreb.setChecked(False)
        ui.ALL_bomb.setChecked(False)
        ui.ALL_trans.setChecked(False)
        ui.ALL_pas.setChecked(False)
        ui.ALL_strat.setChecked(False)
        ui.ALL_evak.setChecked(False)
        ui.ALL_gruz.setChecked(False)
        ui.ALL_shturm.setChecked(False)
        ui.ALL_razv.setChecked(False)
        ui.ALL_ydar.setChecked(False)

        ui.ALL_coun_cb_Rus.setChecked(False)
        ui.ALL_coun_cb_Amer.setChecked(False)
        ui.ALL_coun_cb_GBrit.setChecked(False)
        ui.ALL_coun_cb_Fran.setChecked(False)
        ui.ALL_coun_cb_USSR.setChecked(False)
        ui.ALL_coun_cb_Chinazes.setChecked(False)
        ui.ALL_coun_cb_Itali.setChecked(False)
        ui.ALL_coun_cb_Spain.setChecked(False)

        ui.ALL_eng_type_cb_TRDD.setChecked(False)
        ui.ALL_eng_type_cb_TVD.setChecked(False)
        ui.ALL_eng_type_cb_PD.setChecked(False)
        ui.ALL_eng_type_cb_TRD.setChecked(False)
        ui.ALL_eng_type_cb_GTD.setChecked(False)

        ui.ALL_sport.setChecked(False)
        ui.ALL_agro.setChecked(False)
        ui.ALL_gra.setChecked(False)
        ui.ALL_lab.setChecked(False)
        ui.ALL_med.setChecked(False)
        ui.ALL_milit.setChecked(False)
        ui.ALL_paj.setChecked(False)
        ui.ALL_pro.setChecked(False)
        ui.ALL_ycheb.setChecked(False)

        ui.ALL_bomb.setChecked(False)
        ui.ALL_evak.setChecked(False)
        ui.ALL_gruz.setChecked(False)
        ui.ALL_istreb.setChecked(False)
        ui.ALL_pas.setChecked(False)
        ui.ALL_pere.setChecked(False)
        ui.ALL_razv.setChecked(False)
        ui.ALL_shturm.setChecked(False)
        ui.ALL_strat.setChecked(False)
        ui.ALL_trans.setChecked(False)


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
