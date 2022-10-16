
## Reference http://naelshiab.com/tutorial-send-email-python/
import smtplib
import time
from datetime import date
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

fromaddr = "swatidhoke18@gmail.com"
toaddr = "swatidhoke@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['cc'] = "meghadhoke04@gmail.com"
msg['Subject'] = " %s Test Results" % date.fromtimestamp(time.time())

body = "Please find test results log file attached." \
       "\nThanks, " \
       "\nSwati"

msg.attach(MIMEText(body, 'plain'))
#/Users/swatidhoke/Desktop
filename = "test.log"
attachment = open("/Users/swatidhoke/PycharmProjects/Automation_Frameworks/UI_Selenium_framework/TestResults/test.log", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "ashalata11")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

