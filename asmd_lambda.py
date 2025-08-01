# asmd -> Add substract multiply divide

add = lambda x,y : x+y
substract = lambda x,y: x-y
multiply = lambda x,y : x*y
divide = lambda x,y: x/y

while True: #?This is an infinite loop which cant break automatically 

    function_name = input("Enter any function name to execute:")
    if function_name == "add":
        value1 = int(input("Enter the value 1:"))
        value2 = int(input("Enter the value number 2:"))
        print(add(value1,value2))
    elif function_name == "substract":
        value1 = int(input("Enter the value 1:"))
        value2 = int(input("Enter the value number 2:"))
        print(substract(value1,value2))
    elif function_name == "substract":
        value1 = int(input("Enter the value 1:"))
        value2 = int(input("Enter the value number 2:"))
        print(multiply(value1,value2))
    elif function_name == "substract":
        value1 = int(input("Enter the value 1:"))
        value2 = int(input("Enter the value number 2:"))
        print(divide(value1,value2))
    elif function_name == "break":
        print("Exitted the infinite loop")
        break
    else:
        print("Invalid function name")