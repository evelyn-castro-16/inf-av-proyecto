import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ej3.cambio_var import Ui_MainWindow

class ControlCambioVariable(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.contador_var_1 = 0
        self.configurar_botones()

    def configurar_botones(self):
        # Botones para incrementar y decrementar la variable
        self.ui.pushButton_incrementar_variable_1.clicked.connect(self.incrementar)
        self.ui.pushButton_decrementar_variable_1.clicked.connect(self.decrementar)

    def incrementar(self):
        self.contador_var_1 += 1
        self.actualizar_pantalla_cambio_variable()

    def decrementar(self):
        self.contador_var_1 -= 1
        self.actualizar_pantalla_cambio_variable()

    def actualizar_pantalla_cambio_variable(self):
        # Convertimos a string porque el widget solo acepta texto
        self.ui.plainTextEdit_variable_1.setPlainText(str(self.contador_var_1))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventana = ControlCambioVariable()
    ventana.show()
    
    sys.exit(app.exec())