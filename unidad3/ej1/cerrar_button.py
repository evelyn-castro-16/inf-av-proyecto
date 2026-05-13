# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cerrar_button.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(793, 327)
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
        self.pushButton_cerrar_app = QPushButton(self.centralwidget)
        self.pushButton_cerrar_app.setObjectName(u"pushButton_cerrar_app")
        self.pushButton_cerrar_app.setGeometry(QRect(660, 10, 121, 31))
        self.pushButton_cerrar_app.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Segoe UI\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 793, 22))
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
        self.pushButton_cerrar_app.setText(QCoreApplication.translate("MainWindow", u"CERRAR APP", None))
    # retranslateUi

