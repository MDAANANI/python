# Créé par mohamed.daanani, le 10/11/2022 en Python 3.7
'''
#1
def afficheTuple(tuple):
    prenom,nom,adresse,codePostal,ville=tuple
    print('prenom:',prenom)
    print('nom:',nom)
    print('adresse:',adresse)
    print('code postal:',codePostal)
    print('ville:',ville)
tuple=('bruce','wayne','3 impasse de la chauve spuris','72000','le mans')
afficheTuple(tuple)
'''
'''
#2
def calcul(x,coefficientDroite):
    a,b=coefficientDroite
    y=a*x+b
    return y
coefficients=(2,1)
print("La valeur de y pour x=2 est: y=",calcul(2,coefficients))
'''
'''
#3
from math import sqrt
def distance(ptA,ptB):
    xA,yA=ptA
    xB,yB=ptB
    AB=sqrt((xB-xA)**2+(yB-yA)**2)
    return AB
ptA=(2,8)
ptB=(5,9)
print(distance(ptA,ptB))
'''
'''
#4
def rechercheMin(lst):
    min=lst[0]
    for indice in range(1,len (lst)-1):
        if lst[indice]<min:
            min=lst[indice]
            return min
lst=[20,8,9,2,35,49]
'''
'''
#5
def rechercheMax(lst):
    max=lst[0]
    for indice in range(1,max-1):
        if lst[indice]<max:
            max=lst[indice]
            return max

lst=[20,8,9,2,35,49]
print(rechercheMax(lst))
'''
'''
#6
def somme(lst):
    total=lst[0]
    for indice in range(1,total-1):
        if lst[indice]<total:
            total=lst[indice]
            return total
lst=[20,8,9,2,35,49]
print(somme(lst))
'''
'''
#7
def moyenneVersion1(lst):
    total=0






'''
'''
#8
def moyenneVersion2(lst):
   moy=somme/longueur
   return moy
lst=[20,8,9,2,35,49]
print(moyenneVersion2(lst))
'''

#9
def rechercheMaxMinMoyenne(lst):

