from src.util.connection import select_data
import getpass


class SignIn:

    def __init__(self):
        self.code = 1
        while self.code == 1:
            login = str(input('\033[33m' + 'Login: ' + '\033[0;0m'))
            passwd = getpass.getpass(prompt='\033[33m' + 'Password: ' + '\033[0;0m')
            query = (
                    'SELECT LOGIN, PASSWORD, EMAIL FROM USER WHERE TYPE = "admin" and LOGIN = "%s" AND PASSWORD = "%s";' % (
                login, passwd))

            self.result = select_data(query)

            if len(self.result) > 0:
                print("\n" + '\033[35m' + "User logged..." + '\033[0;0m')
                self.code = 0
            else:
                print('\n' + '\033[31m' + 'Login or Password wrong, please try again!' + '\033[0;0m')

    @staticmethod
    def get_email(self):
        if not self.code == 1:
            return self.result[0][2]
