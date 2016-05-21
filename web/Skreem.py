#!D:/Softwares/Writers/Python_install/python.exe

import urllib2
import os

print "Content-Type: text/html\n"

#https://api.instagram.com/oauth/authorize/?client_id=faf054efe1234187b2be8fcc2fa763d6&redirect_uri=http://localhost/python/access_key.php&response_type=token

client_id = 'faf054efe1234187b2be8fcc2fa763d6'
client_secret = '531980b9b2a84f3bbd4ff1b998fbd19c'

#import urllib2
#response = urllib2.urlopen('https://api.instagram.com/oauth/authorize/?client_id=faf054efe1234187b2be8fcc2fa763d6&redirect_uri=localhost/python/test.py&response_type=token')
#html = response.read()
#print html

print "<h1>Instagram API Login</h1>"
print "<a href=https://api.instagram.com/oauth/authorize/?client_id=faf054efe1234187b2be8fcc2fa763d6&redirect_uri=http://localhost/python/access_token.py&response_type=token target='_blank'>Login with Instagram</a>"


#url = os.environ['HTTP_HOST']
#uri = os.environ['REQUEST_URI']
#print url + uri


#req = urllib2.Request(starturl, datagen, headers)
#res = urllib2.urlopen(req)
#finalurl = res.geturl()
#print finalurl

script = environ.get('PATH_INFO')
print script
