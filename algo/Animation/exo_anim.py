# Créé par MOHAMED.DAANANI, le 14/03/2023 en Python 3.4
#1
'''
import pygame
#constantes de la fenêtre d'affichage
LARGEUR=256       #hauteur de la fenêtre
HAUTEUR=256      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Affichage")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame


def afficheCercle(x,y,rayon): #affiche un cercle aux coordonnées x,y avec un rayon
    pygame.draw.circle(fenetre, ROUGE, (x,y), rayon)

def afficheRectangle(x,y,largeur,hauteur):   #affiche un rectangle en position x,y avec une largeur et une hauteur
    pygame.draw.rect(fenetre, BLEU, [x, y, largeur, hauteur])

def afficheTexte(x,y,txt):  #affiche un texte aux coordonnées x,y
    texteAfficher = font.render(str(txt), True, VERT)
    fenetre.blit(texteAfficher,(x,y))


loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False

    fenetre.fill((0,0,0))   #efface la fenêtre
    afficheCercle(200,200,50)
    afficheRectangle(50,10,80,30)
    afficheTexte(20,150,'bye')
    frequence.tick(60)		#framerate 60 images /sec
    pygame.display.update() #mets à jour la fenêtre graphique
pygame.quit()
'''
'''
#2

import pygame

#constantes de la fenêtre d'affichage
LARGEUR=256       #hauteur de la fenêtre
HAUTEUR=256      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,0,0)
BLEU=(0,0,255)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Affichage")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame

#variables de gestion de la balle
RAYONBALLE=10
balleX=LARGEUR//2
balleY=HAUTEUR//2          #position x y de la balle au milieu dans la fenêtre
vecteurBalleX=2            #vecteur de déplacement
vecteurBalleY=1


def afficheBalle():
    """
    affiche une balle aux coordonnées balleX,balleY avec un RAYON prédéfini
    """
    pygame.draw.circle(fenetre, ROUGE, (balleX,balleY), RAYONBALLE)

def deplacementBalle():
    """
    deplace la balle
    """
    global balleX,balleY        #permet de modifier les variables balleX,balleY
    balleX=balleX+vecteurBalleX #on deplace la balle selon l'axeX
    balleY=balleY+vecteurBalleY #on deplace la balle selon l'axeY

def testeCollisionMurs():
    """
    test les collisions avec les murs
    """
    global vecteurBalleX,vecteurBalleY
    if balleX>LARGEUR:
        vecteurBalleX=vecteurBalleX*-1
    if balleX<0:
        vecteurBalleX=vecteurBalleX*-1
    if balleY>LARGEUR:
        vecteurBalleY=vecteurBalleY*-1
    if balleY<0:
        vecteurBalleY=vecteurBalleY*-1
loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False

    fenetre.fill((0,0,0))   #efface la fenêtre
    afficheBalle()
    deplacementBalle()
    testeCollisionMurs()
    frequence.tick(60)
    pygame.display.update() #mets à jour la fenêtre graphique
pygame.quit()
'''

#3
'''
import pygame
#constantes de la fenêtre d'affichage
LARGEUR=256       #hauteur de la fenêtre
HAUTEUR=256      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)
#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Balle")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame

#variables de gestion de la balle
RAYONBALLE=10
balleX=LARGEUR//2
balleY=HAUTEUR//2          #position x y de la balle au milieu dans la fenêtre
vecteurBalleX=0            #vecteur de déplacement
vecteurBalleY=0

def afficheBalle():
    pygame.draw.circle(fenetre, ROUGE, (balleX,balleY), RAYONBALLE)

def deplacementBalle():
    global balleX,balleY        #permet de modifier les variables balleX,balleY
    balleX=balleX+vecteurBalleX #on deplace la balle selon l'axeX
    balleY=balleY+vecteurBalleY #on deplace la balle selon l'axeY

def testCollisionMurs():
    """
    test les collisions avec les murs en tenant compte du rayon
    """
    global balleX,balleY
    if balleX>LARGEUR:
      balleX=balleX-1
    if balleX<0:
        balleX=balleX-1
    if balleY>LARGEUR:
        balleY=balleY*-1
    if balleY<0:
        balleY=balleY-1
loop=True
while loop==True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
      keys = pygame.key.get_pressed()         #recupération des touches appuyées en continu
      if keys[pygame.K_UP]:    #est-ce la touche UP
        vecteurBalleY=-1
      elif keys[pygame.K_DOWN]:  #est-ce la touche DOWN
        vecteurBalleY = 1
      elif keys[pygame.K_RIGHT]:  #est-ce la touche RIGHT
        vecteurBalleX = 1
      elif keys[pygame.K_LEFT]:  #est-ce la touche LEFT
        vecteurBalleX = -1
      else:
        vecteurBalleY=0
        vecteurBalleX=0
      fenetre.fill((0,0,0))   #efface la fenêtre
      afficheBalle()
      deplacementBalle()
      testCollisionMurs()
      frequence.tick(60)
      pygame.display.update() #mets à jour la fenêtre graphique
pygame.quit()
'''


