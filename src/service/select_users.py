import subprocess

from src.service.sign_in import SignIn
from src.util import connection as con


class SelectUser:

    def __init__(self):
        if SignIn.get_user_type() == 'admin':
            sql = 'SELECT * FROM USER'
            result = con.select_data(sql)

            for user in result:
                print(user)
        else:
            subprocess.run(['clear'])
            print('\033[31m' + 'You have no permissions to do it!' + '\033[0;0m')