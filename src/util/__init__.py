#!/bin/bash

from src.service import add_user
from . import connection as con
from src.service.sign_in import SignIn

__all__ = ['connection', 'table_settings', 'utils']



print('\033[33m' + '1: New user registration' + '\033[0;0m')
print('\033[33m' + '2: Login' + '\033[0;0m')

number = str(input('\033[34m' + '\nChoose one: ' + '\033[0;0m'))


def options(option):
    if option == '1':
        return add_user.register_user()
    if option == '2':
        return None


options(number)

print('\033[32m' + 'Put your login data in the respective fields' + '\033[0;0m')
SignIn()
my_email = SignIn.getEmail()
