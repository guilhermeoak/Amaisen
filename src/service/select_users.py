from src.util import connection as con


class SelectUser:

    def __init__(self):
        sql = 'SELECT * FROM USER'
        result = con.select_data(sql)

        for user in result:
            print(user)
