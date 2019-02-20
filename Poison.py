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
    def __init__(self,cote):
        self.cote = cote
        self.nbPoissons = cote**2
        global grilleCellule, listePoisson
        grilleCellule=[]
        listePoisson =[]
        k=0
        for i in range(self.cote):
            colonneCellule = []
            for j in range(self.cote):
                colonneCellule.append(Cellule(i, j))
                listePoisson.append(Poisson(i, j, k+2))
                print(listePoisson[k].nombre, end=", ")
                k += 1
            grilleCellule.append(colonneCellule)
        print('\n')

    def regulariserPoisson(self):
        for i in listePoisson:
            grilleCellule[i.x][i.y].poissons.append(i.nombre)

    def affichage(self):
        for i in range(self.cote):
            for j in range(self.cote):
                grilleCellule[j][i].affichage()
                print(grilleCellule[j][i].symbole , ",", end="")
            print("")

Terrain = Monde(4)
Terrain.affichage()

print("_________________\n")


Terrain.regulariserPoisson()

Terrain.affichage()

