#!/usr/bin/python3

#Tuple represents one record in a db table
#Can be used when each column/field is of different
#data-type

record1 = ( 1, 'Nitesh', 14 )
record2 = ( 2, 'Sriram', 11 )

print ( record1 )
print ( record2 )

print ( record1[0] )
print ( record1[1] )
print ( record1[2] )

print ( record1[0], record1[1], record1[2] )
print ( str( record1[0] ) + " " + record1[1] +  " " +str(record1[2]) )