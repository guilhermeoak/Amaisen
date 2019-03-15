from src.util import connection as con


class RemoveUser:

    def __init__(self):

        print('\nDelete user\n')

        user_id = int(input('Type the user id: '))

        query = ('DELETE FROM USER WHERE ID = %i' % user_id)
        con.remove_data(query)
