import sys
from interface import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def hello():
	ui.label.setText("Hello")


ui.Sbutton.clicked.connect()
sys.exit(app.exec_())