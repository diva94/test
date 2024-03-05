'''
File name: check.py
Description: checks the availability of the book and adds name of checked out book in a separate dict.
'''

checkouts = []

def check_out_book(book, user, isbn):
    try:
        if book.available:
            book.available = False
            checkouts.append({"user_id": user, "isbn": isbn})
            return True
        else:
            return False
    except Exception as e:
        print("Exception occured, Checkout Unsuccessful")

def check_in_book(book):
    book.available = True
