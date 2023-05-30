# Créé par mohamed.daanani, le 23/03/2023 en Python 3.7

"""
Programme du tron
nom(s), prÃ©nom(s), classe(s)
"""
import pygame
from random import*
#constantes de la fenÃªtre d'affichage
LARGEUR=1000      #hauteur de la fenÃªtre
HAUTEUR=700    #largeur de la fenÃªtre
ROUGE=(255,0,0)     # dÃ©finition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)

#Utilisation de la bibliothÃ¨que pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Tron")             #titre de la fenÃªtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractÃ¨res
frequence = pygame.time.Clock()                     #mode animation dans pygame
motoX=LARGEUR//2
motoY=HAUTEUR//2
direction = 'haut'
tempsPartie=0

def afficheCercle(x,y,rayon): #affiche un cercle aux coordonnées x,y avec un rayon
    pygame.draw.circle(fenetre, ROUGE, (x,y), rayon)

def afficheRectangle(x,y,largeur,hauteur):   #affiche un rectangle en position x,y avec une largeur et une hauteur
    pygame.draw.rect(fenetre, BLEU, [x, y, largeur, hauteur])

def dessineDecor():
    """
    dessine un decor
    """
    pygame.draw.rect(fenetre, ROUGE, [1, 1, LARGEUR-1, HAUTEUR-1],1)


    #pygame.draw.rect(fenetre, BLEU, [x, y, 10, 10],0)  #rectangle plein aux coord x,y

def afficheTexte(x,y,txt):
    """
    affiche un texte aux coordonnÃ©es x,y
    """
    texteAfficher = font.render(str(txt), True, VERT)
    fenetre.blit(texteAfficher,(x,y))

def collisionMur(x,y):
    """
    verifie si on touche un mur ou autre chose
    aucun obstacle correspond Ã  une couleur noire
    """
    color=fenetre.get_at((x, y))[:3]
    somme=color[0]+color[1]+color[2]
    if somme==0:
        collision=False
    else:
        collision=True
    return collision

def deplacementmoto():
    """
    deplace la moto si c'est possible
    """
    global motoX,motoY
    touche=False
    if direction=='haut':
        x=motoX
        y=motoY-1
        touche=collisionMur(x,y)
    elif direction=='bas':
        x=motoX #a completer
        y=motoY+1
    elif direction=='droite':
        x=motoX+1  #a completer
        y=motoY
    elif direction=='gauche':
        x=motoX-1
        y=motoY
        touche=collisionMur(x,y)
    if touche==False:       #si pas d'obstacle alors on trace le point de la moto
        motoX=x
        motoY=y
    fenetre.set_at((x, y), VERT)
    return touche           #retourne la variable booleenne touche pour savoir si la partie est terminÃ©e


loop=True
dessineDecor()
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenÃªtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a Ã©tÃ© pressÃ©e...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
            #fenetre.set_at((200, 200), color)

    keys = pygame.key.get_pressed()         #recupÃ©ration des touches appuyÃ©es en continu
    if keys[pygame.K_UP]:    #est-ce la touche UP
        direction = 'haut'
    elif keys[pygame.K_DOWN]:  #est-ce la touche DOWN
        direction = 'bas'
    elif keys[pygame.K_RIGHT]:  #est-ce la touche RIGHT
        direction = 'droite'
    elif keys[pygame.K_LEFT]:  #est-ce la touche LEFT
        direction = 'gauche'


    #fenetre.fill((0,0,0))   #efface la fenÃªtre, non utilisÃ© ici

    if deplacementmoto()==True:
        loop=False
    frequence.tick(60)
    pygame.display.update() #mets Ã  jour la fenÃªtre graphique
    tempsPartie+=1
    afficheCercle(100,100,10)
    afficheRectangle(100,10,20,70)
pygame.quit()
print('perdu')
print('temps partie',tempsPartie)
