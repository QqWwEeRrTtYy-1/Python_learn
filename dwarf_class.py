import time

class Dwarf:
	"""Дварф с именем"""
	#Колличество дварфов
	population = 0

	def __init__(self, name):
		self.name = name
		print("Инициализация дварфа {}".format(self.name))
		Dwarf.population += 1

	def __del__(self):
		print("Дварф по имени {} выпил много пива и взорвался!".format(self.name))
		Dwarf.population -= 1
		if Dwarf.population == 0:
			print("Все дварфы упились до смерти! Последний дварф скончался...")
		else:
			print("Сейчас в таверне гуляет {} дварфов!".format(Dwarf.population))

	def Drink_beer(self):
		print("Дварф по имени {} пошёл пить пиво".format(self.name))

	def Throw(self):
		print("Дварф по имени {} пошёл кидать бутылки в прохожих".format(self.name))

dwarf_1 = Dwarf("Эльбурн")
dwarf_2 = Dwarf("Бильбурн")
time.sleep(2)
dwarf_1.Drink_beer()
time.sleep(2)
dwarf_2.Throw()
time.sleep(2)
