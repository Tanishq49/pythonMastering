#Library management code in python using the classes (OOP)

class Library:
    def __init__(self):
        self._books = {
             "To Kill a Mockingbird": 7,
            "1984": 6,
            "Pride and Prejudice": 5,
            "The Great Gatsby": 10,
            "The Catcher in the Rye": 8,
            "The Hobbit": 12,
            "Fahrenheit 451": 6,
            "Moby Dick": 9.50,
            "War and Peace": 14,
            "The Odyssey": 11,
            "Crime and Punishment": 13,
            "Brave New World": 7,
            "The Lord of the Rings": 15,
            "Animal Farm": 5,
            "Jane Eyre": 7
}
        self._borrowRecords = {}
    @property
    def totalBooks(self):
        return len(self._books)
    @property
    def addBooks(self):
        return self._books
    @addBooks.setter
    def addBooks(self,dict):
        self._books.update(dict)
    @property
    def borrowBook(self):
        return self._books
    @borrowBook.setter
    def borrowBook(self,bookName):
        try:
            self._borrowRecords.update({bookName:self._books[bookName]})
            del self._books[bookName]
            print("Borrowed the book successfully from the library!")
        except KeyError:
            print("Book not found in the library")
    @property
    def borrowRecords(self):
        return self._borrowRecords
    @borrowRecords.setter
    def borrowRecords(self,bookName):
        try:
            self._books.update({bookName: self._borrowRecords[bookName]})
            del self._borrowRecords[bookName]
            print("Returned the book successfully in the library")
        except KeyError:
            print(f"No borrowed book found with the name {bookName}")
    
library = Library()
while True:
    command = input("Enter the command:")
    if command == "list_books":
        print(library.addBooks)
    elif command == "total_books":
        print(library.totalBooks)
    elif command == "show_borrow_records":
        if library.borrowRecords == {}:
           print("Null")
        else:
            print(library.borrowRecords)
    elif command == "borrow_book":
        bookName = input("Enter the name of the book to borrow:")
        library.borrowBook = bookName
    elif command == "return_book":
        bookName = input("Enter the book name to return:")
        library.borrowRecords = bookName
    else:
        print("Invalid command please enter a valid command..")