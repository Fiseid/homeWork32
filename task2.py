class Dog:
	age_factor = 7
	def __init__(self, old):
		self.old = old
	def human_age(self):
		return self.old * Dog.age_factor
z = int(input())
x = Dog(z)
print(x.human_age())