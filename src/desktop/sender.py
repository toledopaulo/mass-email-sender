import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class MailSender(object):
    def __init__(self):
        return

    def auth(self, email, password, provider: str, custom_host=None):
        # custom host example -> smtp.example.com:1337 (host:port)
        email_providers = {"gmail": "smtp.gmail.com:465", "outlook": "smtp-mail.outlook.com:587", "yahoo": "smtp.mail.yahoo.com:465", "custom": custom_host}
        email_host = str(email_providers[provider]).split(":")[0]
        email_port = str(email_providers[provider]).split(":")[1]
        self.server = smtplib.SMTP_SSL(host=email_host, port=email_port) # connect smtp on the provided host
        try:
            self.server.login(user=email, password=password) # login into mail account
            return True
        except smtplib.SMTPAuthenticationError:
            return False

    def logout(self):
        try:
            self.server.quit()
            return True
        except:
            return False
    def send_simple_email(self, mail_to: str, subject: str):
        pass

    def send_email_with_attachments(self, mail_to: str, subject: str):
        pass
