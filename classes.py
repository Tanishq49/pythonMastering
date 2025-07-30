#Classes in python
class Employee:
    name = 'Null'
    income = 0
    def info(self):
        print(f"{self.name} get the monthly income of ${self.income}")

user = Employee()

username = input("Enter your name:")
user.name = username

user_income = int(input("Enter your income:"))
user.income = user_income

user.info()

 