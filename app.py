import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

subject = "Outstanding/OverDue Payment Reminder"
body = """<html>
AMT- <b>{}</b> /-.
<br>
<br>
<br>
Dear Sir,
<br>
<br>
             PLZ ARRANGE OUTSTANDING/SHORT/PENDING AMOUNT FROM <b>{}</b> {} AS SOON AS POSSIBLE.            
<br>
<br>
<br>
Thanks & Regards,
<br>
<br>
NETAJI OIL DEPOT & GROUPS
<br>
GDM BRANCH: OFFICE NO. 208, 2ND FLOOR,
<br>
RIDDHI SIDDHI ARCADE II, PLOT NO. 40,
<br>
SECTOR 8, GANDHIDHAM, KUTCH - 370201, GUJARAT, INDIA
<br>
</html>"""


sender = "netajioildepotgandhidham@gmail.com"
recipients = ["netajioildepotgandhidham@gmail.com"]
password = "eqgb zwtu nhjz pklb"


context = ssl.create_default_context()

def send_email(subject, amount1,party1,invoicedetails, sender, recipient, password):
    msg = MIMEMultipart('alternative')
    html = body.format(amount1,party1,invoicedetails)
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipient)
    msg['cc'] = 'rakesh_agarwa@hotmail.com'
    print(msg)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipient + ['mridulagarwal8@gmail.com'], msg.as_bytes())


# send_email(subject, body, sender, recipients, password)