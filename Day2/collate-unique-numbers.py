#!/usr/bin/python3
import os

os.system('clear')

file1 = open ('file1.txt', 'r')
firstList = file1.readlines()
file1.close()

file2 = open ('file2.txt', 'r')
secondList = file2.readlines()
file2.close()

unique_numbers = set()

for item in firstList:
    unique_numbers.add ( int(item.strip()) )

for item in secondList:
    unique_numbers.add ( int(item.strip()) )

combined_list = list(unique_numbers)
combined_list.sort()

for item in combined_list:
    print ( item)