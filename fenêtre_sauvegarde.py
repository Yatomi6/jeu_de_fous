import pygame
import paramètre as pm

class Fen_sauvegarde():
    def __init__(self):

        # Fenêtre et fond d'écran
        # Obtenir les dimensions de l'écran de l'utilisateur
        screen_info = pygame.display.Info()
        width, height = screen_info.current_w, screen_info.current_h
        # Définir les dimensions de la fenêtre
        application = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

        # Charger le fond de la fenêtre
        fond_decran = pygame.image.load("image\Fond d'écran jeu.png")
        # Obtenir la taille de l'image
        image_width, image_height = fond_decran.get_size()

        # Calculer le ratio de l'image
        ratio = image_width / image_height

        # Redimensionner l'image en conservant ses proportions pour éviter de la déformer
        if width / height > ratio:
            new_height = int(width / ratio)
            fond_decran = pygame.transform.scale(fond_decran, (width, new_height))
            offset = (0, (height - new_height) // 2) # Calcule pour pouvoir centrer l'image
        else:
            new_width = int(height * ratio)
            fond_decran = pygame.transform.scale(fond_decran, (new_width, height))
            offset = ((width - new_width) // 2, 0) # Calcule pour pouvoir centrer l'image

        # Dessiner l'image sur la surface de la fenêtre
        application.blit(fond_decran, offset)

    # Bouton Retour
        # Créer un bouton retour
        button_x_2 = (application.get_width() - pm.bouton_largeur) // 2
        button_y_2 = (application.get_height() - pm.bouton_hauteur) // 2 + 70
        button_color_2 = pm.couleur_test
        self.button_rect_2 = pygame.Rect(button_x_2, button_y_2, pm.bouton_largeur, pm.bouton_hauteur)

        # Générer une surface de texte
        text_surface = pm.police.render("Retour", True, pm.blanc)

        # Dessiner le bouton
        pygame.draw.rect(application, button_color_2, self.button_rect_2, border_radius= pm.arrondi_angle)

        # Dessiner le texte sur le bouton
        text_rect = text_surface.get_rect(center=self.button_rect_2.center)
        application.blit(text_surface, text_rect)

        #self.update()

    def update(self):
        # Mettre à jour l'affichage
        pygame.display.update()