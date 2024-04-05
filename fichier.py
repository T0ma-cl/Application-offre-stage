class Fichier :
    def __init__(self,nom_fichier):
        self.nf=nom_fichier
    def ecrire (self,data):
        with open(self.nf,'w') as f :
            f.write(data)
    def lire (self,data):
        with open(self.nf,'r') as g :
            data=g.read()
            return data

            
        

