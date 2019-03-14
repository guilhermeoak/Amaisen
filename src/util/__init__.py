#!/bin/bash

import subprocess
from src.service.add_user import AddUser
from . import connection as con
from src.service.sign_in import SignIn
from src.resource import email_resource

__all__ = ['connection', 'table_settings', 'utils']

while True:

    print('\033[33m' + '1: New user registration' + '\033[0;0m')
    print('\033[33m' + '2: Login' + '\033[0;0m')

    number = str(input('\033[34m' + '\nChoose one: ' + '\033[0;0m'))

    if number == '1':
        AddUser()
    if number == '2':
        break

print('\033[32m' + 'Put your login data in the respective fields' + '\033[0;0m')

SignIn()
my_email = SignIn.getEmail()

while True:

    subprocess.run(['clear'])
    print('\033[33m' + '1: Send emails' + '\033[0;0m')
    print('\033[33m' + '2: New user registration' + '\033[0;0m')
    print('\033[33m' + 'q: Exit' + '\033[0;0m')

    number = str(input('\033[32m' + '\nChoose one: ' + '\033[0;0m'))

    if number == '1':
        email_resource.send_email()
    if number == '2':
        AddUser()
    if number == 'q':
        print('\nBye!')
        break
