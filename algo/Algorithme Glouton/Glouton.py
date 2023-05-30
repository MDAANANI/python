# Créé par MOHAMED.DAANANI, le 09/02/2023 en Python 3.7
'''
def renduMonnaie(somme,pieces):
    n=len(pieces)
    choisies=[0]*n
    for i in range(0,n):
        while somme>=pieces[i]:
            somme=somme-pieces[i]
            choisies[i]=choisies[i]+1
    return choisies
pieces=[10,5,2]
somme=31
print('Les pièces choisies sont')
print(renduMonnaie(somme,pieces))
'''

'''
def remplirSac(objets,poidsMax):
    p=0
    n=len(objets)
    objetsChoisis=[0]*n
    for i in range(0,n):
        if p+objets[i][1]<=poidsMax:
            objetsChoisis[i]=1
            p = p + objets[i][1]
    return objetsChoisis

objets=[[2,1],[5,0.5],[1,0.2],[3,4]]
objets=list(reversed(sorted(objets)))
print(objets)
poidsMax=4.7
print('Les objets choisis sont')
print(remplirSac(objets,poidsMax))

'''
'''

#1
def renduMonnaie(somme,pieces):
    n=len(pieces)
    choisies=[0]*n
    for i in range(0,n):
        while somme>=pieces[i]:
            somme=somme-pieces[i]
            choisies[i]=choisies[i]+1
    return choisies

pieces=[50,20,10,5,2,1]
somme=99
print('Les pièces choisies sont')
print(renduMonnaie(somme,pieces))
'''
'''
#2
def remplirSac(objets,poidsMax):
    p=0
    n=len(objets)
    objetsChoisis=[0]*n
    for i in range(0,n):
        if p+objets[i][1]<=poidsMax:
            objetsChoisis[i]=1
            p = p + objets[i][1]
    return objetsChoisis
objets=[[6,5.0,'chaussures'],[5,5.0,'habits'],[4.5,2.0,'trousse de toilette'],[4,2.0,'crêmes'],[3,8.0,'livres'],[2,2.0,'palmes tuba'],[1,0.5,'guide touristique']]
print(objets)
poidsMax=23
print('Les objets choisis sont')
print(remplirSac(objets,poidsMax))
'''
'''
#3
def remplirCamion(meubles,volumeMax):
    v=0
    n=len(meubles)
    meublesChoisis=[]
    for i in range(0,n):
        if v+meubles[i][1]<volumeMax:
            meublesChoisis.append(meubles[i][0])
            v=v+meubles[i][1]
    print('volume max embarqué',v)
    return meublesChoisis


#liste des objets
meubles=[['armoire',3],['fauteuil',1.1],['lave vaisselle',1.0],['lit',0.9],['ordinateur',0.2]]
print(meubles)
volumeMax=5
print('Les meubles choisis sont')
meublesChoisis=remplirCamion(meubles,volumeMax)
print(meublesChoisis)
'''

#4

def journee(activites,dureeMax):
    d=0
    n=len(activites)
    activitesChoisies=[]

    return activitesChoisies


#liste des objets
activites=[[1,"faire la vaisselle"],[2,"passer l'aspirateur"],[3,"terminer le tp NSI"],[4,"vernir l'escalier"]]
print(activites)
dureeMax=6
print('Les activités choisies sont')
activitesChoisies=journee(activites,dureeMax)
print(activitesChoisies)
