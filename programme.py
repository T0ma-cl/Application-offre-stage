from entreprise import Entreprise 
from fichier import Fichier
from stage import Stage
from eleve import Eleve

fichier_ent = Fichier("entreprise.dat")
try:
    liste_ent = fichier_ent.lire()
except (EOFError, FileNotFoundError):
    liste_ent = []

fichier_stage = Fichier("stage.dat")
try:
    liste_stages = fichier_stage.lire()
except (EOFError, FileNotFoundError):
    liste_stages = []

fichier_elv = Fichier("eleve.dat")
try:
    liste_elv = fichier_elv.lire()
except (EOFError, FileNotFoundError):
    liste_elv = []

fichier_cand = Fichier("candidature.dat")
try:
    stage_elv = fichier_cand.lire()
except (EOFError, FileNotFoundError):
    stage_elv = []

fichier_int = Fichier("candidats.dat")
try:
    liste_elvint = fichier_int.lire()
except (EOFError, FileNotFoundError):
    liste_elvint = []
    
#C'est le premier menu dans lequel l'utilisateur indique si il souhaite se connecter en tant qu'entreprise ou élève.
while True:
    choix = input("""---Menu---         
                Qui êtes-vous ? 
                1. Entreprise 
                2. Elève
                3. Quitter le site
Votre choix: """)  

    if choix == "1":
        # L'utilisateur continue en tant qu'entreprise 
        while True:
            choix_ent = input("""Connectez-vous !
                        1. Créer un compte
                        2. S'identifier
                        3. Quitter
Votre choix: """)
#Ici on rentre les informations pour créer une entreprise
            if choix_ent == "1":
                nom = input("Quel est le nom de l'entreprise ?: ")
                adresse = input("Quelle est sa localisation ?: ")
                domaine = input("Dans quel domaine exerce-t-elle ?: ")
                motdepasse = input("Créez un mot de passe: ")
                entreprise = Entreprise(nom, adresse, domaine, motdepasse)
                liste_ent.append(entreprise)
                print("Compte créé avec succès")
            #L'utilisateur a déjà un compte et se connecte 
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
#L'utilisateur à maintenant 3 possibibilités
                    while True:
                        choix_act = input("""---Mon entreprise---
                        Que souhaitez-vous faire ?
                        1. Modifier le compte
                        2. Supprimer le compte
                        3. Gérer mes offres
                        4. Déconnexion
Votre choix: """)
                        #L'utilisateur peut modifier son compte 
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
                        #Il peut également supprimer son compte
                        elif choix_act == "2":
                            liste_ent.remove(entreprise_trouvee)
                            print("L'entreprise a été supprimée")
                            break
                        elif choix_act == "3":
