#Making the resurant menu using the classes
#Items-Coffee,pizza,burger,hotDog

class Menu:
    def __init__(self,_coffeePrice,_pizzaPrice,_burgerPrice,_hotDogPrice):
        self._coffeePrice = 1
        self._pizzaPrice = 10
        self._burgerPrice = 4
        self._hotDogPrice = 2

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
    