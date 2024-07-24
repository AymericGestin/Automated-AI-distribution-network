import pandas as pd
import os
from Trace_reseau import * 
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

    #Topology Validator
    max_num_nodes=max(Num_noeuds)+1
    M=[[0]*max_num_nodes]*max_num_nodes
    Mi=[[0]*max_num_nodes]*max_num_nodes
    for i in range (Reseau_initial.shape[0]-1):
        a=int(Reseau_initial.values[i][0])
        b=int(Reseau_initial.values[i][1])
        #print(a,b,int(Reseau_initial.values[i][2]))
        M[a][b]=0
        M[b][a]=1
        if int(Reseau_initial.values[i][2])==1:
            print(a,b)
            Mi[a][b]=1
            Mi[b][a]=1
    print(Mi)
    return 0
#verification_RI_TR("10")
verification_RI_TR("16")