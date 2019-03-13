import getpass
from .connection import setData
import subprocess
from .utils import whatToSay
from datetime import datetime
import subprocess
import getpass

subprocess.run(['clear'])

user = getpass.getuser()
now = datetime.now()
print('System started...\n' + whatToSay(now.hour), user.capitalize() + '\n')

class SignIn:

    def __init__(self):

        global result

        login = str(input('Login: '))
        passwd = getpass.getpass(prompt='Password: ')
        query = ('SELECT LOGIN, PASSWORD, EMAIL FROM USER WHERE TYPE = "admin" and LOGIN = "%s" AND PASSWORD = "%s";' % (
            login, passwd))

        result = setData(query)

        if len(result) > 0:
            print("User logged...")
        else:
            print('Login or Password wrong, please try again!')


        
    def getEmail():
        return result[0][2]


        
                