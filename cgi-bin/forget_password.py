#!/usr/bin/python
import cgi,cgitb
import smtplib
import os, random, string
import MySQLdb as mariadb
db=mariadb.connect('127.0.0.1','root','redhat','customer')
cursor=db.cursor()
cgitb.enable()
print  "content-type:text/html"
print  ""
x=cgi.FieldStorage()
customer_email=x.getvalue('email')
customer_name=x.getvalue('Username')

#creating random password

length = 13
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
new_password=''.join(random.choice(chars) for i in range(length))

sender_email_id='xxxxxxxxxx@gmail.com'

sender_email_id_password='xxxxxxxxxx'

sql="""select Email,Name from info"""

cursor.execute(sql)

flag=0;

for Email,Name in cursor:
	if  customer_email == Email and customer_name == Name:
		flag=1;
		break;
	
	elif customer_email != Email or customer_name != Name :
		flag=0;

if flag==1:
	
	s = smtplib.SMTP('smtp.gmail.com:587')
	# start TLS for security
	s.ehlo()
	s.starttls()	
	# Authentication
	s.login(sender_email_id, sender_email_id_password)
	receiver_email_id=customer_email
	
#	sending mail to the receiver end
	s.sendmail(sender_email_id, receiver_email_id, "Your new_password is "+new_password)

	# message to be sent
	sql="UPDATE info SET Password = %r WHERE Email = %r" %(new_password,customer_email)

	cursor.execute(sql)

	db.commit()

# terminating the session
	s.quit()          
elif flag==0:
	print "<META HTTP-EQUIV='refresh' content='0; url=http://192.168.122.1/sandy/login.html'/>"



