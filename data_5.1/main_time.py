"""
1)Открыть файл и извлечь обёртку
2)Прочитать обёртку и сохранить в переменную 
3)Преобразовать текст в строчные буквы -> str
4)Заменить "ё" на "е" -> str
5)Оставить в тексте только буквы (убрать остальные знаки) -> list
6)Сохранить все предлоги в переменную
7)Считаем слова с помощью библиотеки "collections" и берём первые 20 -> dict
7)Записываем результат в файл -> txt
8)Узнаём сколько времени понадобилось на исполнение
"""

import re as r
from collections import Counter
import predlog as pl
import timeit
import time
from clint.textui import progress

if __name__ == '__main__':
    def main():
        for i in progress.bar(range(100)):
            def make_file_word_searcher(file_name_start, file_name_written):
                with open(file_name_start, encoding="utf-8") as data:
                    text = data.read()

                text = text.lower()
                text = r.sub("ё", "е", text)

                #СПИСОК
                edited_text = r.findall(r"[а-я]+", text)

                #МНОЖЕСТВО
                pl.stop_set
                #СПИСОК - МНОЖЕСТВО
                for word in edited_text:
                    if word in pl.stop_set:
                        edited_text.remove(word)

                result = dict(Counter(edited_text).most_common(20))

                with open(file_name_written, "w", encoding="utf-8") as result_file:
                    for key, value in result.items():
                        new_line = f"{key} : {value}\n"
                        result_file.write(new_line)

            make_file_word_searcher("text_test.txt", "result.txt")
    
print("Выполнение программы заняло : ", round(timeit.timeit(main, number = 1 )), "ceк")
print("Файл создан")
