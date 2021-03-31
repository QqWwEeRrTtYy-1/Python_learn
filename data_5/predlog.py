import re

with open("pred.txt", encoding="utf-8") as data_1:
	text = data_1.read()

text = text.split("\n")
stop_set = set(text)