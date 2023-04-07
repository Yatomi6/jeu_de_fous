import pygame
import paramètre as pm

class Fen_demarrage():
    def __init__(self):
        # Voix nom du jeu
        self.sound_nom_du_jeu = pygame.mixer.Sound("son\son_nom_du_jeu.mp3")

        # Affiche la première fenêtre de jeu (Fenêtre de démarrage)

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
    
    # Logo
        # Création du rectangle du logo
        logo_x = (application.get_width() - pm.bouton_largeur) // 2
        logo_y = (application.get_height() - pm.bouton_hauteur) // 2 - 400
        self.logo_rect = pygame.Rect(logo_x, logo_y, 500, 250)

        # Charger du logo depuis le fichier
        logo = pygame.image.load("image\Logo_jeu_2-removebg-preview.png")#.convert_alpha()

        # Définir la nouvelle taille souhaitée
        new_width = 300

        # Calculer la nouvelle hauteur en maintenant le ratio d'aspect
        ratio_logo = logo.get_width() / logo.get_height()
        new_height = int(new_width / ratio_logo)

        # Redimensionner l'image
        logo = pygame.transform.scale(logo, (new_width, new_height))

        # Dessiner l'image sur la surface de la fenêtre
        application.blit(logo, self.logo_rect)

    # Bouton Jeu
        # Charger l'image du bouton
        image_jouer = pygame.image.load("image\Bouton_Jouer_final.png")

        # Créer un bouton 1
        button_x = (application.get_width() - pm.bouton_largeur) // 2 + 50
        button_y = (application.get_height() - pm.bouton_hauteur) // 2
        button_color = pm.blanc
        self.button_rect = pygame.Rect(button_x, button_y, image_jouer.get_width(), image_jouer.get_height())

        # Afficher le bouton
        application.blit(image_jouer, (button_x,button_y))

        # Générer une surface de texte
        #text_surface_bouton_1 = pm.police.render("Jouer", True, pm.vert)

        # Dessiner le bouton
        #pygame.draw.rect(application, button_color, self.button_rect, border_radius= pm.arrondi_angle)
    
        # Dessiner le texte sur le bouton (à enlever quand Flo -> logo)
        #text_rect_bouton_1 = text_surface_bouton_1.get_rect(center=self.button_rect.center)
        #application.blit(text_surface_bouton_1, text_rect_bouton_1)

        # Petit test du son
        #self.sound = pygame.mixer.Sound("son\VOXLaff_Rire.ogg")

    # Bouton Quitter
        # Créer un bouton 2
        button_x_2 = (application.get_width() - pm.bouton_largeur) // 2
        button_y_2 = (application.get_height() - pm.bouton_hauteur) // 2 + 70
        button_color_2 = pm.couleur_test
        self.button_rect_2 = pygame.Rect(button_x_2, button_y_2, pm.bouton_largeur, pm.bouton_hauteur)

        # Générer une surface de texte
        text_surface = pm.police.render("Quitter", True, pm.blanc)

        # Dessiner le bouton
        pygame.draw.rect(application, button_color_2, self.button_rect_2, border_radius= pm.arrondi_angle)

        # Dessiner le texte sur le bouton
        text_rect = text_surface.get_rect(center=self.button_rect_2.center)
        application.blit(text_surface, text_rect)

        #self.update()

    def update(self):
        # Mettre à jour l'affichage
        pygame.display.update()