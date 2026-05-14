import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PySide6.QtGui import QIcon
import mysql.connector
import bcrypt
import os
from dotenv import load_dotenv
from JerarquiaUsuarios import Ui_MainWindow

# DB_HOST = "localhost" #Informacion de la base de datos. Es conveniente guardar las credenciales en un archivo archivo .env y leerlas con python-dotenv
# DB_USER = "IAvanzada"
# DB_PASSWORD = "3744"
# DB_NAME = "acceso"
# DB_TABLANAME = "usuarios"
 
load_dotenv() #Cargar variables de entorno desde el archivo .env
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
#DB_HOST = os.getenv("DB_HOST", "localhost") #Se pueden usar valores por defecto (por si el .env no existe o falta una variable)
#DB_NAME = os.getenv("DB_NAME", "acceso")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_TABLANAME = os.getenv("DB_TABLANAME")

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setWindowTitle("Informática Avanzada - Jerarquía de usuarios con Base de datos, hash y variables de entorno")
		self.setWindowIcon(QIcon("logo_unlam.jpg"))		

		self.conexionBd=None
		self.cursorBd=None
		self.nivel_activo=None

		self.iniciarBb()

		self.comboBox_gestion_nivel.addItem("Administrador", userData=1)
		self.comboBox_gestion_nivel.addItem("Supervisor", userData=2)
		self.comboBox_gestion_nivel.addItem("Operario", userData=3)

		self.tableWidget.setColumnCount(4) #Creo la estructura de la tabla
		self.tableWidget.setHorizontalHeaderLabels(["Usuario", "Contraseña", "Nivel", "Fecha"])
		#self.tableWidget.setVisible(False)
		self.habilitarAdministrador(False)

		self.pushButton_agregar_usuario.clicked.connect(self.agregarUsuario) #Conecto método para agregar una nueva fila
		self.pushButton_borrar_usuario.clicked.connect(self.borrarUsuario)
		self.pushButton_iniciar_sesion.clicked.connect(self.inicioSesion)

	def iniciarBb(self):
		try:
			con_inicial = mysql.connector.connect(host=DB_HOST,user=DB_USER,password=DB_PASSWORD)
			cur_inicial = con_inicial.cursor()
			#cur_inicial.execute(f"DROP DATABASE IF EXISTS {DB_NAME}") #Descartar base de datos
			cur_inicial.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}") #Crear base de datos
			cur_inicial.close()
			con_inicial.close()

			self.conexionBd = mysql.connector.connect(host=DB_HOST,user=DB_USER,password=DB_PASSWORD,database=DB_NAME) #Conectar a la base de datos
			self.cursorBd = self.conexionBd.cursor()

			#self.cursorBd.execute(f"DROP TABLE IF EXISTS {DB_NAME}.{DB_TABLANAME}") #Descartar tabla
			self.cursorBd.execute(f"CREATE TABLE IF NOT EXISTS {DB_TABLANAME} (Usuario VARCHAR(50) PRIMARY KEY, Contrasenia VARCHAR(255), Nivel VARCHAR(20), Fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
			
			usuario="f"
			contrasenia="1"
			nivel="Administrador"
			contrasenia_bytes = contrasenia.encode('utf-8')
			salt = bcrypt.gensalt(rounds=12)
			hash_contrasenia = bcrypt.hashpw(contrasenia_bytes, salt)
			self.cursorBd.execute(f"INSERT IGNORE INTO {DB_TABLANAME} (Usuario, Contrasenia, Nivel) VALUES (%s, %s, %s)", (usuario, hash_contrasenia.decode('utf-8'), nivel))
	
			# self.cursorBd.execute(f"INSERT IGNORE INTO {DB_TABLANAME} (Usuario, Contrasenia, Nivel) VALUES (%s, %s, %s)",(usuario, contrasenia, nivel))
			#IGNORE para que si el usuario 'f' ya existe, no de error de Primary Key
			self.conexionBd.commit() # Commit para guardar los datos insertados
			
		except mysql.connector.Error as e:
			QMessageBox.warning(self, "Error en la inicialización de la base de datos", str(e))
		except Exception as e:
			QMessageBox.critical(self, "Error de sistema", str(e))
		
		
	def inicioSesion(self):		
		if self.nivel_activo==None:
			usuario_buscar=self.lineEdit_usuario.text()
			contrasenia_buscar=self.lineEdit_pass.text()
			if usuario_buscar !="" and contrasenia_buscar!="":
				self.cursorBd.execute(f"SELECT Contrasenia, Nivel FROM {DB_TABLANAME} WHERE Usuario = %s", (usuario_buscar,))
				encontrado = self.cursorBd.fetchone()
				if encontrado:
					contrasenia_guardada = encontrado[0]
					nivel_guardado = encontrado[1]

					contrasenia_guardada_bytes = contrasenia_guardada.encode('utf-8') #Hash guardado en bytes
					contrasenia_buscar_bytes = contrasenia_buscar.encode('utf-8') #Contraseña ingresada en bytes

					if bcrypt.checkpw(contrasenia_buscar_bytes,contrasenia_guardada_bytes): #Verifico la contraseña con bcrypt, importa el orden
					# if contrasenia_buscar==contrasenia_guardada:
						self.nivel_activo=nivel_guardado
						self.actualizarInterfaz(True)

						self.label_usuario.setText("Usuario: "+usuario_buscar)
						self.label_nivel.setText("Nivel: "+self.nivel_activo)
						self.lineEdit_usuario.clear()
						self.lineEdit_pass.clear()
					else:
						QMessageBox.warning(self, "Gestion de usuarios", "Contraseña incorecta")
				else:
					QMessageBox.warning(self, "Gestion de usuarios", "El usuario no existe")
			else:
				QMessageBox.warning(self, "Gestion de usuarios", "Ingrese usuario y contraseña")
		else:
			self.actualizarInterfaz(False)
			self.nivel_activo=None

	def actualizarInterfaz(self, estado):		
		if self.nivel_activo=="Administrador":
			self.habilitarAdministrador(estado)
		elif self.nivel_activo=="Supervisor":
			self.habilitarSupervisor(estado)
		elif self.nivel_activo=="Operario":
			self.habilitarOperario(estado)

	def habilitarAdministrador(self,estado):		
		self.habilitarOperario(estado)
		self.habilitarSupervisor(estado)
		
		self.pushButton_admin_1.setEnabled(estado)
		self.pushButton_admin_2.setEnabled(estado)
		self.lineEdit_admin.setEnabled(estado)

		self.lineEdit_gestion_usuario.setEnabled(estado)
		self.lineEdit_gestion_pass.setEnabled(estado)
		self.comboBox_gestion_nivel.setEnabled(estado)
		self.pushButton_agregar_usuario.setEnabled(estado)
		self.pushButton_borrar_usuario.setEnabled(estado)

		self.tableWidget.setVisible(estado)
		if estado:
			self.actualizarTabla()

	def habilitarSupervisor(self,estado):		
		self.habilitarOperario(estado) 
		self.pushButton_supervisor_1.setEnabled(estado)
		self.pushButton_supervisor_2.setEnabled(estado)
		self.lineEdit_supervisor.setEnabled(estado)

	def habilitarOperario(self,estado):		
		self.pushButton_operario_1.setEnabled(estado)
		self.pushButton_operario_2.setEnabled(estado)
		self.lineEdit_operario.setEnabled(estado)

		if self.nivel_activo=="Operario":
			self.pushButton_admin_2.setVisible(not estado)
			self.lineEdit_admin.setVisible(not estado)

			self.lineEdit_usuario.setEnabled(not estado)
			self.lineEdit_pass.setEnabled(not estado)

		if estado:
			self.pushButton_iniciar_sesion.setText("Cerrar Sesión")
		else:

			self.pushButton_iniciar_sesion.setText("Iniciar sesión")
			self.label_usuario.setText("Usuario: ")
			self.label_nivel.setText("Nivel: ")

	def agregarUsuario(self):		
		usuario=self.lineEdit_gestion_usuario.text()
		contrasenia=self.lineEdit_gestion_pass.text()
		nivel=self.comboBox_gestion_nivel.currentText()
		#nivel=self.comboBox_gestion_nivel.currentData() #Es conveniente guardar en la BD currentData (1,2,3), no los nombres de los niveles
		
		if usuario !="" and contrasenia!="":
			self.cursorBd.execute(f"SELECT Usuario FROM {DB_TABLANAME} WHERE Usuario = %s", (usuario,))
			encontrado = self.cursorBd.fetchone()
			if encontrado:
				QMessageBox.warning(self, "Gestion de usuarios", "Ya existe ese nombre de usuario")
			else:
				contrasenia_bytes = contrasenia.encode('utf-8') #Bytes
				salt = bcrypt.gensalt(rounds=12) #Cadena de caracteres aleatorios que se agrega a la contraseña del usuario para evitar igual hash con igual contraseña
				hash_contrasenia = bcrypt.hashpw(contrasenia_bytes, salt) #Hash. En la BD guardo el hash como String (decode('utf-8'))
				self.cursorBd.execute(f"INSERT INTO {DB_TABLANAME} (Usuario, Contrasenia, Nivel) VALUES (%s, %s, %s)", (usuario, hash_contrasenia.decode('utf-8'), nivel))

				# self.cursorBd.execute(f"INSERT INTO {DB_TABLANAME} (Usuario, Contrasenia, Nivel) VALUES (%s, %s, %s)", (usuario, contrasenia, nivel))
				self.conexionBd.commit()
				self.actualizarTabla()
				QMessageBox.information(self, "Gestion de usuarios", "Usuario agregado correctamente")
		else:
			QMessageBox.warning(self, "Gestion de usuarios", "Ingrese usuario y contraseña validos")

	def borrarUsuario(self):		
		usuario=self.lineEdit_gestion_usuario.text()
		if usuario !="":
			self.cursorBd.execute(f"SELECT Usuario FROM {DB_TABLANAME} WHERE Usuario = %s", (usuario,))
			encontrado = self.cursorBd.fetchone()
			if encontrado:
				if usuario == "f":
					QMessageBox.critical(self, "Error", "No está permitido eliminar al administrador principal del sistema")
					return
				respuesta = QMessageBox.question(self, "Confirmar eliminación", f"¿Desea eliminar al usuario '{usuario}'?", QMessageBox.Yes | QMessageBox.No)
				if respuesta == QMessageBox.Yes:
					try:
						self.cursorBd.execute(f"DELETE FROM {DB_TABLANAME} WHERE Usuario = %s", (usuario,))
						self.conexionBd.commit()
						self.actualizarTabla()
						QMessageBox.information(self, "Gestion de usuarios", "Usuario borrado correctamente")
					except mysql.connector.Error as e:
						QMessageBox.warning(self, "Error", f"No se pudo eliminar: {e}")
			else:
				QMessageBox.warning(self, "Gestion de usuarios", "Usuario a borrar no encontrado")
		else:
			QMessageBox.warning(self, "Gestion de usuarios", "Ingrese usuario a borrar")

	def actualizarTabla(self):		
		self.cursorBd.execute(f"SELECT Usuario, Contrasenia, Nivel, Fecha FROM {DB_TABLANAME}")

		resultado = self.cursorBd.fetchall()

		self.tableWidget.setRowCount(0) #Elimino el contenido de tableWidget

		for fila_nro, fila_dato in enumerate(resultado):

			self.tableWidget.insertRow(fila_nro)

		for columna_nro, columna_dato in enumerate(fila_dato):

			self.tableWidget.setItem(fila_nro, columna_nro, QTableWidgetItem(str(columna_dato)))

		self.tableWidget.resizeColumnsToContents()

	def closeEvent(self, event): #Evento que se ejecuta automáticamente al cerrar la ventana
		event.accept()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())

# Instalación bcrypt:
# pip install bcrypt
# Ante el WARNING: Cache entry deserialization failed, entry ignored, no es necesario hacer nada. Opcional: "pip cache purge" limpia la cache
# Se puede verificar la instalacion con "pip list" o con "pip show bcrypt"
# Instalación dotenv:
# pip install python-dotenv
#
"""Nombre de componentes:
lineEdit_usuario							label_usuario
lineEdit_pass								label_nivel
pushButton_iniciar_sesion

pushButton_admin_1		pushButton_supervisor_1		pushButton_operario_1
pushButton_admin_2		pushButton_supervisor_2		pushButton_operario_2
lineEdit_admin			lineEdit_supervisor			lineEdit_operario

lineEdit_gestion_usuario			tableWidget
lineEdit_gestion_pass
comboBox_gestion_nivel
pushButton_agregar_usuario
pushButton_borrar_usuario
"""