names = ["sam", "johnny", "rob", "alice", "zack", "christopher"]

# TODO: Use filter() for length > 4, then map() to upper

def is_long(word):
    return len(word) > 4

long_words = list(filter(is_long,names))
print(f"The words which have more than 4letters are {long_words}")

#Converting the words to the uppercase 
uppercase_converter = lambda word: word.upper()
final_list = list(map(uppercase_converter,long_words))
print(f"The final result is {final_list}")