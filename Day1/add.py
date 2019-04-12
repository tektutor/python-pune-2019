#!/usr/bin/python3

def add(val1, val2):
  print('Inside add function')
  return val1 + val2

n1 = int(input('Enter your first number : '))
n2 = int(input('Enter your second number: '))

print( 'The total is ' + str(add(n1,n2)))
print( 'The total is ' , add(10.5,20.5))
print ('Message ==>', add ('Hello', ' World'))