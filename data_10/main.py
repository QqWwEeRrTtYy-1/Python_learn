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

normal_list = []
spisok = []


def main():
    ui.save_button.setVisible(False) 
    ui.start.setVisible(False)
    start_time = time.time()
    ui.message.clear()
    ui.message.addItem("Подождите, идет анализ текста.")
    QtTest.QTest.qWait(1) # обновить интерфейс
    print("Программа выполняется. Пожалуйста, подождите!")

    text_sou = source(source_file)
    ready_text = regular_text(text_sou)
    morphed_text = morphy_text(ready_text)
    common_words_result = number_and_result(morphed_text)
    write_words(common_words_result)

    stop_time = round(time.time() - start_time, 2)
    ui.message.addItem(f"Анализ завершен за {stop_time} секунд")
    ui.save_button.setVisible(True) 
    ui.start.setVisible(True)

#ВЫБИРАЕМ ФАЙЛ
def choose_file():
    global source_file
    source_file = QFileDialog.getOpenFileName()[0]
    ui.file_path.setText(source_file)

#ОТКРЫВАЕМ ФАЙЛ-ИСТОЧНИК И ЗАПИСЫВАЕМ В ПЕРЕМЕННУЮ
def source(source_file):
    # TODO: file missing exception
    with open(source_file, "r", encoding="utf-8") as source_file:
        text_str = source_file.read()

    if len(text_str) == 0:
        ui.message.addItem("Файл оказался пустым!")
        ui.save_button.setVisible(False)

    return text_str

#ПРИВОДИМ ТЕКСТ К ОДНОМУ ВИДУ(РЕГУЛЯРКИ)
def regular_text(text_source):
    text_str = text_source.lower()
    text_str = re.sub("ё", "е", text_str)
    text_list = re.findall(r"[а-яё]+", text_str)

    return text_list

#ФИЛЬТРУЕМ ТЕКСТ, ОСТАВЛЯЯ ТОЛЬКО НУЖНЫЕ ЧАСТИ РЕЧИ
def morphy_text(reg_text):
    morph = pymorphy2.MorphAnalyzer()

    for word in reg_text:
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

    return normal_list

#БЕРЁМ САМЫЕ ПОВТОРЯЮЩИЕСЯ СЛОВА В КОЛЛИЧЕСТВЕ WORDS_NUMBER
def number_and_result(list_of_words):
    words_number = ui.spinBox.value()
    result = dict(Counter(list_of_words).most_common(words_number))

    return result

#ВЫВОДИМ СЛОВА НА LISTWIDGET И ДОБАВЛЯЕМ В SPISOK
def write_words(common_words):
    for key, value in common_words.items():
        line = f"{key} : {value}"
        ui.listWidget.addItem(line)
        spisok.append(line)

#СОХРАНЯЕМ ФАЙЛ
def save_file():
    save = QFileDialog.getSaveFileName(MainWindow, "result", '/', '.txt')[0]
    file = open(save, 'w')
    file.write("\n".join(spisok))
    file.close()
    file_way = "Файл сохранён в " + str(save)
    ui.message.addItem(file_way) 

    
ui.choose_file.clicked.connect(choose_file)
ui.start.clicked.connect(main)
ui.save_button.clicked.connect(save_file)
sys.exit(app.exec_())