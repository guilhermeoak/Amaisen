#!/bin/bash

from src.resource.email_resource import Email
from src.service.add_user import AddUser
from src.service.sign_in import SignIn
from src.util.utils import whatToSay
from _datetime import datetime
import getpass
import subprocess

subprocess.run(['clear'])

user = getpass.getuser()
now = datetime.now()
print('\033[32m' + 'System started...\n' + whatToSay(now.hour), user.capitalize() + '\n' + '\033[0;0m')

print('\nWhat do you want to do?')

while True:

    print('\033[33m' + '1: New user registration' + '\033[0;0m')
    print('\033[33m' + '2: Login' + '\033[0;0m')

    number = str(input('\033[34m' + '\nChoose one: ' + '\033[0;0m'))

    if number == '1':
        AddUser()
    if number == '2':
        break

print('\033[32m' + 'Put your login data in the respective fields' + '\033[0;0m' + '\n')

SignIn()
my_email = SignIn.getEmail()

while True:

    print('\n' + '\033[33m' + '1: Send emails' + '\033[0;0m')
    print('\033[33m' + '2: New user registration' + '\033[0;0m')
    print('\033[33m' + 'q: Exit' + '\033[0;0m')

    number = str(input('\033[32m' + '\nChoose one: ' + '\033[0;0m'))

    if number == '1':
        Email()
    if number == '2':
        AddUser()
    if number == 'q':
        print('\nBye!')
        break
