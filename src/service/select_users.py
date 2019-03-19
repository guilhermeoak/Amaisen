from src.util.utils import clear_screen

from src.service.sign_in import SignIn
from src.util import connection as con


class SelectUser:

    def __init__(self):
        if SignIn.get_user_type() == 'admin':
            clear_screen()
            sql = 'SELECT * FROM USER'
            result = con.select_data(sql)

            for user in result:
                print(user)
            print(input('Press any key to continue...'))
            clear_screen()
        else:
            clear_screen()
            print('\033[31m' + 'You have no permissions to do it!' + '\033[0;0m')
            print(input('Press any key to continue...'))
