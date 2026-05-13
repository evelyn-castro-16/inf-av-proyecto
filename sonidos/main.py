import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from Interfaz import Ui_MainWindow
from PySide6.QtGui import QIcon
from PySide6 import QtCore, QtMultimedia

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)		
		self.setWindowTitle("Informática Avanzada - Ejemplos clase 3")
		self.setWindowIcon(QIcon("logo_unlam.jpg"))

		self.pushButton_1.clicked.connect(app.beep)
		
		self.player = QtMultimedia.QMediaPlayer() #Se crea una instancia de QMediaPlayer. Necesita una salida de audio QAudioOutput
		self.audio_output = QtMultimedia.QAudioOutput()
		self.player.setAudioOutput(self.audio_output)
		
		self.pushButton_2.clicked.connect(lambda: self.reproducirSonido("SonidoFin.wav"))
		self.pushButton_5.clicked.connect(lambda: self.reproducirSonido("SonidoAlarma.wav"))
		
		self.tableWidget_1.setColumnCount(3)
		self.tableWidget_1.setHorizontalHeaderLabels(["DNI", "Nombre", "Nota"])
		self.pushButton_3.clicked.connect(self.agregarFila)
		
		self.pushButton_4.clicked.connect(lambda: self.tableWidget_1.removeRow(self.spinBox_1.value()))
		
	def reproducirSonido(self,archivo):
		url = QtCore.QUrl.fromLocalFile(archivo) #Ubicación del archivo .wav
		self.player.setSource(url)
		self.player.play()
	
	def agregarFila(self):
		dni=self.lineEdit_1.text()
		nombre=self.lineEdit_2.text()
		nota=self.lineEdit_3.text()
		fila = self.tableWidget_1.rowCount()
		self.tableWidget_1.insertRow(fila)
		self.tableWidget_1.setItem(fila, 0, QTableWidgetItem(dni))
		self.tableWidget_1.setItem(fila, 1, QTableWidgetItem(nombre))
		self.tableWidget_1.setItem(fila, 2, QTableWidgetItem(nota))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())