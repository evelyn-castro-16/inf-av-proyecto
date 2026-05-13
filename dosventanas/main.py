import sys  # Se importa el modulo del sistema
from PySide6.QtWidgets import QApplication, QMainWindow  # Se importan herramientas de PySide6
from PySide6.QtGui import QIcon
from vprincipal import Ui_MainWindow  # Se importa la clase Ui_MainWindow desde vprincipal.py
from vsecundaria import Ui_MainWindow as Ui_Ventana2  # Se importa la clase Ui_MainWindow desde vsecundaria.py


class SegundaVentana(QMainWindow, Ui_Ventana2):  # Se define primero esta clase porque se usa en MainWindow
    def __init__(self, parent=None):  # Parametro parent opcional
        super().__init__(parent)
        self.setupUi(self)  # inicializa la interfaz
        self.setWindowTitle("Informática Avanzada - Dos ventanas - Secundaria")
        self.setWindowIcon(QIcon("ing.png"))

        self.pushButton_volver.clicked.connect(self.volverVentana)  # Conexión del botón "VOLVER A PRINCIPAL"

    def volverVentana(self):
        if self.parent():
            self.parent().show()
        self.close()


class MainWindow(QMainWindow, Ui_MainWindow):  # Se define la clase MainWindow. Hereda de QMainWindow (para ser una ventana) y de Ui_MainWindow (para acceder a los componentes de la ventana)
    def __init__(self):
        super().__init__()  # Metodo constructor de la clase base QMainWindow. No tiene parent, es la ventana principal
        self.setupUi(self)  # Metodo para "dibujar" los componentes dentro de la ventana
        self.setWindowTitle("Informática Avanzada - Dos ventanas - Principal")
        self.setWindowIcon(QIcon("logo_unlam.jpg"))
        self.window2 = None  # Atributo para la segunda ventana

        self.pushButton_cambiar_ventana.clicked.connect(self.cambiarVentana)  # Conexión del botón "CAMBIAR VENTANA"

    def cambiarVentana(self):  # RANURA (slot). Metodo donde se indica que hace el boton al presionarse
        if self.window2 is None:
            self.window2 = SegundaVentana(parent=self)  # Se crea instancia pasando self como parent para establecer ownership, posicionamiento y limpieza automática
        self.hide()
        self.window2.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Se crea la instancia de la aplicación
    window = MainWindow()  # Se crea una instancia de la clase MainWindow
    window.show()  # Se muestra la ventana, por defecto esta oculta
    sys.exit(app.exec())  # Se inicia el bucle de eventos, se espera hasta que se cierre la ventana

