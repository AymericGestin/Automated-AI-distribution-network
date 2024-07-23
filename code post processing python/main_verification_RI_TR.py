import pandas as pd
import os
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
    print (Reseau_initial)
    for i in range(Reseau_initial.shape[0]):
        if Reseau_initial[i][0] > Reseau_initial[i][1]:
            Reseau_initial[i][0],Reseau_initial[i][1]=Reseau_initial[i][1],Reseau_initial[i][0]
    print (Reseau_initial)
    return 0
verification_RI_TR("10")