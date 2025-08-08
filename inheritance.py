#Inheritance in Python

class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    

class Programmer(Employee):
    @property
    def qualities(self):
        print(f"The name of the programmer is {self.name} and the age of the programmer is {self.age}")
        
    @property 
    def change_name(self):
        return self.name
    @change_name.setter
    def change_name(self,newName):
        self.name = newName+".Junior"
    

employee1 = Programmer("Alex",23)
employee1.qualities

employee1.change_name = input("Enter your name to add in the class:")
employee1.qualities


#What is the use of the inheritance in OOP?
# -> Inheritance helps us to do some basic operations with the classes like making an clone class using the 
# parent class.
