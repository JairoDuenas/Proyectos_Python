from email.message import EmailMessage
from dotenv import load_dotenv
import os
import smtplib
import ssl

load_dotenv()

email_sender = os.environ.get("EMAIL_USER")
email_password = os.environ.get("PASS_USER_MAIL")

email_receiver = 'cepisa5141@jthoven.com'

subject = "Dont forget to subscribe"
body = """When you watch a video, please hit subscribe"""

email = EmailMessage()
email['From'] = email_sender
email['To'] = email_receiver
email['subject'] = subject
email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
  smtp.login(email_sender, email_password)
  smtp.sendmail(email_sender, email_receiver, email.as_string())
