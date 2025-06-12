from PyQt5 import QtWidgets, uic
import sys
 
app = QtWidgets.QApplication([])
ui = uic.loadUi("ui_desingnes/ui_design_V_3.ui")

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

ui.pushButton_forward_p.clicked.connect(next_page_plane)
ui.pushButton_back_p.clicked.connect(prev_page_plane)
ui.pushButton_forward_h.clicked.connect(next_page_plane)
ui.pushButton_back_h.clicked.connect(prev_page_plane)
ui.push_forward_all.clicked.connect(next_page_plane)
ui.push_back_all.clicked.connect(prev_page_plane)

# def button_prev_page():
#     print("prev page")
#     ui.stackedWidget.setCurrentIndex(0)

# ui.pushButton_forward.clicked.connect(button_next_page)
# ui.pushButton_back.clicked.connect(button_prev_page)

ui.show()
sys.exit(app.exec())
