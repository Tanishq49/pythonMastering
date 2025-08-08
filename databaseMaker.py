import os
from colorama import Fore,Style,init

init(autoreset=True)

#This code can make the database using the classes

class Database:
    def __init__(self,name,age,programmingLanguage,job,country,phoneNumber,email,discord,work):
        self._name = name
        self._age = age 
        self._programmingLanguage = programmingLanguage
        self._job = job
        self._country = country
        self._phoneNumber = phoneNumber
        self._email = email
        self._discord = discord
        self._work =  work
        
    #Making the functions capable of changing the values of the __init__ using te getters and setters
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @property
    def programmingLanguage(self):
        return self._programmingLanguage
    @property
    def job(self):
        return self._job
    @property
    def country(self):
        return self._country
    @property
    def phoneNumber(self):
        return self._phoneNumber
    @property
    def email(self):
        return self._email
    @property
    def discord(self):
        return self._discord
    @property
    def work(self):
        return self._work

    #Using the setters to enable the editing the __init__ values
    @name.setter
    def name(self,newName):
        self._name = newName
    @age.setter
    def age(self,newAge):
        self._age = newAge
    @programmingLanguage.setter
    def programmingLanguage(self,newProgrammingLanguage):
        self._programmingLanguage = newProgrammingLanguage
    @job.setter
    def job(self,newJob):
        self._job = newJob
    @country.setter
    def country(self,newCountry):
        self._country = newCountry
    @phoneNumber.setter
    def phoneNumber(self,newPhoneNumber):
        self._phoneNumber = newPhoneNumber
    @email.setter
    def email(self,newEmail):
        self._email = newEmail
    @discord.setter
    def discord(self,newDiscordUsername):
        self._discord = newDiscordUsername
    @work.setter
    def work(self,newWork):
        self._work = newWork
    
    #Making an info function using the getter
    @property
    def info(self):
        print("The info of the person is:")
        for key,value in self.__dict__.items():
            mainName = key.split("_")
            print(f"{mainName[1]}:{value}")

try:
    while True:
        command = input("Enter the command:")
        if command == "init":
            name = input("Enter the name here:")
            age = int(input("Enter the age here:"))
            programmingLanguage = input("Enter the programming language here:")
            job = input("Enter the job here:")
            country = input("Enter the country here:")
            phoneNumber = int(input("Enter the phone number here:"))
            email = input("Enter the email here:")
            discord = input("Enter the discord username here:")
            work = input("Enter the work here:")
            person = Database(name,age,programmingLanguage,job,country,phoneNumber,email,discord,work)
        elif command == "changeName":
            newName = input("Enter the newName here:")
            person.name = newName
        elif command == "changeAge":
            newAge = int(input("Enter the new age here:"))
            person.age = newAge
        elif command == "changeProgrammingLanguage":
            newProgrammingLanguage = input("Enter the new programming language here:")
            person.programmingLanguage = newProgrammingLanguage
        elif command == "changeJob":
            newJob = input("Enter the name of the new job:")
            person.job = newJob
        elif command == "changeCountry":
            newCountry = input("Enter the new country:")
            person.country = newCountry
        elif command == "changePhoneNumber":
            newPhoneNumber = int(input("Enter the new phone number here:"))
            person.phoneNumber = newPhoneNumber
        elif command == "changeEmail":
            newEmail = input("Enter the new email here:")
            person.email = newEmail
        elif command == "discord":
            newDiscordUsername = input("Enter the new discord username:")
            person.discord = newDiscordUsername
        elif command == "changeWork":
            newWork = input("Enter the new work here:")
            person.work = newWork
        elif command == "exit":
            break
        elif command == "push":
            template = f"""
            Name:{person.name}
            Age:{person.age}
            ProgrammingLanguage:{person.programmingLanguage}
            Job:{person.job}
            Country:{person.country}
            PhoneNumber:{person.phoneNumber}
            Email:{person.email}
            DiscordUsername:{person.discord}
            Work:{person.work}
            """
            if os.path.exists("database"):
                with open("./database/databaseMain.txt",'a') as database:
                    database.write(template)
                database.close()
            else:
                os.mkdir("database")
                with open("./database/databaseMain.txt",'a') as database:
                    database.write(template)
                database.close()
        elif command == "info":
            person.info
        else:
            print("Invalid Command!Enter a valid command")
except Exception as e:
    print(f"{Fore.RED}Some error occured,Error:{e}")