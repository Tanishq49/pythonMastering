#This is the calculator code in the python using the switch case

num1 = int(input("Enter the first number:"))

num2 = int(input("Enter the second number:"))

operator = input("Enter the operator:")

match(operator):
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
        
        