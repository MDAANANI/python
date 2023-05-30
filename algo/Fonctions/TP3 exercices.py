# Créé par mohamed.daanani, le 11/10/2022 en Python 3.7
'''
#1
def afficheTexte():
    print('bonjour')
afficheTexte()
'''
'''
#2
def afficheTexte(prenom):
    print('bonjour',prenom)
afficheTexte('Gerard')
'''
'''
#3
def somme(a,b):
    s=a+b
    return s
print(somme(3,5))
'''
'''
#4
res= somme(3,5)
print(res)
def calculsurface(longueur,largeur):
    surface=longueur*largeur
    return surface
print(calculsurface(10.5,2))
'''
'''
#5
def calculFormule (x):
    y=2*x**-4*x+3
    return y
print(calculFormule(3.2))
'''
'''
#6
from math import pi
def conversionAngle(radian):
    degre=(180*radian)/pi
    return degre
print(conversionAngle(3*pi/2))
'''
'''
#7
def table(operande,valMin,valMax):
    for i in range(valMin,valMax+1):
        print(i*operande)

table(2,1,10)
'''
'''
#8
def rectangle (hauteur,largeur):
    for i in range(1,hauteur+1):
        for t in range(1,largeur+1):
            print("*",end="")
        print()
rectangle(10,5)
'''
'''
#9
def triangle(hauteur):
    for h in range(1,hauteur+1):
        for i in range(1,h+1):
            print("*",end="")
        print()
triangle(5)
'''
'''
#10
from math import pi
def volume(rayon):
    print((4*pi*rayon**3)/3)
volume(10)
'''
