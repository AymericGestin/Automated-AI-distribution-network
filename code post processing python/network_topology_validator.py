
#fonction ayant pour but de déterminer les noeuds isolés à partir d'une matrice de connexion M
# N1--line1--N2--line2--N3--line3--N4 avec N2 comme source
# la matrice de connexion serait  
#M= [0 1 0 0
#    1 0 1 0
#    0 1 0 1
#    0 0 1 0]
# les 1 aux emplacements [i][j] correspond à une connexion entre le noeud i et le noeud j 
def network_topology_validator(M,max_num_nodes,source_node):
    C=[source_node]
    pts_isoles=[i for i in range(1,max_num_nodes+1)]
    pts_isoles[source_node-1]=0
    Liste=[]
    while M != [[0]*max_num_nodes]*max_num_nodes:
        for i in range (0,len(C)):
            D=[]
            for j in range (max_num_nodes):
                a=C[i]-1
                if M[a][j]==1 or M[j][a]==1:
                    D.append(j+1)
                    M[a][j]=0
                    M[j][a]=0
                    pts_isoles[j]=0
        print(M)        
        C=D  
    return(pts_isoles)

#exemple de l'appel de fonction de l'exemple
# network_topology_validator([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],4,2)

