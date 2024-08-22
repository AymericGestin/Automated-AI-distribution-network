from code_ecriture import *
from xlxs_to_csv import *
import os
from script_planner import *
from main_post_procc import *
from Trace_reseau import trace_reseau
# partie principale du code permet l'appel des différentes fonction du work flow 
#conversion d'excel a csv puis ecriture du pddl puis lancement des planners  
#run_planner(10) # ne marche pas pour le reseau 10 les primaires ont l'air de changer de position donc peut être un probleme dans l'excel
numero_reseau=input("choissisez un numero de reseau")
def work_flow(numero_reseau):
    f_xlxs_to_csv(numero_reseau)
    ecriture_problem(numero_reseau)
    run_planner(numero_reseau)
    cout,action,reseau=post_procc(numero_reseau)
    return reseau,action
reseau,action=work_flow(numero_reseau)
ordre_trace=input("voulez-vous tracer les réseaux intermédiaires ? (oui/non)")

#test d'affichage

def trace_reseau(ax, X, Y, Num_noeuds, Reseau_etudie):
    ax.clear()  # Nettoyer l'axe avant de tracer
    # Tracé des primary
    ax.plot(X[-2], Y[-2], 's', color='black', markerfacecolor='black')
    ax.text(X[-2], Y[-2], str(Num_noeuds[-2]))
    ax.plot(X[-1], Y[-1], 's', color='black', markerfacecolor='black')
    ax.text(X[-1], Y[-1], str(Num_noeuds[-1]))
    # Tracé des secondary
    for i in range(len(X) - 2):
        ax.plot(X[i], Y[i], 'o', color='magenta', markerfacecolor='magenta')
        ax.text(X[i], Y[i], str(i + 1))
    
    for i in range(len(Reseau_etudie)):
        if Reseau_etudie.values[i][2] == 0:  # ligne fermée
            ax.plot([X[int(Reseau_etudie.values[i][0] - 1)], X[int(Reseau_etudie.values[i][1] - 1)]], 
                    [Y[int(Reseau_etudie.values[i][0] - 1)], Y[int(Reseau_etudie.values[i][1] - 1)]], '-b')
        else:  # ligne ouverte
            ax.plot([X[int(Reseau_etudie.values[i][0] - 1)], X[int(Reseau_etudie.values[i][1] - 1)]], 
                    [Y[int(Reseau_etudie.values[i][0] - 1)], Y[int(Reseau_etudie.values[i][1] - 1)]], '--b')

    ax.set_aspect('equal', 'box')  # Assurer que les axes sont égaux

class FigureNavigator:
    def __init__(self, figures_data):
        self.figures_data = figures_data
        self.current_index = 0
        self.total_figures = len(figures_data)

        # Créer une seule figure et un seul axe
        self.fig, self.ax = plt.subplots()
        self.update_figure(self.current_index)

        # Connecter l'événement de la touche à la fonction on_key_press
        self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)

        plt.show()

    def update_figure(self, index):
        X, Y, Num_noeuds, Reseau_etudie, title = self.figures_data[index]
        trace_reseau(self.ax, X, Y, Num_noeuds, Reseau_etudie)
        self.fig.canvas.manager.set_window_title(title)
        self.fig.canvas.draw()

    def on_key_press(self, event):
        if event.key == 'right':
            self.current_index = (self.current_index + 1) % self.total_figures
        elif event.key == 'left':
            self.current_index = (self.current_index - 1) % self.total_figures

        self.update_figure(self.current_index)

if ordre_trace=="oui":
    with open(os.path.join('Reseaux_intermediaires','Reseau_intermediaire_'+str(numero_reseau)+'.pkl'), 'rb') as f:
        Reseau_intermediaire_valide = pickle.load(f)
        k=1
        figures_data=[]
        Noeuds = pd.read_csv(os.path.join(path,"CSV_Problem","point_Reseau_"+numero_reseau+".csv"),sep=";")
        X=Noeuds['X'].values.tolist()
        Y=Noeuds['Y'].values.tolist()
        Num_noeuds=Noeuds['Numero du noeud'].values.tolist()
        for Reseau in Reseau_intermediaire_valide:
            figures_data.append((X, Y, Num_noeuds, Reseau, "Réseau intermediaire "+str(k)))
            k+=1
    navigator = FigureNavigator(figures_data)