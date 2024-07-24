def network_topology_validator2(M, max_num_nodes, source_node):
    """
    Inputs definition:
    - M = Network connectivity matrix : if node i is connected to node j then
    M[i][j] = 1 and M[j][i] = 1,
    - max_num_nodes = node having the highest value in the network,
    - source_node = list of nodes representing the "energy sources"
    """
    
    C = source_node.copy()
    pts_isoles = list(range(1, max_num_nodes + 1))
    
    for node in source_node:
        pts_isoles[node - 1] = 0
    
    Liste = []
    
    while len(C) > 0:
        for node in C:
            D = [i + 1 for i, connected in enumerate(M[node - 1]) if connected == 1]
            M[node - 1] = [0] * max_num_nodes
            for i in range(max_num_nodes):
                M[i][node - 1] = 0
            for d in D:
                pts_isoles[d - 1] = 0
            Liste = list(set(Liste + D))
        C = Liste.copy()
        Liste = []
    
    pts_isoles = [node for node in pts_isoles if node != 0]
    return pts_isoles

# # Example usage:
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