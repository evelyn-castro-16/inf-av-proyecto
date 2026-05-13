# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(748, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 241, 271))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_crear_bd = QPushButton(self.widget)
        self.pushButton_crear_bd.setObjectName(u"pushButton_crear_bd")

        self.verticalLayout.addWidget(self.pushButton_crear_bd)

        self.pushButton_conectar = QPushButton(self.widget)
        self.pushButton_conectar.setObjectName(u"pushButton_conectar")

        self.verticalLayout.addWidget(self.pushButton_conectar)

        self.pushButton_crear_tabla = QPushButton(self.widget)
        self.pushButton_crear_tabla.setObjectName(u"pushButton_crear_tabla")

        self.verticalLayout.addWidget(self.pushButton_crear_tabla)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_guardar_dato = QPushButton(self.widget_2)
        self.pushButton_guardar_dato.setObjectName(u"pushButton_guardar_dato")

        self.horizontalLayout.addWidget(self.pushButton_guardar_dato)

        self.spinBox = QSpinBox(self.widget_2)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout.addWidget(self.spinBox)


        self.verticalLayout.addWidget(self.widget_2)

        self.pushButton_graficar = QPushButton(self.widget)
        self.pushButton_graficar.setObjectName(u"pushButton_graficar")

        self.verticalLayout.addWidget(self.pushButton_graficar)

        self.pushButton_borrar_tabla = QPushButton(self.widget)
        self.pushButton_borrar_tabla.setObjectName(u"pushButton_borrar_tabla")

        self.verticalLayout.addWidget(self.pushButton_borrar_tabla)

        self.pushButton_borrar_bd = QPushButton(self.widget)
        self.pushButton_borrar_bd.setObjectName(u"pushButton_borrar_bd")

        self.verticalLayout.addWidget(self.pushButton_borrar_bd)

        self.pushButton_desconectar = QPushButton(self.widget)
        self.pushButton_desconectar.setObjectName(u"pushButton_desconectar")

        self.verticalLayout.addWidget(self.pushButton_desconectar)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(270, 20, 341, 271))
        self.widget_3 = QChartView(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(40, 350, 271, 181))
        self.widget_4 = QChartView(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(370, 360, 271, 181))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_crear_bd.setText(QCoreApplication.translate("MainWindow", u"crear base de datos", None))
        self.pushButton_conectar.setText(QCoreApplication.translate("MainWindow", u"conectar", None))
        self.pushButton_crear_tabla.setText(QCoreApplication.translate("MainWindow", u"crear tabla", None))
        self.pushButton_guardar_dato.setText(QCoreApplication.translate("MainWindow", u"guardar", None))
        self.pushButton_graficar.setText(QCoreApplication.translate("MainWindow", u"graficar tabla", None))
        self.pushButton_borrar_tabla.setText(QCoreApplication.translate("MainWindow", u"borrar tabla", None))
        self.pushButton_borrar_bd.setText(QCoreApplication.translate("MainWindow", u"borrar base de datos", None))
        self.pushButton_desconectar.setText(QCoreApplication.translate("MainWindow", u"desconectar", None))
    # retranslateUi

