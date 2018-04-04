
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

img_data = open('D:/Desktop/gawwy.png','rb').read()
msg = MIMEMultipart()
msg['Subject'] = 'Another One... and Another One'
msg['From'] = 'DJKhaled'
msg['To'] = 'His Disciples'

text = MIMEText("Someone is breaking in to your home! Its Gawwy!")
msg.attach(text)
image = MIMEImage(img_data)
msg.attach(image)

gmail_user = 'email_to_send_from@gmail.com'
gmail_pwd = 'im_not_telling_you_my_password'
FROM = gmail_user 
TO = 'email_to_send_to@gmail.com'

server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server_ssl.ehlo() 
server_ssl.login(gmail_user, gmail_pwd)
server_ssl.sendmail(FROM, [TO], msg.as_string())
server_ssl.close()
print 'All Done!'
