#Objects in python
#Defination - Object is an function which is used in the classes

class Person:
    def __init__(self,name,occupation,income):
        self.name = name
        self.occupation = occupation
        self.income = income
        
    def info(self):
        print(f"{self.name} is an {self.occupation} and his income is {self.income}")

username = input("Enter your name:")
occupation = input("Enter your occupation:")
income = int(input("Enter your income:"))

user = Person(username,occupation,income)
user.info()
