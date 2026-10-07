import smtplib
import ssl
from email.message import EmailMessage


class EmailSender:
    def __init__(self, sender_email, password):
        self.sender_email = sender_email
        self.password = password

    def send(self, receiver_email, subject, body):
        em = EmailMessage()
        em['From'] = self.sender_email
        em['To'] = receiver_email
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.sender_email, self.password)
            smtp.send_message(em)
        print('email sent')


sender = EmailSender('elhouarimarouane56@gmail.com', 'Unitedflask@html.12345')
sender.send('imadiiimad345@mail.com', 'subject', 'wach akhy hny bikher kolchi mzyan?')