#2
'''
from PIL import Image
img=Image.open("phare1.jpg")
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
        r,v,b=img.getpixel((x,y))
        moyenne=(r+v+b)//3
        r = moyenne
        v = moyenne
        b = moyenne
        img.putpixel((x,y),(r,v,b))
img.show()
'''
#3
'''
import time
import random

N=5             #longueur du tableau
VALEUR_MAX=50   #valeur maximale pouvant être contenue dans le tableau

def creationValeursNonTrie(N):  #fonction de génération d'un tableau de valeurs aléatoires
    tableau=[]
    for indice in range(0,N):
        tableau.append(random.randint(1,VALEUR_MAX))
    return tableau

def tri_Selection(tableau):     #fonction de tri par sélection à compléter
    for i in range(0, N - 1):
        indmini = i
        for j in range(i + 1, N):
            if (tableau[j] < tableau[indmini]):
                indmini = j
        if (i != indmini):
            temp = tableau[i]
            tableau[i] = tableau[indmini]
            tableau[indmini] = temp
            print(tableau[indmini], '<-->', tableau[i], ':', tableau)


tab=creationValeursNonTrie(N)   #génération d'un tableau de valeur aléatoire
print('tableau non trié',tab)
debut = time.time()             #mémorisation de l'heure de début
tri_Selection(tab)
fin = time.time()               #mémorisation de l'heure de fin
print("longueur tableau \t durée de traitement")
print(N,'\t',fin-debut)
print('tableau trié',tab)
'''

'''
"""
tp3 recherche dichotomique
"""
import time
import random

N=16             #longueur du tableau
VALEUR_MAX=100   #valeur maximale pouvant Ãªtre contenue dans le tableau

def creationValeurs(N):
    tableau=[]
    for indice in range(0,N):
        valeur=random.randint(1,VALEUR_MAX)
        while valeur in tableau:
            valeur = random.randint(1, VALEUR_MAX)
        tableau.append(valeur)
    return sorted(tableau)


def recherche_dichotomique( element, tableau ):
    bas = 0
    haut = len(tableau)-1
    trouve=False
    print('{:<8}{:<8}{:<8}{:<8}{:<12}{:<8}'.format('bas:','haut:','milieu:','valeur:','bas<=haut:','trouve:'))
    while bas <= haut and trouve==False:
        milieu = (bas + haut) // 2
        if element==tableau[milieu]:
            trouve=True
            print('{:<8}{:<8}{:<8}{:<8}{:<12}{:<8}'.format(bas, haut, milieu, tableau[milieu], bas <= haut, trouve))
        else:
            print('{:<8}{:<8}{:<8}{:<8}{:<12}{:<8}'.format(bas, haut, milieu, tableau[milieu], bas <= haut, trouve))
            if element>tableau[milieu]:
                bas = milieu+1
            else :
                haut = milieu-1
        time.sleep(0.1)
    print('{:<8}{:<8}{:<8}{:<8}{:<12}{:<8}'.format(bas, haut, milieu, tableau[milieu], bas <= haut, trouve))
    if trouve==True:
        indice = milieu
    else:
        indice = -1
    return indice


def affichage(tableau):
    print('valeur',end='')
    for x in range(0, len(tableau)):
        print('{0:4d}'.format(tableau[x]),end='')
    print()
    print('indice', end='')
    for x in range(0, len(tableau)):
        print('{0:4d}'.format(x),end='')
    print()

tableau=creationValeurs(N)
affichage(tableau)
#tableau=[10,12,15,21,25,31,35,37,42,44,49,53,61,72,75,85]
#print (tableau)


chiffreAtrouver=tableau[1]
print('chiffre Ã  trouver',chiffreAtrouver)

debut = time.time()
indice=recherche_dichotomique(chiffreAtrouver,tableau)
fin = time.time()
print("la valeur",tableau[indice],"se trouve Ã  l'indice", indice,"dans le tableau:")
print(N,'\t',fin-debut)
'''

'''
def Tri_insertion(tab):
      tab=[18,47,8,21,34]
      for n in range(1,n):
        j=i
        memoire=tab[i]
        while j>0 and memoire<tab[j-1]:
            Tab[j-1],Tabl[j] = Tab[j],Tab[j-1]
            j = j - 1
            Tabl[j]= memoire
'''
'''
from random import randint

Tableau = [randint(0, 20000) for i in range(20000)]
Tableau.sort(reverse=True)

nb_affectation = 0

for i in range(1,len(Tableau)):

    j=i

    encours=Tableau[i]
    nb_affectation += 1

    while (j>0) and encours<Tableau[j-1]:

        Tableau[j] = Tableau[j-1]
        nb_affectation += 1

        j-=1

    Tableau[j]=encours

print('taille n=',len(Tableau)," nb affectation =",nb_affectation)
'''



EPAISSEUR_FEUILLE=0.0001

def calcul_nb_pliages(hauteur):
    somme_hauteur=EPAISSEUR_FEUILLE
    pilages=0
    while somme_hauteur<hauteur:




        print(somme_hauteur)
    return pliages

print(calcul_nb_pliages(1.6))
