import sys
from zhmak import *
from PyQt5.QtCore import QCoreApplication


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def addition():
	term = ui.plainTextEdit.toPlainText()
	ui.listWidget.addItem(term)


def calc():
	result = 0
	ui.label.setText(result)

ui.pushButton_10.clicked.connect(addition)
ui.pushButton_11.clicked.connect(calc)

sys.exit(app.exec_())result