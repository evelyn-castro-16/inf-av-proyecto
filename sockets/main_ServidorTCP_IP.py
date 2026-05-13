import sys                                                 #Se importa el modulo del sistema
import socket
from PySide6.QtWidgets import QApplication, QMainWindow    #Se importan herramientas de PySide6
from PySide6.QtCore import QThread, Signal
from interfaz import Ui_MainWindow    #Se importa la clase Ui_MainWindow desde ventanaPrincipal1.py

class ServerThread(QThread): # Hilo para manejar la red sin bloquear la GUI
	mensaje_recibido = Signal(str)
	estado_cambiado = Signal(str, str) # Nueva señal: envía (Texto, Color_CSS)

	def __init__(self):
		super().__init__()
		self.running = True

	def run(self):
		conn = None 
		try:
			self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.server.bind(('127.0.0.1', 65432))
			self.server.listen(1)
			self.server.settimeout(1.0) 

			self.estado_cambiado.emit("En línea - Escuchando", "color: green;")

			while self.running:
				try:
					conn, addr = self.server.accept()
					with conn: # <--- La conexión empieza aca
						self.mensaje_recibido.emit(f"Cliente conectado desde {addr}")
						
						while self.running: # Mientras el cliente no se desconecte
							data = conn.recv(1024)
							if not data:
								break # Si no hay datos, el cliente cerró la conexión
							
							msg = data.decode('utf-8')
							self.mensaje_recibido.emit(f"Cliente: {msg}")
							conn.sendall(f"Recibido: {msg}".encode('utf-8'))
							
				except socket.timeout:
					continue 
				except Exception as e:
					self.mensaje_recibido.emit(f"Error en sesión: {e}")

		except Exception as e:
			self.mensaje_recibido.emit(f"Error crítico: {e}")
		finally:
			if conn:
				conn.close()
			if self.server:
				self.server.close()
			self.mensaje_recibido.emit("Servidor apagado.")

	def stop(self):
		self.running = False

class MainWindow(QMainWindow, Ui_MainWindow): #Se define la clase MainWindow. Hereda de QMainWindow (para ser una ventana) y de Ui_MainWindow (para acceder a los componentes de la ventana)
	def __init__(self):
		super().__init__()                    #Metodo constructor de la clase base QMainWindow
		self.setupUi(self)                    #Metodo para "dibujar" los componentes dentro de la ventana

		self.thread = None #Lo inicializamos como None para que closeEvent sepa que aun no hay hilo
		self.pushButton_iniciar.clicked.connect(self.iniciar_servidor)
		
	def iniciar_servidor(self):
		# Solo creamos el hilo si no existe uno corriendo
		self.thread = ServerThread()
		self.thread.mensaje_recibido.connect(self.actualizar_log) # Se conecta la señal del hilo con una función
		self.thread.estado_cambiado.connect(self.actualizar_estado_label) # Se conecta la señal al método de actualización
		self.thread.start()
		self.pushButton_iniciar.setEnabled(False)
		self.textEdit_logs.append("Servidor iniciado... esperando cliente.")

	def actualizar_log(self, texto):
		self.textEdit_logs.append(texto)

	def actualizar_estado_label(self, texto, estilo):
		"""Cambia el texto y el color del Label de estado"""
		self.label_estado.setText(texto)
		self.label_estado.setStyleSheet(estilo)

	def closeEvent(self, event):
		if hasattr(self, 'thread') and self.thread is not None: # Se verifica que la variable exista y no sea nula para cerrar el thread
			try:
				self.thread.stop()
				self.thread.wait(1000)
			except Exception as e:
				self.textEdit_logs.append(f"Nota al cerrar: {e}")

		self.textEdit_logs.append("Aplicación cerrada.")
		event.accept()


if __name__ == "__main__":
	app = QApplication(sys.argv) #Se crea la instancia de la aplicación
	window = MainWindow()        #Se crea una instancia de la clase MainWindow
	window.show()                #Se muestra la ventana, por defecto esta oculta
	sys.exit(app.exec())    #Se inicia el bucle de eventos, se espera hasta que se cierre la ventana