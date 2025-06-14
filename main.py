from PyQt5 import QtWidgets, uic
import sys
import sqlite3

connection = sqlite3.connect("data/plane_db.db")
cursor = connection.cursor()
 
app = QtWidgets.QApplication([])
ui = uic.loadUi("ui_desingnes/ui_design_V_4.ui")

la = ui.tabWidget.currentIndex()


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
    if button == ui.pushButton_find_p:  
        # finding planes
        # если флажок россия стоит то в вида строки добавить россия
        plany_country_check = False
        plane_country_array = []
        if ui.P_coun_cb_Rus.isChecked():
            plany_country_check = True
            plane_country_array.append("россия")
    elif button == ui.pushButton_find_h:
        # finding helicopters
        obj = ui.stackedWidget_heli
    elif button == ui.push_find_all:
        # finding all
        obj = ui.stackedWidget_all
    
    # сделать проверку на флажки
    # записать итог в строку вида "спортивный, перехватчик, истребитель"
    # добавить переменную bool которая показывается есть ли чтото или нет


    exc = """SELECT * FROM aircrafts
WHERE TYPE IN () 
AND COUNTRY IN () 
AND YEAR BETWEEN X*0.9 AND X*1.1
AND APPLICATION IN ("")
AND PURPOSE
AND ENGINE_NAME
AND ENGINE_TYPE
AND ENGINE_ROD
AND ENGINE_FORSAGE_ROD
AND ENGINE_CONSUMPTION
AND MASS_EMPTY
AND MASS_NORMAL
AND MASS_MAXIMAL
AND LENGTH
AND HEIGHT
AND WING_SPAN
AND WING_AREA
AND WING_SWEEP
AND WHEEL_BASE
AND WHEEL_TRACK
AND SPEED_MAX
AND SPEED_NORMAL
AND RANGE
AND HEIGHT_MAX
AND SERVICE_CEILING
AND STATIC_SEILING
AND CREW
AND ARMAMENT
AND PASSENGERS
AND PAYLOAD;"""
    cursor.execute(exc)
    output = cursor.fetchall()
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
