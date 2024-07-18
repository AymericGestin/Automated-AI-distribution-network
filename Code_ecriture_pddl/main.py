from code_ecriture import *
import os
#ecriture_problem("C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/point_Reseau_16.csv","C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/RI_Reseau_16.csv","C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/TR_Reseau_16.csv","C:/Users/Aymeric/Documents/GitHub/Automated-AI-distribution-network/Code_ecriture_pddl/problem_16_V2.pddl")
os.system('cmd /k "docker run -it -v C:\Users\Aymeric\Documents\GitHub\Automated-AI-distribution-network:/root/projects/benchmarks lapkt/lapkt-public"')
#./siw_plus --domain /root/projects/benchmarks/code_ecriture_pddl/domainv8.pddl --problem /root/projects/benchmarks/code_ecriture_pddl/problem_16.pddl 