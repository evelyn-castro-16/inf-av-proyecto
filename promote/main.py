import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon, QPainter, QColor, QFont
from ventana import Ui_MainWindow

from PySide6.QtCharts import QChart, QChartView, QPieSeries

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setWindowTitle("Informática Avanzada - ")
		self.setWindowIcon(QIcon("ing.png"))
		
		series=QPieSeries()
		series.append("Ene", 15)
		series.append("Feb", 25)
		series.append("Mar", 17)
		series.append("Abr", 30)

		for porcion in series.slices():
			porcion.setLabelVisible()
			# porcion.setPen(QColor("black"))
			# porcion.setLabelColor(QColor("white"))
			# porcion.setLabelFont(QFont("Arial", 10, QFont.Bold))
		
		series.setHoleSize(0.35)
		slice_destacado=series.slices()[1]
		slice_destacado.setExploded()
		slice_destacado.setBrush(QColor("red"))

		chart=QChart()
		chart.setTheme(QChart.ChartThemeDark)

		chart.addSeries(series)
		chart.setTitle("Ventas por Mes")
		chart.setAnimationOptions(QChart.AllAnimations)

		chartview=QChartView(chart)
		self.verticalLayout.addWidget(chartview)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec())