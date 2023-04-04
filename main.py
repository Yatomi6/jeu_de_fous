# Ne pas modifier
# Fichier main.py permet de démarrer le jeu en entier.

# Importation
import pygame
from jeu import Jeu

if __name__ == '__main__':
    pygame.init() # Initialisation obligatoire de Pygame
    pygame.display.set_caption("__Cristals Dungeon__")

    # Charger l'icône
    icon = pygame.image.load("image\Logo_jeu_2-removebg-preview.png")

    # Définir l'icône de la fenêtre
    pygame.display.set_icon(icon)

    jeu = Jeu() # Initialisation de la classe Game(), exécute le __init__ de Game()
    jeu.run() # Exécute le run de Game(), permet de garder la fenêtre ouverte et de faire tout marcher
