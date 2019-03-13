import random
import pygame
from pygame.locals import *
from time import sleep


#----- VARIABLES -----#






#----- CLASS -----#

class poisson:
    def __init__(self, px, py, num):
        self.px = px# coordonnee du poisson = coordonnees de la cellules


class cellule:
    def __init__(self, cx, cy,):
        self.cx = cx
        self.cy = cy
        self.name = 'c' + str(cy) + str(cx)
        self.poissonOccupants = []

    def renvoiPoisson(self, largeur, hauteur):
        if len(tableau[hauteur][largeur].poissonOccupants) > 0:
            return 'P'
        else:
            return '_'


class monde:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.nbPoissons = largeur * hauteur
        self.tableau = []
        for h in range(self.hauteur):
            ligne = []
            for l in range(self.largeur):
                ligne.append(cellule(l, h))
            #print(ligne)
            self.tableau.append(ligne)


    def afficherMonde(self):
        for h in range(self.hauteur):
            for l in range(self.largeur):
                print(tableau[h][l].renvoiPoisson(l, h), end=", ")
            print()




#----- EXECUTION -----#

monde(4, 4).afficherMonde()

