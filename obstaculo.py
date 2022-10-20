import pygame
from settings import *

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, pos, groups,surface = pygame.Surface((escala,escala))):
        super().__init__(groups)
        self.image = surface
        self.rect =  self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-10)
