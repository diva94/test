'''
File name: main.py
Description: Entry point of our program. Main thread is running here.
'''

from models import BookLibrary, UserLibrary
from book import Book
from user import User
from storage import save_to_file, load_from_file
from check import check_out_book, check_in_book

books = BookLibrary()
users = UserLibrary()

#the main function for library management system, also the starting point of product.
def main(self):
    try:
        # books = BookLibrary()
        # users = UserLibrary()

        # Load existing data from files
        books_data = load_from_file('books.json')
        users_data = load_from_file('users.json')

        for book_data in books_data:
            books.add_books(Book(**book_data))
        for user_data in users_data:
            users.add_users(User(**user_data))

        while True:
            print("\nLibrary Management System")
            print("1. Manage Books")
            print("2. Manage Users")
            print("3. Check Out Book")
            print("4. Check In Book")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                manage_books(books)
            elif choice == '2':
                manage_users(users)
            elif choice == '3':
                check_out_book_menu(books, users)
            elif choice == '4':
                check_in_book_menu(books)
            elif choice == '5':
                # Save data to files before exiting
                save_to_file([book.to_dict() for book in books.list_books()], 'books.json')
                save_to_file([user.to_dict() for user in users.list_users()], 'users.json')
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print("Exception occured, Please try again.")

#this method handles all the functions related to books.
def manage_books(self,books):
    try:
        while True:
            print("\nManage Books")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Search Book")
            print("4. List Books")
            print("5. Go Back")

            choice = input("Enter your choice: ")

            if choice == '1':
                add_book(books)
            elif choice == '2':
                remove_book(books)
            elif choice == '3':
                search_book(books)
            elif choice == '4':
                list_book(books)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    except Exception as e:
        print("Exception occured, Please try again.")

#method for adding books.
def add_book(self,books):
    try:
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        book = Book(title, author, isbn)
        books.add_books(book)
        print("Book added successfully.")

    except Exception as e:
        print("Exception occured, Please try again.")

#method for removing books.
def remove_book(self,books):
    try:
        title = input("Enter title of the book to remove: ")
        found_books = books.search_books("title", title) #will call method in model.py to search book.

        #below condition will check if book is present in the system. If yes then remove_books method will run from model.py
        if found_books:
            for i, book in enumerate(found_books):
                print(f"{i+1}. {book.title} by {book.author}")
            choice = int(input("Enter the number of the book to remove: ")) - 1
            books.remove_books(found_books[choice])
            print("Book removed successfully.")
        else:
            print("Book not found.")

    except Exception as e:
        print("Exception occured, Please try again.")

#method for searching the books.
def search_book(self,books):
    try:
        attribute = input("Enter search attribute (title/author/isbn): ").lower()
        value = input(f"Enter {attribute}: ")
        found_books = books.search_books(attribute, value)
        if found_books:
            for book in found_books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available: {book.available}")
        else:
            print("No books found.")

    except Exception as e:
        print("Exception occured, Please try again.")

#mehod for listing the books.
def list_book(self,books):
    try:
        all_books = books.list_books()
        if all_books:
            for book in all_books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available: {book.available}")
        else:
            print("No books in the library.")

    except Exception as e:
        print("Exception occured, Please try again.")

#from here all the methods are for user management.
def manage_users(self,users):
    try:
        while True:
            print("\nManage Users")
            print("1. Add User")
            print("2. Remove User")
            print("3. Search User")
            print("4. List Users")
            print("5. Go Back")

            choice = input("Enter your choice: ")

            if choice == '1':
                add_user(users)
            elif choice == '2':
                remove_user(users)
            elif choice == '3':
                search_user(users)
            elif choice == '4':
                list_user(users)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    except Exception as e:
        print("Exception occured, Please try again.")

def add_user(self,users):
    try:
        name = input("Enter name: ")
        user_id = input("Enter user ID: ")
        user = User(name, user_id)
        users.add_users(user)
        print("User added successfully.")

    except Exception as e:
        print("Exception occured, Please try again.")

def remove_user(self,users):
    try:
        user_id = input("Enter user ID of the user to remove: ")
        found_users = users.search_users("user_id", user_id)
        if found_users:
            for i, user in enumerate(found_users):
                print(f"{i+1}. {user.name}, ID: {user.user_id}")
            choice = int(input("Enter the number of the user to remove: ")) - 1
            users.remove_users(found_users[choice])
            print("User removed successfully.")
        else:
            print("User not found.")

    except Exception as e:
        print("Exception occured, Please try again.")

def search_user(self,users):
    try:
        attribute = input("Enter search attribute (name/user_id): ").lower()
        value = input(f"Enter {attribute}: ")
        found_users = users.search_users(attribute, value)
        if found_users:
            for user in found_users:
                print(f"Name: {user.name}, ID: {user.user_id}")
        else:
            print("No users found.")

    except Exception as e:
        print("Exception occured, Please try again.")

def list_user(self,users):
    try:
        all_users = users.list_users()
        if all_users:
            for user in all_users:
                print(f"Name: {user.name}, ID: {user.user_id}")
        else:
            print("No users in the library.")

    except Exception as e:
        print("Exception occured, Please try again.")

def check_out_book_menu(self,books, users):
    try:
        title = input("Enter the title of the book to check out: ")
        found_books = books.search_book("title", title)
        if found_books:
            book = found_books[0]  # Assuming only one book with the same title
            user_id = input("Enter user ID: ")
            found_users = users.search_user("user_id", user_id)
            if found_users:
                user = found_users[0]  # Assuming only one user with the same ID
                if check_out_book(book, user):
                    print("Book checked out successfully.")
                else:
                    print("Book is not available.")
            else:
                print("User not found.")
        else:
            print("Book not found.")

    except Exception as e:
        print("Exception occured, Please try again.")

def check_in_book_menu(self,books):
    try:
        title = input("Enter the title of the book to check in: ")
        found_books = books.search_book("title", title)
        if found_books:
            book = found_books[0]  # Assuming only one book with the same title
            check_in_book(book)
            print("Book checked in successfully.")
        else:
            print("Book not found.")

    except Exception as e:
        print("Exception occured, Please try again.")

if __name__ == "__main__":
    main()
