# to calculate the sum of first n natural numbers using recursive function

import sys
sys. setrecursionlimit(1000000)


def sum(n):
    if n==0:
        return 0
    return sum(n-1) + n

n = int(input("enter you number: "))
print(f"the sum of first {n} natural numbers is: {sum(n)}")
