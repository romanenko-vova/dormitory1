# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'red_hostel.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import red_hostel_2
import database as dbd

class Ui_red_hostel(object):

    def fill_list(self):

        self.Hostel_list.clear()
        dorm_number = self.Number_line.text()
        db = dbd.init_firebase()
        dorm_mas = db.child("dormitories").order_by_key().equal_to("dormitory" + str(dorm_number)).get().each()
        if dorm_mas == []:
            self.Number_line.clear()
        else:
            dorm = dorm_mas[0].val()
            self.Hostel_list.addItem(f"Название: {dorm['name']}\nАдрес: {dorm['Адрес']}")

    def edit_hostel(self):
        db = dbd.init_firebase()
        dorm_number = self.Number_line.text()
        choosen_num = self.Hostel_list.currentRow()
        if choosen_num == 0:
            dorm_mas = db.child("dormitories").order_by_key().equal_to("dormitory" + str(dorm_number)).get().each()
            if dorm_mas != []:
                dorm = dorm_mas[0].val()
                buffer_mas = {"number":dorm["number"],"Адрес":dorm["Адрес"]}
                db.child("dormitories").child("buffer1").set(buffer_mas)


    def openRed(self):
        from red_hostel_2 import Ui_red_hostel_2
        self.edit_hostel()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_red_hostel_2()
        self.ui.setupUi(self.window)
        self.window.show()

    def openHostel(self):
        from hostel import Ui_hostel
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_hostel()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, red_hostel):
        red_hostel.setObjectName("red_hostel")
        red_hostel.resize(680, 230)
        red_hostel.setMinimumSize(QtCore.QSize(680, 200))
        red_hostel.setMaximumSize(QtCore.QSize(680, 300))
        self.centralwidget = QtWidgets.QWidget(red_hostel)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 80, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.Number_line = QtWidgets.QLineEdit(self.centralwidget)
        self.Number_line.setGeometry(QtCore.QRect(220, 80, 400, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
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
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
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
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 206, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Number_line.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Number_line.setFont(font)
        self.Number_line.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.Number_line.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.Number_line.setText("")
        self.Number_line.setMaxLength(2)
        self.Number_line.setCursorPosition(0)
        self.Number_line.setObjectName("Number_line")

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 20, 431, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(17)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.find_hostel_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.find_hostel_btn.setMinimumSize(QtCore.QSize(150, 40))
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
        self.find_hostel_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.find_hostel_btn.setFont(font)
        self.find_hostel_btn.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.find_hostel_btn.setObjectName("find_hostel_btn")

        self.find_hostel_btn.clicked.connect(self.fill_list)



        self.horizontalLayout.addWidget(self.find_hostel_btn)
        self.back_to_hostel_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.back_to_hostel_btn.setMinimumSize(QtCore.QSize(150, 40))
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
        self.back_to_hostel_btn.clicked.connect(red_hostel.close)

        self.horizontalLayout.addWidget(self.back_to_hostel_btn)

        self.red_hostel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.red_hostel_btn.setGeometry(QtCore.QRect(480, 150, 195, 40))
        self.red_hostel_btn.setMinimumSize(QtCore.QSize(150, 40))
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
        self.red_hostel_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.red_hostel_btn.setFont(font)
        self.red_hostel_btn.setStyleSheet("background-color: rgb(135, 206, 235);")
        self.red_hostel_btn.setObjectName("red_hostel_btn")

        self.red_hostel_btn.clicked.connect(self.openRed)
        self.red_hostel_btn.clicked.connect(red_hostel.close)

        self.Hostel_list = QtWidgets.QListWidget(self.centralwidget)
        self.Hostel_list.setGeometry(QtCore.QRect(40, 140, 400, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(21)
        sizePolicy.setHeightForWidth(self.Hostel_list.sizePolicy().hasHeightForWidth())
        self.Hostel_list.setSizePolicy(sizePolicy)
        self.Hostel_list.setMinimumSize(QtCore.QSize(400, 30))
        self.Hostel_list.setMaximumSize(QtCore.QSize(400, 60))
        self.Hostel_list.setSizeIncrement(QtCore.QSize(0, 30))
        self.Hostel_list.setBaseSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Hostel_list.setFont(font)
        self.Hostel_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.Hostel_list.setObjectName("Hostel_list")
        red_hostel.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(red_hostel)
        self.statusbar.setObjectName("statusbar")
        red_hostel.setStatusBar(self.statusbar)

        self.retranslateUi(red_hostel)
        QtCore.QMetaObject.connectSlotsByName(red_hostel)

    def retranslateUi(self, red_hostel):
        _translate = QtCore.QCoreApplication.translate
        red_hostel.setWindowTitle(_translate("red_hostel", "Редактирование общежитий"))
        self.label.setText(_translate("red_hostel", "Номер общежития"))
        self.Number_line.setInputMask(_translate("red_hostel", "09"))
        self.find_hostel_btn.setText(_translate("red_hostel", "Найти"))
        self.back_to_hostel_btn.setText(_translate("red_hostel", "Вернуться в меню общежитий"))
        self.red_hostel_btn.setText(_translate("red_hostel", "Редактирование"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    red_hostel = QtWidgets.QMainWindow()
    ui = Ui_red_hostel()
    ui.setupUi(red_hostel)
    red_hostel.show()
    sys.exit(app.exec_())
