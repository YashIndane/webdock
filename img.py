#!/usr/bin/python3

from subprocess import getoutput as go

print("content-type:text/plain")
print()

status = go("sudo docker images")

print(status)
