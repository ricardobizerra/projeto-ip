import pygame
from settings import *

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, pos, grupo_sprite):
        super().__init__(grupo_sprite)
        self.image = pygame.image.load('graphics/cenario/piso/chao.png').convert_alpha()
        self.rect =  self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-10)