#4
'''
import pygame

#constantes de la fenêtre d'affichage
LARGEUR=256       #hauteur de la fenêtre
HAUTEUR=256      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Balle")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame

#variables de gestion de la balle
RAYONBALLE=10
balleX=LARGEUR//2
balleY=HAUTEUR//2          #position x y de la balle au milieu dans la fenêtre
vecteurBalleX=0            #vecteur de déplacement
vecteurBalleY=0


def afficheBalle():
    """
    affiche une balle aux coordonnées balleX,balleY avec un RAYON prédéfini
    """
    pygame.draw.circle(fenetre, ROUGE, (balleX,balleY), RAYONBALLE)

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            fenetre.fill((0,0,0))   #efface la fenêtre

    balleX, balleY = pygame.mouse.get_pos()

    afficheBalle()
    frequence.tick(60)
    pygame.display.update() #mets à jour la fenêtre graphique
pygame.quit()
'''



#5
'''
import pygame

#constantes de la fenêtre d'affichage
LARGEUR=256       #hauteur de la fenêtre
HAUTEUR=256      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Affichage")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame
mouseX=0
mouseY=0


def afficheCercle(x,y,rayon):
    """
    affiche un cercle aux coordonnées x,y avec un rayon
    """
    pygame.draw.circle(fenetre, ROUGE, (x,y), rayon)

def afficheRectangle(x,y,largeur,hauteur):
    """
    affiche un rectangle en position x,y avec une largeur et une hauteur
    """
    pygame.draw.rect(fenetre, BLEU, [x, y, largeur, hauteur])

def afficheTexte(x,y,txt):
    """
    affiche un texte aux coordonnées x,y
    """
    texteAfficher = font.render(str(txt), True, VERT)
    fenetre.blit(texteAfficher,(x,y))

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            color=fenetre.get_at((mouseX, mouseY))[:3]
            print(color)

    mouseX, mouseY = pygame.mouse.get_pos()

    fenetre.fill((0,0,0))   #efface la fenêtre
    afficheCercle(30,100,10)
    afficheRectangle(100,150,20,70)
    afficheTexte(100,50,str(mouseX)+' '+str(mouseY))
    frequence.tick(60)
    pygame.display.update() #mets à jour la fenêtre graphique
pygame.quit()
'''


#6

import pygame

#constantes de la fenêtre d'affichage
LARGEUR=256       #hauteur de la fenêtre
HAUTEUR=256      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)
#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Scrolling")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame

texteX=LARGEUR

def afficheTexte(x,y,txt):
    """
    affiche un texte aux coordonnées x,y
    """
    texteAfficher = font.render(str(txt), True, VERT)
    fenetre.blit(texteAfficher,(x,y))

def defilementTexte():
    global texteX

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False


    fenetre.fill((0,0,0))   #efface la fenêtre
    afficheTexte(texteX,100,'Lycée Gabriel Touchard')
    defilementTexte()
    frequence.tick(60)
    pygame.display.update() #mets à jour la fenêtre graphique
pygame.quit()
