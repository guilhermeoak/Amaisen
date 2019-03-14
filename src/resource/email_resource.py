import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
from src import util
from src.util import table_settings
from src.service.sign_in import SignIn


class Email:

    def __init__(self):

        table_settings.set_table()
        table = table_settings.get_table()

        sql = ('SELECT * FROM %s ' % table)
        query = util.connection.setData(sql)

        my_email = SignIn.getEmail()
        print("Your email: " + '\033[32m' + my_email + '\033[0;0m')

        #my_email = str(input('Your email: '))

        password = getpass.getpass(prompt='[*]Type your email password: ')
        subject = str(input('[*]Type the subject: '))
        message = str(input('[*]Write your message: '))

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
        print('[!] Finished')
