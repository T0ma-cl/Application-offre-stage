class Eleve:    
    def __init__(self,nom,prenom,age,mdp):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.mdp = mdp
        self.stage_elv=[]
    
    
    def afficher(self):
        print("nom:",self.nom,"prenom:",self.prenom,"age:",self.age,"mdp:",self.mdp)