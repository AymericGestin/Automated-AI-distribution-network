import pandas as pd
import os
from Trace_reseau import * 
from network_topology_validator import *
from network_topology_validator2 import *

def setdiff(a, b):
    return list(set(a) - set(b))

def verification_RI_TR(Num_reseau):
    path=os.path.dirname(os.path.dirname(__file__))
    #lecture des tableau d'entree
    Noeuds = pd.read_csv(os.path.join(path,"CSV_Problem","point_Reseau_"+Num_reseau+".csv"),sep=";")
    Reseau_initial = pd.read_csv(os.path.join(path,"CSV_Problem","RI_Reseau_"+Num_reseau+".csv"),sep=";")
    Reseau_final = pd.read_csv(os.path.join(path,"CSV_Problem","TR_Reseau_"+Num_reseau+".csv"),sep=";")
    Parametres = pd.read_csv(os.path.join(path,"CSV_Problem","Parametre_Reseau_"+Num_reseau+".csv"),sep=";")
    Voltage_ref_transfo=Parametres.values[0][1]
    Sbase=Parametres.values[1][1]
    Ubase=Parametres.values[2][1]
    for i in range(Reseau_initial.shape[0]):
        if int(Reseau_initial.values[i][0]) > int(Reseau_initial.values[i][1]):
            a,b=Reseau_initial.values[i][0],Reseau_initial.values[i][1]
            Reseau_initial.at[i,"Noeud depart"],Reseau_initial.at[i,"Noeud arrivee"]=b,a
    for i in range(Reseau_final.shape[0]):
        if int(Reseau_final.values[i][0]) > int(Reseau_final.values[i][1]):
            a,b=Reseau_final.values[i][0],Reseau_final.values[i][1]
            Reseau_final.at[i,"Noeud depart"],Reseau_final.at[i,"Noeud arrivee"]=b,a
    X=Noeuds['X'].values.tolist()
    Y=Noeuds['Y'].values.tolist()
    Num_noeuds=Noeuds['Numero du noeud'].values.tolist()
    # trace_reseau(X,Y,Num_noeuds,Reseau_initial)
    # trace_reseau(X,Y,Num_noeuds,Reseau_final)

    #Topology Validator reseau initial
    max_num_nodes=max(Num_noeuds)
    M= [[0 for _ in range(max_num_nodes)] for _ in range(max_num_nodes)]
    Mi = [[0 for _ in range(max_num_nodes)] for _ in range(max_num_nodes)]
    for i in range (Reseau_initial.shape[0]):
        a=int(Reseau_initial.values[i][0]-1)
        b=int(Reseau_initial.values[i][1]-1)
        M[a][b]=1
        M[b][a]=1
        if int(Reseau_initial.values[i][2])==0:
            Mi[a][b]=1
            Mi[b][a]=1
    source_node=[]
    for i in range (Noeuds.shape[0]):
            if Noeuds.values[i][1] == "Primary substation":
                source_node.append(Noeuds.values[i][0])
    pts_isoles=network_topology_validator2(Mi,max_num_nodes,source_node)
    compteur_ok=0
    for node in source_node:
        M_test=[row[:] for row in M]
        noeud_remove=setdiff(source_node,[node])
        for x in noeud_remove:
            for j in range(max_num_nodes):
                M_test[x-1][j]=0
                M_test[j][x-1]=0
        pts_isoles=network_topology_validator2(M_test,max_num_nodes,source_node)
        if pts_isoles==[]:
            compteur_ok+=1
    if compteur_ok == len(source_node):
        print("RI: condition n-1 respecté pour tout les noeuds sources")
    else:
        print("RI: n-1 non respecté")
    #Topology Validator reseau final
    max_num_nodes=max(Num_noeuds)
    M= [[0 for _ in range(max_num_nodes)] for _ in range(max_num_nodes)]
    Mi = [[0 for _ in range(max_num_nodes)] for _ in range(max_num_nodes)]
    for i in range (Reseau_final.shape[0]):
        a=int(Reseau_final.values[i][0]-1)
        b=int(Reseau_final.values[i][1]-1)
        M[a][b]=1
        M[b][a]=1
        if int(Reseau_final.values[i][2])==0:
            Mi[a][b]=1
            Mi[b][a]=1
    source_node=[]
    for i in range (Noeuds.shape[0]):
            if Noeuds.values[i][1] == "Primary substation":
                source_node.append(Noeuds.values[i][0])
    pts_isoles=network_topology_validator2(Mi,max_num_nodes,source_node)
    compteur_ok=0
    for node in source_node:
        M_test=[row[:] for row in M]
        noeud_remove=setdiff(source_node,[node])
        for x in noeud_remove:
            for j in range(max_num_nodes):
                M_test[x-1][j]=0
                M_test[j][x-1]=0
        pts_isoles=network_topology_validator2(M_test,max_num_nodes,source_node)
        if pts_isoles==[]:
            compteur_ok+=1
    if compteur_ok == len(source_node):
        print("TR: condition n-1 respecté pour tout les noeuds sources")
    else:
        print("TR:n-1 non respecté")

    return 0
#verification_RI_TR("10")
verification_RI_TR("16")