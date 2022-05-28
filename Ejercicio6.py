#Dado un numero N, invertir N cada K digitos y componer un nuevo numero con los digitos invertidos

from sympy import true
import sys
from timeit import default_timer
def ultimoDigito(n):
    if n == 0:
        return 0
    else:
        return n % 10
def eliminarUltimoDigito(n):
    if n == 0:
        return 0
    else:
        return n // 10
def invertir_cadena(cadena):
    return cadena[::-1]
def cantidadVueltas(n, k):
    z = len(str(n))
    cont = 0
    while true:
        z = z-k
        if z < 0:
            break
        cont = cont + 1
    return cont
def cantidadNum(n, k):
    if len(str(n)) == 1:
        return 1
    else:
        x = ''
        z = cantidadVueltas(n, k)
        for i in range(z):
            x1 = ''
            for i in range(k):
                x1 = x1+ str(ultimoDigito(n))
                n = eliminarUltimoDigito(n)
            x =x1+x
        return x
def main():
    #n = int(sys.stdin.readline())
    n = (10*18)-5
    k = (10*18)-56
    #k = int(sys.stdin.readline())
    while true:
        if n >= 0 and n <= 10**18 and k >= 0 and k <= 10**18:
            break
        else:
            n = int(sys.stdin.readline())
            k = int(sys.stdin.readline())
    if k > len(str(n)):
        print(0)
    else:
        print(cantidadNum(n, k))


inicio = default_timer()
main()
final = default_timer()
print(final-inicio)