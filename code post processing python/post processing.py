
def network_topology_validator(M,max_num_nodes,source_node):
    C=[source_node]
    pts_isoles=[i for i in range(1,max_num_nodes+1)]
    pts_isoles[source_node]=0
    Liste=[]
    #while M != [[0]*max_num_nodes]*max_num_nodes:
    for k in range(20):
        for i in range (0,len(C)):
            D=[]
            for j in range (max_num_nodes):
                print(j)
                a=C[i]
                if M[C[i]][j]==1 or M[j][C[i]]==1:
                    D.append(j)
                    M[a][j]=0
                    #M[j][a]=0
                #     pts_isoles[j]=0
                #     print(D)
            print(M,i)
            C=D   
    return(pts_isoles)

network_topology_validator([[0,1,0,1],[1,0,1,0],[0,1,0,1],[0,0,1,0]],4,2)