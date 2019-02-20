import random


class Poisson:
    def __init__(self,x,y, nombre):
        self.x = x
        self.y = y
        self.nombre = nombre


class Cellule:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.poissons = []
        self.symbole = "P"

    def affichage(self):
        if len(self.poissons)==0:
            self.symbole= "-"
        else :
            self.symbole="P"



    def nbspoisson(self):


        print("Je suis pelle")

class Monde :
    def __init__(self,taille , n):
        self.taille = taille
        self.nbPoissons = n
        global grille
        grille=[]
        k=0
        for i in range(self.taille):
            colonne = []
            for j in range(self.taille):
                colonne.append(Cellule(i,j))
            grille.append(colonne)

    def affichage(self):
        for i in range(self.taille):
            for j in range(self.taille):
                grille[j][i].affichage()
                print(grille[j][i].symbole , ",", end="")
            print("")

Terrain = Monde(10,100)
Terrain.affichage()

print("_________________")

Terrain.affichage()

