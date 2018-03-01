#!/usr/bin/env python3.6
# Author: Binglin Ji
import getpass

_username = 'bji'
_password = 'redhat'

username = input("username: ")
password = getpass.getpass("password: ")


if _username == username and _password == password:
    print("welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password!")