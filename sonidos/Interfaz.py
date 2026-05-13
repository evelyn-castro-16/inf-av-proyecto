# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(100, 50, 121, 41))
        self.pushButton_1.setStyleSheet(u"QPushButton{\n"
"\n"
"	color: white;\n"
"\n"
"	background-color: #2979ff;\n"
"\n"
"	border-style: solid;\n"
"\n"
"	border-width: 2px;\n"
"\n"
"	border-radius: 8px;\n"
"\n"
"	border-color: #0000ff;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"	background-color: #5393ff;\n"
"\n"
"	border-color: #00ff00;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"	background-color: #0b63d6;\n"
"\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"\n"
"	background-color: #cfd8e6;\n"
"\n"
"	color: #8a98b8;\n"
"\n"
"}\n"
" ")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(300, 50, 121, 41))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(490, 50, 121, 41))
        self.lineEdit_1 = QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setGeometry(QRect(190, 350, 113, 21))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(340, 350, 113, 21))
        self.tableWidget_1 = QTableWidget(self.centralwidget)
        self.tableWidget_1.setObjectName(u"tableWidget_1")
        self.tableWidget_1.setGeometry(QRect(100, 110, 551, 211))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(490, 350, 113, 21))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(90, 350, 75, 24))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(90, 430, 75, 24))
        self.spinBox_1 = QSpinBox(self.centralwidget)
        self.spinBox_1.setObjectName(u"spinBox_1")
        self.spinBox_1.setGeometry(QRect(200, 430, 81, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"sonido BEEP", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"sonido FIN", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"sonido ALARMA", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Agregar fila", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Eliminar fila", None))
    # retranslateUi

