import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTimer
from intro_gui import Ui_MainWindow
from pathlib import Path
from PySide6 import QtGui
 
class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setWindowTitle("Informática Avanzada - Cerrar App")
		self.setWindowIcon(QIcon("ing.png"))
		self.contador = 0
		self.timer_segundos = 0

		self.pushButton_cerrar_app.clicked.connect(app.quit)

		self.pushButton_fondo_verde.clicked.connect(lambda: window.setStyleSheet("background-color: #00ff00;"))
		self.pushButton_fondo_rojo.clicked.connect(lambda: window.setStyleSheet("background-color: red;"))

		self.pushButton_incrementar.clicked.connect(self.incrementar_valor)

		self.lineEdit_texto_replicado.textChanged.connect(lambda text: self.label_texto_replicado.setText(text))

		self.radioButton_amarillo.toggled.connect(lambda checked: self.groupBox_color.setStyleSheet("background-color: yellow;" if checked else ""))
		self.radioButton_celeste.toggled.connect(lambda checked: self.groupBox_color.setStyleSheet("background-color: cyan;" if checked else ""))

		self.checkBox_gb1_naranja.toggled.connect(self.groupBox_check1.setVisible)
		self.checkBox_gb2_violeta.toggled.connect(self.groupBox_check2.setVisible)

		img_path = Path(__file__).parent / "ing.png"
		pixmap_imagen = QtGui.QPixmap(str(img_path))
		self.label_imagen.setScaledContents(True)
		self.label_imagen.setPixmap(pixmap_imagen)

		self.timer = QTimer()
		self.timer.setInterval(1000)  # 1 segundo
		self.timer.timeout.connect(self.timer_incrementar)
		self.timer.start()

	def incrementar_valor(self):
		try:
			nuevo_valor = self.contador + 1
			self.lcdNumber_incrementar.display(nuevo_valor)
			self.lineEdit_incrementar.setText(str(nuevo_valor))
			self.textEdit_incrementar.setPlainText(f"{nuevo_valor}")
			self.contador = nuevo_valor
		except ValueError:
			pass
	
	def timer_incrementar(self):
		self.timer_segundos += 1
		self.lcdNumber_tiempo.display(self.timer_segundos)
		if self.timer_segundos % 2 == 0:
			self.label_warning.setStyleSheet(f"background-color: red;")
		else:
			self.label_warning.setStyleSheet(f"background-color: blue;")
 
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())