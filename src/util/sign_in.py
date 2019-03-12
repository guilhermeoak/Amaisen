import getpass
from .connection import setData
import subprocess
from .utils import whatToSay
from datetime import datetime
import subprocess

subprocess.run(['clear'])

user = str(subprocess.check_output(['whoami']))[2:-3]
now = datetime.now()
print('System started',whatToSay(now.hour), user.capitalize(), '\n')

class SignIn:

    def __init__(self):
        global result
        login = str(input('Login: '))
        passwd = getpass.getpass(prompt='Password: ')
        query = ('SELECT LOGIN, PASSWORD FROM USER WHERE TYPE = "admin" and LOGIN = "%s" AND PASSWORD = "%s";' % (
            login, passwd))
        result = setData('guilherme', '3141', query)
        if len(result) > 0:
            print("User logged...")
        else:
            print('Login or Password wrong, please try again!')