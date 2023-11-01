import math


def delta(a, b, c):
    return b * b - 4 * a * c


def NombreRacine(a, b, c):
    d = delta(a, b, c)
    if d > 0:
        return 2
    elif d == 0:
        return 1
    elif d < 0:
        return -2


def Racine1(a, b, c):
    d = delta(a, b, c)
    if d >= 0:
        return (-b - math.sqrt(d)) / 2 * a
    else:
        return (complex(-b, -(math.sqrt(-d)))) / 2 * a


def Racine2(a, b, c):
    d = delta(a, b, c)
    if d >= 0:
        return (-b + math.sqrt(d)) / 2 * a
    else:
        return (complex(-b, +(math.sqrt(-d)))) / 2 * a


def AfficheNombreRacine(a, b, c):
    if NombreRacine(a, b, c) == 1:
        print("Racine Double")
    elif NombreRacine(a, b, c) == 2:
        print("Deux Racines")
    else:
        print("Deux solutions complexes")


def checkIfRight(a, b, c):
    r1 = Racine1(a, b, c)
    r2 = Racine2(a, b, c)
    res1 = a * r1 * r1 + b * r1 + c

    res2 = a * r2 * r2 + b * r2 + c
    print(res1, res2)


tup = (3, 8, 0)
checkIfRight(*tup)
AfficheNombreRacine(*tup)
print(Racine1(*tup))
print(Racine2(*tup))
