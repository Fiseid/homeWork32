class Person:
	def __init__(self, name, firstname, old):
		self.name = name
		self.fistname = firstname
		self.old = old
	def talk(self):
		print(f'Привет, меня зовут {self.name} {self.fistname} мне {self.old} лет')

