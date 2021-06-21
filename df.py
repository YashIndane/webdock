#!/usr/bin/python3

from subprocess import getoutput as go
import cgi

print('content-type:text/plain')
print()

form_values = cgi.FieldStorage()

content = form_values.getvalue("co")
name_of_image = form_values.getvalue("na")
image_version = form_values.getvalue("ver")
username = form_values.getvalue("user")
password = form_values.getvalue("pass")

status = go('sudo mkdir /dockerfiles')

path = f'/dockerfiles/{name_of_image}'

status = go(f'sudo mkdir {path}')
status = go(f'sudo touch {path}/Dockerfile')
status = go(f'sudo chown apache {path}/Dockerfile')
status = go(f'sudo echo "{content}" > {path}/Dockerfile')
status = go(f'sudo dos2unix {path}/Dockerfile')
status = go('sudo systemctl start docker')
status = go(f'sudo docker build -t {username}/{name_of_image}:{image_version} {path}')
status = go(f'sudo docker login -u {username} -p {password}') 
status = go(f'sudo docker push {username}/{name_of_image}:{image_version}')

print(status)
