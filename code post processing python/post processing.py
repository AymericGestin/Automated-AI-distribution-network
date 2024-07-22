
def network_topology_validator(M,max_num_nodes,source_node):
    C=source_node
    pts_isoles=[i for i in range(1,max_num_nodes)]
    pts_isoles[source_node]=0
    Liste=[]
    while C != [0]*source_node:
        for i in range (1,len(C)):
            D=[]
            for j in range (len (max_num_nodes)):
                if M[C[i],j]==1 or M[j,C[i]]:
                    D.append(j)
                    M[C[i],j]=0
                    M[j,C[i]]=0
                pts_isoles(D)     
    

