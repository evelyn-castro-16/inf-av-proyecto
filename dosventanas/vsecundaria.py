# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vsecundaria.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(698, 205)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_volver = QPushButton(self.centralwidget)
        self.pushButton_volver.setObjectName(u"pushButton_volver")
        self.pushButton_volver.setGeometry(QRect(220, 100, 271, 41))
        self.label_sec = QLabel(self.centralwidget)
        self.label_sec.setObjectName(u"label_sec")
        self.label_sec.setGeometry(QRect(260, 30, 231, 71))
        self.label_sec.setStyleSheet(u"font: 24pt \"Segoe UI\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 698, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_volver.setText(QCoreApplication.translate("MainWindow", u"VOLVER A PRINCIPAL", None))
        self.label_sec.setText(QCoreApplication.translate("MainWindow", u"SECUNDARIO", None))
    # retranslateUi

