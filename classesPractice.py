from colorama import Fore,Style,init

#Autoresetting the coloring of the colorama
init(autoreset=True)

#Doing the practice of classes 
class User:
    def __init__(self,name,age,occupation,salary):
            self.name = name
            self.age = age
            self.occupation = occupation
            self.salary = salary
    def User_info(self):
        print(f"{Fore.GREEN}{self.name} is {self.age} years old and his occupation is {self.occupation} and his salary is ${self.salary}")

username = input("Enter your name:")
age = int(input("Enter your age:"))
occupation = input("Enter your occupation:")
salary = int(input("Enter your salary(in $):"))
user1 = User(username,age,occupation,salary)
user1.User_info()

#Making another user but with some changes in value
user2 = User(username+"bhai",age+1,occupation+".Junior",salary+100)
user2.User_info()
