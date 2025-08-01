#This function will double all the numbers in the list

double = lambda x: x*2

numbers = [3,5,7,9]

doubled_numbers_list = list(map(double,numbers))
print(f"The doubled numbers in the list are:{doubled_numbers_list}")