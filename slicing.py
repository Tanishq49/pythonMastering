string = input("Enter any string:")
result = 0

starting_index = int(input("Enter the starting index:"))
ending_index = int(input("Enter the ending index:"))
step_allow = input("Do you want stepping while slicing(yes/no)?:")

if(step_allow == "yes"):
    stepping = int(input("Enter the stepping value:"))
    result = string[starting_index:ending_index:stepping]
    print("The result is:",result)
else:
    result = string[starting_index:ending_index]
    print("The result is:",result)