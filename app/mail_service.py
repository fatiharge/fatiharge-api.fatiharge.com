from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_MAIL_PASSWORD = os.getenv("SENDER_MAIL_PASSWORD")


async def send_email(recipient: str, subject: str, body: str):
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = recipient
    message["Subject"] = subject
    message["Date"] = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_MAIL_PASSWORD)
        server.sendmail(SENDER_EMAIL, recipient, message.as_string())
