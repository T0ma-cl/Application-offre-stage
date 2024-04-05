class Entreprise: 
    def __init__(self,nom,adresse,domaine,motdepasse):
        self.n=nom
        self.a=adresse
        self.d=domaine
        self.m=motdepasse
    
    def afficher (self):
        print("nom:",self.n,"adresse:",self.a,"domaine:",self.d,"mdp:",self.m)
        
        