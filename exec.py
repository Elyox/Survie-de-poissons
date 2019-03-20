import Poisson as P

# VARIABLES
compteur, poissonsRestants, rencontre, deplacements = P.execPoissonAff(5, 0.1)

print('Nombre de tours :', compteur)
print(poissonsRestants)
print('Renconres :', rencontre, '   ||  Deplacements :', deplacements)
