from verification_RI_TR import *
import pickle
import copy
from cherche_boucles import cherche_boucles

def post_procc(numero_reseau,affichage=0):
    numero_reseau=str(numero_reseau)
    Reseau_initial,Reseau_final,Noeuds,Parametres=verification_RI_TR(numero_reseau)
    X=Noeuds['X'].values.tolist()
    Y=Noeuds['Y'].values.tolist()
    Num_noeuds=Noeuds['Numero du noeud'].values.tolist()
    path=os.path.dirname(os.path.dirname(__file__))
    fichier=open(os.path.join(path,"Plan","plan_"+numero_reseau+".txt"),"r")
    plan=fichier.read()
    fichier.close()
    Reseau_intermediaire=Reseau_initial
    list_action=[]
    a=0
    F_cout=[0]
    list_action=plan.split("\n")
    cout_NO=12
    cout_ligne_moy=500
    cont_cout=0
    cont_action=0
    Reseau_fusion=[]
    Liste_reseau_intermediaire_valide=[]
    Liste_reseau_intermediaire_non_valide=[]
    indicateur_cas=0
    Bus=[]
    for action in list_action[:len(list_action)-1]:
        cont_action+=1
        b=action.split()
        if b[0] == "(ADD_OPENLINE":
            indicateur_cas=1
            node1=b[1]
            node2=b[2][:len(b[2])-1]
            if int(node1[1:])>int(node2[1:]):
                Line_added=[int(node2[1:]),int(node1[1:])]
            else:
                Line_added=[int(node1[1:]),int(node2[1:])]
            for i in range(Reseau_final.shape[0]):
                if int(Reseau_final.values[i][0])==Line_added[0] and int(Reseau_final.values[i][1])==Line_added[1]:
                    Reseau_intermediaire.loc[Reseau_intermediaire.index[-1]+1] = Reseau_final.values[i]
                    Reseau_intermediaire.iloc[-1,2]=1
            F_cout.append(F_cout[cont_cout]+cout_ligne_moy+cout_NO)

        if b[0] == "(REMOVE_ADD_OPENLINE":
            indicateur_cas=2
            node1=b[1]
            node2=b[2]
            node3=b[3][:len(b[3])-1]
            if int(node1[1:])>int(node2[1:]):
                Line_removed=[int(node2[1:]),int(node1[1:])]
            else:
                Line_removed=[int(node1[1:]),int(node2[1:])]
            if int(node2[1:])>int(node3[1:]):
                Line_added=[int(node3[1:]),int(node2[1:])]
            else:
                Line_added=[int(node2[1:]),int(node3[1:])]
            for i in range(Reseau_intermediaire.shape[0]-2): #erreur possible à ce niveau la de moncde par rapport au -2
                if int(Reseau_intermediaire.values[i][0])==Line_removed[0] and int(Reseau_intermediaire.values[i][1])==Line_removed[1]:
                    Reseau_intermediaire=Reseau_intermediaire.drop(Reseau_intermediaire.index[i])
            for i in range(Reseau_final.shape[0]):
                if int(Reseau_final.values[i][0])==Line_added[0] and int(Reseau_final.values[i][1])==Line_added[1]:
                    Reseau_intermediaire.loc[Reseau_intermediaire.index[-1]+1] = Reseau_final.values[i]
                    Reseau_intermediaire.iloc[-1,2]=1
            F_cout.append(F_cout[cont_cout]+cout_ligne_moy+cout_NO)

        if b[0] == "(CHANGE_SWITCH_CONNECTION":
            indicateur_cas=3
            node1=b[1]
            node2=b[2]
            node3=b[3][:len(b[3])-1]
            if int(node1[1:])>int(node2[1:]):
                Line_closed=[int(node2[1:]),int(node1[1:])]
            else:
                Line_closed=[int(node1[1:]),int(node2[1:])]
            if int(node1[1:])>int(node3[1:]):
                Line_open=[int(node3[1:]),int(node1[1:])]
            else:
                Line_open=[int(node1[1:]),int(node3[1:])]
            for i in range(Reseau_intermediaire.shape[0]):
                

                if int(Reseau_intermediaire.values[i][0])==Line_closed[0] and int(Reseau_intermediaire.values[i][1])==Line_closed[1]:
                    Reseau_intermediaire.iloc[i,2]=0
                if int(Reseau_intermediaire.values[i][0])==Line_open[0] and int(Reseau_intermediaire.values[i][1])==Line_open[1]:
                    
                    Reseau_intermediaire.iloc[i,2]=1
        if b[0] == "(REMOVE_OPENLINE":
            indicateur_cas=4
            node1=b[1]
            node2=b[2][:len(b[2])-1]
            if int(node1[1:])>int(node2[1:]):
                Line_removed=[int(node2[1:]),int(node1[1:])]
            else:
                Line_removed=[int(node1[1:]),int(node2[1:])]
            for i in range(Reseau_intermediaire.shape[0]-1):
                if int(Reseau_intermediaire.values[i][0])==Line_removed[0] and int(Reseau_intermediaire.values[i][1])==Line_removed[1]:
                    Reseau_intermediaire=Reseau_intermediaire.drop(Reseau_intermediaire.index[i])
                    
        if indicateur_cas == 1 or indicateur_cas == 2:
            cont_cout+=1

        #verfication topologique 
        max_num_nodes=max(Num_noeuds)
        M= [[0 for _ in range(max_num_nodes)] for _ in range(max_num_nodes)]
        Mi = [[0 for _ in range(max_num_nodes)] for _ in range(max_num_nodes)]
        for i in range (Reseau_intermediaire.shape[0]):
            a=int(Reseau_intermediaire.values[i][0]-1)
            b=int(Reseau_intermediaire.values[i][1]-1)
            M[a][b]+=1
            M[b][a]+=1
            if int(Reseau_intermediaire.values[i][2])==0:
                Mi[a][b]=1
                Mi[b][a]=1
        source_node=[]
        for i in range (Noeuds.shape[0]):
                if Noeuds.values[i][1] == "Primary substation":
                    source_node.append(Noeuds.values[i][0])
        pts_isoles=network_topology_validator(Mi,max_num_nodes,source_node)
        compteur_ok_i=1 #compteur de point isolé si il y a des point isolés:1 ou sinon: 0 
        if pts_isoles ==[]:
            compteur_ok_i=0
        else:
            print("pts isoles:",pts_isoles)
            if indicateur_cas == 1 or indicateur_cas == 2:

                # On ferme la ligne et on refait un test de validation de topo.
                Mi[int(Reseau_intermediaire.values[-1][0]) - 1][int(Reseau_intermediaire.values[-1][1]) - 1] = 1
                Mi[int(Reseau_intermediaire.values[-1][1]) - 1][int(Reseau_intermediaire.values[-1][0]) - 1] = 1

                pts_isoles_i = network_topology_validator(Mi, max_num_nodes, source_node)
                
                if pts_isoles_i == []:  # si pas de points isolés alors on laisse la ligne fermée
                    compteur_ok_i += 1
                    Reseau_intermediaire.values[-1][2] = 0
                    Candidats = cherche_boucles(Reseau_intermediaire, max_num_nodes, source_node, Reseau_final)
                    print("Il n'y a plus de point isolé, il faut vérifier la présence de cycle et ouvrir une ligne le cas échéant pour que le réseau reste radial")
                    print(sum([1 for row in Reseau_intermediaire if row[2] == 0]) > len(Bus) - 2)
                    if sum([1 for row in Reseau_intermediaire if row[2] == 0]) > len(Bus) - 2:  # présence de cycle dans le réseau?
                        print("l'ajout de la ligne fermée a créé un cycle et il faut ouvrir une ligne")
                        Candidats = cherche_boucles(Reseau_intermediaire, max_num_nodes, source_node, Reseau_final)
                        print(Candidats)
                        Candidats_1 = [c for c in Candidats if c[1] == 3]  # On cherche les lignes qui ne feront pas partis du réseau final et on en ouvre une
                        Selection = Candidats_1[0][0]
                        Reseau_intermediaire.iloc[int(Selection),2] = 1

                else:
                    print("Topologie non valide -> points isolés donc on rouvre la ligne")  # On ne fait pas le loadflow et on passe directement au réseau
                    Mi[int(Reseau_intermediaire.values[-1][0]) - 1][int(Reseau_intermediaire.values[-1][1]) - 1] = 0
                    Mi[int(Reseau_intermediaire.values[-1][1]) - 1][int(Reseau_intermediaire.values[-1][0]) - 1] = 0

        compteur_ok=0 #compteur condition n-1
        for node in source_node:
            M_test=[row[:] for row in M]
            noeud_remove=setdiff(source_node,[node])
            for x in noeud_remove:
                for j in range(max_num_nodes):
                    M_test[x-1][j]+=-1
                    M_test[j][x-1]+=-1
            pts_isoles=network_topology_validator(M_test,max_num_nodes,source_node)
            if pts_isoles==[]:
                compteur_ok+=1
        if compteur_ok == len(source_node):
            print("Reseau intermediaire n°"+str(cont_action)+": condition n-1 respecté pour tout les noeuds sources")
        else:
            print("Reseau intermediaire n°"+str(cont_action)+": n-1 non respecté")

    #calcul du load flow pour le reseau intermediaire
        cas1,cas2=0,0
        if compteur_ok == len(source_node) and compteur_ok_i==0:
            
            network=network_for_lf(Num_noeuds,Noeuds,Reseau_intermediaire,Parametres)
            Bus=network["bus"]
            I,V=lf(network)
            if len(I) !=0:
                for k in range (Reseau_intermediaire.shape[0]):
                    
                    if abs(I[k])>Reseau_intermediaire.values[k][5]:
                        print("contraintes courant pour le reseau n°"+str(cont_action)+": il faut renforcer la ligne "+str(Reseau_intermediaire.values[k][0])+" "+str(Reseau_intermediaire.values[k][1]))
                        cas1=1
                for v in V:
                    if abs(v)>1.05 or abs(v)<0.95:
                        print("contraintes tension pour le reseau n°"+str(cont_action))
                        cas2=1
            if cas1 ==0 and cas2==0:
                print("pas de containtes électrique")
        if cas1==0 and cas2==0 and compteur_ok==len(source_node) and compteur_ok_i==0:
            Reseau_fusion.append(cont_action)
            Liste_reseau_intermediaire_valide.append(copy.deepcopy(Reseau_intermediaire))



    #creation des listes d'actions présentes dans le plan permettant d'être toujours valdie 
    Liste_action_groupe=[]
    indice=0
    for num_reseau_fusion in Reseau_fusion:
        action_groupe=""
        portion_fusion=list_action[indice:num_reseau_fusion]
        for action in portion_fusion:
            action_groupe=action_groupe+action
        Liste_action_groupe.append(action_groupe)
        indice=num_reseau_fusion

    print("le cout total de l'opération est",F_cout[-1])
    with open(os.path.join(path,'Reseaux_intermediaires','Reseau_intermediaire_'+str(numero_reseau)+'.pkl'), 'wb') as f:
        pickle.dump(Liste_reseau_intermediaire_valide, f)

    return(F_cout[-1],Liste_action_groupe,Liste_reseau_intermediaire_valide)