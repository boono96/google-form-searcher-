# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verstion2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyautogui
import keyboard
import setting_save_maneger as ssm

class Ui_MainWindow(object):
    def __init__(self) -> None:
        setting_save = ssm.load()
        self.xmouse = int(setting_save['xmouse'])
        self.ymouse = int(setting_save['ymouse'])
        self.key_set = setting_save['set_key']
        self.key_stop = setting_save['key_stop']

    def save(self):
        save_setting = {
            'xmouse' : self.xmouse,
            'ymouse' : self.ymouse,
            'set_key' : self.key_set,
            'key_stop' : self.key_stop,
        }
        ssm.save(save_setting)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(275, 224)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 111, 21))
        self.pushButton.setObjectName("pushButton")
        self.xtextedit = QtWidgets.QTextEdit(self.centralwidget)
        self.xtextedit.setGeometry(QtCore.QRect(10, 90, 111, 21))
        self.xtextedit.setObjectName("xtextedit")
        self.ytextedit = QtWidgets.QTextEdit(self.centralwidget)
        self.ytextedit.setGeometry(QtCore.QRect(140, 90, 111, 21))
        self.ytextedit.setObjectName("ytextedit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 61, 21))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 161, 21))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 70, 61, 21))
        self.label_2.setObjectName("label_2")
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(140, 120, 75, 23))
        self.run_button.setObjectName("run_button")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(170, 10, 91, 31))
        self.save_button.setObjectName("save_button")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 111, 16))
        self.label_4.setObjectName("label_4")
        self.set_button_textedit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.set_button_textedit.setGeometry(QtCore.QRect(50, 150, 31, 31))
        self.set_button_textedit.setObjectName("set_button_textedit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 160, 111, 16))
        self.label_5.setObjectName("label_5")
        self.stop_button_textedit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.stop_button_textedit.setGeometry(QtCore.QRect(170, 150, 31, 31))
        self.stop_button_textedit.setObjectName("stop_button_textedit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 275, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.set_button_textedit.setPlainText(str(self.key_set))
        self.stop_button_textedit.setPlainText(str(self.key_stop))

        self.xtextedit.setPlainText(str(self.xmouse))
        self.ytextedit.setPlainText(str(self.ymouse))

        self.pushButton.clicked.connect(self.set_pos_button)
        self.save_button.clicked.connect(self.save_button_func)
        self.run_button.clicked.connect(self.runprogram)

    
    def set_pos_button(self):
        run = True
        while run:
            if keyboard.is_pressed(self.key_set):
                pos = pyautogui.position()
                self.xmouse = pos.x
                self.ymouse = pos.y
                self.xtextedit.setPlainText(str(self.xmouse))
                self.ytextedit.setPlainText(str(self.ymouse))

                run = False

    def save_button_func(self):
        self.xmouse = self.xtextedit.toPlainText()
        self.ymouse = self.ytextedit.toPlainText()
        self.key_set = self.set_button_textedit.toPlainText()
        self.key_stop = self.stop_button_textedit.toPlainText()
        self.save()

    def runprogram(self):
        running = True
        while running:
            if keyboard.is_pressed(self.key_stop):
                running = False
            if keyboard.is_pressed('control') and keyboard.is_pressed('c'):
                bfm_x,bfm_y = pyautogui.position()
                pyautogui.click(int(self.xmouse),int(self.ymouse))
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('Enter')   
                pyautogui.moveTo(bfm_x,bfm_y)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ABP"))
        self.pushButton.setText(_translate("MainWindow", "set position"))
        self.label.setText(_translate("MainWindow", "x"))
        self.label_3.setText(_translate("MainWindow", "browser searching bar position"))
        self.label_2.setText(_translate("MainWindow", "y"))
        self.run_button.setText(_translate("MainWindow", "run"))
        self.save_button.setText(_translate("MainWindow", "save"))
        self.label_4.setText(_translate("MainWindow", "press              to set"))
        self.label_5.setText(_translate("MainWindow", "press              to set"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

