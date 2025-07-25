#Indexing helps us to get the value at the specified index(indexing starts from 0)

name = "Tanishq49"

#You can also try this
# for i in range(len(name)):
#     print(name[i]) 

#Lets access the characters from index 1 to 4..
print(name[1:5])

#Another way to access the string from the starting
print(name[:5]) #This will get from 0-5 OR 0-4(according to python)

#Now accessing all the characters after the index number 2->
print(name[2:])

#Accessing the last value of the string
print(name[-1])

#Printing the values by leaving one index
print(name[::2])