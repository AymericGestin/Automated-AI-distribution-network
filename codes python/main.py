from code_ecriture import *
from xlxs_to_csv import *
import os
from script_planner import *
from main_post_procc import *
# partie principale du code permet l'appel des différentes fonction du work flow 
#conversion d'excel a csv puis ecriture du pddl puis lancement des planners  
f_xlxs_to_csv("68")
f_xlxs_to_csv("10")
f_xlxs_to_csv("16")
f_xlxs_to_csv("6")
ecriture_problem(68)
ecriture_problem(10)
ecriture_problem(16)
ecriture_problem(6)
run_planner(68)
run_planner(16)
#run_planner(10) # ne marche pas pour le reseau 10 les primaires ont l'air de changer de position donc peut être un probleme dans l'excel
run_planner(6)
post_procc(6)
