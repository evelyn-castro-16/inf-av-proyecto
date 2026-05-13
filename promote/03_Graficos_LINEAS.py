import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from ventana import Ui_MainWindow

from PySide6.QtCharts import QChart, QLineSeries, QBarCategoryAxis, QValueAxis
from PySide6.QtCore import Qt,QPointF
from PySide6.QtGui import QPainter, QColor, QFont

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setWindowTitle("Informática Avanzada - Grafico de lineas")
		self.setWindowIcon(QIcon("logo_unlam.jpg"))

		#Crear la serie y agregar los datos
		serie_a = QLineSeries()
		serie_b = QLineSeries()

		serie_a.append(1, 5)	# Punto 1 (X=0, Y=5)
		serie_a.append(2, 12.3)	# Punto 2
		serie_a.append(3, -3)	# Punto 3
		serie_a.append(4, 18)
		serie_a.append(5, 8)

		meses = [1, 2, 3, 4, 5]
		ventas_a = [5, 12.3, -3, 18, 8]
		puntos = [QPointF(x, y) for x, y in zip(meses, ventas_a)]
		serie_a.replace(puntos)
		serie_a.setName("Locar Nº1")

		ventas_b = [15, 22.3, 7, 28, 18]
		puntos = [QPointF(x, y) for x, y in zip(meses, ventas_b)]
		serie_b.replace(puntos)
		serie_b.setName("Locar Nº2")

		# Crear el gráfico
		chart = QChart()
		#chart.setTheme(QChart.ChartThemeLight)
		#chart.setTheme(QChart.ChartThemeBlueIcy)
		#chart.setTheme(QChart.ChartThemeBlueNcs)
		#chart.setTheme(QChart.ChartThemeDark)
		chart.setTheme(QChart.ChartThemeBlueCerulean)
		#chart.setTheme(QChart.ChartThemeBrownSand)		
		#chart.setTheme(QChart.ChartThemeHighContrast)
		#chart.setTheme(QChart.ChartThemeQt)

		chart.addSeries(serie_a)
		#chart.addSeries(serie_b)
		chart.legend().setVisible(False)
		chart.createDefaultAxes() #Crear los ejes X e Y

		#fuente = QFont("Arial", 14)
		#fuente.setBold(True)
		#chart.setTitleFont(fuente)
		chart.setTitle("Reporte Mensual de Ventas")

		#chart.setAnimationOptions(QChart.NoAnimation)
		#chart.setAnimationOptions(QChart.GridAxisAnimations)
		#chart.setAnimationOptions(QChart.SeriesAnimations)
		chart.setAnimationOptions(QChart.AllAnimations)

		#Asignar el gráfico al widget
		self.widget_grafico.setChart(chart)
		self.widget_grafico.setRenderHint(QPainter.Antialiasing)	#Eliminar el efecto de escalonado


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())