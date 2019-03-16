from src.util import connection as con
from src.service.select_users import SelectUser


class RemoveUser:

    def __init__(self):

        SelectUser()

        print('\nDelete user\n')

        print('\n' + '\033[31m' + '0: Cancel' + '\033[0;0m')
        user_id = int(input('Type the user id: '))

        if user_id == 0:
            #amaisen.start()
            None
        else:
            query = ('DELETE FROM USER WHERE ID = %i' % user_id)
            con.remove_data(query)
