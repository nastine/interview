import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email():
    def __init__(self, mail_from, mail_to, subject, text):
        self.mail_from = mail_from
        self.mail_to = ', '.join(mail_to)
        self.subject = subject
        self.text = text
        

    def send(self, login, password):
        msg_to_send = MIMEMultipart()
        msg_to_send['From'] = self.mail_from
        msg_to_send['To'] = self.mail_to
        msg_to_send['Subject'] = self.subject
        msg_to_send.attach(MIMEText(self.text))

        connect = smtplib.SMTP("smtp.gmail.com", 587)
        connect.ehlo()
        connect.starttls()
        connect.ehlo()
        connect.login(login, password)
        connect.sendmail(login,connect, msg_to_send.as_string())
        connect.quit()

    def receive(self, login, password, header=None):
        connect = imaplib.IMAP4_SSL("imap.gmail.com")
        connect.login(login, password)
        connect.list()
        connect.select("inbox")
        search_subject = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = connect.uid('search', None, search_subject)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = connect.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        connect.logout()

if __name__ == "__main__":
    email = Email('login@gmail.com', ['vasya@email.com', 'petya@email.com'], 'Subject', 'Message')
    email.send('login@gmail.com', 'qwerty')
    email.receive('login@gmail.com', 'qwerty')