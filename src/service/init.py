import sys

from src.service.add_user import AddUser
from src.util import utils


class Init:

    def __init__(self):
        None

    @staticmethod
    def init():
        if not utils.check_user():

            print('\033[33m' + '1: Sign Up' + '\033[0;0m')
            print('\033[33m' + '2: Login' + '\033[0;0m')
            print('\033[33m' + 'q: Exit' + '\033[0;0m')

            number = str(input('\033[34m' + '\nChoose one: ' + '\033[0;0m'))

            if number == 'q':
                utils.clear_screen()
                print('\033[31m' + 'System finished!' + '\033[0;0m')
                sys.exit()
            if number == '1':
                AddUser()
            if number == '2':
                None
        else:
            print('\033[33m' + '1: Login' + '\033[0;0m')
            print('\033[33m' + 'q: Exit' + '\033[0;0m')

            number = str(input('\033[34m' + '\nChoose one: ' + '\033[0;0m'))

            if number == 'q':
                utils.clear_screen()
                print('\033[31m' + 'System finished!' + '\033[0;0m')
                sys.exit()
            if number == '1':
                None
