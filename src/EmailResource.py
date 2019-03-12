#!/bin/bash

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import sys
from . import util

util.sign_in()

util.setTable()
table = util.getTable()
sql = ('SELECT * FROM %s ' % table)
query = util.Connection.setData('guilherme', '3141', sql)

my_email = str(input('[*]Type your email: '))
password = getpass.getpass(prompt='[*]Type your password: ')
subject = str(input('[*]Type the subject: '))
message = str(input('[*]Write your message: '))


def send_email():
    try:

        print('\n[>] - Emails to be sent: %i' % len(query))

        msg = MIMEMultipart()

        number_of_sent = 0
        for receiver in query:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(my_email, password)
            msg['from'] = my_email
            msg['To'] = receiver[3]
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            text = msg.as_string()
            server.sendmail(my_email, receiver[3], text)
            number_of_sent += 1
            print('[%i] of' % number_of_sent, len(query), 'sent to ' + '\033[32m' +
                  '%s %s --> %s' % (receiver[1], receiver[2], receiver[3]) + '\033[0;0m')
            server.quit()

        print('[!] %i emails sent!' % len(query))

    except:
        print('An error occured:', sys.exc_info()[0], '\n', sys.exc_info()[1])

    finally:
        print('[!] Finished')
        

send_email()