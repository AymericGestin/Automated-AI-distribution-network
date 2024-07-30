import numpy as np

# Load a sample case (IEEE 9-bus system)
def network_for_lf(Num_noeuds,Noeuds,Reseau,Parametres):
    S_base=Parametres.values[1][1]
    Ubase=Parametres.values[2][1]
    bus=np.zeros((len(Num_noeuds),13))
    gen=np.zeros((2,10))
    k=0
    for i in range(len(Num_noeuds)):
        bus[i][0]=int(Num_noeuds[i])
        if Noeuds.values[i][1] == "Primary substation":
            bus[i][1]=3
            gen[k][0]=i+1
            gen[k][7]=1
            gen[k][3]=300
            gen[k][4]=-300
            gen[k][8]=300
            gen[k][9]=-300
            gen[k][5]=1.02
            k+=1
        else:
            bus[i][1]=1
        bus[i][2]=Noeuds.values[i][6]*S_base
        bus[i][3]=Noeuds.values[i][7]*S_base
        bus[i][7]=1
        bus[i][8]=0
        bus[i][11]=1.1
        bus[i][12]=0.9
        bus[i][9]=Ubase
    line=np.zeros((len(Reseau),13))
    for i in range(len(Reseau)):
        line[i][0]=int(Reseau.values[i][0])
        line[i][1]=int(Reseau.values[i][1])
        line[i][2]=Reseau.values[i][3]
        line[i][3]=Reseau.values[i][4]
        if Reseau.values[i][2] == 1:
            line[i][10]=0
            line[i][2]=99999
            line[i][3]=99999
        else:
            line[i][10]=1
    ppc = {
    "baseMVA": S_base,
    "bus": bus,
    "gen": gen,
    "branch": line
}
    return ppc
