import getpass

from src.service.sign_in import SignIn
from src.util import tables
from src.service.email_service import SendEmail
from src.util.utils import clear_screen


class Email:

    def __init__(self):
        table = tables.set_table()
        clear_screen()
        sql = ('SELECT * FROM %s ' % table)
        sign_in = SignIn()
        my_email = sign_in.get_email()
        print("Your email: " + '\033[32m' + my_email + '\033[0;0m')

        password = getpass.getpass(prompt='[*]Type your email password: ')
        subject = str(input('[*]Type the subject: '))
        message = str(input('[*]Write your message: '))

        send_email = SendEmail(my_email, password, sql, subject, message)

        print('[!] %i emails sent!' % send_email.get_emails())
        print('[!] Finished')
