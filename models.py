'''
File name: model.py
Description: program to manage books as well as users, calls book.py & users.py for adding books and users respectively.
'''

from book import Book
from user import User

class BookLibrary:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def remove_books(self, book):
        self.books.remove(book)

    def search_books(self, attribute, value):
        return [book for book in self.books if getattr(book, attribute) == value]

    def list_books(self):
        return self.books

class UserLibrary:
    def __init__(self):
        self.users = []

    def add_users(self, user):
        self.users.append(user)

    def remove_users(self, user):
        self.users.remove(user)

    def search_users(self, attribute, value):
        return [user for user in self.users if getattr(user, attribute) == value]

    def list_users(self):
        return self.users
