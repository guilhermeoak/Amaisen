from src.model.user import User
from src.util import connection as con
import getpass


class AddUser:

    def __init__(self):
        print('\nNew user registration\n')

        name = str(input('Name: '))
        lastname = str(input('Lastname: '))
        tp = str(input('Type of account[admin or common user]: '))
        login = str(input('Login: '))
        password = getpass.getpass(prompt='Password: ')
        email = str(input('Email: '))

        new_user = User(name, lastname, tp, email, login, password)

        user = 'guilherme'
        db_passwd = '3141'
        query = (
                    "INSERT INTO USER (TYPE, LOGIN, PASSWORD, NAME, LASTNAME, EMAIL) VALUES('%s', '%s','%s', '%s', '%s', '%s')" %
                    (str(new_user.tp), str(new_user.login), str(new_user.password), str(new_user.name),
                     str(new_user.lastname), str(new_user.email)))

        con.insertData(user, db_passwd, query)
