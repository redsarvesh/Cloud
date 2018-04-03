#!/usr/bin/python
import  cgi,cgitb
import MySQLdb as mariadb
db=mariadb.connect('127.0.0.1','root','redhat','customer')
cursor=db.cursor()
cgitb.enable()
print  "content-type:text/html"
print  ""

x=cgi.FieldStorage()
customer_email=x.getvalue('email')
customer_password=x.getvalue('password')

sql="""select Email,Password from info"""
cursor.execute(sql)
flag=0;

for Email,Password in cursor:

	if  customer_email == Email and customer_password == Password:
		flag=1;
		break;
	
	elif customer_email != Email or customer_password != Password:
		flag=0;

if flag==1:
	print "<META HTTP-EQUIV='refresh' content='0; url=http://192.168.122.1/sandy/sandy2.html'>"

elif flag==0:
	print "<META HTTP-EQUIV='refresh' content='0; url=http://192.168.122.1/sandy/login.html'/>"	

