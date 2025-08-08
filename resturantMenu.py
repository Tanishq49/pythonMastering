from colorama import Fore,Style,init

init(autoreset=True)

#Making the resurant menu using the classes
#Items-Coffee,pizza,burger,hotDog

#*NOTE: This is also an concept of the OOP (Object Orianted Programming)

class Menu:
    def __init__(self,coffeePrice,pizzaPrice,burgerPrice,hotDogPrice):
        self._coffeePrice = coffeePrice
        self._pizzaPrice = pizzaPrice
        self._burgerPrice = burgerPrice
        self._hotDogPrice = hotDogPrice

    #Making the value returning function for all the items
    @property 
    def coffeePrice(self):
        return self._coffeePrice
    @property 
    def pizzaPrice(self):
        return self._pizzaPrice
    @property
    def burgerPrice(self):
        return self._burgerPrice
    @property
    def hotDogPrice(self):
        return self._hotDogPrice
    
    #Making the setter which allows us to change the value
    @coffeePrice.setter
    def coffeePrice(self,newPrice):
        self._coffeePrice = newPrice
    @pizzaPrice.setter
    def pizzaPrice(self,newPrice):
        self._pizzaPrice = newPrice
    @burgerPrice.setter
    def burgerPrice(self,newPrice):
        self._burgerPrice = newPrice
    @hotDogPrice.setter
    def hotDogPrice(self,newPrice):
        self._hotDogPrice = newPrice
    
    @property
    def get_food_names(self):
        return "coffee","pizza","burger","hotDog"
    
    @property
    def changePrices(self):
         return self._coffeePrice,self._burgerPrice,self._pizzaPrice,self._hotDogPrice     
        
    @changePrices.setter
    def changePrices(self,amount):
        self.coffeePrice =  self.coffeePrice+amount
        self.pizzaPrice = self.pizzaPrice+amount
        self.burgerPrice = self.burgerPrice+amount
        self.hotDogPrice = self.hotDogPrice+amount
        
menu = Menu(1,5,4,2)
print(f"The price of coffee is:${menu.coffeePrice}")
print(f"The price of burger is:${menu.burgerPrice}")
print(f"The price of pizza is:${menu.pizzaPrice}")
print(f"The price of hotDog is:${menu.hotDogPrice}")

#! menu.changePrices = int(input("How much price you want to increase/decrease in the items?:"))

print(f"\n{Fore.GREEN}The menu after changing is:\n")

for food,price in menu.__dict__.items():
    tempName = food.split("Price")
    mainName = tempName[0].split("_")
    print(f"The price of {mainName[1]} is:{price}")