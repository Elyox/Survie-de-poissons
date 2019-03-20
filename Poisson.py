import random
from time import sleep
from tabulate import tabulate  # Affichage du tableau


#  CLASSES

class Poisson:  # La classe qui definit les Poisson
    def __init__(self, x, y, nombre):
        self.x = x
        self.y = y
        self.nombre = nombre
        self.deplacements = 0

    # Definit comment comparer les Poissons entre eux
    def __lt__(self, other):  # less than
        return self.nombre < other.nombre

    def __gt__(self, other):  # greater than
        return self.nombre > other.nombre


class Cellule:  # Restes de Marco
    def __init__(self):
        print("Je suis pelle")


# MONDE

class Monde:  # la superclasse qui definit le Monde
    def __init__(self, taille):
        self.taille = taille  # Taille d'1 cote, car le Monde est carre
        self.nbPoissons = taille * taille  # nb Poisson = aire du Monde
        self.ListePoisson = []  # Contient les Poisson
        self.nombreMorts = 0  # Compteur de morts
        self.mortsTotaux = []  # Liste les Poisson morts
        # Creation des poissons
        # Cree une liste de 2 a self.nbPoissons+2 soit de nbPoissons
        NombreListe = [i for i in range(2, self.nbPoissons+2)]
        for x in range(self.taille):  # Pour chaque ligne
            for y in range(self.taille):  # Pour chaque colone
                # Choisit un nombre au hasard dans NombreListe
                nombre = random.choice(NombreListe)
                # Cree un poisson avec ses coordonnees et un numero unique
                self.ListePoisson.append(Poisson(x, y, nombre))
                # Supprime le nombre attribue au poisson
                NombreListe.remove(nombre)

    def deplacer(self):
        for i in self.ListePoisson:  # Pour chaque Poisson
            # Change x et son y du Poisson
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)
            i.x = (x + i.x) % self.taille
            i.y = (y + i.y) % self.taille
            if x != 0 and y != 0:
                i.deplacements += 1

    def affichage(self, koRound):  # Affichage pour le debogage
        tableauMonde = []  # Tableau pour utiliser la fonction tabulate
        # Pour chaque ligne
        for y in range(self.taille):
            poissonsLigne = []  # Contient les Poissons de la ligne y
            # Pour chaque Case
            for x in range(self.taille):
                placeContainer = ''  # String qui stocke les poissons d'1 case
                listePoissCase = []  # Liste qui stocke les poisson d'1 case
                # Cette methode permet de verifier qu'il y a 1+ Poisson sur la
                # case et de retourner '_' si il n'y en a pas ainsi que de
                # retourner les Poisson sans les '[]' des listes
                for p in self.ListePoisson:  # Pour chaque Poisson
                    if p.x == x and p.y == y:  # Si coord Poisson == coord Case
                        # Ajoute les Poisson de la case
                        listePoissCase.append(p.nombre)
                if listePoissCase == []:  # Si pas de poisson dans la case
                    placeContainer += '\033[35m_\033[0m'  # Met un '_' violet
                else:
                    # Trie Poisson dans l'ordre croissant pour + de lisibilite
                    listePoissCase = sorted(listePoissCase)
                    for poisson in listePoissCase:  # Pour chaque Poisson
                        # Si le Poisson est le dernier
                        if poisson == listePoissCase[-1]:
                            placeContainer += str(poisson)
                        else:  # Sinon ajoute ', ' derriere le Poisson
                            placeContainer += str(poisson) + ', '
                # Ajoute les Poisson a la liste de la ligne
                poissonsLigne.append(placeContainer)
            # Ajoute la ligne dans le tableau
            tableauMonde.append(poissonsLigne)
        # Affiche le tableau
        print(tabulate(tableauMonde, tablefmt='grid'))
        print('Morts du tour : ', koRound, '\n')  # Affiche les Poisson morts

    def bataille(self):  # Gere les conflicts entre les Poisson d'1 meme case
        # print('ko :')  # DEBUG
        koRound = []  # Liste les Poisson ko a la fin du round/bataille
        for y in range(self.taille):
            for x in range(self.taille):
                listePoissCase = []  # Liste qui stocke les poisson d'1 case
                for p in self.ListePoisson:
                    if p.x == x and p.y == y:  # Si coord Poisson == coord Case
                        # Ajoute les Poisson de la case
                        listePoissCase.append(p.nombre)
                # Combat seulement si il y au moins 2 Poisson dans la case
                if len(listePoissCase) > 1:
                    # Trie les Poisson dans l'ordre croissant pour simplifier
                    listePoissCase = sorted(listePoissCase)
                    koCase = []  # liste les ko pour la case actuelle

                    # Ici on fait cmobatre chaque poisson entre eux une seule
                    # fois. Par ex pour 3 Poisson : 1 vs 2 || 1 vs 3 && 2 vs 3
                    # On prend tous les Poisson SAUF le dernier -> '[:-1]'
                    for aPos, a in enumerate(listePoissCase[:-1]):
                        for b in listePoissCase[aPos+1:]:
                            # Si a % b == 0 alors b est divisible par a
                            # On ajoute b aux ko
                            if b in koCase:
                                pass
                            else:
                                if b % a == 0:
                                    koCase.append(b)
                                    koRound.append(b)
                                    self.mortsTotaux.append(b)
        # Tuer les poissons
        for i in koRound:
            toRemove = next(x for x in self.ListePoisson if x.nombre == i)
            self.ListePoisson.remove(toRemove)
        self.nombreMorts += len(koRound)

        return len(koRound)

    def renvoi(self):
        listeNum = []
        for i in self.ListePoisson:
            listeNum.append(i.nombre)
        return listeNum


# FONCTIONS

def cls(): print('\n' * 10)


def primeNumber(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return True
                break
            else:
                return False


def execPoisson(tailleMonde=5, nombreRep=5):
    zone = Monde(tailleMonde)
    rep = 0
    while rep < nombreRep:
        rep += 1
        zone.deplacer()
        zone.bataille()
    return zone.renvoi()


def execPoissonAff(tailleMonde=5, nombreRep=5, sleepTime=1):
    zone = Monde(tailleMonde)
    zone.affichage(0)
    print("DEPART\n_________________\n")
    rep = 0
    while rep < nombreRep:
        sleep(sleepTime)
        cls()
        rep += 1
        print('/\\/\\/\\/\\/\\/\\/\\ TOUR N° :', rep, ' /\\/\\/\\/\\/\\/\\/\\')
        zone.deplacer()
        ko = zone.bataille()
        zone.affichage(ko)

    print('Liste morts : ', zone.mortsTotaux, '\nNombre de tours : ', rep)


# **** SCRIPT ****

testLP = execPoissonAff(3, 100, 0.01)
# print(testLP)
