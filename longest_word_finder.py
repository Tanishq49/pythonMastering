from functools import reduce

words = ["apple", "banana", "cherry", "mango"]

longest = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(f"The longest word is: {longest}")
