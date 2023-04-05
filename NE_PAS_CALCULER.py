import pygame

pygame.init()

# Définition des couleurs
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
TRANSPARENT = (255, 0, 0, 100)

# Définition de la police
font = pygame.font.Font(None, 36)

# Création de la surface du texte
text_surface = font.render('Cliquez ici', True, WHITE)

# Création de la surface du bouton
button_surface = pygame.Surface((200, 50), pygame.SRCALPHA)
button_surface.fill(TRANSPARENT)

# Placement du texte sur le bouton
text_rect = text_surface.get_rect(center=button_surface.get_rect().center)
button_surface.blit(text_surface, text_rect)

# Affichage du bouton
screen = pygame.display.set_mode((400, 300))
screen.blit(button_surface, (100, 100))
pygame.display.flip()

# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_surface.collidepoint(event.pos):
                print("Jouer !!!")

    pygame.display.flip()

pygame.quit()
