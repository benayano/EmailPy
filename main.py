from email.message import EmailMessage
from app2 import password
import ssl
import smtplib


email_sender = '0544354125m@gmail.com'
email_password = password

email_reciver = '0544354125m@gmail.com'
subject = ' this is my subject!'
body = """
gjhgjhgjgjhg
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciver
em['Subject'] = subject
em.set_content(body)



context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context = context) as smtp
smtp.login(email_sender,email_password)
smtp.sendmail(email_sender ,email_reciver,em.as_string)




