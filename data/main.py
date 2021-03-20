"""
1)Открыть файл и извлечь обёртку
2)Прочитать обёртку и сохранить в переменную 
3)Преобразовать текст в строчные буквы
4)Заменить "ё" на "е"
5)Оставить в тексте только буквы (убрать остальные знаки)
6)Считаем слова с помощью библиотеки "collections" и берём первые 20
"""
import re as r
from collections import Counter

with open("text.txt", encoding="utf-8") as data:
	text = data.read()

text = text.lower()
text = r.sub("ё", "е", text)

edited_text = r.findall(r"[А-Яа-я]+", text)

result = dict(Counter(edited_text).most_common(20))
print(result)
