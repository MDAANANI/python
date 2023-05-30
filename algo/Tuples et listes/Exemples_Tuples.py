#Tuples
'''
a=(1,2)
print (type(a))
print(a)
'''
'''
a=(1,'bonjour')
b=a*2
print(b)
'''
'''
tuple_1 = (5, 2, 25, 56)
tuple_2 = ("jack","tony")
tuple_3 = tuple_1 + tuple_2
print(tuple_3)
'''
'''
couleur=(255,128,64)
rouge=couleur[0]
vert=couleur[1]
bleu=couleur[2]
print(rouge,vert,bleu)
'''
'''
tuple=('a',1,5.6,45,'toto')
longueur=len(tuple)
print("longueur du tuple",longueur)
for i in range(0,longueur):
print(tuple[i])
'''
'''
tuple=('a',1,5.6,45,'toto')
longueur=len(tuple)
print("longueur du tuple",longueur)
for valeur in tuple:
print(valeur)
'''
'''
a=(1,2) # ou a=1,2
a[0]=0
'''
'''
a=(1,2)
b=(0,a[1])
print(a,b)
'''
'''
couleur=(255,128,64)
rouge=couleur[0]
vert=couleur[1]
bleu=couleur[2]
print(rouge,vert,bleu)
'''
'''
def donne_moi_ton_nom():
tuple=("Roger", "Federer")
return tuple
print(donne_moi_ton_nom())
'''
'''
lst=[45,12,4,78]
print (type(lst))
print(lst)
'''
'''
lst=[45,12,4,78]
lst[1]=0
print(lst)
'''
'''
lst=[45,12,4,78]
longueur=len(lst)
print("longueur de la liste",longueur)
for i in range(0,longueur):
print(lst[i])
'''
'''
lst=[45,12,4,78]
for valeur in lst:
print(valeur)
'''
'''
lst=[0] *10
print(lst)
lst[2]=5
print(lst)
'''
'''
lst=[i for i in range(0,10)]
print(lst)
'''
'''
lst=[i*2 for i in range(0,10)]
print(lst)
'''
'''
#ajout d’un élément dans la liste
lst=[i for i in range(0,10)]
print(lst)
lst.append(50)
print(lst)
'''
'''
#affiche les derniers éléments en partant de l’indice 2
lst=[i for i in range(0,10)]
print(lst)
print(lst[2:])
'''
'''
#affiche les 3 premiers éléments
lst=[i for i in range(0,10)]
print(lst)
print(lst[:3])
'''
'''
#affiche le 2ème élément en partant de la fin
lst=[i for i in range(0,10)]
print(lst)
print(lst[-2])
'''
'''
#affiche les éléments entre l’indice 2 et l’indice 6 (exclu)
lst=[i for i in range(0,10)]
print(lst)
print(lst[2:6])
'''
'''
lst=[i for i in range(0,10)]
print(lst)
lst.remove(5)
print(lst)
'''
'''
lst=[i for i in range(0,10)]
print(lst)
lst.insert(7,12)
print(lst)
'''
'''
lst=[[1,2,3],
[4,5,6],
[7,8,9]]
print(lst)
'''
'''
#accès à un élément du tableau
lst=[[1,2,3],
[4,5,6],
[7,8,9]]
ligne=1
colonne=2
print(lst[ligne][colonne])
'''
'''
#affichage sous forme de tableau
lst=[[1,2,3],
[4,5,6],
[7,8,9]]
for ligne in range(0,3):
for colonne in range(0,3):
print(lst[ligne][colonne],end=' ')
print()
'''
'''
#initialisation d’un tableau à 2 dimensions
ligne = 3
colonne = 4
lst = [[0] * ligne for i in range(colonne)]
lst[1][1]=2
print(lst)
'''
'''
liste=[5,6,7,8,9,4] somme=0 for n in range(len(liste)): somme=somme+liste[n] print(somme)
'''

