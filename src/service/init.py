import sys
from src.service.add_user import AddUser
from src.util import utils
from datetime import datetime


class Init:

    def __init__(self):
        utils.clear_screen()

        now = datetime.now()
        message = (utils.welcome(now.hour) + ' Amaisen is running')
        utils.format_message(message)

        utils.check_database()
        utils.check_tables()

        if not utils.check_user():

            print('1: Sign Up')
            print('2: Login')
            print('q: Exit')

            number = str(input('\033[34m' + '\nChoose one: '))

            if number == 'q':
                utils.clear_screen()
                print('System finished!')
                sys.exit()
            if number == '1':
                AddUser()
            if number == '2':
                None
        else:
            print('1: Login')
            print('q: Exit')

            number = str(input('\nChoose one: '))

            if number == 'q':
                utils.clear_screen()
                print('System finished!')
                sys.exit()
            if number == '1':
                None
