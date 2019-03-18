import os
import platform
import subprocess


def welcome(hour):
    if 00 <= hour < 12:
        return 'Good morning!'
    if 12 <= hour < 18:
        return 'Good afternoon!'
    if 18 <= hour <= 23:
        return 'Good evening!'


def format_message(message):
    y, x = os.popen('stty size', 'r').read().split()
    space = ''
    count = 0
    while count < (int(x) / 3):
        space = space + ' '
        count += 1

    print(space, message)


def clear_screen():
    os_name = platform.system()
    if os_name == 'Linux' or os_name == 'Mac':
        subprocess.run(['clear'])
    if os_name == 'Windows':
        subprocess.run(['cls'])


