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
        self.x=x
        self.y=y
        self.poissons = []

    def recupPoisson(self):
        for i in ListePoisson:
            if i.x == self.x and i.y == self.y:
                self.poissons.append(i)


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

    def deplacer(self):
        for i in ListePoisson:
            print('1 : ', i.x, i.y)
            i.x = (random.randint(-1, 1) + i.x) % 10
            i.y = (random.randint(-1, 1) + i.y) % 10
            print('2 : ', i.x, i.y)

    def CreationPoisson(self):
        for a in range (self.taille):
            for b in range (self.taille):
                nombre = random.choice(NombreListe)
                ListePoisson.append(Poisson(a,b,nombre))
                NombreListe.remove(nombre)

    def affichage(self):
        for i in range(self.taille):
            for j in range(self.taille):
                listAff =  []
                for p in ListePoisson:
                    if p.x == j and p.y == i:
                        listAff.append(p.nombre)
                if listAff == []:
                    print('_ ,', end='')
                else:
                    print(listAff, ' ,', end='')
            print('')


Terrain = Monde(10,100)
Terrain.CreationPoisson()
Terrain.affichage()

print("_________________\n")

Terrain.deplacer()

Terrain.affichage()

