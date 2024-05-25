import pygame
import sys

def check_events(ship):

    """
    Responde a eventos de  pressionamento de teclas e de mouse.
    """
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_RIGHT:
                      ship.moving_right = True
                      ship.rect.conterx +=1
            elif event.type == pygame.KEYUP:
                 if event.key == pygame.K_RIGHT:
                      ship.moving_right = False


def update_screen(ai_settings, screen, ship):
     """
     Atualiza as imagens na tela e altera para nova tela.
     """
     screen.fill(ai_settings.bg_color)
     ship.blitme()
     pygame.display.flip()