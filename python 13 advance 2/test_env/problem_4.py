# write  program to find the greater number from  a list using reduce function

from functools import reduce
l = [74,78,658,85,96,742,753,951]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))