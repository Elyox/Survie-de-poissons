import random
import pygame
from pygame.locals import *



#----- VARIABLES -----#

Size=Widght,height =800 , 630 #Taille de l'ecran en pixels
tailleCase=((height-(2*10))/10) #Taille d'une case en pixel
EcartCase=tailleCase + 2 #Taille d'une case + pixel entre les case. Permet de determiner le decalage entre la position de 2 cases

#Couleurs
Blanc= 250,250,250
Bleu=10,50,255
Color=[Blanc, Bleu]

#Variables globales
global ListePoisson
ListePoisson=[] #Liste des attibuts des poissons

#création liste des nombres
NombreListe=[i for i in range(2,102)]

pygame.init() # initialisation fenetre



font=pygame.font.Font(None, 40) # creation police d'ecriture

#parametrage fenetre
Display = pygame.display.set_mode((Size))
pygame.display.set_caption("poisson")





#Class Poisson qui definit les poissons
class Poisson:
    def __init__(self,x,y,nombre):
        self.x = x #Coordonne x du poisson
        self.y = y #Coordonne y du poisson
        self.nombre = nombre #nombre du poisson


#Class Monde Creations de la grille et gestions de la grille
class Monde:
    def __init__(self ,longueur ,Largeur,NbsPoisson):
        self.longueur = longueur #Taille en longueur de la grille
        self.Largeur = Largeur #taille en largeur de la grille
        self.NbsPoisson = NbsPoisson #Nombre de poisson

    #Résultat: Creation de la grille de deplacement des poissons
    def CréationMonde(self):
        x,y=0,0
        #Création des case de la grille
        for j in range (self.Largeur):
            for i in range(self.longueur):
                pygame.draw.rect(Display,Color[0],(x,y,tailleCase,tailleCase))
                x+=EcartCase
                if x==(10*EcartCase):
                    x=0
                    y+=EcartCase

        #Placement des poissons sur la grille
        pygame.draw.rect(Display, Color[1],((ListePoisson[x].x) + 2, (ListePoisson[x].y) + 2, tailleCase - 4, tailleCase - 4))
        for loop in range (self.NbsPoisson-1):
            pygame.draw.rect(Display,Color[1],((ListePoisson[x].x)+2,(ListePoisson[x].y)+2,tailleCase-4,tailleCase-4))
            text = font.render(str(ListePoisson[x].nombre ),0,(0,0,0))
            Display.blit(text,((ListePoisson[x].x+(tailleCase/2))-15,(ListePoisson[x].y+(tailleCase/2))-15))
            x+=1


    #Resulta: Creation des poisson au depart
    def CréationPoisson(self):
        x, y = 0, 0
        n = 0


        for loop in range(self.NbsPoisson - 1):
            n=random.choice(NombreListe)
            ListePoisson.append(Poisson((x), (y), n))
            print(NombreListe)
            NombreListe.remove(n)
            if len(NombreListe)==1:
                NombreListe.append(NombreListe[0])
            x += EcartCase
            if x == (10 * EcartCase):
                x = 0
                y += EcartCase

                    

#init grille ( taille x, taille y , nombre de poisson)
Terrain = Monde(10,10 ,102)

#placement des poissons dans la grille
Terrain.CréationPoisson()

pygame.mouse.set_cursor(*pygame.cursors.broken_x)

salut=True
while salut:
    Display.fill((0, 0, 0))
    Terrain.CréationMonde()

    for event in pygame.event.get(): # pour chaque évenement donner
        if event.type == pygame.QUIT:
            salut= False
    pygame.display.update()
pygame.quit()
quit()

