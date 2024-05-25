import pygame
class Ship:
   
   def __init__(self, screen):
      """
      Inicializa a espaçonave e define sua posição inicial
      """

      self.screen = screen
      self.image = pygame.image.load('imagens/ship.png')
      self.image_size = (70,70)
      self.image = pygame.transform.scale(self.image)
      self.rect = self.image.get_rect()
      self.screen_rect = screen.get_rect()
      self.rect.centerx = self.screen_rect.centerx
      self.rect.bottom = self.screen_rect.bottom
      self.moving_right = False
      self.moving_left = False

def update(self):
   if self.move_right and self.rect.right < self.screen_rect.right:
      self.rect.centerx +=1

def blitme(self):
   """
   Desenha a espaçonave em sua posição inicial
   """

   self.screen.blit(self.image, self.rect)
