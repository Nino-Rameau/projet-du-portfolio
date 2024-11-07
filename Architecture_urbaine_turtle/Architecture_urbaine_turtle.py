###############################
### IMPORTATION DES MODULES ###
###############################

from turtle import *
import random

################################
### DEFINITION DES FONCTIONS ###
################################

def choix_couleur():            
    rouge = random.randint(0, 255)
    vert = random.randint(0, 255)
    bleu = random.randint(0, 255)
    return (rouge, vert, bleu)


def nuage(x, y, h):
    penup()
    goto(x, y)  #position de depart
    pendown()   
    color("white", "white")     #couleur contour et remplissage 
    begin_fill()    
    for i in range(random.randint(3, 6)):  #boucle qui crée entre 3 et 6 cercle par nuage
        penup()
        goto(x, y)
        pendown()
        circle(h)       #fonction pour cercle de rayon h
        x = x + h * 1.2  # decale le cercle suivant vers la droite
    end_fill()


def soleil(x, y, h):
    penup()
    goto(x, y)
    pendown()
    color("yellow", "yellow")
    begin_fill()
    circle(h)
    end_fill()


def decors(y):     
    # sol
    penup()
    goto(-400, y)   #position depart
    pendown()
    begin_fill()
    color("grey", "grey")
    forward(800)    # largeur
    right(90)
    forward(250)    # hauteur
    right(90)
    forward(800)    
    right(90)
    forward(250)    
    end_fill()
    
    # ciel
    penup()
    right(90)
    goto(-400, 0)   #position depart
    begin_fill()
    color("#00ccff", "#00ccff")
    forward(800)    #largeur
    left(90)
    forward(250)    #hauteur
    left(90)
    forward(800)
    left(90)
    forward(250)
    end_fill()
    
    # soleil et nuage
    left(90)
    soleil(300, 180, 40)

    #nuage gauche
    nuage(200, 120, 15)
    nuage(175, 108, 15)

    #nuage droite
    nuage(-200, 100, 15)
    nuage(-175, 88, 15)


def mur(x, y, w, h):
    penup()
    goto(x - w / 2, y)  # position de depart centrée 
    pendown()
    color(choix_couleur())  # fonction pour avoir la couleur aleatoire
    begin_fill()
    forward(w)
    left(90)
    forward(h)
    left(90)
    forward(w)
    left(90)
    forward(h)
    left(90)
    end_fill()


def fenetre(x, y, w, h):
    penup()
    goto(x + w , y)  
    pendown()
    color("black", "white") # contour noir et fond blanc
    begin_fill()
    forward(w)
    right(90)
    forward(h)
    right(90)
    forward(w)
    right(90)
    forward(h)
    right(90)
    end_fill()


def porte(x, y, w, h):
    penup()
    goto(x - w, y)
    pendown()
    color(choix_couleur())
    begin_fill()
    forward(w)
    left(90)
    forward(h)
    left(90)
    forward(w)
    left(90)
    forward(h)
    left(90)
    end_fill()


def toit(x, y, w, h):
    penup()
    goto(x, y)
    pendown()
    color(choix_couleur())
    begin_fill()
    forward(w / 2)
    goto(x, y + h)
    goto(x - w / 2, y)
    end_fill()


def immeuble(x, y, w, h):
    nb_etage = random.randint(2, 4)
    for i in range(nb_etage):
        mur(x, y + (h * i), w, h)   #creation des murs
        fenetre(x, y + (h * i) + h / 2, w / 6, h / 4)   #creation des fenetres
    porte(x, y, w / 5, h / 2)   # la porte
    toit(x, y + h * nb_etage, w, h) # le toit


def rue(x, y, w, h):
    x = -(2 * w + 45)   #permet de centrer les immeuble
    for i in range(5):      # crée 5 immeuble dans la rue
        immeuble(x, y, w, h)
        x += w + 15     # ecart entre immeuble


###########################
### PROGRAMME PRINCIPAL ###
###########################

Largeur = 800 
Hauteur = 500
setup(Largeur, Hauteur, 10, 10) #crée la dimension de la fenetre (fonction native)
colormode(255)    # definit couleur sur code RGB

speed(0)    #vitesse
ht()    # cache le curseur
decors(0)   #crée la route, ciel, nuage et soleil

x_r = 0
y_r = 0
w_r = 80
h_r = 50

rue(x_r, y_r, w_r, h_r) #crée la rue
done()
