#!/usr/bin/python3

from functools import reduce

'''
def compute_squares ( listOfNumbers ):
    squares = [ ]

    for item in listOfNumbers:
        squares.append( item * item )

    return squares

if __name__ == "__main__":
    numbers = [ 1,2,3,4,5 ]

    squared_list = compute_squares( numbers )

    print ( 'The list entries are ...')
    print ( numbers )

    print ( 'The squared entries are ...')
    print ( squared_list )
    print ( sum(squared_list) )



numbers = [ 1,2,3,4,5 ]

#Lambda functions a.k.a anonymous functions
squares = lambda x : x * x
squared_list = []
for item in numbers:
    squared_list.append( squares(item) )

print ( numbers )
print ( squared_list )
'''

#def maximum(x, y):
#    return x if x > y else y

#print ( maximum(5,10) )

#Another version of the same code
numbers = [ 1,2,3,4,5 ]
squares = lambda x : x * x
add = lambda x, y: x + y
maximum = lambda x, y:  x if x > y else y

squared_list = map( squares, numbers )
slist = list(squared_list)
sum = reduce( maximum , slist )

print ( sum )

print ( squared_list )