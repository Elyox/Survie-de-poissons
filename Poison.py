import random



class Poisson:
    def __init__(self,x,y, nombre):
        self.x = x
        self.y = y
        self.nombre = nombre
           
        
        
class Monde:
    def __init__(self ,longueur ,Largeur,NbsPoisson):
        self.longueur = longueur
        self.Largeur = Largeur
        self.NbsPoisson = NbsPoisson
        
    def CreationMonde(self):
        global grille
        grille=[]
        for j in range(self.Largeur):
            Colonne = ["" for i in range(self.longueur)]
            grille.append(Colonne)

            
    
    def CreationPoisson (self):
        global listepoison
        for loop in range(self.NbsPoisson):
            x=random.randint(0,14)
            y=random.randint(0,14)
            n=0
            grille[y][x] = "P"
            n+=1
            
    
            

    def AfficherMonde(self):
        n=0
        for loop in range(self.Largeur):
            print(grille[n])
            n+=1
        for loop in range(98):
            x=poison[n][1]
            y=listepoisso




Espace = Monde(15,15,98)
Espace.CreationMonde()
Espace.CreationPoisson()
Espace.AfficherMonde()

print(Espace.NbsPoisson)
    
    
    
        
        
        




