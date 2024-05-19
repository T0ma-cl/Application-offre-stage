from entreprise import Entreprise 
from fichier import Fichier
from stage import Stage
from eleve import Eleve

# Initialisation des listes (les lectures de fichier sont commentées)
liste_ent = []
liste_stages = []
liste_elv = []
stage_elv = []
liste_elvint = []

while True:
    choix = input("""---Menu---
                Qui êtes-vous ? 
                1. Entreprise 
                2. Elève
                3. Quitter le site
Votre choix: """)
    
    if choix == "1":
        while True:
            choix_ent = input("""Connectez-vous !
                        1. Créer un compte
                        2. S'identifier
                        3. Quitter
Votre choix: """)
            if choix_ent == "1":
                nom = input("Quel est le nom de l'entreprise ?: ")
                adresse = input("Quelle est sa localisation ?: ")
                domaine = input("Dans quel domaine exerce-t-elle ?: ")
                motdepasse = input("Créez un mot de passe: ")
                entreprise = Entreprise(nom, adresse, domaine, motdepasse)
                liste_ent.append(entreprise)
                print("Compte créé avec succès")
            elif choix_ent == "2":
                entreprise_trouvee = None
                nom = input("Quel est le nom de l'entreprise ?: ")
                motdepasse = input("Rentrez votre mot de passe: ")

                for entreprise in liste_ent:
                    if entreprise.n == nom and entreprise.m == motdepasse:
                        entreprise_trouvee = entreprise
                        break

                if entreprise_trouvee:
                    print("Connexion réussie. Bonjour", entreprise.n, "!")
                    
                    while True:
                        choix_act = input("""---Mon entreprise---
                        Que souhaitez-vous faire ?
                        1. Modifier le compte
                        2. Supprimer le compte
                        3. Gérer mes offres
                        4. Déconnexion
Votre choix: """)
                        
                        if choix_act == "1":
                            nv_nom = input("Quel est le nom de votre nouvelle entreprise ?: ")
                            nv_adresse = input("Quelle est sa nouvelle localisation ?: ")
                            nv_domaine = input("Dans quel domaine exerce-t-elle ?: ")
                            nv_motdepasse = input("Créez un nouveau mot de passe: ")
                            entreprise_trouvee.n = nv_nom
                            entreprise_trouvee.a = nv_adresse
                            entreprise_trouvee.d = nv_domaine
                            entreprise_trouvee.m = nv_motdepasse
                            print("Informations modifiées avec succès")
                        elif choix_act == "2":
                            liste_ent.remove(entreprise_trouvee)
                            print("L'entreprise a été supprimée")
                            break
                        elif choix_act == "3":
                            while True:
                                choix_cons = input("""---Mes offres---
                                1. Créer une offre
                                2. Modifier une offre
                                3. Supprimer une offre
                                4. Afficher mes offres
                                5. Revenir au menu précédent
Votre choix: """)
                                
                                if choix_cons == "1":
                                    entreprise = input("Quel est le nom de l'entreprise ?: ")
                                    duree = input("Combien de temps durera le stage ?: ")
                                    remuneration = input("Indiquez la rémunération: ")
                                    places = input("Indiquez le nombre de places disponibles: ")
                                    reference = input("Créez une référence à l'offre: ")
                                    stage = Stage(duree, entreprise, remuneration, places, reference)
                                    liste_stages.append(stage)
                                    print("Offre créée avec succès")
                                elif choix_cons == "2":
                                    reference = input("Quelle est la référence de l'offre ?")
                                    trouve = False
                                    for stage in liste_stages:
                                        if stage.ref == reference:
                                            trouve = True
                                            duree = input("Entrez la nouvelle durée du stage: ")
                                            remuneration = input("Entrez la nouvelle rémunération: ")
                                            places = input("Entrez le nouveau nombre de places disponibles: ")
                                            stage.d = duree
                                            stage.r = remuneration
                                            stage.p = places
                                            print("L'offre a été modifiée avec succès")
                                            break
                                    if not trouve:
                                        print("L'offre avec la référence donnée n'a pas été trouvée.")
                                elif choix_cons == "3":
                                    reference = input("Quelle est la référence de l'offre à supprimer ?: ")
                                    trouve = False
                                    for stage in liste_stages:
                                        if stage.ref == reference:
                                            trouve = True
                                            liste_stages.remove(stage)
                                            print("L'offre a été supprimée avec succès")
                                            break
                                    if not trouve:
                                        print("L'offre avec la référence donnée n'a pas été trouvée.")
                                elif choix_cons == "4":
                                    for stage in liste_stages:
                                        stage.afficher()
                                elif choix_cons == "5":
                                    break
                                else:
                                    print("Choix invalide. Veuillez entrer un choix valide (1/2/3/4/5).")
                        elif choix_act == "4":
                            print("Déconnexion réussie!")
                            break
                        else:
                            print("Choix invalide. Veuillez entrer un choix valide (1/2/3/4).")
                else:
                    print("Nom ou mot de passe incorrect. Veuillez vérifier vos informations.")
            elif choix_ent == "3":
                break
            else:
                print("Choix invalide. Veuillez entrer un choix valide (1/2/3).")
    
    elif choix == "2":
        while True:
            choix_elv = input("""Connectez-vous !
                            1. Créer un compte
                            2. S'identifier
                            3. Quitter
Votre choix: """)
            
            if choix_elv == "1":
                nom = input(" - Entrer le nom : ")
                prenom = input(" - Entrer le prénom : ")
                age = input(" - Entrer l'âge : ")
                mdp = input(" - Entrer votre mot de passe : ")
                eleve = Eleve(nom, prenom, age, mdp)
                liste_elv.append(eleve)
                print("Compte créé avec succès")
            
            elif choix_elv == "2":
                nom = input("Quel est le nom de l'étudiant ?: ")
                motdepasse = input("Rentrez votre mot de passe: ")
                trouve = False
                for eleve in liste_elv:
                    if eleve.nom == nom and eleve.mdp == motdepasse:
                        trouve = True
                        elv_connecte = eleve
                        print("Connexion réussie")
                if not trouve:
                        print("Ce compte n'existe pas, veuillez vérifier vos informations svp.")
                if trouve :
                        while True:
                            choix_connect = input("""---Mon Espace Elève---
                            Que souhaitez-vous faire ?
                            1. Modifier le compte
                            2. Supprimer le compte
                            3. Consulter les offres disponibles
                            4. Mes candidatures
                            5. Déconnexion
Votre choix: """)
                            
                            if choix_connect == "1":
                                nv_nom = input(" - Saisissez un nouveau nom : ")
                                nv_prenom = input(" - Entrer le nouveau prénom : ")
                                nv_age = input(" - Entrer le nouvel âge : ")
                                nv_mdp = input(" - Entrez votre nouveau mot de passe : ")
                                eleve.nom = nv_nom
                                eleve.prenom = nv_prenom
                                eleve.age = nv_age
                                eleve.mdp = nv_mdp
                                print("Les informations ont été modifiées")
                            
                            elif choix_connect == "2":
                                liste_elv.remove(eleve)
                                print("Compte supprimé avec succès")
                                break
                            
                            elif choix_connect == "3":
                                if not liste_stages:
                                    print("Aucune offre disponible pour le moment.")
                                else:
                                    for i, stage in enumerate(liste_stages, start=1):
                                        stage.afficher()  # Appel à la méthode afficher pour montrer les détails du stage
                                    x = int(input("Entrez le numéro du stage qui vous intéresse: ")) - 1
                                    if 0 <= x < len(liste_stages):
                                        liste_stages[x].liste_elvint.append(eleve)  # Assure-toi que `eleve` est une instance valide
                                        stage_elv.append(liste_stages[x])
                                        print("Candidature enregistrée")
                                    else:
                                        print("Numéro de stage invalide")
                            
                            elif choix_connect == "4":
                                while True:
                                    choix_cand = input("""--- Mes Candidatures---
                                    Que souhaitez-vous faire ?
                                    1. Supprimer une candidature
                                    2. Suivi de mes candidatures
                                    3. Retourner au menu précédent
Votre choix: """)
                                    
                                    if choix_cand == "1":
                                        if not stage_elv:
                                            print("Aucune candidature à supprimer.")
                                        else:
                                            for i, stage in enumerate(stage_elv, start=1):
                                                print(f"{i}. {stage.titre}")
                                            a = int(input("Entrez le numéro de la candidature que vous souhaitez supprimer: ")) - 1
                                            if 0 <= a < len(stage_elv):
                                                stage_elv[a].liste_elvint.remove(eleve)  # Utilisation de la notation pointée pour accéder à elvint
                                                del stage_elv[a]
                                                print("Candidature supprimée")
                                            else:
                                                print("Numéro de candidature invalide")
                                    
                                    elif choix_cand == "2":
                                        if not stage_elv:
                                            print("Aucune candidature en cours.")
                                        else:
                                            for stage in stage_elv:
                                                stage.afficher()
                                    
                                    elif choix_cand == "3":
                                        break
                                    
                                    else:
                                        print("Choix invalide, veuillez réessayer.")
                            
                            elif choix_connect == "5":
                                print("Déconnexion réussie")
                                break
                            
                            else:
                                print("Choix invalide, veuillez réessayer.")
            
            elif choix_elv == "3":
                break
            
            else:
                print("Choix invalide. Veuillez entrer un choix valide (1/2/3).")
    
    elif choix == "3":
        print("Merci et au revoir !")
        break
    
    else:
        print("Choix invalide. Veuillez entrer un choix valide (1/2/3).")
        
                        
            
            
                                        
                            
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
