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
def display_users():
    return User.display_users()
#------------------------------------------------------------
def main():
    print("\033[1;36;40m PASSWORD LOCKER App\n")
    print("")
    prom = input("Hello, welcome to Password Locker  whats your name. ")
    print("  ")
    print("hello, " + prom + ", To get you started up kindly choose one of the following .")
    print(" ")
    print("\033[1;34;1m  Options On how to Get Started on Password Locker\n")
    print("")
    # print("\033[1;35;1m cc -> To Create an Account\n")
    # print("\033[1;35;1m Log -> To log in\n")
    # print("\033[1;35;1m ex -> Exit\n")   