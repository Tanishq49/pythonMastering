from colorama import Fore,Style,init

init(autoreset=True)

#This code shows how we can get the value and name of the each varibe inside the __init__ using the for loop

class Programmer:
    def __init__(self,name,programmingLanguage,experience):
        self._name = name
        self._programmingLanguage = programmingLanguage
        self._experience = experience
    
    #? Main topic of the code..
    @property
    def info(self):
        print(f"{Fore.GREEN}Info of the programmer is:")
        for key,value in self.__dict__.items():
            realName = key.split("_")
            print(f"{Fore.BLUE}{realName[1]} = {Fore.YELLOW}{value}")
    
    #Making some functions using the getters and setters to change the name,programmingLanguage and exprience
    @property
    def name(self):
        return self._name
    @property
    def programmingLanguage(self):
        return self._programmingLanguage
    @property
    def experience(self):
        return self._experience

    @name.setter
    def name(self,newName):
        self._name = newName
    @programmingLanguage.setter
    def programmingLanguage(self,newProgrammingLanguage):
        self._programmingLanguage = newProgrammingLanguage
    @experience.setter
    def experience(self,newExperience):
        self._experience = newExperience


username = input("Enter your name here:")
programmingLanguage = input("Enter your programming language here:")
experience = int(input("Enter your experience in the programming language here:")) 

programmer1 = Programmer(username,programmingLanguage,experience)
programmer1.info

while True:
    command = input("Enter any command to execute:")
    if command == "info":
        programmer1.info
        
    elif command == "changeName":
        newName = input("Enter the new name:")
        programmer1.name = newName
        print(f"{Fore.GREEN}Changed the name successfully!")
        
    elif command == "changeProgrammingLanguage":
        newProgrammingLanguage = input("Enter the new programming language:")
        programmer1.programmingLanguage = newProgrammingLanguage
        print(f"{Fore.GREEN}Changed the name of the programmming language!")
        
    elif command == "changeExperience":
        newExperience = int(input("Enter the new experience here:"))
        programmer1.experience = newExperience
        print(f"{Fore.GREEN}Changed the number of experience years")
        
    elif command == "break":
        print(f"{Fore.GREEN}Broke out of the loop successfully!")
        break
    
    else:
        print(f"{Fore.RED}Invalid command please enter a valid command to execute")