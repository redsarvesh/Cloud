#!/usr/bin/python2
import os,sys,time
import commands,os
import cgi,cgitb

cgitb.enable()
print "Content-type:text/html\r\n\r\n"

#Data is retrieved
data=cgi.FieldStorage()
choice=data.getvalue('radio')

print "run the downloaded .sh file on your terminal"
print "\n"
print "eg:- bash xxx.sh"




if  choice == "Webcam":

	print "<META HTTP-EQUIV='refresh' content='0; url=/Webcam.sh'/>"
	
	
elif  choice == "Opera":

	print "<META HTTP-EQUIV='refresh' content='0; url=/Opera.sh'>"

elif  choice == "Vlc":

	print "<META HTTP-EQUIV='refresh' content='0; url=/vlc.sh'>"	
elif  choice == "Terminal":

	print "<META HTTP-EQUIV='refresh' content='0; url=/Terminal.sh'>"

elif  choice == "Firefox":
	

	print "<META HTTP-EQUIV='refresh' content='0; url=/Firefox.sh'>"

elif  choice == "Notepad":

	print "<META HTTP-EQUIV='refresh' content='0; url=/gedit.sh'>"

elif  choice == "Gedit":

	print "<META HTTP-EQUIV='refresh' content='0; url=/gedit.sh'>"
else: 
	print "<script>alert('You have not selected anything')</script>" 
	print "<META HTTP-EQUIV='refresh' content='0; url=/sandy/saas.html'/>"
