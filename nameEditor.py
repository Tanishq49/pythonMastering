#Making the name editor using the Getters and Setters..

class Person:
	def __init__(self,name):
		self._name = name
	#Making an getter function which will return the value of the self._name
	@property
	def name(self):
		return self._name
	#Using the setter which allows the code to change the value of self._name
	@name.setter
	def name(self,newName):
		self._name = newName

user = Person("Guest")
print(f"The default name of the user is:{user.name}")

user.name = "Trifalic"
print(f"The name after changing is:{user.name}")