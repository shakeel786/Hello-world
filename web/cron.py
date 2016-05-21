#!D:/Softwares/Writers/Python_install/python.exe

import cgi, cgitb , urllib2, json
print "Content-Type: text/html\n"
print "<html>"
print "<title>Information</title>"
print "<head></head>"
print "<body>"

form = cgi.FieldStorage() 


access_token = form.getvalue('token')
access_token = access_token.split("#access_token=")
access_token =  access_token[1]
user_id = ''
#print access_token

# Gathering user information 
response = urllib2.urlopen('https://api.instagram.com/v1/users/self/?access_token='+access_token)
data =  json.load(response)
#print data

user_id = data['data']['id']
print "<center>"
print "<table style='width:40%' border=2 cellpadding=2 cellspacing=2>"
print "<tr>"
print "<td align=center colspan=3>Basic Information</td></tr><tr>"
print "<td style='width:30%' rowspan=5><img src=" + data['data']['profile_picture'] + "></td></tr>"
print "<tr><td><b>Username : </td><td>"+ data['data']['username'] + "</td></tr>"
print "<tr><td><b>Followed By : </td><td>"+ str(data['data']['counts']['followed_by']) + "</td></tr>"
print "<tr><td><b>Follows : </td><td>"+ str(data['data']['counts']['follows']) + "</td></tr>"
print "<tr><td><b>Total Potential  : </td><td>"+ str(data['data']['counts']['follows'] + data['data']['counts']['followed_by']) + "</td></tr>"


print "</table>"
print "</center>"

#Gathering recent media information
recent_media = urllib2.urlopen('https://api.instagram.com/v1/users/'+user_id+'/media/recent/?access_token='+access_token)
recent_data = json.load(recent_media)
#print recent_data['data']

total_likes = 0
total_comments = 0
for item in recent_data['data']:
	comments =  item['comments']['count']
	post_img = item['images']['thumbnail']['url']
	media_id =  item['id']
	likes = item['likes']['count']
	total_likes = total_likes + likes
	total_comments = total_comments + comments
	print "<br><br>"
	print "<center>"
	print "<table style='width:40%' border=2 cellpadding=2 cellspacing=2>"
	print "<tr>"
	print "<td align=center colspan=3>Recent Media Information</td></tr><tr>"
	print "<td style='width:30%' rowspan=4><img src=" + post_img + "></td></tr>"
	print "<tr><td><b>Media ID  : </td><td>"+ media_id + "</td></tr>"

	print "<tr><td><b>Likes  : </td><td>"+ str(likes) + "</td></tr>"
	print "<tr><td><b>Comments : </td><td>"+ str(comments) + "</td></tr>"

	print "</table>"
	print "</center>"

	print "</body>"
	print "</html>"

print "<center><p>Total Likes : "+ str(total_likes) + "</p><br> Total Comments : " + str(total_comments) + "</center>"
