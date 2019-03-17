from src.util.connection import select_data
import getpass
import subprocess
from src.util.utils import format_message


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

            subprocess.run(['clear'])
            format_message('\033[32m' + 'Put your login data in the respective fields' + '\033[0;0m' + '\n')
            login = str(input('\033[33m' + 'Login: ' + '\033[0;0m'))
            passwd = getpass.getpass(prompt='\033[33m' + 'Password: ' + '\033[0;0m')
            query = (
                    'SELECT LOGIN, PASSWORD, NAME, EMAIL, TYPE FROM USER WHERE LOGIN = "%s" AND PASSWORD = "%s";' % (
                login, passwd))

            result = select_data(query)
            if len(result) > 0:
                login = result[0][0]
                user_name = result[0][2]
                user_type = result[0][4]
                email = result[0][3]

            if len(result) > 0:
                subprocess.run(['clear'])
                message = ('\033[34m' + 'Hello ' + user_name.capitalize() + '\033[0;0m')
                format_message(message)
                print(input('\nPress Enter to continue...'))

                code = 0
            else:
                subprocess.run(['clear'])
                format_message('\033[31m' + 'Login or Password wrong, please try again!' + '\033[0;0m')
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
