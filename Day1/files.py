#!/usr/bin/python

import second

def readFile(fileName):

    file = open (fileName, 'r' )
    lines = file.readlines()
    file.close()

    for line in lines:
        print ( line )

def writeToFile(fileName, value):
    file = open (fileName, 'a+' )
    file.write ( value + "\n")
    file.close()

if __name__ == "__main__":
    print ( __name__ )
    writeToFile('mobiles.txt', "Motorola")
    readFile( 'mobiles.txt' )
