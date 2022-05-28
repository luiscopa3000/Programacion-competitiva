from sympy import true
def descomponer(n):
    if n == 0:
        return []
    else:
        return descomponer(n // 10) + [n % 10]

def sumarVec(v):
    if len(v) == 0:
        return 0
    else:
        return v[0] + sumarVec(v[1:])

def adicionarInicio(v, n):
    if len(v) == 0:
        return [n]
    else:
        return [n] + v
def eliminarUltimo(v):
    if len(v) == 0:
        return []
    else:
        return v[:-1]
def componer(v):
    if len(v) == 0:
        return 0
    else:
        return v[0] * 10 ** (len(v) - 1) + componer(v[1:])
def eliminarCaracter(s, c):
    if len(s) == 0:
        return ""
    else:
        if s[0] == c:
            return eliminarCaracter(s[1:], c)
        else:
            return s[0] + eliminarCaracter(s[1:], c)

entrada = int(input())
for j in range (entrada):
    res = ''
    while true:  
        n, k = map(int, input().split())
        if n >= 100 and n <= 1000000000000000:
            if k >= 0 and k <= 100:
               break
    n = int(n)
    y = descomponer(n)
    x = sumarVec(y)
    s = 0
    for i in range(k):
        while len(str(x)) > 1:
            x = sumarVec(descomponer(x))
        res = str(x)+ res
        y = eliminarUltimo(y)
        y = adicionarInicio(y, x)
        x = sumarVec(y)
        s = s + componer(y)
    j = descomponer(int(res))
    res = ''
    for i in range(len(str(n))):
        res = res + str(j[i])
    print(res)