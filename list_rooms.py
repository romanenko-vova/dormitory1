# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_rooms.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import database as dbd


class Ui_list_rooms(object):

    def fill_list(self):
        room_mas = dbd.list_of_all_rooms()
        i = 0
        for room in room_mas:
            room_data = room[2]
            if "capacity" in room_data:
                item = QtWidgets.QListWidgetItem()
                self.Rooms_info.addItem(item)
                pole = self.Rooms_info.item(i)
                pole.setText(f"Общежитие: {room[0]}; Номер: {room[1]}\nВместимость: {room_data['capacity']}\nЗанято: {room_data['occupied']}\nСтатус – {room_data['status']}\n")
                i += 1

    def openRoom(self):
        from rooms import Ui_Rooms
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Rooms()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, list_rooms):
        list_rooms.setObjectName("list_rooms")
        list_rooms.resize(480, 491)
        list_rooms.setMinimumSize(QtCore.QSize(300, 300))
        list_rooms.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(list_rooms)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 452, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(17)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.import_rooms_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.import_rooms_btn.setMinimumSize(QtCore.QSize(213, 40))
        self.import_rooms_btn.setMaximumSize(QtCore.QSize(213, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.import_rooms_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.import_rooms_btn.setFont(font)
        self.import_rooms_btn.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.import_rooms_btn.setObjectName("import_rooms_btn")
        self.horizontalLayout.addWidget(self.import_rooms_btn)
        self.back_to_rooms_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.back_to_rooms_btn.setMinimumSize(QtCore.QSize(220, 40))
        self.back_to_rooms_btn.setMaximumSize(QtCore.QSize(220, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.back_to_rooms_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.back_to_rooms_btn.setFont(font)
        self.back_to_rooms_btn.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.back_to_rooms_btn.setObjectName("back_to_rooms_btn")

        self.back_to_rooms_btn.clicked.connect(self.openRoom)
        self.back_to_rooms_btn.clicked.connect(list_rooms.close)

        self.horizontalLayout.addWidget(self.back_to_rooms_btn)
        self.Rooms_info = QtWidgets.QListWidget(self.centralwidget)
        self.Rooms_info.setGeometry(QtCore.QRect(20, 89, 440, 371))
        self.Rooms_info.setAutoFillBackground(False)
        self.Rooms_info.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"selection-color: rgb(85, 170, 255);")
        self.Rooms_info.setObjectName("Rooms_info")
        # item = QtWidgets.QListWidgetItem()
        # self.Rooms_info.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.Rooms_info.addItem(item)
        list_rooms.setCentralWidget(self.centralwidget)

        self.retranslateUi(list_rooms)
        QtCore.QMetaObject.connectSlotsByName(list_rooms)
        self.fill_list()

    def retranslateUi(self, list_rooms):
        _translate = QtCore.QCoreApplication.translate
        list_rooms.setWindowTitle(_translate("list_rooms", "Список комнат"))
        self.import_rooms_btn.setText(_translate("list_rooms", "Импортировать в Excel"))
        self.back_to_rooms_btn.setText(_translate("list_rooms", "Вернуться в меню комнат"))
        __sortingEnabled = self.Rooms_info.isSortingEnabled()
        self.Rooms_info.setSortingEnabled(False)
        # item = self.Rooms_info.item(0)
        # item.setText(_translate("list_rooms", "addawd"))
        # item = self.Rooms_info.item(1)
        # item.setText(_translate("list_rooms", "dtyjhn"))
        self.Rooms_info.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    list_rooms = QtWidgets.QMainWindow()
    ui = Ui_list_rooms()
    ui.setupUi(list_rooms)
    list_rooms.show()
    sys.exit(app.exec_())
