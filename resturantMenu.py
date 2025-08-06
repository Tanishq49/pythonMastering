from colorama import Fore,Style,init

init(autoreset=True)

#Making the resurant menu using the classes
#Items-Coffee,pizza,burger,hotDog

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
        
menu = Menu(1,5,4,2)
print(f"The price of coffee is:${menu.coffeePrice}")
print(f"The price of burger is:${menu.burgerPrice}")
print(f"The price of pizza is:${menu.pizzaPrice}")
print(f"The price of hotDog is:${menu.hotDogPrice}")

#Increasing the price of the items by .5
menu.coffeePrice =  menu.coffeePrice+0.5
menu.pizzaPrice = menu.pizzaPrice+0.5
menu.burgerPrice = menu.burgerPrice+0.5
menu.hotDogPrice = menu.hotDogPrice+0.5

print(f"\n{Fore.GREEN}The menu after changing is:\n")

print(f"The price of coffee is:${menu.coffeePrice}")
print(f"The price of burger is:${menu.burgerPrice}")
print(f"The price of pizza is:${menu.pizzaPrice}")
print(f"The price of hotDog is:${menu.hotDogPrice}")