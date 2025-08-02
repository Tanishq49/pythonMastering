# 'is' vs '==' in python

a = [1,2,3]
b = [1,2,3]

print(a is b) #This will return false because these both are stored in different location in the memory
print(a == b) #This will return true because a == b

#Checking this with integers
x = 10
y = 10

#The x and y values are same so the 10 will be assigned only one time and x and y use 10 in same memory

print("Checking with integers")

print(x is y) #This will return true
print(x == y ) #This will also return true

#Now checking with strings
print("Checking with strings")
name1 = "tanishq"
name2 = "tanishq"

#The concept will be same as with the integers

print(name1 is name2) #This will return true
print(name1 == name2) #This will again return true

# '===' is same to 'is' (=== dosent exixts in python but in other languages like JavaScript and c++ it exists)