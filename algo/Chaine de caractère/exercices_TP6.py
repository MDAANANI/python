# Créé par mohamed.daanani, le 01/12/2022 en Python 3.7
'''
#1
phrase = "bonjour"
print (phrase[1:4])
'''
'''
chaine = "NE PARLEZ PAS SI FORT !"
print(chaine.lower())
chaine="nsi"
chaine=chaine.upper()
print(chaine)
'''
'''
w = "Washington"
t= "Touchard"
lycee= w+" "+t
print (lycee)
print (len(lycee))
'''
'''
chaine = "Bonjour "
for i in range(0, len(chaine)):
    print(chaine[i], end = '')

chaine = "Au revoir"
for c in chaine:
    print(c, end = '')
'''
'''
chaine=str(input("votre chaine ?"))
if chaine=='bonjour':
    print('hello')
else:
    print('j\'ai rien compris')
'''
'''
s = "Welcome"
print(s[-1])
print(s[-2])
'''
'''
s = "Welcome"
print(s[:6])
print(s[4:])
print(s[1:-1])
'''
'''
s = "Hello computer"
print(s.endswith("uter"))
print(s.startswith("good"))
print(s.find("comp"))
print(s.rfind("o"))
print(s.count("o"))
'''
'''
chaine = "\r  Bien le bonjour\t \t"
s = chaine.strip()
print(s)
'''
'''
ch = 'A'
print(ord(ch))
'''
'''
valeur=66
print(chr(valeur))
'''
'''
chaine = "10.5"
print(type(chaine))
valeur=float(chaine)
print(type(valeur))
print(valeur)
'''
'''
#2
def compteLettre(lettre,chaine):
    chaine.count("e")
    return chaine.count("e")
print(compteLettre('e','je vais au cine ce soir'))
'''
'''
def compteLettre(lettre,chaine):
    chaine="je vais au cine ce soir"
    total=0
    for i in range(len(chaine)):
        if chaine[i]=='e':
            total+=1
print(compteLettre('e','je vais au cine ce soir'))
'''
'''
#3
def fonctionpremierMot(chaine):
    pos=chaine.find(" ")
    return chaine[:pos]
print(fonctionpremierMot("enfin il arrête de pleuvoir "))
'''
'''
#4
print("Un peu")
print("Beaucoup")
print("Passionnément")
'''
'''
#5
semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
for i in range(len(semaine)):
    print(semaine[i])
'''
'''
semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
for s in semaine:
    print(s)
'''
'''
#6
semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
for jour in semaine:
    print(jour)

depart=3-1
for n in range(1,32):
    print(semaine[(n+depart)%7],n,"decembre")
'''
'''
#7
voyelles=['a','e','i','o','u','y']
def compteVoyelles(chaine):
    somme=0
    for v in voyelles:
        somme=somme+chaine.count(v)
    return somme
chaine=str(input("votre chaine ?"))
print(chaine,compteVoyelles(chaine))
'''
'''
#8
def compteDesMots(chaine):
    chaine.count(" ")
    return chaine.count(" ")


chaine=str(input("votre chaine ?"))
print(chaine,compteDesMots(chaine))
'''
'''
#9
#lycée Touchard
latitude="47° 59.698'N"
longitude="  0° 12.276'E"

#VLT au Chili
#latitude="24° 37.649'S"
#longitude=" 70° 24.250'W"

degLatitude=int(latitude[0:2])
degLatitudeDec=float(latitude[3:10])/60
latitudeDecimal=degLatitude+degLatitudeDec

degLongitude=int(longitude[0:3])
degLongitudeDec=float(longitude[4:11])/60
longitudeDecimal=degLongitude+degLongitudeDec

if latitude[11]=='s':
    latitudeDecimal=latitudeDecimal*-1

if longitude[12]=='W':
    longitudeDecimal=longitudeDecimal*-1

print(latitudeDecimal,longitudeDecimal)
'''
'''
#10
valeur=int(input("saisir un nombre entre 1 et 12"))

compteur=0
for rouge in range(1,7):
    for vert in range(1,7):
        somme= rouge+vert
        if somme==valeur:
            compteur+=1
print('il y a',compteur,'facon(s) de faire',valeur,'avec deux dés.')
'''

#Compliments
'''
#1
brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢','⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅','⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵']

def affichagebaille(texte):
    texte=texte.upper()
    texteBraille=''
    for c in range(0,len(texte)):
        if texte[c]>=' ' and texte[c]<='Z':
            texteBraille+=brailles[ord(texte[c])-32]
    return texteBraille


texte=str(input("votre texte ?"))
print(affichagebaille(texte))
'''
'''
#2
cr="*"
def insertionTexte(texte):
    ntexte=texte[0]
    for i in texte:
        ntexte=ntexte+cr+i
    return ntexte
chaine="Touchard"
print(insertionTexte(chaine)[2:])


def insertionTexte(texte):
    nouveauTexte=''
    for indice in range(len(texte)-1):
        nouveauTexte+=texte[indice]+'*'
    nouveauTexte+=texte[-1]
    return nouveauTexte
texte=str(input("votre texte ?"))
print(insertionTexte(texte))
'''

#3
def inversionMot(texte):


