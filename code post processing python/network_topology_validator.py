
#fonction ayant pour but de déterminer les noeuds isolés à partir d'une matrice de connexion M
# N1--line1--N2--line2--N3--line3--N4 avec N2 comme source
# la matrice de connexion serait  
#M= [0 1 0 0
#    1 0 1 0
#    0 1 0 1
#    0 0 1 0]
# les 1 aux emplacements [i][j] correspond à une connexion entre le noeud i et le noeud j 
def network_topology_validator(M,max_num_nodes,source_node):
    C=source_node
    pts_isoles=[i for i in range(1,max_num_nodes+1)]
    for i in range(len(C)):
        pts_isoles[source_node[i]-1]=0
    Liste=[]
    while len(C)>0:
        for i in range (0,len(C)):
            D=[]
            for j in range (max_num_nodes):
                a=C[i]-1
                if M[a][j]==1 or M[j][a]==1: 
                    D.append(j+1)
                    M[a][j]=0
                    M[j][a]=0
                    pts_isoles[j]=0       
        C=D  
    pts_isoles= [node for node in pts_isoles if node!=0]
    return(pts_isoles)

#exemple de l'appel de fonction pour le cas du haut
# M = [
#     [0, 1, 0, 0],
#     [1, 0, 1, 0],
#     [0, 1, 0, 1],
#     [0, 0, 1, 0]
# ]
# max_num_nodes = 4
# source_node = [2]

# isolated_points = network_topology_validator(M, max_num_nodes, source_node)
# print(isolated_points)

