import numpy as np

# créer la structure caseforamt de pypower associer au réseau fournit pour effectuer les opérations Pypower nécessaire 
def network_for_lf(Num_noeuds,Noeuds,Reseau,Parametres):
    S_base=Parametres.values[1][1]
    Ubase=Parametres.values[2][1]
    bus=np.zeros((len(Num_noeuds),13))
    gen=np.zeros((2,10))
    k=0
    for i in range(len(Num_noeuds)):
        bus[i][0]=int(Num_noeuds[i]) #indice du bus
        if Noeuds.values[i][1] == "Primary substation":#pour les stations primaires
            bus[i][1]=3 #mode slack
            gen[k][0]=i+1 #indice du générateur correpondant au slack bus
            gen[k][7]=1 # 1 generateur en service
            gen[k][3]=300 # valeur maximal et minimal généré les slack bus en MVA/MW
            gen[k][4]=-300
            gen[k][8]=300
            gen[k][9]=-300 
            gen[k][5]=1.02 #tension du generateur
            k+=1
        else: #bus pq
            bus[i][1]=1 #1 indique un bus pq
        bus[i][2]=Noeuds.values[i][6]*S_base # valeur de P(MW)
        bus[i][3]=Noeuds.values[i][7]*S_base # valeur de Q(MVAR)
        bus[i][7]=1 #tension p.u
        bus[i][8]=0 #angle de la tension
        bus[i][11]=1.1 #tension max
        bus[i][12]=0.9 #tension min
        bus[i][9]=Ubase #Ubase
    line=np.zeros((len(Reseau),13))
    for i in range(len(Reseau)): #definition des branches
        line[i][0]=int(Reseau.values[i][0]) #noeud départ
        line[i][1]=int(Reseau.values[i][1]) #noeud arrivée
        line[i][2]=Reseau.values[i][3] #résistance
        line[i][3]=Reseau.values[i][4] #reactance
        if Reseau.values[i][2] == 1: #si la ligne est ouverte
            line[i][10]=0 #ligne hors service
            line[i][2]=99999 # résistance infinie pour les lignes ouvertes
            line[i][3]=99999 # réactance infinie pour les lignes ouvertes
        else:
            line[i][10]=1 #ligne en service
    ppc = {
    "baseMVA": S_base,
    "bus": bus,
    "gen": gen,
    "branch": line
}
    return ppc
