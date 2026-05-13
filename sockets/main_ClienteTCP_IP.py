import sys                                                 #Se importa el modulo del sistema
import socket
from PySide6.QtWidgets import QApplication, QMainWindow    #Se importan herramientas de PySide6
from interfaz_cliente import Ui_MainWindow     #Se importa la clase Ui_MainWindow desde ventanaPrincipal1.py


class MainWindow(QMainWindow, Ui_MainWindow): #Se define la clase MainWindow. Hereda de QMainWindow (para ser una ventana) y de Ui_MainWindow (para acceder a los componentes de la ventana)
	def __init__(self):
		super().__init__()                    #Metodo constructor de la clase base QMainWindow
		self.setupUi(self)                    #Metodo para "dibujar" los componentes dentro de la ventana
		
		self.socket_cliente = None #Atributos de red
		self.host = '127.0.0.1'
		self.port = 65432
 
		self.pushButton_conectar.clicked.connect(self.conectar_servidor) #Conectar señales de los botones
		self.pushButton_enviar.clicked.connect(self.enviar_mensaje)
		self.pushButton_enviar.setEnabled(False) #Deshabilitar botón de enviar hasta que estemos conectados
	
	def conectar_servidor(self): #Establece la conexión persistente con el servidor
		try:
			self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.socket_cliente.settimeout(3.0)  # Timeout para que no se bloquee la GUI si el servidor no existe
			self.socket_cliente.connect((self.host, self.port))

			self.textEdit_recibido.append(">>> Conectado al servidor con éxito.")
			self.pushButton_enviar.setEnabled(True)
			self.pushButton_conectar.setEnabled(False) # Para evitar múltiples conexiones

		except Exception as e:
			self.textEdit_recibido.append(f"<b>Error de Conexión:</b> No se pudo conectar al servidor.<br>Detalle: {e}")

	def enviar_mensaje(self): #Envía el texto del QLineEdit y espera respuesta
		mensaje = self.lineEdit_mensaje.text()
		if not mensaje:
			return

		try:
			self.socket_cliente.sendall(mensaje.encode('utf-8')) # Enviar datos convertidos a bytes
			data = self.socket_cliente.recv(1024) # Recibir respuesta
			if data:
				self.textEdit_recibido.append(f"Servidor dice: {data.decode('utf-8')}")

			self.lineEdit_mensaje.clear() # Limpiar campo luego de enviar

		except socket.timeout:
			self.textEdit_recibido.append("Error: El servidor no respondió a tiempo.")
		except Exception as e:
			self.textEdit_recibido.append(f"Conexión perdida: {e}")
			self.pushButton_enviar.setEnabled(False)
			self.pushButton_conectar.setEnabled(True)


	def closeEvent(self, event): #Cierre limpio al presionar la X de la ventana
		if self.socket_cliente:
			try:
				self.socket_cliente.shutdown(socket.SHUT_RDWR) # Avisar al SO y cerrar
				self.socket_cliente.close()
				self.textEdit_recibido.append("Socket del cliente cerrado correctamente.")
			except Exception:
				pass # Si ya estaba cerrado, ignoramos

		self.textEdit_recibido.append("Aplicación cliente cerrada.")
		event.accept()

if __name__ == "__main__":
	app = QApplication(sys.argv) #Se crea la instancia de la aplicación
	window = MainWindow()        #Se crea una instancia de la clase MainWindow
	window.show()                #Se muestra la ventana, por defecto esta oculta
	sys.exit(app.exec())    #Se inicia el bucle de eventos, se espera hasta que se cierre la ventana