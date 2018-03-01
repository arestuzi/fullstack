#!/usr/bin/env python3.6
# Author: Binglin Ji
import getpass
import csv
with open('user_info.csv', 'r') as f:
    reader = csv.reader(f)
    user_info = list(reader)
with open('bid_info.csv', 'r') as f:
    reader = csv.reader(f)
    bid_user = list(reader)

locked = False
for i in range(3):
    username = input("username: ")
    password = getpass.getpass("password: ")
    for name in bid_user:
        if name[0] == username:
            print("Your account has been locked!")
            locked = True
            break

    for user in user_info:
        if user[0] == username and user[1] == password and locked == False:
            print("welcome user {name} login...".format(name=username))
            break
    else:
        print("authorization failed, please try again")
    if i == 2:
        f = open('bid_info.csv','w')
        f.write(username)
        f.close()
        print("your account has been locked, please contact with the administrator.")
