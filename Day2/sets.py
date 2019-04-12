#!/usr/bin/python3

s1 = set()
s2 = { 100, 200, 300, 10 }

s1.add(10)
s1.add(20)
s1.add(30)
s1.add(10)
'''
print ( len(s1) )
print ( s1 )

print ( len(s2) )
print ( s2 )
'''

print ( s1.difference(s2) )
print ( s2.difference(s1) )

print ( s1.intersection(s2) )