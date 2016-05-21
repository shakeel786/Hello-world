#!D:/Softwares/Writers/Python_install/python.exe

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 


# Get data from fields
#first_name = form.getvalue('first_name')
#last_name  = form.getvalue('last_name')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<script>function MyFunction(){document.getElementById('myText').value = window.location.href;document.frm.submit();}</script>"
print "<title>Getting Access token</title>"
print "</head>"
print "<body onload='MyFunction()'>"
print "<form name=frm action='cron.py' method=post>"
print "<input type=hidden id=myText name=token>"
print "</form>"
print "</body>"
print "</html>"