#L'utilisateur a choisi de gérer ses offres et a maintenant 4 choix : créer, modifier, supprimer ou afficher les offres 
                            while True:
                                choix_cons = input("""---Mes offres---
                                1. Créer une offre
                                2. Modifier une offre
                                3. Supprimer une offre
                                4. Afficher mes offres
                                5. Revenir au menu précédent
Votre choix: """)
                                #Il crée une offre
                                if choix_cons == "1":
                                    entreprise = input("Quel est le nom de l'entreprise ?: ")
                                    duree = input("Combien de temps durera le stage ?: ")
                                    remuneration = input("Indiquez la rémunération: ")
                                    places = input("Indiquez le nombre de places disponibles: ")
                                    reference = input("Créez une référence à l'offre: ")
                                    stage = Stage(duree, entreprise, remuneration, places, reference)
                                    liste_stages.append(stage)
                                    print("Offre créée avec succès")
                                #Il peut modifier une ou plusieurs offres
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
                                #Il peut supprimer une ou plusieurs offres
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
                                #L'utilisateur peut également consulter les offres qu'il a publié 
                                elif choix_cons == "4":
                                    for i, stage in enumerate(liste_stages, start=1):
                                        print(f"{i}. {stage.e} - {stage.d} - {stage.r} - {stage.p} places - Réf: {stage.ref}")
                                
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
#Cette fois-ci l'utilisateur continue en tant qu'élève    
    elif choix == "2":
        while True:
            choix_elv = input("""Connectez-vous !
                            1. Créer un compte
                            2. S'identifier
                            3. Quitter
Votre choix: """)
            #L'utilisateur veut créer un compte, donc il rentre ses informations
            if choix_elv == "1":
                nom = input(" - Entrer le nom : ")
                prenom = input(" - Entrer le prénom : ")
                age = input(" - Entrer l'âge : ")
                mdp = input(" - Entrer votre mot de passe : ")
                eleve = Eleve(nom, prenom, age, mdp)
                liste_elv.append(eleve)
                print("Compte créé avec succès")
            #L'utilisateur a déjà un compte donc il se connecte
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
                
                if trouve:
                    #Une fois connecté, l'utilisateur a le choix entre modifier ou supprimer son compte, consulter les offres de stage ou consulter ses candidatures 
                    while True:
                        choix_connect = input("""---Mon Espace Elève---
                        Que souhaitez-vous faire ?
                        1. Modifier le compte
                        2. Supprimer le compte
                        3. Consulter les offres disponibles
                        4. Mes candidatures
                        5. Déconnexion
Votre choix: """)
                        #L'utilisateur veut modifier son compte
                        if choix_connect == "1":
                            nv_nom = input(" - Saisissez un nouveau nom : ")
                            nv_prenom = input(" - Entrer le nouveau prénom : ")
                            nv_age = input(" - Entrer le nouvel âge : ")
                            nv_mdp = input(" - Entrez votre nouveau mot de passe : ")
                            elv_connecte.nom = nv_nom
                            elv_connecte.prenom = nv_prenom
                            elv_connecte.age = nv_age
                            elv_connecte.mdp = nv_mdp
                            print("Les informations ont été modifiées")
                        #L'utilisateur veut supprimer son compte 
                        elif choix_connect == "2":
                            liste_elv.remove(elv_connecte)
                            print("Compte supprimé avec succès")
                            break
                        #L'utilisateur veut consulter les offres de stage 
                        elif choix_connect == "3":
                            if not liste_stages:
                                print("Aucune offre disponible pour le moment.")
                            else:
                                for i, stage in enumerate(liste_stages, start=1):
                                    print(f"{i}. {stage.e} - {stage.d} - {stage.r} - {stage.p} places - Réf: {stage.ref}")  # Appel à la méthode afficher pour montrer les détails du stage
                                x = int(input("Entrez le numéro du stage qui vous intéresse: ")) - 1
                                if 0 <= x < len(liste_stages):
                                    liste_stages[x].liste_elvint.append(elv_connecte)  # Assure-toi que `eleve` est une instance valide
                                    stage_elv.append(liste_stages[x])
                                    print("Candidature enregistrée")
                                else:
                                    print("Numéro de stage invalide")
                        #L'utilisateur consulter les offes auxquels il a candidaté 
                        elif choix_connect == "4":
                            while True:
                                choix_cand = input("""--- Mes Candidatures---
                                Que souhaitez-vous faire ?
                                1. Supprimer une candidature
                                2. Suivi de mes candidatures
                                3. Retourner au menu précédent
Votre choix: """)
                                #Il peut supprimer une ou plusieurs candidatures 
                                if choix_cand == "1":
                                    if not stage_elv:
                                        print("Aucune candidature à supprimer.")
                                    else:
                                        for i, stage in enumerate(stage_elv, start=1):
                                            print(f"{i}. {stage.e} - {stage.d} - {stage.r} - {stage.p} places - Réf: {stage.ref}")
                                        a = int(input("Entrez le numéro de la candidature que vous souhaitez supprimer: ")) - 1
                                        if 0 <= a < len(stage_elv):
                                            stage_elv[a].liste_elvint.remove(elv_connecte)  # Utilisation de la notation pointée pour accéder à liste_elvint
                                            del stage_elv[a]
                                            print("Candidature supprimée")
                                        else:
                                            print("Numéro de candidature invalide")
                                #Il peut consulter ses candidatures 
                                elif choix_cand == "2":
                                    if not stage_elv:
                                        print("Aucune candidature en cours.")
                                    else:
                                        for i, stage in enumerate(stage_elv, start=1):
                                            print(f"{i}. {stage.e} - {stage.d} - {stage.r} - {stage.p} places - Réf: {stage.ref}")
                                
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
    #L'utilisateur quitte le site 
    elif choix == "3":
        print("Merci et au revoir !")
        break
    
    else:
        print("Choix invalide. Veuillez entrer un choix valide (1/2/3).")
        
fichier_ent.ecrire(liste_ent)
fichier_elv.ecrire(liste_elv) 
fichier_stage.ecrire(liste_stages)
fichier_cand.ecrire(stage_elv)
fichier_int.ecrire(liste_elvint)
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
