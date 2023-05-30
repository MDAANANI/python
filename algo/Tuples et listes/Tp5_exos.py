# Créé par mohamed.daanani, le 22/11/2022 en Python 3.7



#1

from PIL import Image,ImageDraw,ImageFont
img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def traceDroite(nbDroites,ecart):
    for i in range(0,nbDroites):
         draw.line((0,),fill=(0,255,0))
         return traceDroite

traceDroite(10,20)

img.show()


'''
#2
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def cercle(x,y,rayon,couleur):
    draw.ellipse((x-rayon,y-rayon,x+rayon, y+rayon),fill=couleur)

def tracecible():



tracecible()
img.show()
'''