'''
File name: books.py
Description: Adds books title, author, isbn to the dictionary.
'''

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        self.books = []

    def add_books_to_dict(self):
        try:
            return {
                "title": self.title,
                "author": self.author,
                "isbn": self.isbn,
                "available": self.available
            }
        except Exception as e:
            print("Exception occured, could not add book. Please try again")



