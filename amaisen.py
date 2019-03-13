#!/bin/bash

from src import add_user
import src.EmailResource as EmailResource
import subprocess

print('\nWhato do you want to do?')

def start():
    subprocess.run(['clear'])
    print('1: Send emails')
    print('2: New user registration')
    print('q: Exit')

    number = str(input('\nChoose one: '))

    def options(option):
        if option == '1':
            return EmailResource.send_email()
        if option == '2':
            return add_user.register_user()
        if option == 'q':
            return False

    options(number)


while True:
    start()
