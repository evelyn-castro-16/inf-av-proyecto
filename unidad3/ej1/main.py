from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
from ej1.cerrar_button import Ui_MainWindow

class ControlCierre:
    def __init__(self, button):
        self.button = button
        self.button.clicked.connect(self.cerrar_aplicacion)

    @Slot()
    def cerrar_aplicacion(self):
        QApplication.instance().quit()

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Integrate the close button logic
        self.control_cierre = ControlCierre(self.ui.pushButton_cerrar_app)

if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec()