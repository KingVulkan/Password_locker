# import unittest
class User :

    user_list = []
    def __init__ (self, account, username, password):
        self.account = account
        self.username = username
        self.password = password

    contact_list = [] # Empty contact list
 # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)