import statistics as stat
import Poisson as P

# VARIABLES
compteur, poissonsRestants, rencontre, deplacements = P.execPoisson(10, 5, 0.1)

print('Nombre de tours moyen :', stat.mean(compteur))
# print(poissonsRestants)
print('Renconres moyennes:', stat.mean(rencontre), end='')
print('   ||  Deplacements moyens :', stat.mean(deplacements))
