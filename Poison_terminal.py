import random
from resize import console_resize  # Fonction pour redimentionner le terminal
from time import sleep
from tabulate import tabulate  # Affichage du tableau


# **** VARIABLES ****
global nombre, nombreMorts
NombreListe = [i for i in range(2, 102)]
ListePoisson = []
rep = 0


# **** CLASSES ****
class Poisson:
    def __init__(self, x, y, nombre):
        self.x = x
        self.y = y
        self.nombre = nombre

    def __lt__(self, other):
        return self.nombre < other.nombre

    def __gt__(self, other):
        return self.nombre > other.nombre


class Cellule:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.poissons = []

    def recupPoisson(self):
        for i in ListePoisson:
            if i.x == self.x and i.y == self.y:
                self.poissons.append(i)

    def nbspoisson(self):
        print("Je suis pelle")


class Monde:
    def __init__(self, taille, n):
        self.taille = taille
        self.nbPoissons = n
        self.nombreMorts = 0
        self.mortsTotaux = []
        global grille
        grille = []
        for i in range(self.taille):
            colonne = []
            for j in range(self.taille):
                colonne.append(Cellule(i, j))
            grille.append(colonne)

        # Creation des poissons
        for a in range(self.taille):
            for b in range(self.taille):
                nombre = random.choice(NombreListe)
                ListePoisson.append(Poisson(a, b, nombre))
                NombreListe.remove(nombre)

    def deplacer(self):
        for i in ListePoisson:
            # print('1 : ', i.x, i.y)
            i.x = (random.randint(-1, 1) + i.x) % 10
            i.y = (random.randint(-1, 1) + i.y) % 10
            # print('2 : ', i.x, i.y)

    def affichage(self):
        tableauMonde = []
        # Pour chaque Colone
        for i in range(self.taille):
            listCol = []
            # Pour chaque Case
            for j in range(self.taille):
                placeContainer = ''
                listPoissCase = []
                for p in ListePoisson:
                    if p.x == j and p.y == i:
                        listPoissCase.append(p.nombre)
                if listPoissCase == []:
                    placeContainer += '_'
                else:
                    listPoissCase = sorted(listPoissCase)
                    for chfr in listPoissCase:
                        if chfr == listPoissCase[-1]:
                            placeContainer += str(chfr)
                        else:
                            placeContainer += str(chfr) + ', '
                listCol.append(placeContainer)
            tableauMonde.append(listCol)

        print(tabulate(tableauMonde, tablefmt='fancy_grid', numalign='left'))
        print('Morts : ', self.nombreMorts)

    def bataille(self):
        ko = []
        for i in range(self.taille):
            for j in range(self.taille):
                listTemp = []
                for p in ListePoisson:
                    if p.x == j and p.y == i:
                        listTemp.append(p.nombre)
                if not(listTemp == []) and len(listTemp) > 1:
                    listTemp = sorted(listTemp)
                    koTemp = []

                    for divPos, div in enumerate(listTemp[:-1]):
                        for m in listTemp[divPos+1:]:
                            if m % div == 0 and not(m in ko):
                                koTemp.append(m)
                                ko.append(m)
                                self.mortsTotaux.append(m)
        print('Ko ce tour :', len(ko), '||', ko, '\n')

        # Tuer les poissons
        for i in ko:
            ListePoisson.remove(next(x for x in ListePoisson if x.nombre == i))
        self.nombreMorts += len(ko)


# **** FONCTIONS ****
def cls(): print('\n' * 30)


# **** CODE ****
console_resize(150)

Terrain = Monde(10, 100)
Terrain.affichage()

print("_________________\n")
# sleep(1)
input('press enter to start')

while rep < 5:
    sleep(0.1)
    cls()
    sleep(0.1)
    rep += 1
    print('/\\/\\/\\/\\/\\/\\/\\/ TOUR N° :', rep, ' /\\/\\/\\/\\/\\/\\/\\/')
    Terrain.deplacer()
    Terrain.bataille()
    Terrain.affichage()
    sleep(1)

print('Liste morts : ', Terrain.mortsTotaux, '\nNombre de tours : ', rep, '\n')

input('press enter to exit\n')
