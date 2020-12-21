from typing import *
import sys

Building = Tuple[int, int]


def entrada():
    n = int(sys.stdin.readline())
    v = []

    for i in range(n):
        h = int(sys.stdin.readline())
        b = (i, h)
        v.append(b)

    return v


def derecha(v):
    n = v.__len__()-1
    d = []
    act = -1
    while n >= 0:
        if v[n][1] > act:
            d.append(v[n])
            act = v[n][1]
        n -= 1
    return d


def resolver(v, d):
    izq = (0, 0)
    dn = d.__len__()-1
    der = d[dn]
    res = -1
    riz = -1
    rde = -1
    rh = 0
    n = 0

    while n < v.__len__()-1:
        cand = True
        if v[n][1] > izq[1]:
            izq = v[n]
            cand = False
        if v[n][0] == der[0]:
            dn -= 1
            der = d[dn]
            cand = False
        if cand:
            act = min(izq[1], der[1]) - v[n][1]
            if act > rh:
                rh = act
                res = v[n][0]
                riz = izq[0]
                rde = der[0]
        n += 1

    if v[rde][1] > v[riz][1]:
        n = res
        while n < v.__len__()-1:
            if v[n][1] > v[riz][1]:
                rde = n
                n = v.__len__()-1
            n += 1

    if v[rde][1] < v[riz][1]:
        n = res
        while n > 0:
            if v[n][1] > v[rde][1]:
                riz = n
                n = 0
            n -= 1

    return res, rh, riz, rde


buildings = entrada()
dere = derecha(buildings)
result, height, iz, de = resolver(buildings, dere)
if result == -1 or height == 0:
    print("NO HAY SOLUCIÓN")
else:
    print(iz, de, result, height)
