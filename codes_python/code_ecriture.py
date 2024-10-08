import pandas as pd
import os

#chemin vers le dossier Automated-AI-distribution-network
path=os.path.dirname(os.path.dirname(__file__))
 
#fonction qui écrit un fichier pddl correspondant au problème associé du réseau et pour le domaine domainv8 uniquement
# requiert le numéro du réseau à étudier ainsi que la présence des fichiers csv (Point,Target Réseau, Réseau initial) avec la bonne
# syntaxe dans le dossier CSV_Problem et renvoie le fichier ppdl dans le même dossier 
def ecriture_problem(Num_reseau):
    with open(os.path.join(path,"CSV_Problem","problem_"+str(Num_reseau)+".pddl"), 'w') as f: 
        Points = pd.read_csv(os.path.join(path,"CSV_Problem","point_Reseau_"+str(Num_reseau)+".csv"),sep=";") #lecture des csv
        RI = pd.read_csv(os.path.join(path,"CSV_Problem","RI_Reseau_"+str(Num_reseau)+".csv"),sep=";")
        TR = pd.read_csv(os.path.join(path,"CSV_Problem","TR_Reseau_"+str(Num_reseau)+".csv"),sep=";")
        dico_primary={} #definition des dictionnaires nécessaires
        dico_secondary={}
        dico_ligne_RI={}
        dico_ligne_TR={}
        dico_mutable={}
        f.write("(define (problem disnet"+str(Num_reseau)+"n) (:domain disnet)\n(:objects\n\t") 
        # object et definition dico
        for i in range (Points.shape[0]):
            if Points.values[i][1] == "Primary substation": #déclaration des stations primaires et mis à jour du dico contenant les stations primaires
                f.write("P"+str(int(Points.values[i][0]))+" ")
                dico_primary.update({"P"+str(int(Points.values[i][0])):0})
        f.write("- Primary\n\t")
        for i in range (Points.shape[0]): # même chose pour les stations secondaires
            if Points.values[i][1] == "Secondary substation":
                f.write("S"+str(int(Points.values[i][0]))+" ")
                dico_secondary.update({"S"+str(int(Points.values[i][0])):0})
        f.write("- Secondary\n\t)\n(:init\n")
        
        # is primary
        for x in dico_primary.keys():
            f.write("\t(is-primary "+x+")\n")
        f.write("\t")
        for i in range (RI.shape[0]):
            ouvert=int(RI.values[i][2])
            node_depart=int(RI.values[i][0])
            node_arrive=int(RI.values[i][1])
            #update de 2 dico pour full et available: compte le nombre d'occurence pour chaque noeuds pour savoir ensuite si le noeud est full ou avaiable 
            if ("P"+str(node_depart)) in dico_primary.keys():
                dico_primary["P"+str(node_depart)]=dico_primary["P"+str(node_depart)]+1
            if ("P"+str(node_arrive)) in dico_primary.keys():
                dico_primary["P"+str(node_arrive)]=dico_primary["P"+str(node_arrive)]+1
            if ("S"+str(node_depart)) in dico_secondary.keys():
                dico_secondary["S"+str(node_depart)]=dico_secondary["S"+str(node_depart)]+1
            if ("S"+str(node_arrive)) in dico_secondary.keys():
                dico_secondary["S"+str(node_arrive)]=dico_secondary["S"+str(node_arrive)]+1
            # update le dictionnaire des réseaux initial sous la forme {(Point départ Point arrivée): 1 ou 0,(Point arrivée Point départ):1 ou 0,...}
            # si ligne S1 S2 ouverte on aurait {"S1 S2":1,"S2 S1":1}
            if ("P"+str(node_depart)) in dico_primary.keys():
                dico_ligne_RI.update({"S"+str(node_arrive)+" P"+str(node_depart):ouvert})
                dico_ligne_RI.update({"P"+str(node_depart)+" S"+str(node_arrive):ouvert})
            elif ("P"+str(node_arrive)) in dico_primary.keys():
                dico_ligne_RI.update({"P"+str(node_arrive)+" S"+str(node_depart):ouvert})
                dico_ligne_RI.update({"S"+str(node_depart)+" P"+str(node_arrive):ouvert})
            elif ("S"+str(node_arrive) in dico_secondary.keys() and ("S"+str(node_arrive))) in dico_secondary.keys():
                dico_ligne_RI.update({"S"+str(node_arrive)+" S"+str(node_depart):ouvert})
                dico_ligne_RI.update({"S"+str(node_depart)+" S"+str(node_arrive):ouvert})
            
            # Partie connected closed open feed
            if ("P"+str(node_depart)) in dico_primary.keys():
                f.write("(connected P"+ str(node_depart)+" S"+str(node_arrive)+")")
                f.write("(connected S"+ str(node_arrive)+" P"+str(node_depart)+")")
                f.write("\n\t(feed S"+ str(node_arrive)+" P"+str(node_depart)+")")
                f.write("\n\t")
                if ouvert == 1:
                    f.write("(open_line P"+ str(node_depart)+" S"+str(node_arrive)+")")
                    f.write("(open_line S"+ str(node_arrive)+" P"+str(node_depart)+")")
                else:
                    f.write("(closed P"+ str(node_depart)+" S"+str(node_arrive)+")")
                    f.write("(closed S"+ str(node_arrive)+" P"+str(node_depart)+")")
            elif ("P"+str(node_arrive)) in dico_primary.keys():
                f.write("(connected S"+ str(node_depart)+" P"+str(node_arrive)+")")
                f.write("(connected P"+ str(node_arrive)+" S"+str(node_depart)+")")
                f.write("\n\t(feed P"+ str(node_arrive)+" S"+str(node_depart)+")")
                f.write("\n\t")
                if ouvert == 1:
                    f.write("(open_line S"+ str(node_depart)+" P"+str(node_arrive)+")")
                    f.write("(open_line P"+ str(node_arrive)+" S"+str(node_depart)+")")
                else:
                    f.write("(closed S"+ str(node_depart)+" P"+str(node_arrive)+")")
                    f.write("(closed P"+ str(node_arrive)+" S"+str(node_depart)+")")
            else:
                f.write("(connected S"+ str(node_depart)+" S"+str(node_arrive)+") ")
                f.write("(connected S"+ str(node_arrive)+" S"+str(node_depart)+")")
                f.write("\n\t(feed S"+ str(node_arrive)+" S"+str(node_depart)+")")
                f.write("\n\t")
                if ouvert == 1:
                    f.write("(open_line S"+ str(node_depart)+" S"+str(node_arrive)+") ")
                    f.write("(open_line S"+ str(node_arrive)+" S"+str(node_depart)+")")
                else:
                    f.write("(closed S"+ str(node_depart)+" S"+str(node_arrive)+") ")
                    f.write("(closed S"+ str(node_arrive)+" S"+str(node_depart)+")")
            f.write("\n\t")
        # feed d'un primaire à un primaire (tout les primaires sont considérés comme feed eux même dans ce domaine)
        for i in dico_primary.keys():
            f.write("(feed "+i+" "+i+")\n\t")
                                      
        
        # ecriture full ou available
        for i in dico_primary.items():
            if i[1]==3:
                f.write("(full "+i[0]+")\n\t")
            else:
                f.write("(available "+i[0]+")\n\t")
        for i in dico_secondary.items():
            if i[1]==3:
                f.write("(full "+i[0]+")\n\t")
            else:
                f.write("(available "+i[0]+")\n\t")
         
        
        #update du dictionnaire TR même construction que pour le réseau initiale
        for i in range (TR.shape[0]):
            ouvert=int(TR.values[i][2])
            node_depart=int(TR.values[i][0])
            node_arrive=int(TR.values[i][1])
            if ("P"+str(node_depart)) in dico_primary.keys():
                dico_ligne_TR.update({"S"+str(node_arrive)+" P"+str(node_depart):ouvert})
                dico_ligne_TR.update({"P"+str(node_depart)+" S"+str(node_arrive):ouvert})
            elif ("P"+str(node_arrive)) in dico_primary.keys():
                dico_ligne_TR.update({"P"+str(node_arrive)+" S"+str(node_depart):ouvert})
                dico_ligne_TR.update({"S"+str(node_depart)+" P"+str(node_arrive):ouvert})
            elif ("S"+str(node_arrive) in dico_secondary.keys() and ("S"+str(node_arrive))) in dico_secondary.keys():
                dico_ligne_TR.update({"S"+str(node_arrive)+" S"+str(node_depart):ouvert})
                dico_ligne_TR.update({"S"+str(node_depart)+" S"+str(node_arrive):ouvert})        
        
        
        # ecriture buildable (buildable si une ligne est présente dans le réseau cible mais pas dans celui de départ)
        for i in dico_ligne_TR.keys():
            if i not in dico_ligne_RI.keys():
                f.write("(buildable "+i+")")
                f.write("\n\t")
                dico_mutable.update({i[:i.index(" ")]:0}) # ajout des stations "buildables" dans le dico des mutable
            if i in dico_ligne_RI.keys():
                if dico_ligne_RI[i] != dico_ligne_TR[i]:
                    dico_mutable.update({i[:i.index(" ")]:0}) 
        
        # ecriture mutable (mutable correspond à tout les stations ou a lieu un changement removed/add ou passage d'ouvert à fermé)
        for i in dico_ligne_RI.keys():
            if i not in dico_ligne_TR.keys():
                dico_mutable.update({i[:i.index(" ")]:0}) #ajout des cas de changement ouvert à ferme dans les mutable
        for i in dico_mutable.keys():
            f.write("(mutable "+i+")\n\t")
        f.write(")")
                    
        #partie goal qui contient de nouveau les informations sur connected open closed mais pour le Réseau cible
        f.write("\n(:goal (and")
        for i in range (TR.shape[0]):
            f.write("\n\t")
            ouvert=int(TR.values[i][2])
            node_depart=int(TR.values[i][0])
            node_arrive=int(TR.values[i][1])
            if ("P"+str(node_depart)) in dico_primary.keys():
                f.write("(connected P"+ str(node_depart)+" S"+str(node_arrive)+")")
                f.write("(connected S"+ str(node_arrive)+" P"+str(node_depart)+")")
                f.write("\n\t")
                if ouvert == 1:
                    f.write("(open_line P"+ str(node_depart)+" S"+str(node_arrive)+")")
                    f.write("(open_line S"+ str(node_arrive)+" P"+str(node_depart)+")")
                else:
                    f.write("(closed P"+ str(node_depart)+" S"+str(node_arrive)+")")
                    f.write("(closed S"+ str(node_arrive)+" P"+str(node_depart)+")")
            elif ("P"+str(node_arrive)) in dico_primary.keys():
                f.write("(connected S"+ str(node_depart)+" P"+str(node_arrive)+")")
                f.write("(connected P"+ str(node_arrive)+" S"+str(node_depart)+")")
                f.write("\n\t")
                if ouvert == 1:
                    f.write("(open_line S"+ str(node_depart)+" P"+str(node_arrive)+")")
                    f.write("(open_line P"+ str(node_arrive)+" S"+str(node_depart)+")")
                else:
                    f.write("(closed S"+ str(node_depart)+" P"+str(node_arrive)+")")
                    f.write("(closed P"+ str(node_arrive)+" S"+str(node_depart)+")")
            else:
                f.write("(connected S"+ str(node_depart)+" S"+str(node_arrive)+") ")
                f.write("(connected S"+ str(node_arrive)+" S"+str(node_depart)+")")
                f.write("\n\t")
                if ouvert == 1:
                    f.write("(open_line S"+ str(node_depart)+" S"+str(node_arrive)+") ")
                    f.write("(open_line S"+ str(node_arrive)+" S"+str(node_depart)+")")
                else:
                    f.write("(closed S"+ str(node_depart)+" S"+str(node_arrive)+") ")
                    f.write("(closed S"+ str(node_arrive)+" S"+str(node_depart)+")")
            
            
        # partie remove de goal (fonctionne comme buildable mais dans l'autre sens)
        f.write("\n\t")
        for i in dico_ligne_RI.keys():
            if i not in dico_ligne_TR.keys():
                f.write("(removed "+i+")")
                f.write("\n\t") 
        f.write(")\n)\n)")


