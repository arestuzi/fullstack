#!/usr/bin/env python3.6
# Author: Binglin Ji
'''
count = 0
while True:
    print("count: ", count)
    count = count + 1

for i in range(0,10,3):
    print("loop: ",i)
'''
'''
for i in range(0,10):
    if i < 3:
        print("loop ",i)
    else:
        continue
    print("hehe...")
'''

for i in range (10):
    print('----------', i)
    for j in range(10):
        print(j)
        if j > 5:
            break