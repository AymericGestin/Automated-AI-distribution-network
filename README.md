# Automated-AI-distribution-network

Work flow pour la plannification de constuction de reseau électrique de distribution utilisant la plannification automatique (pddl).<br>

 Prend en paramètre d'entré un fichier excel correspondant correspondant aux caractéristiques du réseau. (voir modèle dans le dossier correponsdant) et renvoie un plan ainsi que les réseaux intermédiaires satisfaisant les contraintes électriques et n-1.   

### **Prérequis:**<br>
-Pypower<br>
-pandas<br>
-docker avec l'image LAPKT<br> 
-matplotlib

### **Installation:**<br>
**Windows**<br>
Vérifier votre installation de python et de pip<br>
*python --version* et *pip --version*<br>
puis entrez les commandes: <br>
-pip install numpy <br>
-pip insall pypower <br>
-pip install pandas <br>
-pip install matplotlib <br>
pour l'installation de docker suivre les instructions du lien suivant https://docs.docker.com/engine/install/ <br>
executer ensuite la commande *docker pull lapkt/lapkt-public*
l'installation devrait être terminé.<br>

**Linux**<br>
utiliser pip3 au lieu de pip mais l'installation devrait être similaire

### **Comment executer le script**<br>
prerequis: Mettre le fichier excel correspondant au réseau de distribution étudié dans le dossier "Fichier_excel". Ce fichier doit respecter la même syntaxe que les réseaux présent en exemple. Le fichier doit contenir les inforamtions sur le réseau de départ, cible, ainsi que les postes sources et secondaires et les caractéristiques du réseau.<br>

depuis l'invite de commande:
-acceder au repertoire local .\Automated-AI-distribution-network\codes_python<br> -executer la commande "python main.py"<br>
-indiquer le numéro du réseau étudié<br>
-précisez si vous voulez afficher et naviguer en utilisant les flèches du clavier

### **Liste des fonctions secondaires pouvant être utile:**<br> 
**run_planner**: execute le docker LAPKT avec la méthode bfs_plus par défaut pour le numéro de réseau et écrit un fichier txt correspondant au plan dans le dossier plan sous le nom plan_"Numero du réseau". Les fichiers csv doivent être présent dans le répertoire CSV_Problem (voir xlsx pour ce point).<br>
**xlsx to csv**: simple conversion du fichier excel en 4 csv pour chaque feuille. Le fichier excel doit se trouver dans le repertoire Fichier_excel et l'excel sous la forme Reseau_"Numéro du réseau".<br>
**code_ecriture**: traduit le réseaux présent sous forme de csv en un fichier problem pddl en l'écrivant sous le nom problem_"Numérodu réseau".<br>
**post_procc**: effectue les verifications de powerflow et de topologie et peut permettre l'affichage des réseaux intermédiaires. (option à ajouter)

### **Workflow**
![alt text](https://github.com/AymericGestin/Automated-AI-distribution-network/blob/main/workflow.jpg?raw=true)
