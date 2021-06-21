#!/usr/bin/python3

from subprocess import getoutput as go
import cgi

print("content-type:text/plain")
print()

form_values = cgi.FieldStorage()

command = form_values.getvalue("cmd")

if "docker" in command :
  status = go(f"sudo {command}")
  print(status)

else :
  print("ONLY DOCKER COMMANDS ALLOWED, TRY AGAIN")
