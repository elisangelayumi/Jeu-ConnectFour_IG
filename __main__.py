'''
Module de lancement du package connectfour. 

C'est ce module que nous allons exécuter pour démarrer votre jeu.
'''

#from connectfour.partie import PartieConnectFour

from interface.interface_connectfour import FenetrePrincipale



if __name__ == '__main__':


    fenetre = FenetrePrincipale()

    fenetre.mainloop()





    #partie = PartieConnectFour()

    # Pour charger d'une partie déjà sauvegardée
    #partie = PartieConnectFour("partie_sauvegardee.txt")

    # Pour sauvegarder une partie
    # partie.sauvegarder("partie_sauvegardee.txt")

    #partie.jouer()