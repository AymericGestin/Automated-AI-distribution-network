import pandas as pd

#fichier 1,2 et 3: format csv avec séparateur ";" correspondant à chaque feuille excel exporter
#problem: nom du fichier pddl renvoyé 

def ecriture_problem(fichier1,fichier2,fichier3,problem):
    with open(problem, 'w') as f:
        Points = pd.read_csv(fichier1,sep=";")
        RI = pd.read_csv(fichier2,sep=";")
        TR = pd.read_csv(fichier3,sep=";")
        dico_primary={}
        dico_secondary={}
        dico_ligne_RI={}
        dico_ligne_TR={}
        dico_mutable={}
        f.write("(define (problem disnet68n) (:domain disnet)\n(:objects\n\t") 
        # object et definition dico
        for i in range (Points.shape[0]):
            if Points.values[i][1] == "Primary substation":
                f.write("P"+str(int(Points.values[i][0]))+" ")
                dico_primary.update({"P"+str(int(Points.values[i][0])):0})
        f.write("- Primary\n\t")
        for i in range (Points.shape[0]):
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
            
            
            #update dico pour full et available
            if ("P"+str(node_depart)) in dico_primary.keys():
                dico_primary["P"+str(node_depart)]=dico_primary["P"+str(node_depart)]+1
            if ("P"+str(node_arrive)) in dico_primary.keys():
                dico_primary["P"+str(node_arrive)]=dico_primary["P"+str(node_arrive)]+1
            if ("S"+str(node_depart)) in dico_secondary.keys():
                dico_secondary["S"+str(node_depart)]=dico_secondary["S"+str(node_depart)]+1
            if ("S"+str(node_arrive)) in dico_secondary.keys():
                dico_secondary["S"+str(node_arrive)]=dico_secondary["S"+str(node_arrive)]+1
            
            
            if ("P"+str(node_depart)) in dico_primary.keys():
                dico_ligne_RI.update({"S"+str(node_arrive)+" P"+str(node_depart):ouvert})
                dico_ligne_RI.update({"P"+str(node_depart)+" S"+str(node_arrive):ouvert})
            elif ("P"+str(node_arrive)) in dico_primary.keys():
                dico_ligne_RI.update({"P"+str(node_arrive)+" S"+str(node_depart):ouvert})
                dico_ligne_RI.update({"S"+str(node_depart)+" P"+str(node_arrive):ouvert})
            elif ("S"+str(node_arrive) in dico_secondary.keys() and ("S"+str(node_arrive))) in dico_secondary.keys():
                dico_ligne_RI.update({"S"+str(node_arrive)+" S"+str(node_depart):ouvert})
                dico_ligne_RI.update({"S"+str(node_depart)+" S"+str(node_arrive):ouvert})
            
            #connected closed open feed
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
        # feed d'un primaire à un primaire:
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
         
        
        #update du dictionnaire TR
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
        
        
        # ecriture buildable
        for i in dico_ligne_TR.keys():
            if i not in dico_ligne_RI.keys():
                f.write("(buildable "+i+")")
                f.write("\n\t")
                dico_mutable.update({i[:i.index(" ")]:0})
            if i in dico_ligne_RI.keys():
                # if (dico_ligne_RI[i]==1 and dico_ligne_TR[i]==0):
                #     f.write("(buildable "+i+")")
                #     f.write("\n\t")
                if dico_ligne_RI[i] != dico_ligne_TR[i]:
                    dico_mutable.update({i[:i.index(" ")]:0})
        
        # ecriture mutable
        for i in dico_ligne_RI.keys():
            if i not in dico_ligne_TR.keys():
                dico_mutable.update({i[:i.index(" ")]:0})
        for i in dico_mutable.keys():
            f.write("(mutable "+i+")\n\t")
        f.write(")")
                    
        #partie goal
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
            
            
        # partie remove de goal
        f.write("\n\t")
        for i in dico_ligne_RI.keys():
            if i not in dico_ligne_TR.keys():
                f.write("(removed "+i+")")
                f.write("\n\t") 
        f.write(")\n)\n)")
            
ecriture_problem("C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/point_Reseau_68.csv","C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/RI_Reseau_68.csv","C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/TR_Reseau_68.csv","C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/problem_68.pddl")
ecriture_problem("C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/point_Reseau_10.csv","C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/RI_Reseau_10.csv","C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/TR_Reseau_10.csv","C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/problem_10.pddl")
ecriture_problem("C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/point_Reseau_16.csv","C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/RI_Reseau_16.csv","C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/TR_Reseau_16.csv","C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/problem_16.pddl")
ecriture_problem("C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/point_Reseau_6.csv","C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/RI_Reseau_6b.csv","C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/TR_Reseau_6.csv","C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/problem_6b.pddl")