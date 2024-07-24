from code_ecriture import *
from xlxs_to_csv import *
import os

f_xlxs_to_csv("68")
f_xlxs_to_csv("10")
f_xlxs_to_csv("16")
f_xlxs_to_csv("6")
ecriture_problem(os.path.join(path,"CSV_Problem","point_Reseau_68.csv"),os.path.join(path,"CSV_Problem","RI_Reseau_68.csv"),os.path.join(path,"CSV_Problem","TR_Reseau_68.csv"),os.path.join(path,"CSV_Problem","problem_68.pddl"))
ecriture_problem(os.path.join(path,"CSV_Problem","point_Reseau_10.csv"),os.path.join(path,"CSV_Problem","RI_Reseau_10.csv"),os.path.join(path,"CSV_Problem","TR_Reseau_10.csv"),os.path.join(path,"CSV_Problem","problem_10.pddl"))
ecriture_problem(os.path.join(path,"CSV_Problem","point_Reseau_16.csv"),os.path.join(path,"CSV_Problem","RI_Reseau_16.csv"),os.path.join(path,"CSV_Problem","TR_Reseau_16.csv"),os.path.join(path,"CSV_Problem","problem_16.pddl"))
ecriture_problem(os.path.join(path,"CSV_Problem","point_Reseau_6.csv"),os.path.join(path,"CSV_Problem","RI_Reseau_6.csv"),os.path.join(path,"CSV_Problem","TR_Reseau_6.csv"),os.path.join(path,"CSV_Problem","problem_6b.pddl"))
