import unittest
import random
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Argumentss:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Instagram", "Suwa", "12345") # create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.account,"Instagram")
        self.assertEqual(self.new_user.username,"Mano")
        self.assertEqual(self.new_user.password,"12345")