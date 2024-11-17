import asyncio
from aplication_main import ApplicationLogic
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1419, 570)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(380, 0, 91, 551))
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 61, 61))
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/app_icon_3.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 91, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/app_icon_2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 61, 61))
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img/app_icon_1.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 381, 551))
        self.label.setMouseTracking(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/app_0.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(345, 6, 20, 20))
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("img/app_icon_X.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 0, 51, 31))
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_6.setStyleSheet("background-color: red;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(490, 0, 381, 551))
        self.widget_2.setObjectName("widget_2")
        self.label_7 = QtWidgets.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 381, 551))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("img/app_base.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.progressBar = QtWidgets.QProgressBar(self.widget_2)
        self.progressBar.setGeometry(QtCore.QRect(20, 480, 341, 23))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: orange;\n"
"    width: 20px;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(10, 513, 361, 31))
        self.label_8.setStyleSheet("color: #ea622b;\n"
"")
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser.setGeometry(QtCore.QRect(20, 80, 341, 391))
        self.textBrowser.setStyleSheet("QTextBrowser {\n"
"    background-color: black;\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(90, 510, 281, 31))
        self.label_9.setStyleSheet("color: #ea622b;\n"
"")
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(880, 0, 381, 551))
        self.widget_3.setObjectName("widget_3")
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 381, 551))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("img/app_base.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.widget_3)
        self.label_11.setGeometry(QtCore.QRect(10, 513, 361, 31))
        self.label_11.setStyleSheet("color: #ea622b;\n"
"")
        self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.widget_3)
        self.label_12.setGeometry(QtCore.QRect(10, 40, 361, 31))
        self.label_12.setStyleSheet("color: white;\n"
"font-size: 14px;\n"
"")
        self.label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.line = QtWidgets.QFrame(self.widget_3)
        self.line.setGeometry(QtCore.QRect(10, 60, 361, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.comboBox = QtWidgets.QComboBox(self.widget_3)
        self.comboBox.setGeometry(QtCore.QRect(180, 80, 181, 31))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet("color: #e5e5e5;\n"
"min-width: 80px;\n"
"border: 1px solid gray;\n"
"cursor: pointer;\n"
"background-color: transparent;\n"
"line-height: 18px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_13 = QtWidgets.QLabel(self.widget_3)
        self.label_13.setGeometry(QtCore.QRect(10, 80, 171, 31))
        self.label_13.setStyleSheet("color: white;\n"
"font-size: 14px;\n"
"")
        self.label_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_13.setScaledContents(False)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setGeometry(QtCore.QRect(70, 470, 251, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: #ff784d;\n"
"color: #e5e5e5;\n"
"font-size: 20px;\n"
"border: none;\n"
"font-family: inherit;\n"
"cursor: pointer;")
        self.pushButton.setObjectName("pushButton")
        self.label_14 = QtWidgets.QLabel(self.widget_3)
        self.label_14.setGeometry(QtCore.QRect(10, 470, 51, 41))
        self.label_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_14.setStyleSheet("cursor: pointer;")
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("img/back.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(90, 40, 281, 31))
        self.label_15.setStyleSheet("color: white;\n"
"font-size: 14px;\n"
"")
        self.label_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_15.setScaledContents(False)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 460, 251, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: #ff784d;\n"
"color: #e5e5e5;\n"
"font-size: 20px;\n"
"border: none;\n"
"font-family: inherit;\n"
"cursor: pointer;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(80, 400, 281, 51))
        self.label_16.setStyleSheet("color: white;\n"
"font-size:20px;")
        self.label_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_16.setScaledContents(False)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 80, 261, 31))
        self.lineEdit.setStyleSheet("width: 100%;\n"
"    height: 36px;\n"
"    padding: 2px 12px 0;\n"
"    background-color: #262626;\n"
"    border: none;\n"
"    font-family: inherit;\n"
"    font-size: 16px;\n"
"    line-height: 36px;\n"
"    color: gray;\n"
"    transition: color .15s ease;\n"
"    cursor: pointer;")
        self.lineEdit.setObjectName("lineEdit")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(90, 120, 281, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(90, 130, 281, 31))
        self.label_17.setStyleSheet("color: white;\n"
"font-size:20px;")
        self.label_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_17.setScaledContents(False)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(90, 170, 281, 31))
        self.label_18.setStyleSheet("color: orange;\n"
"font-size:30px;")
        self.label_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_18.setScaledContents(False)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(90, 210, 281, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label.raise_()
        self.label_6.raise_()
        self.widget.raise_()
        self.label_5.raise_()
        self.widget_2.raise_()
        self.label_9.raise_()
        self.widget_3.raise_()
        self.label_15.raise_()
        self.pushButton_2.raise_()
        self.label_16.raise_()
        self.lineEdit.raise_()
        self.line_2.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.line_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # -----------------------------------------------------------
        self.label_18.setText("online")
        self.logic = ApplicationLogic()
        # Conectează semnalul din logică la funcția de actualizare a textului
        self.logic.update_text_signal.connect(self.update_text_browser)
        # Apelează funcția din logică (pentru exemplu)
        self.logic.Run_launcher()
        self.pushButton_2.clicked.connect(self.logic.Run_launcher)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "created by Marter"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Debug-Tool: loading...</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "created by Marter"))
        self.label_11.setText(_translate("MainWindow", "created by Marter"))
        self.label_12.setText(_translate("MainWindow", "Setings:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "2GB"))
        self.comboBox.setItemText(1, _translate("MainWindow", "3GB"))
        self.comboBox.setItemText(2, _translate("MainWindow", "4GB"))
        self.comboBox.setItemText(3, _translate("MainWindow", "6GB"))
        self.label_13.setText(_translate("MainWindow", "Select the amount of RAM:"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.label_15.setText(_translate("MainWindow", "Enter Accaunt Key:"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))
        self.label_16.setText(_translate("MainWindow", "Hello!"))
        self.lineEdit.setText(_translate("MainWindow", "sss"))
        self.label_17.setText(_translate("MainWindow", "Server Status"))
        self.label_18.setText(_translate("MainWindow", "Offline"))

    def update_text_browser(self, text):
        # Actualizează textul în textBrowser
        try:

            self.textBrowser.append(text)
        except Exception as e:
            print(f"error{e}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


    def closeApp():
        sys.exit(app.exec_())