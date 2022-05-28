from ntpath import join
from sympy import true
def generarMatriz(n):
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)
    return matriz
def mostrarMatriz(matriz):
    for line in matriz:
        print (' '.join(map(str, line)))
def main():
    n = int(input())
    while true:
        if n >= 2 and n <= 700 and n %2 == 0:
            break
        else:
            n = int(input())
    m = generarMatriz(n)
    z = 1; x = 1
    for i in range(n):
        for j in range(n):
            m[i][j] = z
            z = z+2
        z = m[i][n-1]
        if z % 2 == 0:
            z = z+1
            x = z
        else:
            z = x+1
    mostrarMatriz(m)
main()