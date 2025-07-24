#String methods in python

name = input("Enter your full name:")

length = len(name) #Gives the length of the string
print(f"The length of your name is {length}")

space = name.find(" ") #Finds the number at the given index
if(space == -1):
    print("You didnt enetred your full name")
else:
    print("Nice!You entered your full name")
    
letter_a = name.rfind("a") #Finds the given character from the last

if(letter_a == -1):
    print("No character found \"a\"")
else:
    print(f"The letter a in your name from last is in the index number {letter_a}")
    
capitalized_name = name.capitalize() #This will capitalize the given string
print(f"Your capitalized name is: {capitalized_name}")

upper_name = name.upper() #Make all the characters in the string capitalized
print(f"The upper name is {upper_name}")

lower_name = name.lower() #Make all the characters in the string in the lower case\
print(f"The name in the lower case is {lower_name}")

is_digit = name.isdigit() #Checks the string if the name is digit
print(f"Your name is digit {is_digit}")

is_alpha = name.isalpha() #Checks if the name is alpha numeric 
print(f"Your name is alpha numeric.The answer is {is_alpha}")