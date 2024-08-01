# Automated-AI-distribution-network

Work flow pour la plannification de constuction de reseau électrique de distribution utilisant la plannification automatique (pddl).<br>

 Prend en paramètre d'entré un fichier excel correspondant correspondant aux caractéristiques du réseau. (voir modèle dans le dossier correponsdant) et renvoie un plan ainsi que les réseaux intermédiaires satisfaisant les contraintes électriques et n-1.   

### **Prérequis:**<br>
-Pypower<br>
-pandas<br>
-docker avec l'image LAPKT<br> 
-matplotlib

### **Liste des fonctions pouvant être utile:**<br> 
**run_planner**: execute le docker LAPKT avec la méthode bfs_plus par défaut pour le numéro de réseau et écrit un fichier txt correspondant au plan dans le dossier plan sous le nom plan_"Numero du réseau".<br>
**xlsx to csv**: simple conversion du fichier excel en 4 csv pour chaque feuille

![alt text](https://github.com/AymericGestin/Automated-AI-distribution-network/blob/main/workflow.jpg?raw=true)
