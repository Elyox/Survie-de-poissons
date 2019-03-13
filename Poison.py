import random

NombreListe=[i for i in range(2,102)]
ListePoisson=[]
global nombre


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

        self.poissons = [1]


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
    def CreationPoisson(self):
        for a in range (self.taille):
            for b in range (self.taille):
                nombre = random.choice(NombreListe)
                ListePoisson.append(Poisson(a,b,nombre))
                NombreListe.remove(nombre)


    def Deplacer(self):
        print("je me deplace")


print("_________________\n")
    def affichage(self):
        x=0
        for i in range(self.taille):
            for j in range(self.taille):
                print(ListePoisson[x].nombre , ",", end="")
                x+=1
            print("")


Terrain = Monde(10,100)
Terrain.CreationPoisson()
Terrain.affichage()

print("_________________")


Terrain.affichage()

