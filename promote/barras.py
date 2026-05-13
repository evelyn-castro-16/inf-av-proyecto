import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon, QPainter, QColor, QFont, Qt
from ventana import Ui_MainWindow

from PySide6.QtCharts import QChart, QChartView, QPieSeries, QBarSeries, QBarSet

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setWindowTitle("Informática Avanzada - ")
		self.setWindowIcon(QIcon("ing.png"))

		serie=QBarSeries()
		set_datos=QBarSet("Ventas")
		set_datos.append([15, 25, 17, 30])
		serie.append(set_datos)
		
		# series=QPieSeries()
		# series.append("Ene", 15)
		# series.append("Feb", 25)
		# series.append("Mar", 17)
		# series.append("Abr", 30)


		chart=QChart()
		chart.setTheme(QChart.ChartThemeDark)

		chart.addSeries(serie)
		chart.setTitle("Ventas por Mes")
		chart.setAnimationOptions(QChart.AllAnimations)
		categorias=["Ene", "Feb", "Mar", "Abr"]        
		eje_x=QBarCategoryAxis()
		eje_x.append(categorias)
		chart.addAxis(eje_x, Qt.AlignBottom)
		serie.attachAxis(eje_x)
		eje_y=QValueAxis()
		chart.addAxis(eje_y, Qt.AlignLeft)
		serie.attachAxis(eje_y)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())