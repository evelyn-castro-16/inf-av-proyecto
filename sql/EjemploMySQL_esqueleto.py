import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox
import mysql.connector
from ventanaPrincipal import Ui_MainWindow

from PySide6.QtCharts import QChart, QLineSeries, QValueAxis
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
"""Nombre de los componentes:
pushButton_crear_bd
pushButton_conectar
pushButton_crear_tabla
pushButton_guardar_dato
pushButton_graficar
pushButton_borrar_tabla
pushButton_borrar_bd
pushButton_desconectar
spinBox
textEdit
widget_grafico_1
widget_grafico_2
"""

DB_HOST = "localhost" #Informacion de la base de datos. Es conveniente guardar las credenciales en un archivo archivo .env y leerlas con python-dotenv

DB_USER = "IAvanzada"

DB_PASSWORD = "3744"

DB_NAME = "mediciones"

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setWindowTitle("Informática Avanzada - MySQL")
		self.setWindowIcon(QIcon("logo_unlam.jpg"))

		self.pushButton_crear_bd.clicked.connect(self.crear_bd) #Conexion de señales
		self.pushButton_conectar.clicked.connect(self.conectar)
		self.pushButton_crear_tabla.clicked.connect(self.crear_tabla)
		self.pushButton_guardar_dato.clicked.connect(self.guardar_dato)
		self.pushButton_graficar.clicked.connect(self.graficar)
		self.pushButton_borrar_tabla.clicked.connect(self.borrar_tabla)
		self.pushButton_borrar_bd.clicked.connect(self.borrar_bd)
		self.pushButton_desconectar.clicked.connect(self.desconectar)

		self.pushButton_crear_tabla.setEnabled(False) #Deshabilito botones
		self.pushButton_guardar_dato.setEnabled(False)
		self.pushButton_graficar.setEnabled(False)
		self.pushButton_borrar_tabla.setEnabled(False)
		self.pushButton_borrar_bd.setEnabled(False)
		self.pushButton_desconectar.setEnabled(False)

		self.spinBox.setMinimum(-32768) #Configuro límites del spinBox según el tipo de dato a usar en la base de datos (SMALLINT)
		self.spinBox.setMaximum(32767)

	def crear_bd(self): #Crear base de datos
		try:
			conBd = mysql.connector.connect(host=DB_HOST,user=DB_USER,password=DB_PASSWORD)
			cur = conBd.cursor()
			cur.execute("CREATE DATABASE IF NOT EXISTS mediciones")
			conBd.close()
			QMessageBox.information(self, "DB", "Base de datos creada o ya existente.")
			self.textEdit.append("Base de datos creada o ya existente.")
			self.pushButton_conectar.setEnabled(True)
		except mysql.connector.Error as e:
			self.textEdit.append(f"Error al crear la base de datos: {e}")

	def conectar(self): #Conectar a la base de datos
		try:
			self.conexionBd = mysql.connector.connect(host=DB_HOST,user=DB_USER,password=DB_PASSWORD,database=DB_NAME)
			self.cursorBd = self.conexionBd.cursor()
			self.pushButton_crear_tabla.setEnabled(True)
			self.pushButton_guardar_dato.setEnabled(True)
			self.pushButton_graficar.setEnabled(True)
			self.pushButton_borrar_tabla.setEnabled(True)
			self.pushButton_borrar_bd.setEnabled(True)
			self.pushButton_desconectar.setEnabled(True)
			self.pushButton_crear_bd.setEnabled(False)
			self.pushButton_conectar.setEnabled(False)
			QMessageBox.information(self, "Éxito", "Conectado a la base de datos.")
			self.textEdit.append("Conectado a la base de datos.")
		except Exception as e:
			QMessageBox.critical(self, "Error", f"No se pudo conectar: {e}")
			self.textEdit.append(f"Error. No se pudo conectar: {e}")


	def crear_tabla(self): #Crear tabla
		if self.cursorBd:
			try:

				self.cursorBd.execute("CREATE TABLE IF NOT EXISTS Temperatura (NroRegistro INT AUTO_INCREMENT PRIMARY KEY, Fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP, Temp SMALLINT)")

				self.conexionBd.commit()

				#QMessageBox.information(self, "Tabla", "Tabla Temperatura lista.")

				self.textEdit.append("Tabla Temperatura lista.")

				self.pushButton_guardar_dato.setEnabled(True)

				self.pushButton_graficar.setEnabled(True)

			except mysql.connector.Error as e:

				self.textEdit.append(f"Error al crear la tabla: {e}")


	def guardar_dato(self): #Guardar información en la tabla de la base de datos
		if self.cursorBd:
			try:
				self.cursorBd.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %s AND table_name = 'Temperatura'", (DB_NAME,)) #Verifico que la tabla exista
				if self.cursorBd.fetchone()[0] == 0:
					self.textEdit.append("Error: No existe la tabla, primero se la debe crear.")
					return

				lectura = self.spinBox.value() #Guardo dato en la tabla
				self.cursorBd.execute("INSERT INTO Temperatura (Temp) VALUES (%s)", (lectura,))
				self.conexionBd.commit()
				self.textEdit.append("Dato guardado.")

				self.serie_a.append(self.index, lectura) #Agrego dato a la serie del grafico 1

				"""if self.index > self.axis_x.max(): #Grafico 1: toda la información de la sesion
				self.axis_x.setMax(self.index)
				if lectura > self.axis_y.max():
				self.axis_y.setMax(lectura)
				elif lectura < self.axis_y.min():
				self.axis_y.setMin(lectura)"""

				if self.index > self.ventana: #Grafico 1: tipo ventana
					self.axis_x.setMax(self.index)
					self.axis_x.setMin(self.index-self.ventana+1)
					puntos = self.serie_a.points()
				if len(puntos) > self.ventana:
					ultimos_puntos = puntos[-self.ventana:]
				else:
					ultimos_puntos = puntos
					min_y = min(p.y() for p in ultimos_puntos)
					max_y = max(p.y() for p in ultimos_puntos)
				if min_y == max_y:
					min_y -= 1
					max_y += 1
					self.axis_y.setRange(min_y, max_y)

					self.index+=1

			except mysql.connector.Error as e:
				self.textEdit.append(f"Error al guardar: {e}")

	def graficar(self): #Grafico en el 2do grafico todos los datos almacenados en la base de datos
		try:
			self.cursorBd.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %s AND table_name = 'Temperatura'", (DB_NAME,)) #Verifico que la tabla exista

			if self.cursorBd.fetchone()[0] == 0:
				self.textEdit.append("Error: No existe la tabla, primero se la debe crear.")
				return

			"""self.cursorBd.execute("SELECT * FROM Temperatura") #SOlicito toda la tabla para mostrarla en el textEdit

			resultados = self.cursorBd.fetchall()

			if not resultados:

			self.textEdit.append("La tabla está vacía.")

			return

			for fila in resultados:

			self.textEdit.append(str(fila))"""

			self.cursorBd.execute("SELECT Temp FROM Temperatura") #SOlicito solo la columna Temp de la tabla

			resultados = self.cursorBd.fetchall()

			if not resultados:

				self.textEdit.append("La tabla está vacía.")

				return

			self.serie_b.clear() #Grafico toda la información de Temp en el grafico 2

			self.index_b = 0

			min_y = resultados[0][0] #Configuro eje vertical

			max_y = resultados[0][0]

			for fila in resultados:
				self.serie_b.append(self.index_b, fila[0])
				self.index_b += 1
				if fila[0]<min_y:
					min_y = fila[0]
				if fila[0]>max_y:
					max_y = fila[0]
			if min_y == max_y:
				min_y -= 1
				max_y += 1
			self.axis_y_b.setRange(min_y, max_y)

			if self.index_b <= 1: #Configuro eje horizontal
				self.axis_x_b.setRange(0, 1)
			else:
				self.axis_x_b.setRange(0, self.index_b - 1)
		except Exception as e:
			self.textEdit.append(f"Error al graficar: {e}")

	def borrar_tabla(self): #Borrar tabla
		if self.cursorBd:

			respuesta = QMessageBox.question(self, "Confirmar", "¿Desea borrar la tabla?", QMessageBox.Yes | QMessageBox.No)

			if respuesta == QMessageBox.Yes:
				self.cursorBd.execute("DROP TABLE IF EXISTS Temperatura")
				self.conexionBd.commit()
				#QMessageBox.warning(self, "Borrar", "Tabla eliminada.")
				self.textEdit.append("Tabla eliminada.")
				self.pushButton_guardar_dato.setEnabled(False)
				self.pushButton_graficar.setEnabled(False)		

	def borrar_bd(self): #Borrar base de datos
		pass

	def desconectar(self): #Desconectar de la base de datos
		try:
			if self.conexionBd and self.conexionBd.is_connected():
				self.cursorBd.close()   # Cerramos el cursor primero
				self.conexionBd.close() # Luego la conexión
				self.textEdit.append("Desconectado del servidor MySQL.")

				self.pushButton_crear_tabla.setEnabled(False)
				self.pushButton_guardar_dato.setEnabled(False)
				self.pushButton_graficar.setEnabled(False)
				self.pushButton_borrar_tabla.setEnabled(False)
				self.pushButton_borrar_bd.setEnabled(False)
				self.pushButton_desconectar.setEnabled(False)
				self.pushButton_conectar.setEnabled(True)
				self.pushButton_crear_bd.setEnabled(True)
			else:
				self.textEdit.append("No hay ninguna conexión activa para cerrar.")

		except Exception as e:
			self.textEdit.append(f"Error al intentar desconectar: {e}")

	def closeEvent(self, event): #Evento que se ejecuta automáticamente al cerrar la ventana
		if self.conexionBd and self.conexionBd.is_connected():
			self.cursorBd.close()
			self.conexionBd.close()
			print("Conexión cerrada automáticamente al salir.") #No uso el textEdit, ya se cerró la ventana
			event. Accept()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())

#pip install mysql-connector-python
# https://dev.mysql.com/doc/refman/8.4/en/data-types.html