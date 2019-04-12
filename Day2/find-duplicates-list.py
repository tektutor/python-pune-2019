#/usr/bin/python3

l = [1, 5, 3, 2, 1, 5, 2, 1]
d = { }

for element in l:
    d[element] = l.count(element)

for item in d.items():
    print ( item )