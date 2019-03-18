from src.util.utils import clear_screen

from src.util import connection as con
from src.service.select_users import SelectUser
from src.service.sign_in import SignIn


class RemoveUser:

    def __init__(self):

        if SignIn.get_user_type() == 'admin':

            SelectUser()

            print('\nDelete user')

            print('\n' + '\033[31m' + '0: Cancel' + '\033[0;0m')
            user_id = int(input('Type the user id: '))

            if user_id == 0:
                None
            else:
                query = ('DELETE FROM USER WHERE ID = %i' % user_id)
                con.remove_data(query)

        else:
            clear_screen()
            print('\033[31m' + 'You have no permissions to do it!' + '\033[0;0m')
            print(input('Press any key to continue...'))
