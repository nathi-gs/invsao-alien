import pygame
import sys
import Settings
import Ship
import game_functions as gf

def run_game(): 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_widht,
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
   

    while True:
        gf.check_events(Ship)
        Ship.update()
        gf.update_screen(ai_settings,screen,Ship)

run_game()