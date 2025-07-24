#Validate user input excercise
#conditions:
#Username should not be more than 25chars
#Username if contain spaces then replace with -
#Username should not contain numbers

name = input("Enter your name here:")#Taking the name as the input

if(len(name) >= 25):
    print("Username should be less than 12 characters")
else:
    if(name.isalpha()):
        print("Name should not contain numbers ")
    else:
        if(name.find(" ") != -1):
            name1 = name.replace(" ","-")
            final_name = name1
            print(f"Added the name successfully!\nThe final name is:{final_name}")
        else:
            final_name = name
            print(f"Added the name successfully!\nThe final name is:{final_name}")
