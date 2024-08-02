import pandas as pd
import os
# extrait l'excel Reseau_"num" dans le dossier Fichier_excel 4 csv correspondant aux feuilles vers le dossier scv_problem
# Point_Reseau_"num":information sur les bus; TR_Reseau_"num": réseau cible; RI_Reseau_"num" réseau intial; Parametre: paramètres  
def f_xlxs_to_csv(Num_reseau):
    path=os.path.dirname(os.path.dirname(__file__))
    excel_file_path=os.path.join(path,"Fichier_excel","Reseau_"+Num_reseau+".xlsx")

    df1 = pd.read_excel(excel_file_path,0)
    df2 = pd.read_excel(excel_file_path,1)
    df3 = pd.read_excel(excel_file_path,2)
    df4 = pd.read_excel(excel_file_path,3)
    csv_file_path1 = os.path.join(path,"CSV_Problem","point_Reseau_"+Num_reseau+".csv")
    csv_file_path2 = os.path.join(path,"CSV_Problem","RI_Reseau_"+Num_reseau+".csv")
    csv_file_path3 = os.path.join(path,"CSV_Problem","TR_Reseau_"+Num_reseau+".csv")
    csv_file_path4 = os.path.join(path,"CSV_Problem","Parametre_Reseau_"+Num_reseau+".csv")
    # Convert to CSV
    df1.to_csv(csv_file_path1, index=False,sep=";")
    df2.to_csv(csv_file_path2, index=False,sep=";")
    df3.to_csv(csv_file_path3, index=False,sep=";")
    df4.to_csv(csv_file_path4, index=False,sep=";")

