from tkinter import Tk, Canvas, NSEW, messagebox
from connectfour.grille import Grille
from connectfour.partie import PartieConnectFour
from connectfour.exceptions import ErreurPositionCoup



class CanvasConnect4(Canvas):

    def __init__(self, parent, grille):

        self.grille = grille

        self.nb_pixels_par_case = 140

        super().__init__(master=parent, width = Grille.N_COLONNES * self.nb_pixels_par_case,
                         height = Grille.N_LIGNES * self.nb_pixels_par_case,)

        self.dessiner_cases() #on apppele ici pour qu'elle soit initialise !!



    def dessiner_cases(self):

        for ligne in range(Grille.N_LIGNES):
            for colonne in range(Grille.N_COLONNES): self.create_rectangle(self.nb_pixels_par_case * colonne,
                      self.nb_pixels_par_case * ligne, self.nb_pixels_par_case * (colonne+1),
                      self.nb_pixels_par_case * (ligne+1), fill="grey98", tag = "cases")


    def dessiner_jetons(self):
        for position, case in self.grille.cases.items():
            if case.jeton is not None:
                #on doit dessiner le jeton
                jeton = case.jeton
                coordonne_y = position[1] * self.nb_pixels_par_case + self.nb_pixels_par_case//2
                coordonne_x = position[0] * self.nb_pixels_par_case + self.nb_pixels_par_case//2
                self.create_text(coordonne_x, coordonne_y,text=str(jeton.symbole), font=("Deja Vu",
                                self.nb_pixels_par_case//2), fill=jeton.couleur_affichage,tags="piece")

    def actualiser(self):
        #on supprime les anciennes cases et ajoute les nouvelles
        self.delete("cases")
        self.dessiner_cases()

        # on supprime les anciennes pièces et ajoute les nouvelles
        self.delete("piece")
        self.dessiner_jetons()


class FenetrePrincipale(Tk):

    def __init__(self, nom_fichier=None):
        super().__init__()
        self.partie = PartieConnectFour(nom_fichier)
        self.title("ConnectFour")

        # creation de canvas
        self.canvas_jeu = CanvasConnect4(self, self.partie.grille)
        self.canvas_jeu.grid(sticky=NSEW)
        self.canvas_jeu.bind("<Button-1>", self.selectioner_case)  # para capturar a posicao do clique
        self.canvas_jeu.actualiser()

        #format
        self.geometry("980x840")
        self.resizable(0,0)


    def selectioner_case(self, event): #capturar posicao do clique!!

        colonne = event.x // self.canvas_jeu.nb_pixels_par_case
        couleur = self.partie.couleur_joueur_courant

        try:

            self.partie.grille.jouer_coup(colonne, couleur)
            self.canvas_jeu.actualiser()
            Tk.update(self)

            if self.partie.partie_terminee():
                if self.partie.traitement_fin_partie():
                    self.canvas_jeu.actualiser()
                    Tk.update(self)
                    messagebox.showinfo("Fin de la partie", "Le gagnant de la partie est le joueur {}! "
                                        .format(self.partie.couleur_joueur_courant))
                else:
                    messagebox.showinfo("Fin de la partie", "match nul!")

                self.canvas_jeu.actualiser()
                Tk.update(self)
                self.recommencer_partie()
            else:
                self.partie.changer_joueur()

        except ErreurPositionCoup as e:
            messagebox.showwarning("ConnectFour", e)


    def recommencer_partie(self ):


        if messagebox.askyesno("Recommencer", "Desirez-vous lancer une nouvelle partie? "):
            self.partie.grille.cases = self.partie.grille.initialiser_cases_par_defaut()
            self.canvas_jeu.actualiser()
        else:
            self.destroy()



















