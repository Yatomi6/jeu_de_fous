# Fichier jeu.py est le plus important.
# Il relit tous les fichiers entre eux et leurs coabitations.

# Importation
import pygame
import fenêtre_démarrage as f_dem
import fenêtre_sauvegarde as f_sau
import paramètre as pm

# 
class Jeu():
    def __init__(self):
        self.fenetre_demarrage = f_dem.Fen_demarrage()

    def fen_sauvegarde(self):
        self.fenetre_sauvegarde = f_sau.Fen_sauvegarde()

    def update(self):
        # Mettre à jour l'affichage
        pygame.display.update()
    
    def run(self):
        self.fenetre_demarrage.sound_nom_du_jeu.play()
        # Boucle de jeu
        while True:
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Vérifier si les boutons sont cliqués
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.fenetre_demarrage.button_rect.collidepoint(event.pos):
                        self.fen_sauvegarde()
                    if self.fenetre_demarrage.button_rect_2.collidepoint(event.pos):
                        pygame.quit()
                        quit()
