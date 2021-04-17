# https://pymorphy2.readthedocs.io/en/0.2/user/index.html

import re
import pymorphy2  # pip install pymorphy2
from collections import Counter
import sys
from interface import *
from PyQt5.QtWidgets import QFileDialog


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def choose_file():
    global source_file
    source_file = QFileDialog.getOpenFileName()[0]
    ui.file_path.setText(source_file)

def main():
    global source_file
    print("Программа выполняется. Пожалуйста, подождите!")
    # TODO: file missing exception
    with open(source_file, "r", encoding="utf-8") as source_file:
        text_str = source_file.read()

    text_str = text_str.lower()
    text_str = re.sub("ё", "е", text_str)
    text_list = re.findall(r"[а-яё]+", text_str)

    normal_list = []
    morph = pymorphy2.MorphAnalyzer()

    for word in text_list:
        first_parse = morph.parse(word)[0]  # TODO: Parse с самым высоким Score
        if "NOUN" in first_parse.tag:
            normal_list.append(first_parse.normal_form)

    words_number = ui.spinBox.value()
    result = dict(Counter(normal_list).most_common(words_number))

   # with open("result.txt", "w", encoding="utf-8") as destination_file:
    #    for key, value in result.items():
    #        line = f"{key} : {value}\n"
    #        destination_file.write(line)

    for key, value in result.items():
        line = f"{key} : {value}\n"
        ui.listWidget.addItem(line)

ui.choose_file.clicked.connect(choose_file)
ui.start.clicked.connect(main)
sys.exit(app.exec_())