import smtplib
import ssl
from email.mime.text import MIMEText

subject = "REQUEST FOR REFUND OUR CREDIT"
body = """AMT- {}/-.

Dear Sir, 
             PLZ REFUND OUR CREDIT FROM {} AS SOON AS POSSIBLE.            

Thanks & Regards,

NETAJI OIL DEPOT & GROUPS
GDM BRANCH: OFFICE NO. 208, 2ND FLOOR,
RIDDHI SIDDHI ARCADE II, PLOT NO. 40,
SECTOR 8, GANDHIDHAM, KUTCH - 370201, GUJARAT, INDIA"""


sender = "netajioildepotgandhidham@gmail.com"
recipients = ["netajioildepotgandhidham@gmail.com"]
password = "eqgb zwtu nhjz pklb"


context = ssl.create_default_context()

def send_email(subject, amount1,party1, sender, recipient, password):
    msg = MIMEText(body.format(amount1,party1))
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipient)
    msg['cc'] = 'rakesh_agarwa@hotmail.com'
    print(msg)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipient + ['rakesh_agarwa@hotmail.com'], msg.as_bytes())


# send_email(subject, body, sender, recipients, password)