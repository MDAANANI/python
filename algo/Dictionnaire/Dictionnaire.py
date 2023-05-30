# Créé par MOHAMED.DAANANI, le 02/02/2023 en Python 3.7
#1
'''
d = { 'nom':'Dupuis' , 'prenom':'Jacque', 'age':30}
inventaire=""
for nom in d.keys():
    inventaire += nom + ', '
for num in d.values():
    print(inventaire,num)
'''
#2
'''
D = {'Croissants':6,'Pizza':2:'Café en grains':3,'Riz':1}
print(courses)
'''

#3
'''
def occurrences(chaine) :
   D = {}
   for caractere in chaine :
      if caractère in D.keys():
          D[caractere] = D[caractere] + 1
      else:
           D[caractere] = 1
   return D

print(occurrences('tortue'))
'''

#4
'''
def anagramme(chaine1, chaine2) :
    occurenceChaine1 = occurence(chaine1)
    occurenceChaine2 = occurence(chaine2)
    del occurenceChaine1 [‘  ‘]
    del occurenceChaine2 [‘  ‘]
    return occurenceChaine1 == occurenceChaine2
'''

#5
'''

def renduMonnaie(somme,pieces):
    choisies={}
    for p in pieces:
        choisies[p]=0
        while somme>=p :
            somme=somme-p
            choisies[p]+=1
    return choisies


pieces=[500,200,100,50,20,10,5,2,1]
somme=780
print('Les pièces choisies sont')
print(renduMonnaie(somme,pieces)
'''
#7
'''
import csv
fichier = open("ballon2019.csv", "r", encoding="utf-8")
lecture_fichier = csv.DictReader(fichier ,delimiter=’,’)
liste_enregistrement=[]
for ligne in lecture_fichier:
    liste_enregistrement.append(dict(ligne))
    fichier.close()

'''
'''
horaire_tmp_min = ''
tmp_min = 100.
for enregistrement in liste_enregistrements:
    if float(enregistrement(‘Temp Ext c’ 1)) < tmp_min :
        tmp_min = float(enregistrement(‘Temp Ext c’ 1))
        horaire_tmp_min = enregistrement['Horaire']
print(horaire_tmp_min,tmp_min)

'''

#8

'''
from pylab import *

x = [1, 3, 4, 6]
y = [2, 3, 5, 1]
plot(x, y) # affiche y en fonction de x

show() # affiche la figure l’écran
'''
'''
import csv
from pylab import *

def listePourUneCle(liste_dico, cle):
    resultat=[]
    for dico in liste_dico:
        resultat.append(float(dico[cle]))

    return resultat


fichier = open("ballon2019.csv", "r", encoding="utf-8")
lecture_fichier = csv.DictReader(fichier, delimiter=',')
liste_enregistrements = []
for ligne in lecture_fichier:
    liste_enregistrements.append(dict(ligne))
fichier.close()

liste_altitudes = listePourUneCle(liste_enregistrements,'Altitude m')
print(liste_altitudes)
x=liste_altitudes
y=liste_temperatures
plot(x.y)
show()
'''

import csv
from pylab import *


def listePourUneCle(liste_dico, cle):
    resultat=[]
    for dico in liste_dico:
        resultat.append(float(dico[cle]))
    return resultat


fichier = open("ballon2019.csv", "r", encoding="utf-8")
lecture_fichier = csv.DictReader(fichier, delimiter=',')
liste_enregistrements = []
for ligne in lecture_fichier:
    liste_enregistrements.append(dict(ligne))
fichier.close()
liste_altitudes=listePourUneCle(liste_enregistrements,"Altitude m")


