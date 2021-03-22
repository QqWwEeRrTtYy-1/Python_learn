class Person:
	def __init__(self, name):
		self.name = name

	def SayHello(self):
		print("{0}, hello!".format(self.name))

finish = Person("John")
finish.SayHello()
