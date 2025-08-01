#This will do the sum of all odd numbers 
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7]

def is_odd(a):
    return a % 2 != 0

odd_list = list(filter(is_odd,numbers))
print("The odd numbers in the list are:",odd_list)

odd_sum = reduce(lambda x,y: x+y,odd_list)
print("The sum of all the odd numbers in the list is:",odd_sum)