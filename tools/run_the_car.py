from colorama import Fore,Style,init
import random

init(autoreset=True)

#Defining the state of the car
state = "off"

class Car:
    def __init__(self,name):
        self.name = name
    def car_name(self):
        print(f"{Fore.BLUE}You have the car:{self.name}")
    def start_car(self):
        print(f"{Fore.GREEN}Started the car successfully")
        global state
        state = "on"
    def drift(self):
        global state
        randomNumber = random.randint(1,3)
        if randomNumber == 1 and state == "on":
            print(f"{Fore.YELLOW}Nice drift")
        elif randomNumber == 0 or state == "off":
            if state == "off":
                print("Turn on the car first")
            else:
                print(f"{Fore.RED}Oh no!You crashed the car")
                state = "off"
        else:
            state = "off"
            print(f"{Fore.YELLOW}Oh no!You crashed the car")
    def restart(self):
        print(f"{Fore.CYAN}Restarted the game")
        self.start_car()
    def stop(self):
        global state
        state = "off"
        print(f"{Fore.MAGENTA}Turned off the car")
            
car_name = input("Enter your car name:")
car = Car(car_name)
while True:
    command = input("Enter the command:")
    if command == "car_name":
        car.car_name()
    elif command == "start":
        car.start_car()
    elif command == "drift":
        car.drift()
    elif command == "restart":
        car.restart() 
    elif command == "stop":
        car.stop()
    else:
        print(f"{Fore.RED}Invalid command")