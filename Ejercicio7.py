import math
from sympy import true
from functools import reduce
def fibonacci(x):
    n=(math.sqrt(5)+1)/2
    return round(math.pow(n,x)/math.sqrt(5))
def factorial(x):
    return reduce((lambda x, y: x * y), range(1, x+1))
def mostrar(v):
    for i in range(len(v)):
        if i != len(v)-1:
            print(v[i], end=" ")
        else:
            print(v[i])
def main():
    z = int(input())
    for i in range(z):
        n=int(input())
        y = 1
        lista = []
        for j in range(0, n):
            x = fibonacci(j)
            if len(lista) == n:
                break
            lista.append(x)
            for i in range(1, x+1):
                if len(lista) == n:
                    break
                lista.append(x)
            while true:
                if y %2 != 0:
                    if len(lista) == n:
                        break
                    lista.append(factorial(y))
                    y = y+1
                    break
                else:
                    y = y+1
        del lista[n+1:]
        mostrar(lista)
main()