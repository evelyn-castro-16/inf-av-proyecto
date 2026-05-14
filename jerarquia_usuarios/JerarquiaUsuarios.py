# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'JerarquiaUsuarios.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_pushButton_admin_2(object):
    def setupUi(self, pushButton_admin_2):
        if not pushButton_admin_2.objectName():
            pushButton_admin_2.setObjectName(u"pushButton_admin_2")
        pushButton_admin_2.resize(800, 600)
        self.centralwidget = QWidget(pushButton_admin_2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_iniciar_sesion = QPushButton(self.centralwidget)
        self.pushButton_iniciar_sesion.setObjectName(u"pushButton_iniciar_sesion")
        self.pushButton_iniciar_sesion.setGeometry(QRect(140, 110, 101, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 70, 49, 16))
        self.lineEdit_usuario = QLineEdit(self.centralwidget)
        self.lineEdit_usuario.setObjectName(u"lineEdit_usuario")
        self.lineEdit_usuario.setGeometry(QRect(130, 40, 113, 21))
        self.lineEdit_pass = QLineEdit(self.centralwidget)
        self.lineEdit_pass.setObjectName(u"lineEdit_pass")
        self.lineEdit_pass.setGeometry(QRect(130, 80, 113, 21))
        self.lineEdit_admin = QLineEdit(self.centralwidget)
        self.lineEdit_admin.setObjectName(u"lineEdit_admin")
        self.lineEdit_admin.setGeometry(QRect(120, 260, 113, 21))
        self.lineEdit_supervisor = QLineEdit(self.centralwidget)
        self.lineEdit_supervisor.setObjectName(u"lineEdit_supervisor")
        self.lineEdit_supervisor.setGeometry(QRect(330, 260, 113, 21))
        self.lineEdit_operario = QLineEdit(self.centralwidget)
        self.lineEdit_operario.setObjectName(u"lineEdit_operario")
        self.lineEdit_operario.setGeometry(QRect(580, 260, 113, 21))
        self.pushButton_admin_1 = QPushButton(self.centralwidget)
        self.pushButton_admin_1.setObjectName(u"pushButton_admin_1")
        self.pushButton_admin_1.setGeometry(QRect(140, 170, 75, 24))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(140, 210, 75, 24))
        self.pushButton_supervisor_1 = QPushButton(self.centralwidget)
        self.pushButton_supervisor_1.setObjectName(u"pushButton_supervisor_1")
        self.pushButton_supervisor_1.setGeometry(QRect(340, 170, 75, 24))
        self.pushButton_supervisor_2 = QPushButton(self.centralwidget)
        self.pushButton_supervisor_2.setObjectName(u"pushButton_supervisor_2")
        self.pushButton_supervisor_2.setGeometry(QRect(340, 210, 75, 24))
        self.pushButton_operario_1 = QPushButton(self.centralwidget)
        self.pushButton_operario_1.setObjectName(u"pushButton_operario_1")
        self.pushButton_operario_1.setGeometry(QRect(600, 170, 75, 24))
        self.pushButton_operario_2 = QPushButton(self.centralwidget)
        self.pushButton_operario_2.setObjectName(u"pushButton_operario_2")
        self.pushButton_operario_2.setGeometry(QRect(600, 210, 75, 24))
        self.pushButton_agregar_usuario = QPushButton(self.centralwidget)
        self.pushButton_agregar_usuario.setObjectName(u"pushButton_agregar_usuario")
        self.pushButton_agregar_usuario.setGeometry(QRect(130, 450, 101, 24))
        self.lineEdit_gestion_usuario = QLineEdit(self.centralwidget)
        self.lineEdit_gestion_usuario.setObjectName(u"lineEdit_gestion_usuario")
        self.lineEdit_gestion_usuario.setGeometry(QRect(120, 320, 113, 21))
        self.lineEdit_gestion_pass = QLineEdit(self.centralwidget)
        self.lineEdit_gestion_pass.setObjectName(u"lineEdit_gestion_pass")
        self.lineEdit_gestion_pass.setGeometry(QRect(120, 360, 113, 21))
        self.comboBox_gestion_nivel = QComboBox(self.centralwidget)
        self.comboBox_gestion_nivel.setObjectName(u"comboBox_gestion_nivel")
        self.comboBox_gestion_nivel.setGeometry(QRect(130, 400, 101, 22))
        self.pushButton_borrar_usuario = QPushButton(self.centralwidget)
        self.pushButton_borrar_usuario.setObjectName(u"pushButton_borrar_usuario")
        self.pushButton_borrar_usuario.setGeometry(QRect(130, 490, 101, 24))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 40, 49, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(390, 70, 49, 16))
        self.label_user = QLabel(self.centralwidget)
        self.label_user.setObjectName(u"label_user")
        self.label_user.setGeometry(QRect(460, 40, 49, 16))
        self.label_nivel = QLabel(self.centralwidget)
        self.label_nivel.setObjectName(u"label_nivel")
        self.label_nivel.setGeometry(QRect(460, 70, 49, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 200, 81, 16))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 300, 771, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 150, 771, 16))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 400, 49, 16))
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(310, 320, 401, 211))
        pushButton_admin_2.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(pushButton_admin_2)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        pushButton_admin_2.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(pushButton_admin_2)
        self.statusbar.setObjectName(u"statusbar")
        pushButton_admin_2.setStatusBar(self.statusbar)

        self.retranslateUi(pushButton_admin_2)

        QMetaObject.connectSlotsByName(pushButton_admin_2)
    # setupUi

    def retranslateUi(self, pushButton_admin_2):
        pushButton_admin_2.setWindowTitle(QCoreApplication.translate("pushButton_admin_2", u"MainWindow", None))
        self.pushButton_iniciar_sesion.setText(QCoreApplication.translate("pushButton_admin_2", u"iniciar sesion", None))
        self.label.setText(QCoreApplication.translate("pushButton_admin_2", u"inicio", None))
        self.pushButton_admin_1.setText(QCoreApplication.translate("pushButton_admin_2", u"admin", None))
        self.pushButton_3.setText(QCoreApplication.translate("pushButton_admin_2", u"admin", None))
        self.pushButton_supervisor_1.setText(QCoreApplication.translate("pushButton_admin_2", u"sup", None))
        self.pushButton_supervisor_2.setText(QCoreApplication.translate("pushButton_admin_2", u"super", None))
        self.pushButton_operario_1.setText(QCoreApplication.translate("pushButton_admin_2", u"oper", None))
        self.pushButton_operario_2.setText(QCoreApplication.translate("pushButton_admin_2", u"oper", None))
        self.pushButton_agregar_usuario.setText(QCoreApplication.translate("pushButton_admin_2", u"agregar usuario", None))
        self.pushButton_borrar_usuario.setText(QCoreApplication.translate("pushButton_admin_2", u"Borrar Usuario", None))
        self.label_2.setText(QCoreApplication.translate("pushButton_admin_2", u"Usuario", None))
        self.label_3.setText(QCoreApplication.translate("pushButton_admin_2", u"Nivel", None))
        self.label_user.setText(QCoreApplication.translate("pushButton_admin_2", u"TextLabel", None))
        self.label_nivel.setText(QCoreApplication.translate("pushButton_admin_2", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("pushButton_admin_2", u"programa", None))
        self.label_5.setText(QCoreApplication.translate("pushButton_admin_2", u"gestion", None))
    # retranslateUi

