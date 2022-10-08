import pygame
from settings import *

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, pos, grupo_sprite):
        super().__init__
        self.image = pygame.image.load('local da imagem do obstaculo.png').convert_alpha()
        self.rect =  self.image.get_rect(topleft=pos)