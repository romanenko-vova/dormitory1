# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_hostel.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import database as dbd

class Ui_list_hostel(object):
    def fill_list(self):
        '''заполняет список'''

        mas = dbd.list_of_dormitories()
        print(mas)
        i = 1
        for person in mas:
            print(person[1]['name'])
            #Допилить чутка

    def openHostel(self):
        from hostel import Ui_hostel
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_hostel()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, list_hostel):
        list_hostel.setObjectName("list_hostel")
        list_hostel.resize(480, 491)
        list_hostel.setMinimumSize(QtCore.QSize(300, 300))
        list_hostel.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(list_hostel)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 20, 471, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(17)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.import_hostel_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.import_hostel_btn.setMinimumSize(QtCore.QSize(195, 40))
        self.import_hostel_btn.setMaximumSize(QtCore.QSize(195, 16777215))
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
        self.import_hostel_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.import_hostel_btn.setFont(font)
        self.import_hostel_btn.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.import_hostel_btn.setObjectName("import_hostel_btn")
        self.horizontalLayout.addWidget(self.import_hostel_btn)
        self.back_to_hostel_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.back_to_hostel_btn.setMinimumSize(QtCore.QSize(240, 40))
        self.back_to_hostel_btn.setMaximumSize(QtCore.QSize(240, 16777215))
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
        self.back_to_hostel_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.back_to_hostel_btn.setFont(font)
        self.back_to_hostel_btn.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.back_to_hostel_btn.setObjectName("back_to_hostel_btn")

        self.back_to_hostel_btn.clicked.connect(self.openHostel)
        self.back_to_hostel_btn.clicked.connect(list_hostel.close)

        self.horizontalLayout.addWidget(self.back_to_hostel_btn)
        self.hostel_info = QtWidgets.QListWidget(self.centralwidget)
        self.hostel_info.setGeometry(QtCore.QRect(20, 89, 440, 371))
        self.hostel_info.setAutoFillBackground(False)
        self.hostel_info.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"selection-color: rgb(85, 170, 255);")
        self.hostel_info.setObjectName("hostel_info")
        item = QtWidgets.QListWidgetItem()
        self.hostel_info.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.hostel_info.addItem(item)
        list_hostel.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(list_hostel)
        self.statusbar.setObjectName("statusbar")
        list_hostel.setStatusBar(self.statusbar)

        self.retranslateUi(list_hostel)
        QtCore.QMetaObject.connectSlotsByName(list_hostel)
        self.fill_list()

    def retranslateUi(self, list_hostel):
        _translate = QtCore.QCoreApplication.translate
        list_hostel.setWindowTitle(_translate("list_hostel", "Список общежитий"))
        self.import_hostel_btn.setText(_translate("list_hostel", "Импортировать в Excel"))
        self.back_to_hostel_btn.setText(_translate("list_hostel", "Вернуться в меню общежитий"))
        __sortingEnabled = self.hostel_info.isSortingEnabled()
        self.hostel_info.setSortingEnabled(False)
        self.hostel_info.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    list_hostel = QtWidgets.QMainWindow()
    ui = Ui_list_hostel()
    ui.setupUi(list_hostel)
    list_hostel.show()
    sys.exit(app.exec_())
