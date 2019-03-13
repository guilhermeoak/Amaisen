from src.util.connection import setData
from src.util.utils import whatToSay
from datetime import datetime
import subprocess
import getpass

subprocess.run(['clear'])

user = getpass.getuser()
now = datetime.now()
print('\033[32m' + 'System started...\n' + whatToSay(now.hour), user.capitalize() + '\n' + '\033[0;0m')

class SignIn:

    def __init__(self):

        global result

        login = str(input('\033[33m' + 'Login: ' + '\033[0;0m'))
        passwd = getpass.getpass(prompt='\033[33m' + 'Password: '+ '\033[0;0m')
        query = ('SELECT LOGIN, PASSWORD, EMAIL FROM USER WHERE TYPE = "admin" and LOGIN = "%s" AND PASSWORD = "%s";' % (
            login, passwd))

        result = setData(query)

        if len(result) > 0:
            print("User logged...")
        else:
            print('Login or Password wrong, please try again!')


        
    def getEmail():
        return result[0][2]


        
                