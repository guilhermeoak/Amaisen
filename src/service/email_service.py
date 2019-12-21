#!/bin/bash

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src import util
from settings import EmailServerInfo as emailSetting


class SendEmail:

    def __init__(self, my_email, password, sql, subject, message):
        global code
        code = 1

        try:

            while code == 1:

                query = util.connection.select_data(sql)
                self.emails_to_send = len(query)
                print('\n[>] - Emails to be sent: %i' % len(query))

                msg = MIMEMultipart()

                number_of_sent = 0
                for receiver in query:
                    server = smtplib.SMTP(emailSetting.SERVER, emailSetting.PORT)
                    server.starttls()
                    server.login(my_email, password)

                    msg['from'] = my_email
                    msg['To'] = receiver[3]
                    msg['Subject'] = subject
                    msg.attach(MIMEText(message, 'plain'))

                    text = msg.as_string()

                    server.sendmail(my_email, receiver[3], text)

                    number_of_sent += 1
                    print('[%i] of' % number_of_sent, len(query), '| sent to ' +
                          '%s %s --> %s' % (receiver[1], receiver[2], receiver[3]))

                    server.quit()
                    code = 0

        except KeyboardInterrupt:
            code = 0

    def get_emails(self):
        return self.emails_to_send
