import sys
from timeit import default_timer
from sympy import true
def rotarVector(vector, n):
    return vector[n:] + vector[:n]
def obtenValorDeXaY(vector, a, b):
    return vector[a-1:b]
def pasarDatos(a,b, x):
    for i in a:
        b[x] = i
        x = x + 1
def mostrarVector(vector):
    for i in vector:
        print(i, end=" ")

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    while true:
        if n%k == 0 and n>=1 and n<= 1000 and k>=1 and k<= n:
            break
        else:
            n, k = map(int, sys.stdin.readline().split())
            a = list(map(int, sys.stdin.readline().split()))
    x = 0
    for i in range(int(n/k)):
        v1 = obtenValorDeXaY(a, x+1, x+k)
        pasarDatos(rotarVector(v1, 1), a, x)
        x = x +k
    mostrarVector(a)
main()


"""""
20 5
5 -8 9 12 0 4 -1 25 3 10 6 2 15 7 11 5 26 31 0 4
"""