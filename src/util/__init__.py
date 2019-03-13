from . import connection as con
import getpass
from .sign_in import SignIn


__all__ = ['whatToSay', 'connection', 'table_settings', 'utils', 'sign_in']

SignIn()
my_email = SignIn.getEmail()
SignIn.db_auth()