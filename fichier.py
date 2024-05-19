import pickle

class Fichier :
    def __init__(self,nom_fichier):
        self.nom_fichier = nom_fichier
   
    def ecrire (self,data):
        fichier = open(self.nom_fichier, "wb")
        pickle.dump(data, fichier)
        fichier.close()
        
    
    def lire (self,data):
        fichier = open(self.nom_fichier, "rb")
        data = pickle.load(fichier)
        fichier.close()
        return data
        
        

