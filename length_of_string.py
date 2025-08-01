#This will give the length of the string
fruit_names = ["apple", "banana", "cherry"]

length_counter = lambda word: len(word)

length_of_fruits = list(map(length_counter,fruit_names))
print(f"The length is:{length_of_fruits}")