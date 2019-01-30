#!/usr/bin/env python3.6
import pyperclip
from user import User
#To add an account
def create_contact(account,username,password):
    '''
    Function to create a new account
    '''
    new_user = User(account,username,password)
    return new_user
#To save a user
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()    
def find_user(account):
    return User.find_by_account(account)    
def check_existing_user(account):
    return User.user_exist(account)    