#Map filter and reduce functions

#* Map function example

#Making an function which will do the square of the number

square = lambda x: x**2

#Making an lists of the number to get its square
numbers = [1,2,3,4,5,6,7,8,9,0]

newList = list(map(square,numbers))
print("The square of the numbers is:",newList)

#* Filter function 

def filter_function(x):
    return x > 50

#Filtering the list newList
filtered_list = list(filter(filter_function,newList))
print("The new filtered list is:",filtered_list)

#* Reduce function 
from functools import reduce #We have to import reduce to use it

addition_numbers = [1,2,3,4,5]

addedNumber = reduce(lambda x,y: x+y , addition_numbers)
print("The total sum is:",addedNumber)