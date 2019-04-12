#!/usr/bin/python3

import os

#While loop
index = 0

os.system('clear')
print ( os.getcwd() )
print ( os.getenv('PATH'))
print ( os.getenv('MY_VAR'))

while ( index < 10 ):
    print ( index, end=" " )
    index = index + 1

print ("\n")
index = 0
while ( True ):
    if index == 10:
        break
    elif index < 10:
        print ( index, end=" ")
    index = index + 1
print ( "\n")