#Lambda functions in python
#*Lambda functions are the anonymus function which dont have their names and cant be identified

#Making an Lambda function to do the double of the given number
double = lambda x: x*2

#*This is same to-->>
#def double(x):
#   return x*2

print(double(10))

#Making an lambda function which will take the 2values as the argument
sum = lambda x,y: x+y
print(sum(4,5))

#Passing an function to an function
def main_function(fx,value):
    return "The result is:",fx(value)

print(main_function(double,2))