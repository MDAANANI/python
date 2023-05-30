# Créé par MOHAMED.DAANANI, le 09/03/2023 en Python 3.7
'''
#2
new_message =""     # initialise new_message avec un message vide
message = input("Veuillez saisir un texte en MAJUSCULE et terminer par ENTER")
print("Vous avez saisi ",message)  # Affiche le message saisi

for n in message:               # pour chaque caractère n dumessage saisi (de la chaine message)
    code_initial = ord(n)       # la variable code_initial prend le code (Unicode)
                              # du caractère courant (n)
    code_minuscule = code_initial +32    # calcul le codecorrespondant au caractère minuscule

    car_minuscule = chr(code_minuscule) # car_minuscule prend le caractère/symbole correspondant
                                        #à la variable code_minuscule
    print(car_minuscule)      # Affiche le caractère obtenu
    new_message = new_message + car_minuscule  # ajoute le caractère obtenu à new_message

print (new_message)    # Affiche le nouveau message
'''

#3
'''
import os
fichier=open("texte.txt","r")
chaine=fichier.read()
print(chaine)
fichier.close()

import os
fichier=open("texte.txt","w")
fichier.write("bonjour\n")
fichier.write("salut")
fichier.close()

import os
fichier=open("texte.txt","r")
chaine=fichier.read()
print(chaine)
fichier.close()
'''


#4
'''
message="Spécialité NSI 2019-2020"

#Ouverture/création du fichier1 en encodage Latin 1
fichier1=open("Exemple_encodage_Latin1.txt",'w',encoding="latin-1")

#Ouverture/création du fichier2 en encodage UTF-8
fichier2=open("Exemple_encodage_UTF-8.txt",'w',encoding="utf-8")

#Ouverture/création du fichier1 en encodage UTF-8 avec signature (BOM)
fichier3=open("Exemple_encodage_UTF-8_BOM.txt",'w',encoding="utf-8-sig")

fichier1.write(message)
fichier2.write(message)
fichier3.write(message)

fichier1.close()
fichier2.close()
fichier3.close()
'''


