from src.util.connection import select_data
import getpass


class SignIn:

    def __init__(self):

        global result

        login = str(input('\033[33m' + 'Login: ' + '\033[0;0m'))
        passwd = getpass.getpass(prompt='\033[33m' + 'Password: ' + '\033[0;0m')
        query = (
                'SELECT LOGIN, PASSWORD, EMAIL FROM USER WHERE TYPE = "admin" and LOGIN = "%s" AND PASSWORD = "%s";' % (
            login, passwd))

        result = select_data(query)

        if len(result) > 0:
            print("User logged...")
        else:
            print('Login or Password wrong, please try again!')

    def getEmail():
        return result[0][2]
