# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'del_facility.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import database as dbd

class Ui_del_facility(object):

    def del_facility(self):
        item = self.NameBox.currentText()
        n = self.NameBox.currentIndex()
        dbd.remove_facility(item.split(" -")[0])
       #self.NameBox.


    def fill_list(self):
        fac_mas = dbd.list_of_facilities()
        i = 0
        for fac in fac_mas:
            self.NameBox.setItemText(i,f"{fac[0]} – {fac[1]}")
            i += 1


    def openHelp(self):
        from facilities import Ui_Facilities
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Facilities()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, del_facility):
        del_facility.setObjectName("del_facility")
        del_facility.resize(680, 140)
        del_facility.setMinimumSize(QtCore.QSize(680, 140))
        del_facility.setMaximumSize(QtCore.QSize(680, 140))
        self.centralwidget = QtWidgets.QWidget(del_facility)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 80, 146, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 20, 431, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(17)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.del_facility_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.del_facility_btn.setMinimumSize(QtCore.QSize(150, 40))
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
        self.del_facility_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.del_facility_btn.setFont(font)
        self.del_facility_btn.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.del_facility_btn.setObjectName("del_facility_btn")
        self.horizontalLayout.addWidget(self.del_facility_btn)
        self.del_facility_btn.clicked.connect(self.del_facility)
        self.back_to_facilities_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.back_to_facilities_btn.setMinimumSize(QtCore.QSize(150, 40))
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
        self.back_to_facilities_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.back_to_facilities_btn.setFont(font)
        self.back_to_facilities_btn.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.back_to_facilities_btn.setObjectName("back_to_facilities_btn")

        self.back_to_facilities_btn.clicked.connect(self.openHelp)
        self.back_to_facilities_btn.clicked.connect(del_facility.close)

        self.horizontalLayout.addWidget(self.back_to_facilities_btn)
        self.NameBox = QtWidgets.QComboBox(self.centralwidget)
        self.NameBox.setGeometry(QtCore.QRect(220, 80, 400, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
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
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
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
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.NameBox.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.NameBox.setFont(font)
        self.NameBox.setToolTip("")
        self.NameBox.setStatusTip("")
        self.NameBox.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.NameBox.setEditable(False)
        self.NameBox.setMaxCount(10)
        self.NameBox.setIconSize(QtCore.QSize(16, 16))
        self.NameBox.setModelColumn(0)
        self.NameBox.setObjectName("NameBox")
        del_facility.setCentralWidget(self.centralwidget)

        self.retranslateUi(del_facility)
        self.NameBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(del_facility)


    def retranslateUi(self, del_facility):
        _translate = QtCore.QCoreApplication.translate
        del_facility.setWindowTitle(_translate("del_facility", "Удаление стоимостей/льгот"))
        self.label.setText(_translate("del_facility", "Название \nстоимости/льготы"))
        self.del_facility_btn.setText(_translate("del_facility", "Удалить"))
        self.back_to_facilities_btn.setText(_translate("del_facility", "Вернуться в меню"))
        fac_mas = dbd.list_of_facilities()
        i = 0
        for i in range(dbd.list_of_facilities()[1]):
            self.NameBox.addItem(f"{fac_mas[0][i][0]} - {fac_mas[0][i][1]}")
            # self.NameBox.setItemText(i, _translate("del_facility", f"{fac[0]} – {fac[1]}"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    del_facility = QtWidgets.QMainWindow()
    ui = Ui_del_facility()
    ui.setupUi(del_facility)
    del_facility.show()
    sys.exit(app.exec_())
