#Static methods in python

#We can use the methods to ship the function with classes

class Math:
    def __init__(self,num):
        self._num = num
    @staticmethod
    def add(a , b): #Now we dont have to give the self as an argument to this function
        return a + b

m1 = Math(1)
print(f"The number you gave is:{m1._num}")

#Using the add method
print(f"The sum of 5 and 9 is:{m1.add(5,9)}")

#We can also do like this..
print(f"Adding the numbers using the name of the class and the answer is:{Math.add(5,9)}")