from entreprise import Entreprise 
from fichier import Fichier
from stage import Stage
from eleve import Eleve
choix=input("""---Menu---
            Qui êtes-vous ? 
            1. Entreprsie 
            2. Elève""")
fini=False 
while not fini:

    if choix=="1":
        fichier=Fichier("entreprise.dat")
        liste_ent=fichier.lire()
        choix_ent=input(""" Connectez-vous !
                    1. Créer un compte
                    2. S'identifier""")
        choix_ent= True
        if choix_ent == "1":
                nom=input("Quel est le nom de l'entreprise ?:")
                adresse= input("Quel est sa localisation ?:")
                domaine=input("Dans quel domaie exerce-t-elle ?:")
                motdepasse=input("Créez un mot de passe:")
                entreprise=Entreprise(nom,adresse,domaine,motdepasse)
                liste_ent.append(entreprise)
        if choix_ent == "2":
            nom=input("Quel est le nom de l'entreprise ?:")
            motdepasse=input("Rentrez votre mot de passe:")
            trouve= False
            for entreprise in liste_ent:
                if entreprise.n==nom and entreprise.m==motdepasse:
                    trouve = True
                    entreprise_connect=entreprise
                    choix_connect="""---Mon entreprise---
                    Que souhaitez-vous faire ?
                    1.Modifier le compte
                    2.Supprimer le compte
                    3.Consulter mes offres"""
                
                    choix_connect=True
                    if choix_connect=="1":
                            nom=input("Quel est le nom de l'entreprise ?:")
                            motdepasse=input("Rentrez votre mot de passe:")
                            for entreprise in liste_ent:
                                if entreprise.n==nom and entreprise.m==motdepasse:
                                    nom=input("Quel est le nom de votre nouvelle entreprise ?:")
                                    adresse= input("Quel est sa nouvelle localisation ?:")
                                    domaine=input("Dans quel domaine exerce-t-elle ?:")
                                    motdepasse=input("Créez un nouveau mot de passe:")
                                    entreprise=Entreprise(nom,adresse,domaine,motdepasse)
                                    liste_ent.append(entreprise_connect)
                                    
                            else:
                                print("Nom ou mot de passe incorrect. Veuillez véifier vos informations ")
                    if choix_connect=="2":
                            nom=input("Quel est le nom de l'entreprise ?:")
                            motdepasse=input("Rentrez votre mot de passe:")
                            trouve=False
                            for entreprise in liste_ent:
                                if entreprise.n==nom and entreprise.m==motdepasse:
                                    trouve=True 
                                    liste_ent.remove(entreprise_connect)
                                if trouve:
                                     print("L'entreprise a été supprimée")
                                else:
                                    print("Nom ou mot de passe incorrect. Veuillez véifier vos informations ")
                    if choix_connect=="3":
                        choix_cons="""---Mes offres---
                                    1. Créer une offre
                                    2. Modifier une offre
                                    3.Supprimer une offre
                                    4.Afficher mes offres"""
                        choix_cons=True
                        fichier=Fichier("stage.dat")
                        liste_stage=fichier.lire()
                        if choix_cons=="1":
                                entreprise=input("Quel est le nom de l'entreprise ?:")
                                durée= input("Combien de temps durera le stage ?:")
                                rémunération=input("Indiquez la rémunération:")
                                places=input("Indiquez le nombre de places disponibles:")
                                référence=input("Créez un référence à l'offre:")
                                stage=Stage(durée,entreprise,rémunération,places,référence)
                                liste_stage.append(stage)
                        if choix_cons=="2":
                                référence=input("Créez un référence à l'offre:")
                                for stage in liste_stage:
                                    if stage.ref==référence :
                                        entreprise=input("Quel est le nom de l'entreprise ?:")
                                        durée= input("Cobien de temps durera le stage ?:")
                                        rémunération=input("Indiquez la rémunération:")
                                        places=input("Indiquez le nombre de places disponibles:")
                                        référence=input("Créez un référence à l'offre:")
                                        stage=Stage(durée,entreprise,rémunération,places,référence)
                                        liste_stage.append(stage)
                        if choix_cons=="3":
                                référence=input("Quelle est la référence de l'offre ?:")
                                trouve=False
                                for stage in liste_stage:
                                    if stage.ref==référence:
                                        trouve=True
                                        liste_stage.remove(stage)
                                    if trouve:
                                        print("L'offre a bien été supprimée")
                                    else:
                                        print("L'offre est introuvable. Veuillez vérifier que la référence soit correcte")
                        if choix_cons=="4":
                                for stage in liste_stage:
                                    print(stage)
                                
        else:
            print("Cette entreprise n'existe pas.Veuillez vérifier vos informations")
    if choix=="2":
        fichier=Fichier("eleve.dat")
        liste_elv=fichier.lire()
        liste_elvint=fichier.lire()
        choix_elv=input(""" Connectez-vous !
                    1. Créer un compte
                    2. S'identifier""")
        choix_elv= True
        if choix_elv == "1":
                nom = input(" - Entrer le nom : ")
                prenom = input(" - Entrer le prénom : ")
                age = input (" - Entrer l'age - ")
                mdp = input (" - Entrer votre mot de passe - ")
                eleve = Eleve(nom,prenom,age,mdp)
                liste_elv.append(eleve)
        
        if choix_elv=="2":
            nom=input("Quel est le nom de l'etudiant ?:")
            motdepasse=input("Rentrez votre mot de passe:")
            trouve= False
            for eleve in liste_elv:
                if eleve.nom==nom and eleve.mdp ==motdepasse:
                    trouve = True
                    eleve_connect=eleve
                    choix_connect="""---Mon entreprise---
                    Que souhaitez-vous faire ?
                    1.Modifier le compte
                    2.Supprimer le compte
                    3.Consulter les offres disponibles
                    4.Mes candidatures"""
                    
                    
                    choix_connect=True
                    if choix_connect=="1":
                            nom = input(" - Entrer le nom : ")
                            mdp = input (" - Entrer votre mot de passe - ")
                            trouve = False
                            for eleve in liste_elv:
                                if eleve.nom == nom and eleve.mdp == mdp:
                                    trouve = True
                                    nom = input(" - saississez un nom  - ")
                                    prenom = input(" - Entrer le prénom : ")
                                    age = input (" - Entrer l'age - ")
                                    mdp = input (" - Entrer votre mot de passe - ")
                                    eleve = Eleve(nom,prenom,age,mdp)
                                    liste_elv.append(eleve_connect)
                                    if trouve:
                                        print("Les informations ont ete modifiées")
                            
                            else:
                                print(" Réessayer")
                    
                    if choix_connect=="2":
                           nom = input(" - Entrer le nom : ")
                           prenom = input(" - Entrer le prénom : ")
                           trouve = False
                           for eleve in liste_elv:
                               if eleve.nom == nom and eleve.prenom == prenom:
                                   trouve = True
                                   liste_elv.remove(eleve_connect)
                                
                           if trouve:
                                    print("La personne a été supprimée")
                           else:
                               print("Cette personne n'existe pas, Veuillez réessayer")
                            
                    
                    if choix_connect=="3":
                        i=0
                        for stage in liste_stage:
                            i=i+1
                            print(i)
                            stage.afficher()
                        a=input("entrer le numerode stage qui vous interesse")
                        liste_stage[a].liste_elvint.append(eleve_connect)
            
                    
                    
                    if choix_connect=="4":
                        choix_cand="""----Mes candidatures---
                        1.Supprimer une candidature
                        2.suivi de mes candidature"""
                        
                        if choix_cand=="1":
                            i=0
                            for stage in stage:
                                i=i+1
                                stage_elv.afficher()
                            a=input("entrer le numerode stage que vous voulez supprimez")
                            del(stage_elv[a])
                
                        
                        
                        
                        
                        
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                