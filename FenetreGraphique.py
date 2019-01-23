import random
import pygame
from pygame.locals import *



#----- VARIABLES -----#

Size=Widght,height =800 , 630 #Taille de l'ecran en pixels
tailleCase=40 #Taille d'une case en pixel
EcartCase=tailleCase + 2 #Taille d'une case + pixel entre les case. Permet de determiner le decalage entre la position de 2 cases

#Couleurs
Blanc= 250,250,250
Bleu=10,50,255
Color=[Blanc, Bleu]

#Variables globales
global ListePoisson, rencontre
ListePoisson=[] #Liste des attibuts des poissons
rencontre=[] #Liste





pygame.init() # initialisation fenetre



font=pygame.font.Font(None, 30) # creation police d'ecriture

#parametrage fenetre
Display = pygame.display.set_mode((Size))
pygame.display.set_caption("poisson")

#Class Poisson qui definit les poissons
class Poisson:
    def __init__(self,x,y, nombre):
        self.x = x #Coordonne x du poisson
        self.y = y #Coordonne y du poisson
        self.nombre = nombre #nombre du poisson

    #deplace le poisson aleatoirement
    #@deplacer.setter
    def _set_deplacer(self):
        self.x += random.randint(-1, 1) * EcartCase
        self.y += random.randint(-1, 1) * EcartCase






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
                if x==630:
                    x=0
                    y+=42
        #Placement des poissons sur la grille
        for loop in range (self.NbsPoisson):
            pygame.draw.rect(Display,Color[1],(ListePoisson[x].x,ListePoisson[x].y,40,40))
            text = font.render(str(ListePoisson[x].nombre ),0,(0,0,0))
            Display.blit(text, (ListePoisson[x].x,ListePoisson[x].y))
            x+=1


    #Resulta: Creation des poisson au depart
    def CréationPoisson(self):
        n=2
        ListePoisson.append(Poisson((((random.randint(1,self.longueur)*EcartCase))-EcartCase),((random.randint(1,self.Largeur)*EcartCase)-EcartCase),n))
        for loop in range(self.NbsPoisson-1):
            nbs=0
            ListePoisson.append(Poisson((((random.randint(1,self.longueur)*EcartCase))-EcartCase),((random.randint(1,self.Largeur)*EcartCase)-EcartCase),n))
        
            while(nbs-1!=(len(ListePoisson)-1)):
                if ListePoisson[-1].x == ListePoisson[nbs-1].x and ListePoisson[-1].y == ListePoisson[nbs-1].y:
                    ListePoisson[-1].x =(((random.randint(1,self.longueur)*EcartCase))-EcartCase)
                    ListePoisson[-1].y = (((random.randint(1,self.Largeur)*EcartCase))-EcartCase)
                    nbs=0
                    
                nbs+=1
            n+=1
           


#init grille ( taille x, taille y , nombre de poisson)
Terrain = Monde(15,15 ,102)
#placement des poisson dans la grille
Terrain.CréationPoisson()


exit=True
status=True
while salut:
    Terrain.CréationMonde()

    while status:
        status = False
       
    for event in pygame.event.get(): # pour chaque evenement donner 
        if event.type == pygame.QUIT:
            exit= False
        pygame.display.update()
pygame.quit()
quit()

