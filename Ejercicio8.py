import sys
from sympy import false, true
def verifica(n):
    for digito in str(n):
        if digito != "0" and digito != "1":
            return false
    return true
def contar(n,z):
    cont = 0
    for digito in str(n):
        if digito == z:
            cont = cont + 1
    return cont
def main():
    k = int(sys.stdin.readline())
    n = input()
    while true:
        if k >=1 and k <= 200000 and verifica(n) == true:
            break
        else:
            k = int(sys.stdin.readline())
            n = sys.stdin.readline()
    k = abs(contar(n, "1") - contar(n, "0"))
    print(k)
main()