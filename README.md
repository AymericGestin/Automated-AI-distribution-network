# Automated-AI-distribution-network

Work flow pour la plannification de constuction de reseau électrique de distribution utilisant la plannification automatique (pddl).<br>

 Prend en paramètre d'entré un fichier excel correspondant correspondant aux caractéristiques du réseau. (voir modèle dans le dossier correponsdant) et renvoie un plan ainsi que les réseaux intermédiaires satisfaisant les contraintes électriques et n-1.   

### **Prérequis:**<br>
-Pypower<br>
-pandas<br>
-docker avec l'image LAPKT<br> 
-matplotlib

### **Liste des fonctions pouvant être utile:**<br> 
**run_planner**: execute le docker LAPKT avec la méthode bfs_plus par défaut pour le numéro de réseau et écrit un fichier txt correspondant au plan dans le dossier plan sous le nom plan_"Numero du réseau". Les fichiers csv doivent être présent dans le répertoire CSV_Problem (voir xlsx pour ce point).<br>
**xlsx to csv**: simple conversion du fichier excel en 4 csv pour chaque feuille. Le fichier excel doit se trouver dans le repertoire Fichier_excel et l'excel sous la forme Reseau_"Numéro du réseau".<br>
**code_ecriture**: traduit le réseaux présent sous forme de csv en un fichier problem pddl en l'écrivant sous le nom problem_"Numérodu réseau"
**post_procc**: effectue les verifications de powerflow et de topologie et peut permettre l'affichage des réseaux intermédiaires. (option à ajouter)

![alt text](https://github.com/AymericGestin/Automated-AI-distribution-network/blob/main/workflow.jpg?raw=true)
