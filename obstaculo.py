import pygame
from settings import *

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, pos, groups,sprite_type,surface = pygame.Surface((escala,escala))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - escala ))
        else:
            self.rect =  self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-10)