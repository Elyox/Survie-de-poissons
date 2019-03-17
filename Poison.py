import random
from time import sleep
from tabulate import tabulate


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
        header = [
            '//',
            '\033[32m0\033[0m',
            '\033[32m1\033[0m',
            '\033[32m2\033[0m',
            '\033[32m3\033[0m',
            '\033[32m4\033[0m',
            '\033[32m5\033[0m',
            '\033[32m6\033[0m',
            '\033[32m7\033[0m',
            '\033[32m8\033[0m',
            '\033[32m9\033[0m'
        ]
        # Pour chaque Colone
        for i in range(self.taille):
            listCol = ['\033[32m'+str(i)+'\033[0m']
            # Pour chaque Case
            for j in range(self.taille):
                placeContainer = ''
                listPoissCase = []
                for p in ListePoisson:
                    if p.x == j and p.y == i:
                        listPoissCase.append(p.nombre)
                if listPoissCase == []:
                    placeContainer += '\033[35m_\033[0m'
                else:
                    listPoissCase = sorted(listPoissCase)
                    for chfr in listPoissCase:
                        if chfr == listPoissCase[-1]:
                            placeContainer += str(chfr)
                        else:
                            placeContainer += str(chfr) + ', '
                listCol.append(placeContainer)
            tableauMonde.append(listCol)

        print(tabulate(tableauMonde, header, tablefmt='grid', numalign='left'))
        print('Morts : ', self.nombreMorts, '\n')

    def bataille(self):
        print('ko :')
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
        print('Total :', len(ko), '||', ko, '\n')

        # Tuer les poissons
        for i in ko:
            ListePoisson.remove(next(x for x in ListePoisson if x.nombre == i))
        self.nombreMorts += len(ko)


# **** FONCTIONS ****
def cls(): print('\n' * 10)


# **** CODE ****
Terrain = Monde(10, 100)
Terrain.affichage()

print("DEPART\n_________________\n")
sleep(1)

while rep < 5:
    cls()
    rep += 1
    print('/\\/\\/\\/\\/\\/\\/\\/ TOUR N° :', rep, ' /\\/\\/\\/\\/\\/\\/\\/')
    Terrain.deplacer()
    Terrain.bataille()
    Terrain.affichage()
    rep += 1
    sleep(3)

print('Liste morts : ', Terrain.mortsTotaux, '\nNombre de tours : ', rep)
