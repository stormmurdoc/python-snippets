#!/usr/bin/python3

import random

items = ["\033[0;92m*\033[0m","\033[1;91mo\033[0m","\033[1;94mo\033[0m","\033[1;93mo\033[0m"]
print(" "*10+"\033[1;93m*\033[0m")
for i in range(3,21,2):
    stn=""
    for j in range(0,i):
        if random.randint(0,5)==1:
            stn+=items[random.randint(1,3)]
        else:
            stn+=items[0]
    print(" "*(round((21-i)/2))+stn)
for k in range(1,3):
    print(" "*9+"\033[0;37m| |\033[0m")
print("\n")
print(" "*2+"\033[0;37mMerry christmas!\033[0m")
