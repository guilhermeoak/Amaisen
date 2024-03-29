from src.util import utils
from src.util.utils import clear_screen
from src.util.utils import format_message
from src.util.connection import select_data
from src.util.connection import insert_data
import getpass
import sys


class SignIn:
    @staticmethod
    def __init__():
        None

    @staticmethod
    def sign_in():
        global code
        code = 1
        while code == 1:

            global result
            global login
            global user_name
            global user_type
            global email

            clear_screen()
            if utils.os_name != 'Windows':
                format_message('Put your login data in the respective fields\n')
            else:
                print('Put your login data in the respective fields\n')
            login = str(input('Login: '))
            passwd = getpass.getpass(prompt='Password: ')
            query = (
                    'SELECT LOGIN, PASSWORD, NAME, EMAIL, TYPE, LOGADO FROM USER WHERE LOGIN = "%s" AND PASSWORD = '
                    '"%s";' % (login, passwd))

            result = select_data(query)
            if len(result) > 0:

                if result[0][5] == 1:
                    print("This user is already signed in to another session.")
                    sys.exit()

                insert_data('UPDATE USER SET LOGADO = 1')
                clear_screen()
                login = result[0][0]
                user_name = result[0][2]
                user_type = result[0][4]
                email = result[0][3]

            if len(result) > 0:

                if result[0][5] == 1:
                    print("This user is already signed in to another session.")
                    sys.exit()

                insert_data('UPDATE USER SET LOGADO = 1')
                clear_screen()
                message = ('Hello ' + user_name.capitalize())
                if utils.os_name != 'Windows':
                    format_message(message)
                else:
                    print(message)
                print(input('\nPress Enter to continue...'))

                code = 0
            else:
                clear_screen()
                if utils.os_name != 'Windows':
                    format_message('Login or Password wrong, please try again!')
                else:
                    print('Login or Password wrong, please try again!')
                print(input('\nPress Enter to continue...'))

    @staticmethod
    def get_user_type():
        if not code == 1:
            return user_type

    @staticmethod
    def get_email():
        if not code == 1:
            return email

    @staticmethod
    def get_login():
        if not code == 1:
            return login

    @staticmethod
    def get_user_type():
        if not code == 1:
            return user_type
