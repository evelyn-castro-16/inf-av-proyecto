import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPixmap
from intro_gui import Ui_MainWindow 

class ControlPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.contador_var_1 = 0
        self.segundos_timer = 0

        # --- Configuración del QTimer ---
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_tiempo)
        self.timer.start(1000)

        # --- Configuración del QTimer para intermitencia ---
        self.timer_intermitente = QTimer(self)
        self.timer_intermitente.timeout.connect(self.cambiar_color_intermitente)
        self.timer_intermitente.start(500)  # Cambia cada 500 ms

        self.color_actual_warning = True  # Estado inicial del color

        self.actualizar_pantalla_cambio_variable()
        self.configurar_botones()
        self.configurar_line_edit_carga_valor()
        self.configurar_navegacion_stacked_widget()
        self.configurar_radio_buttons()
        self.configurar_checkboxes()
        self.configurar_imagen()

    def configurar_botones(self):
        # Botón para cerrar la aplicación
        self.ui.pushButton_cerrar_app.clicked.connect(self.close)
        
        # Botones para cambiar el color de fondo
        self.ui.pushButton_fondo_azul.clicked.connect(lambda: self.cambiar_fondo("blue"))
        self.ui.pushButton_fondo_verde.clicked.connect(lambda: self.cambiar_fondo("green"))
        self.ui.pushButton_fondo_violeta.clicked.connect(lambda: self.cambiar_fondo("darkviolet"))

        self.ui.pushButton_incrementar_variable_1.clicked.connect(self.incrementar)
        self.ui.pushButton_decrementar_variable_1.clicked.connect(self.decrementar)

        self.ui.pushButton_reset_timer.clicked.connect(self.reset_timer)

    def configurar_line_edit_carga_valor(self):
        # Conectar el evento de presionar ENTER en el lineEdit_carga_valor
        self.ui.lineEdit_carga_valor.returnPressed.connect(self.actualizar_label_carga_valor)

    def configurar_navegacion_stacked_widget(self):
        # Conectar los botones de navegación a las funciones correspondientes
        self.ui.commandLinkButton_go_next.clicked.connect(self.ir_a_siguiente_pagina)
        self.ui.commandLinkButton_go_prev.clicked.connect(self.ir_a_pagina_anterior)
        self.ui.commandLinkButton_go_home.clicked.connect(self.ir_a_pagina_inicial)

    def ir_a_siguiente_pagina(self):
        # Cambiar a la siguiente página del stackedWidget
        indice_actual = self.ui.stackedWidget.currentIndex()
        total_paginas = self.ui.stackedWidget.count()
        nuevo_indice = (indice_actual + 1) % total_paginas 
        self.ui.stackedWidget.setCurrentIndex(nuevo_indice)

    def ir_a_pagina_anterior(self):
        # Cambiar a la página anterior del stackedWidget
        indice_actual = self.ui.stackedWidget.currentIndex()
        total_paginas = self.ui.stackedWidget.count()
        nuevo_indice = (indice_actual - 1 + total_paginas) % total_paginas 
        self.ui.stackedWidget.setCurrentIndex(nuevo_indice)

    def ir_a_pagina_inicial(self):
        # Cambiar a la página inicial (índice 0) del stackedWidget
        self.ui.stackedWidget.setCurrentIndex(0)

    def actualizar_label_carga_valor(self):
        # Obtener el texto del lineEdit y establecerlo en el label
        texto = self.ui.lineEdit_carga_valor.text()
        self.ui.label_carga_valor.setText(texto)

    def cambiar_fondo(self, color):
        # Aplicamos el estilo al centralwidget para cambiar el fondo del formulario
        self.ui.centralwidget.setStyleSheet(f"background-color: {color};")

    def incrementar(self):
        self.contador_var_1 += 1
        self.actualizar_pantalla_cambio_variable()

    def decrementar(self):
        self.contador_var_1 -= 1
        self.actualizar_pantalla_cambio_variable()

    def actualizar_pantalla_cambio_variable(self):
        # Convertimos a string porque el widget solo acepta texto
        self.ui.plainTextEdit_variable_1.setPlainText(str(self.contador_var_1))

    def actualizar_tiempo(self):
        self.segundos_timer += 1
        self.ui.plainTextEdit_timer.setPlainText(str(self.segundos_timer))

    def reset_timer(self):
        self.segundos_timer = 0
        self.ui.plainTextEdit_timer.setPlainText("0")

    def cambiar_color_intermitente(self):
        # Alternamos el color entre rojo y amarillo
        color_1 = "red" if self.color_actual_warning else "yellow"
        color_2 = "yellow" if self.color_actual_warning else "red"

        self.ui.label_warning_1.setStyleSheet(f"background-color: {color_1};")
        self.ui.label_warning_2.setStyleSheet(f"background-color: {color_2};")

        self.color_actual_warning = not self.color_actual_warning

    def configurar_radio_buttons(self):        
        self.ui.radioButton_panel_rosa.toggled.connect(lambda: self.cambiar_color_panel("pink"))
        self.ui.radioButton_panel_negro.toggled.connect(lambda: self.cambiar_color_panel("black"))
        self.ui.radioButton_panel_naranja.toggled.connect(lambda: self.cambiar_color_panel("orange"))

    def cambiar_color_panel(self, color):
        # Cambiar el color de fondo del label_panel
        self.ui.label_panel.setStyleSheet(f"background-color: {color};")

    def configurar_checkboxes(self):
        # Conectar los checkboxes a sus respectivas funciones
        self.ui.checkBox_panel_1.toggled.connect(lambda checked: self.mostrar_panel(self.ui.label_panel_1, checked))
        self.ui.checkBox_panel_2.toggled.connect(lambda checked: self.mostrar_panel(self.ui.label_panel_2, checked))
        self.ui.checkBox__panel_3.toggled.connect(lambda checked: self.mostrar_panel(self.ui.label_panel_3, checked))

    def mostrar_panel(self, label, mostrar):
        label.setVisible(mostrar)

    def configurar_imagen(self):
        pixmap = QPixmap("ing.png")
        self.ui.label_imagen.setPixmap(pixmap)
        self.ui.label_imagen.setScaledContents(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventana = ControlPrincipal()
    ventana.show()
    
    sys.exit(app.exec())