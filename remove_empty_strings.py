#This will remove all the empty strings in the list using filter

words = ["hello", "", "world", "", "python", " "]

newList = list(filter(lambda x: x != "", words))