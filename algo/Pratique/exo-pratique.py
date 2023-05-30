# Créé par mohamed.daanani, le 09/05/2023 en Python 3.7

#3

def recherche(caractere, chaine):
    occurence=0
    for n in range(0,len(caractere)):
        occurence+=chaine.count(caractere[n])
    return occurence

print(recherche('e', "sciences")) #2
print(recherche('i', "mississippi")) #4
print(recherche('a', "mississippi"))#0





#4

def correspond (mot, mot_a_trou):
    mot=''
    for i in range(len(mot)):
        if mot_a_trou:
            print (True)
        else :
            print(False)
    return mot

print(correspond('INFORMATIQUE', 'INFO*MA*IQUE')) #True
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE')) #False
print(correspond('STOP', 'S*')) #False
print(correspond('AUTO', '*UT*')) #True
