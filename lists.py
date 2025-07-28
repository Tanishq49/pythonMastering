names = ["Tanishq","Yugank","Ashish","Rahul"]

#Printing the length of an array
print(f"The length of the array is {len(names)}")

#Printing all the elements of the array using the while loop

i = 0 
while(i < len(names)):
    print(f"{i+1} {names[i]}")
    i += 1
    
#Printing the rough list
print(names)

#Doing the slicing in the lists
print(names[0:3])

#Adding the value inside the list
user_name = input("Enter the name that you want to append in the list:")
names.append(user_name)

print(f"The final list is {names}")

#Deleting the value from the list
user_index = int(input("Enter the index number you want to delete from the list:"))
names.pop(user_index)

print(f"The final list after deleting the element is {names}")