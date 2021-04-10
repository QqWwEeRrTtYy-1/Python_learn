# https://pymorphy2.readthedocs.io/en/0.2/user/index.html

import re
import pymorphy2  # pip install pymorphy2
from collections import Counter
import timeit
import time

def main():
    print("Программа выполняется. Пожалуйста, подождите!")
    # TODO: file missing exception
    with open("source.txt", "r", encoding="utf-8") as source_file:
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

    result = dict(Counter(normal_list).most_common(20))

    with open("result.txt", "w", encoding="utf-8") as destination_file:
        for key, value in result.items():
            line = f"{key} : {value}\n"
            destination_file.write(line)

print("Программа выполнена за", round(timeit.timeit(main, number=1), 2), "секунд")
print("Результат записан в файл result.txt")