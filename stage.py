class Stage:
    liste_stage:[]
    def __init__(self,durée,entreprise,rémunération,places,référence):
        self.d=durée 
        self.e=entreprise
        self.r=rémunération
        self.p=places
        self.ref=référence
    def afficher(self):
        print("Entreprise:",self.e)
        print("Durée:",self.d)
        print("Rémunération",self.r)
        print("Places disponibles:",self.p)
        print ("Référence:",self.ref)
