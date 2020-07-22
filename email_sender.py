import smtplib
from email.message import EmailMessage

from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())



email = EmailMessage()
email['from'] = 'Sidhant Khosla'
email['to'] = 'sidkhosla2@gmail.com'
email['subject'] = 'you won 10k pounds'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('varsid1811@gmail.com', '*****')
    smtp.send_message(email)
    print('all good boss!')
