import pandas as pd
Points1 = pd.read_csv("point_Reseau_68.csv",sep=";")
RI = pd.read_csv("RI_Reseau_68.csv",sep=";")
TR = pd.read_csv("TR_Reseau_68.csv",sep=";")

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
            f.write("\t(is-primaray "+x+")\n")
        
        
        f.write("\t")
        for i in range (RI.shape[0]):
            ouvert=int(RI.values[i][2])
            node_depart=int(RI.values[i][0])
            node_arrive=int(RI.values[i][1])
            
            
            #update dico pour full et available
            if ("P"+str(node_depart)) in dico_primary.keys():
                dico_primary["P"+str(node_depart)]=dico_primary["P"+str(node_depart)]+1
                dico_ligne_RI.update({"S"+str(node_arrive)+" P"+str(node_depart):0})
                dico_ligne_RI.update({"P"+str(node_depart)+" S"+str(node_arrive):0})
            if ("P"+str(node_arrive)) in dico_primary.keys():
                dico_primary["P"+str(node_arrive)]=dico_primary["P"+str(node_arrive)]+1
                dico_ligne_RI.update({"P"+str(node_arrive)+" S"+str(node_depart):0})
                dico_ligne_RI.update({"S"+str(node_depart)+" P"+str(node_arrive):0})
            if ("S"+str(node_depart)) in dico_secondary.keys():
                dico_secondary["S"+str(node_depart)]=dico_secondary["S"+str(node_depart)]+1
                dico_ligne_RI.update({"S"+str(node_arrive)+" S"+str(node_depart):0})
                dico_ligne_RI.update({"S"+str(node_depart)+" S"+str(node_arrive):0})
            if ("S"+str(node_arrive)) in dico_secondary.keys():
                dico_secondary["S"+str(node_arrive)]=dico_secondary["S"+str(node_arrive)]+1
                dico_ligne_RI.update({"S"+str(node_arrive)+" S"+str(node_depart):0})
                dico_ligne_RI.update({"S"+str(node_depart)+" S"+str(node_arrive):0})
                
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
            node_depart=int(TR.values[i][0])
            node_arrive=int(TR.values[i][1])
            if ("P"+str(node_depart)) in dico_primary.keys():
                dico_primary["P"+str(node_depart)]=dico_primary["P"+str(node_depart)]+1
                dico_ligne_TR.update({"S"+str(node_arrive)+" P"+str(node_depart):0})
                dico_ligne_TR.update({"P"+str(node_depart)+" S"+str(node_arrive):0})
            if ("P"+str(node_arrive)) in dico_primary.keys():
                dico_primary["P"+str(node_arrive)]=dico_primary["P"+str(node_arrive)]+1
                dico_ligne_TR.update({"P"+str(node_arrive)+" S"+str(node_depart):0})
                dico_ligne_TR.update({"S"+str(node_depart)+" P"+str(node_arrive):0})
            if ("S"+str(node_depart)) in dico_secondary.keys():
                dico_secondary["S"+str(node_depart)]=dico_secondary["S"+str(node_depart)]+1
                dico_ligne_TR.update({"S"+str(node_arrive)+" S"+str(node_depart):0})
                dico_ligne_TR.update({"S"+str(node_depart)+" S"+str(node_arrive):0})
            if ("S"+str(node_arrive)) in dico_secondary.keys():
                dico_secondary["S"+str(node_arrive)]=dico_secondary["S"+str(node_arrive)]+1
                dico_ligne_TR.update({"S"+str(node_arrive)+" S"+str(node_depart):0})
                dico_ligne_TR.update({"S"+str(node_depart)+" S"+str(node_arrive):0})
        
        # ecriture buildable
        for i in dico_ligne_TR.keys():
            if i not in dico_ligne_RI.keys():
                f.write("(Buildable "+i+")")
                f.write("\n\t")
                dico_mutable.update({i[:i.index(" ")]:0})
        # ecriture mutable
        for j in dico_ligne_RI.keys():
            if j not in dico_ligne_TR.keys():
                dico_mutable.update({i[:i.index(" ")]:0})
        for i in dico_mutable.keys():
            f.write("(mutable "+i+")\n\t")
        
                    
        #partie goal
        f.write("\n(:goal (and")
        for i in range (TR.shape[0]):
            f.write("\n\t")
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
        for i in dico_ligne_RI.keys():
            if i not in dico_ligne_TR.keys():
                f.write("(removed "+i+")")
                f.write("\n\t") 
        f.write("\t)\n)\n)")
            
ecriture_problem("point_Reseau_68.csv","RI_Reseau_68.csv","TR_Reseau_68.csv","problem_68.txt")
ecriture_problem("point_Reseau_10.csv","RI_Reseau_10.csv","TR_Reseau_10.csv","problem_10.txt")
ecriture_problem("point_Reseau_16.csv","RI_Reseau_16.csv","TR_Reseau_16.csv","problem_16.txt")