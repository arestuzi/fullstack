#!/usr/bin/env python3.6
# Author: Binglin Ji

age_of_oldboy = 56

count = 0

while count < 3:
    guess_age = int(input("guess age: "))
    if guess_age == age_of_oldboy:
        print("yes, you got it. ")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller...")
    else:
        print("think bigger!")
    count += 1
    if count == 3:
        continue_confirm = input("do you want to keep trying...? ")
        if (continue_confirm != 'n' or continue_confirm != 'N'):
            count = 0
#else:
#    print("you have tried too many times..fuck off")