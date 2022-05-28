import sys

from sympy import true
b = int(sys.stdin.readline())
j = int(sys.stdin.readline())
while true:
    if 1 <= j and j <= b and b <= 1000000000:
        break
    else:
        b = int(sys.stdin.readline())
        j = int(sys.stdin.readline())

def totalPiramide(n):
    x = 0
    for i in range(0,n):
        x = x+ (n-i)
    return x
def cantNumPiram2(b,j):
    j = j-1
    if b-j ==0:
        return b
    else:
        return b-j
x = totalPiramide(b)-cantNumPiram2(b,j)*j
print(cantNumPiram2(b,j)*j)
print(x)












"""""
10000000
5000000


1659874
565465


"""
