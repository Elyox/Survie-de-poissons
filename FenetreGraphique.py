import random
import pygame
from pygame.locals import *


Size=Widght,height =630 , 630
Blanc= 250,250,250
Bleu=10,50,255

global ListePoisson
ListePoisson=[]


Color=[Blanc, Bleu]


# initialisation fenetre



pygame.init()



font=pygame.font.Font(None, 30)

Display = pygame.display.set_mode((Size))
pygame.display.set_caption("poisson")


class Poisson:
    def __init__(self,x,y, nombre):
        self.x = x
        self.y = y
        self.nombre = nombre

class Monde:
    def __init__(self ,longueur ,Largeur,NbsPoisson):
        self.longueur = longueur
        self.Largeur = Largeur
        self.NbsPoisson = NbsPoisson

    def CréationMonde(self):
        x,y=0,0
        for j in range (self.Largeur):
            for i in range(self.longueur):
                pygame.draw.rect(Display,Color[0],(x,y,40,40))
                x+=42
                if x==630:
                    x=0
                    y+=42

    def CréationPoisson(self):
        x=0
        n=2
        for loop in range(self.NbsPoisson):
            ListePoisson.append(Poisson((((random.randint(1,15)*42))-42),((random.randint(1,15)*42)-42),n))
            pygame.draw.rect(Display,Color[1],(ListePoisson[x].x,ListePoisson[x].y,40,40))
            text = font.render(str(ListePoisson[x].nombre ),0,(0,0,0))
            Display.blit(text, (ListePoisson[x].x,ListePoisson[x].y))
            x+=1
            n+=1




Terrain = Monde(15,15 ,98)


salut=True
while salut:
    Terrain.CréationMonde()
    Terrain.CréationPoisson()       
    for event in pygame.event.get(): # pour chaque evenement donner 
        if event.type == pygame.QUIT:
            salut= False
        pygame.display.update()
pygame.quit()
quit()
