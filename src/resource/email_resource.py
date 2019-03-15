import getpass
from src.util import tables
from src.service.email_service import SendEmail


class Email:

    def __init__(self):
        table = tables.set_table()

        sql = ('SELECT * FROM %s ' % table)

        password = getpass.getpass(prompt='[*]Type your email password: ')
        subject = str(input('[*]Type the subject: '))
        message = str(input('[*]Write your message: '))

        send_email = SendEmail(password, sql, subject, message)

        print('\n[>] - Emails to be sent: %i' % send_email.get_emails())

        print('[!] %i emails sent!' % send_email.get_emails())
        print('[!] Finished')
