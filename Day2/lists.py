#!/usr/bin/python3

if __name__ == "__main__":

    numbers = [100, 50, 1, 3, 80, 100, 20]

    array2d = [ [1,2,3, 4], [4,5,6, 0], [7,8,9, 10] ]

    print ( 'No of elements in lists :' , len ( numbers ))
    print ( '100 occurs ==>', numbers.count(100) )

    numbers.sort()

    for num in numbers:
        print ( num )

    print ( array2d )

    print ( 'Total rows    ==> ', len(array2d))
    print ( 'Total columns ==> ', len(array2d[0]))

    rows = len(array2d)
    cols = len(array2d[0])

    print ('Entries in 2 dimension list are ...')
    for row in range(0,rows):
        print ( "|", end='\t')
        for col in range (0,cols):
            print ( array2d[row][col],end="\t" )
        print ( "|", end='\t')

        print("\n")