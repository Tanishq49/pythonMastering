#Cloning the class into the another class using the inheritance

class Employee:
    def __init__(self,name,occupation,salary):
        self._name = name
        self._occupation = occupation
        self._salary = salary
        
#Using the class
emp1 = Employee("Tanishq","Hacker",100)

#Making another class with the same values as the Employee class

class JuniorEmployees(Employee):
    @property
    def info(self):
        print(f"{self._name} is an {self._occupation} with the salary {self._salary}")

#Checking that if this class is working
junior1 = JuniorEmployees("Alexander","Hacker",40)
junior1.info

#! We can't do emp1.info because the class Employee has not the properties of the class JuniorEmployees 