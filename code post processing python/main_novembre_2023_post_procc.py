from main_verification_RI_TR import *
path=os.path.dirname(os.path.dirname(__file__))
fichier=open(os.path.join(path,"Plan","plan.txt"),"r")
plan=fichier.read()
fichier.close()
list_action=[]
a=0
for i in range(len(plan)):
    if plan[i] == "\n":
        list_action.append(plan[a:i])
        a=i+1
cout_NO=12
cout_ligne_moy=500
cont=1
Reseau_fusion=[]
indicateur_cas=0

for action in list_action:
    if action[:action.index(" ")] == "(ADD_OPENLINE":
        indicateur_cas=1
    if action[:action.index(" ")] == "(REMOVE_ADD_OPENLINE":
        indicateur_cas=2
    if action[:action.index(" ")] == "(CHANGE_SWITCH_CONNECTION":
        indicateur_cas=3
    if action[:action.index(" ")] == "(REMOVE_OPENLINE":
        indicateur_cas=4   