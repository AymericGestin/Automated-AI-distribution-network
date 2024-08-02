import matplotlib.pyplot as plt
import pandas as pd
# def Trace_reseau(X,Y,Num_noe,Reseau_etudie):
#     import matplotlib.pyplot as plt

def trace_reseau(X, Y, Num_noeuds, Reseau_etudie):
    plt.figure()
    plt.plot(X[-2], Y[-2], 's', color='black', markerfacecolor='black')
    plt.text(X[-2], Y[-2], str(Num_noeuds[-2]))
    plt.plot(X[-1], Y[-1], 's', color='black', markerfacecolor='black')
    plt.text(X[-1], Y[-1], str(Num_noeuds[-1]))
    
    for i in range(len(X) - 2):
        plt.plot(X[i], Y[i], 'o', color='magenta', markerfacecolor='magenta')
        plt.text(X[i], Y[i], str(i + 1))
    
    for i in range(len(Reseau_etudie)):
        if Reseau_etudie.values[i][2] == 0:  # ligne fermée
            plt.plot([X[int(Reseau_etudie.values[i][0] - 1)], X[int(Reseau_etudie.values[i][1] - 1)]], 
                     [Y[int(Reseau_etudie.values[i][0] - 1)], Y[int(Reseau_etudie.values[i][1] - 1)]], '-b')
        else:
            plt.plot([X[int(Reseau_etudie.values[i][0] - 1)], X[int(Reseau_etudie.values[i][1] - 1)]], 
                     [Y[int(Reseau_etudie.values[i][0] - 1)], Y[int(Reseau_etudie.values[i][1] - 1)]], '--b')
    
    plt.axis('equal')
    plt.show()

