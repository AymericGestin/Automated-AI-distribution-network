import numpy as np
from network_topology_validator import network_topology_validator
#fonction a lancé si il y a des points isolés pour vérifier si il s'agit d'une boucle 
# et donne des lignes candidates pour raccorder la boucle au réseau intermédiaire
def cherche_boucles(Reseau_intermediaire, max_num_nodes, source_node, Reseau_final):
    Candidats = []
    # Initialize a matrix with zeroes using a list of lists
    M = [[0 for _ in range(max_num_nodes)] for _ in range(max_num_nodes)]
    
    for j in range(len(Reseau_intermediaire)):
        M[int(Reseau_intermediaire.values[j][0]) - 1][Reseau_intermediaire.values[j][1] - 1] = 1 - Reseau_intermediaire.values[j][2]
        M[Reseau_intermediaire[j][1] - 1][Reseau_intermediaire[j][0] - 1] = 1 - Reseau_intermediaire[j][2]
    
    for line_open in range(len(Reseau_intermediaire)):
        if Reseau_intermediaire[line_open][2] == 0:  # Si la ligne est normalement fermée
            M[Reseau_intermediaire[line_open][0] - 1][Reseau_intermediaire[line_open][1] - 1] = 0
            M[Reseau_intermediaire[line_open][1] - 1][Reseau_intermediaire[line_open][0] - 1] = 0
            
            pts_isoles = network_topology_validator(M, max_num_nodes, source_node)
            
            if len(pts_isoles) == 0:
                Candidats.append(line_open)
            
            M[Reseau_intermediaire[line_open][0] - 1][Reseau_intermediaire[line_open][1] - 1] = 1
            M[Reseau_intermediaire[line_open][1] - 1][Reseau_intermediaire[line_open][0] - 1] = 1
    
    MC = [Reseau_intermediaire[i] for i in Candidats]
    
    for i in range(len(MC)):
        if MC[i][0] > MC[i][1]:
            Vect1 = [MC[i][1], MC[i][0]]
        else:
            Vect1 = [MC[i][0], MC[i][1]]
        
        for j in range(len(Reseau_final)):
            if Reseau_final[j][0] > Reseau_final[j][1]:
                Vect2 = [Reseau_final[j][1], Reseau_final[j][0]]
            else:
                Vect2 = [Reseau_final[j][0], Reseau_final[j][1]]
            
            if set(Vect1).intersection(set(Vect2)):
                if Vect1 == Vect2:
                    # Ligne présente dans le réseau final
                    Candidats[i] = [Candidats[i], Reseau_final[j][2]]
                    break
                else:
                    # Ligne non présente dans le réseau final
                    Candidats[i] = [Candidats[i], 3]
            else:
                # Ligne non présente dans le réseau final
                Candidats[i] = [Candidats[i], 3]
    
    return Candidats