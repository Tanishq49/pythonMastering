#String methods in python and using the if else statements

current_programming_language = input("Enter the current programming language in which you are currently working:")

print(f"Oh so you are working in {current_programming_language}")

string_method = input("Enter the string method you want to use:")
 
if(string_method == "lower"):
    result = current_programming_language.lower()
    print(result)
elif(string_method == "upper"):
    result = current_programming_language.upper()
    print(result)
elif(string_method == "len"):
    result = len(current_programming_language)
    print(result)
elif(string_method == "capitalize"):
    result = current_programming_language.capitalize()
    print(result)
else:
    print("Invalid Method..")