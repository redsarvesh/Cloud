#!/usr/bin/python
import  cgi,cgitb
import MySQLdb as mariadb
db=mariadb.connect('127.0.0.1','root','redhat','customer')
cursor=db.cursor()
cgitb.enable()
print  "content-type:text/html"
print  ""

x=cgi.FieldStorage()
customer_name=x.getvalue('name')
customer_email=x.getvalue('email')
customer_password=x.getvalue('password')

sql="""insert into info(Name,Email,Password)values('"""+customer_name+"""','"""+customer_email+"""','"""+customer_password+"""')"""

try:
        cursor.execute(sql)
        db.commit()
except:
        db.rollback()

db.close()
