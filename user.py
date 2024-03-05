'''
File name: user.py
Description: for adding user details to dict.
'''

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def add_users_to_dict(self):
        return {
            "name": self.name,
            "user_id": self.user_id
        }
