import statistics as stat
import Poisson as P

# VARIABLES
nbRep = 10
taille = 2
nbPoissons = 10

compteur, poissonsRestants, rencontre, deplacements = P.execPoissonAff(
    nbRep, taille, nbPoissons, 0.05)

print('Nombre de tours moyen :', stat.mean(compteur))
# print(poissonsRestants)
print('Renconres moyennes:', stat.mean(rencontre), end='')
print('   ||  Deplacements moyens :', stat.mean(deplacements))


with open('statistcs.txt', 'a') as f:
    f.write('/\\/\\/\\/\\ STATISTICS /\\/\\/\\/\\/\\' + '\n')
    f.write('Nombre de poissons : ' + str(taille * taille) + '\n')
    f.write('Nombre de repetitions : ' + str(nbRep) + '\n\n')
    f.write('Moyenne de rencontres : ' + str(stat.mean(rencontre)) + '\n')
    f.write('Moyenne de deplacements : ' + str(stat.mean(deplacements)) + '\n')

    f.write('\n\n\n\n\n')
