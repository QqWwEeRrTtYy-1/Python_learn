# https://pymorphy2.readthedocs.io/en/0.2/user/index.html
# кнопка сохранения непустого результата
# прогресс-бар
# сделать неактивным интерфейс во время анализа

import re
import pymorphy2  # pip install pymorphy2
from collections import Counter
import sys
import time
from interface import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtTest 


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def choose_file():
    global source_file
    source_file = QFileDialog.getOpenFileName()[0]
    ui.file_path.setText(source_file)


def save_file():
    global line
    save = QFileDialog.getSaveFileName(MainWindow, "result", '/', '.txt')[0]
    file = open(save, 'w')
    file.write(line)
    file.close()
    file_way = "Файл сохранён в " + str(save)
    ui.message.addItem(file_way) 


def main():
    ui.save_button.setVisible(False) 
    ui.start.setVisible(False)
    start_time = time.time()
    ui.message.clear()
    ui.message.addItem("Подождите, идет анализ текста.")
    QtTest.QTest.qWait(1) # обновить интерфейс
    global source_file
    global line
    print("Программа выполняется. Пожалуйста, подождите!")
    # TODO: file missing exception
    with open(source_file, "r", encoding="utf-8") as source_file:
        text_str = source_file.read()

    if len(text_str) == 0:
        ui.message.addItem("Файл оказался пустым!")
        ui.save_button.setVisible(False)

    text_str = text_str.lower()
    text_str = re.sub("ё", "е", text_str)
    text_list = re.findall(r"[а-яё]+", text_str)

    normal_list = []
    morph = pymorphy2.MorphAnalyzer()

    for word in text_list:
        first_parse = morph.parse(word)[0]  # TODO: Parse с самым высоким Score
        if ui.checkbox_noun.isChecked():     
            if "NOUN" in first_parse.tag:
                normal_list.append(first_parse.normal_form)
        if ui.checkbox_adjective.isChecked():
            if "ADJF" or "ADJS" in first_parse.tag:
                normal_list.append(first_parse.normal_form)
        if ui.checkbox_verb.isChecked():
            if "VERB" in first_parse.tag:
                normal_list.append(first_parse.normal_form)

    words_number = ui.spinBox.value()
    result = dict(Counter(normal_list).most_common(words_number))

   # with open("result.txt", "w", encoding="utf-8") as destination_file:
    #    for key, value in result.items():
    #        line = f"{key} : {value}\n"
    #        destination_file.write(line)

    for key, value in result.items():
        line = f"{key} : {value}"
        ui.listWidget.addItem(line)

    stop_time = round(time.time() - start_time, 2)
    ui.message.addItem(f"Анализ завершен за {stop_time} секунд")
    ui.save_button.setVisible(True) 
    ui.start.setVisible(True)

ui.choose_file.clicked.connect(choose_file)
ui.start.clicked.connect(main)
ui.save_button.clicked.connect(save_file)
sys.exit(app.exec_())