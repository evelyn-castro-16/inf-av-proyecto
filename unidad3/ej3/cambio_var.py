# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cambio_var.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(359, 224)
        self.actionNuevo_Usuario = QAction(MainWindow)
        self.actionNuevo_Usuario.setObjectName(u"actionNuevo_Usuario")
        self.actionCambiar_Usuario = QAction(MainWindow)
        self.actionCambiar_Usuario.setObjectName(u"actionCambiar_Usuario")
        self.actionJerarqu_as = QAction(MainWindow)
        self.actionJerarqu_as.setObjectName(u"actionJerarqu_as")
        self.actionAlarmas = QAction(MainWindow)
        self.actionAlarmas.setObjectName(u"actionAlarmas")
        self.actionAjustes = QAction(MainWindow)
        self.actionAjustes.setObjectName(u"actionAjustes")
        self.actionImportar_Exportar = QAction(MainWindow)
        self.actionImportar_Exportar.setObjectName(u"actionImportar_Exportar")
        self.actionB_squeda = QAction(MainWindow)
        self.actionB_squeda.setObjectName(u"actionB_squeda")
        self.actionHistorial_Actividad = QAction(MainWindow)
        self.actionHistorial_Actividad.setObjectName(u"actionHistorial_Actividad")
        self.actionEstado_de_Sistema = QAction(MainWindow)
        self.actionEstado_de_Sistema.setObjectName(u"actionEstado_de_Sistema")
        self.actionReporte_Diario_Mensual = QAction(MainWindow)
        self.actionReporte_Diario_Mensual.setObjectName(u"actionReporte_Diario_Mensual")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_cambio_variable = QGroupBox(self.centralwidget)
        self.groupBox_cambio_variable.setObjectName(u"groupBox_cambio_variable")
        self.groupBox_cambio_variable.setGeometry(QRect(40, 40, 271, 101))
        self.groupBox_cambio_variable.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 700 12pt \"Segoe UI\";")
        self.pushButton_incrementar_variable_1 = QPushButton(self.groupBox_cambio_variable)
        self.pushButton_incrementar_variable_1.setObjectName(u"pushButton_incrementar_variable_1")
        self.pushButton_incrementar_variable_1.setGeometry(QRect(20, 30, 131, 24))
        self.pushButton_incrementar_variable_1.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.plainTextEdit_variable_1 = QPlainTextEdit(self.groupBox_cambio_variable)
        self.plainTextEdit_variable_1.setObjectName(u"plainTextEdit_variable_1")
        self.plainTextEdit_variable_1.setGeometry(QRect(190, 40, 61, 41))
        self.pushButton_decrementar_variable_1 = QPushButton(self.groupBox_cambio_variable)
        self.pushButton_decrementar_variable_1.setObjectName(u"pushButton_decrementar_variable_1")
        self.pushButton_decrementar_variable_1.setGeometry(QRect(20, 70, 131, 24))
        self.pushButton_decrementar_variable_1.setStyleSheet(u"background-color: rgb(255, 85, 255);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 359, 22))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNuevo_Usuario.setText(QCoreApplication.translate("MainWindow", u"Nuevo Usuario", None))
        self.actionCambiar_Usuario.setText(QCoreApplication.translate("MainWindow", u"Cambiar Usuario", None))
        self.actionJerarqu_as.setText(QCoreApplication.translate("MainWindow", u"Jerarqu\u00edas", None))
        self.actionAlarmas.setText(QCoreApplication.translate("MainWindow", u"Generar PDF", None))
        self.actionAjustes.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
        self.actionImportar_Exportar.setText(QCoreApplication.translate("MainWindow", u"Importar/Exportar Datos", None))
        self.actionB_squeda.setText(QCoreApplication.translate("MainWindow", u"B\u00fasqueda", None))
        self.actionHistorial_Actividad.setText(QCoreApplication.translate("MainWindow", u"Historial Actividad", None))
        self.actionEstado_de_Sistema.setText(QCoreApplication.translate("MainWindow", u"Estado del Sistema", None))
        self.actionReporte_Diario_Mensual.setText(QCoreApplication.translate("MainWindow", u"Reporte Diario/Mensual", None))
        self.groupBox_cambio_variable.setTitle(QCoreApplication.translate("MainWindow", u"CAMBIO VARIABLE", None))
        self.pushButton_incrementar_variable_1.setText(QCoreApplication.translate("MainWindow", u"INCREMENTAR", None))
        self.pushButton_decrementar_variable_1.setText(QCoreApplication.translate("MainWindow", u"DECREMENTAR", None))
    # retranslateUi

