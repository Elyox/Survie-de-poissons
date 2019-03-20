import random
from time import sleep
from tabulate import tabulate  # Affichage du tableau


#  ██████ ██       █████  ███████ ███████ ███████ ███████
# ██      ██      ██   ██ ██      ██      ██      ██
# ██      ██      ███████ ███████ ███████ █████   ███████
# ██      ██      ██   ██      ██      ██ ██           ██
#  ██████ ███████ ██   ██ ███████ ███████ ███████ ███████


class Poisson:  # La classe qui definit les Poisson
    def __init__(self, x, y, nombre):
        self.x = x
        self.y = y
        self.nombre = nombre

    # Definit comment comparer les Poissons entre eux
    def __lt__(self, other):  # less than
        return self.nombre < other.nombre

    def __gt__(self, other):  # greater than
        return self.nombre > other.nombre


class Cellule:  # Restes de Marco
    def __init__(self):
        print("Je suis pelle")


# ███    ███  ██████  ███    ██ ██████  ███████
# ████  ████ ██    ██ ████   ██ ██   ██ ██
# ██ ████ ██ ██    ██ ██ ██  ██ ██   ██ █████
# ██  ██  ██ ██    ██ ██  ██ ██ ██   ██ ██
# ██      ██  ██████  ██   ████ ██████  ███████


class Monde:  # la superclasse qui definit le Monde
    def __init__(self, taille):
        self.taille = taille  # Taille d'1 cote, car le Monde est carre
        self.nbPoissons = taille * taille  # nb Poisson = aire du Monde
        self.ListePoisson = []  # Contient les Poisson
        self.nombreMorts = 0  # Compteur de morts
        self.mortsTotaux = []  # Liste les Poisson morts
        self.rencontre = 0
        self.deplacements = 0

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
                self.deplacements += 1

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

                    # Ici on fait combatre chaque poisson entre eux une seule
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
                            self.rencontre += 1
        # Tuer les poissons
        for i in koRound:
            toRemove = next(x for x in self.ListePoisson if x.nombre == i)
            self.ListePoisson.remove(toRemove)
        self.nombreMorts += len(koRound)

        return len(koRound)
    # Renvoie liste des Poisson en vie + total de rencontres et de deplacements

    def renvoi(self, arg=0):
        listeNum = []
        for i in self.ListePoisson:
            listeNum.append(i.nombre)
        if arg == 0:
            return listeNum
        else:
            return listeNum, self.rencontre, self.deplacements


# ███████  ██████  ███    ██  ██████ ████████ ██  ██████  ███    ██ ███████
# ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ ██
# █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ ███████
# ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██      ██
# ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████ ███████


def cls(): print('\n' * 10)


def primeNumber(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def onlyPrimeNumber(liste):
    onlyPrime = 0
    for number in liste:
        if not primeNumber(number):
            onlyPrime += 1
    if onlyPrime > 0:
        return False
    else:
        return True


# ███████ ██   ██ ███████  ██████     ██████   ██████  ██ ███████ ███████  ██████  ███    ██
# ██       ██ ██  ██      ██          ██   ██ ██    ██ ██ ██      ██      ██    ██ ████   ██
# █████     ███   █████   ██          ██████  ██    ██ ██ ███████ ███████ ██    ██ ██ ██  ██
# ██       ██ ██  ██      ██          ██      ██    ██ ██      ██      ██ ██    ██ ██  ██ ██
# ███████ ██   ██ ███████  ██████     ██       ██████  ██ ███████ ███████  ██████  ██   ████

def execPoisson(tailleMonde=5):
    zone = Monde(tailleMonde)
    queNombrePrimaire = False
    rep = 0
    while not queNombrePrimaire:
        rep += 1
        zone.deplacer()
        zone.bataille()
        queNombrePrimaire = onlyPrimeNumber(zone.renvoi())

    poissonsRestants, rencontre, deplacements = zone.renvoi(arg=1)
    return rep, poissonsRestants, rencontre, deplacements


def execPoissonAff(tailleMonde=5, sleepTime=1):
    zone = Monde(tailleMonde)
    nombreCompose = True
    rep = 0
    zone.affichage(0)
    print("DEPART\n_________________\n")
    while nombreCompose:
        sleep(sleepTime)
        cls()
        rep += 1
        print('/\\/\\/\\/\\/\\/\\/\\ TOUR N° :', rep, ' /\\/\\/\\/\\/\\/\\/\\')
        zone.deplacer()
        ko = zone.bataille()
        zone.affichage(ko)
        nombreCompose = not onlyPrimeNumber(zone.renvoi())

    poissonsRestants, rencontre, deplacements = zone.renvoi(arg=1)
    return rep, poissonsRestants, rencontre, deplacements

# **** SCRIPT ****

# testLP = execPoissonAff(10, 100, 0.01)
# print(testLP, '\n', testMT)
