import random

NombreListe=[i for i in range(2,102)]
listePoisson = []


class Poisson:
    def __init__(self,x,y, nombre):
        self.x = x
        self.y = y
        self.nombre = nombre


class Cellule:
    def __init__(self,x,y):
        global nombre
        nombre= random.choice(NombreListe)
        self.x=x
        self.y=y
        self.poissons = [Poisson(self.x , self.y,nombre)]
        self.symbole = str(nombre)

    def recupPoisson(self):
        for i in listePoisson:
            if i.x == self.x and i.y == self.y:
                self.poissons.append(i)



    def nbspoisson(self):
        print("Je suis pelle")

class Monde :
    def __init__(self,taille , n):
        self.taille = taille
        self.nbPoissons = n
        global grille, listePoisson
        grille=[]
        k=0
        for i in range(self.taille):
            colonne = []
            for j in range(self.taille):
                colonne.append(Cellule(i,j))
                NombreListe.remove(nombre)
                print(NombreListe)
            grille.append(colonne)

    def creationPoisson(self):
        for i in range(self.nbPoissons):


    def deplacer(self):
        for i in listePoisson:
            i.x += (random.randint(-1, 1)) % 10
            i.y += (random.randint(-1, 1)) % 10


Terrain = Monde(10,100)
Terrain.affichage()

print("_________________\n")





Terrain.affichage()

