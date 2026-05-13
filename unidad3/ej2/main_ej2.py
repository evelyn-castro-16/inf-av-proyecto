import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ej2.fondo_form import Ui_MainWindow

class ControlFondo(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.configurar_botones()

    def configurar_botones(self):
        # Botones para cambiar el color de fondo
        self.ui.pushButton_fondo_azul.clicked.connect(lambda: self.cambiar_fondo("blue"))
        self.ui.pushButton_fondo_verde.clicked.connect(lambda: self.cambiar_fondo("green"))
        self.ui.pushButton_fondo_violeta.clicked.connect(lambda: self.cambiar_fondo("darkviolet"))

    def cambiar_fondo(self, color):
        # Cambiar el color de fondo del formulario
        self.ui.centralwidget.setStyleSheet(f"background-color: {color};")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventana = ControlFondo()
    ventana.show()
    
    sys.exit(app.exec())