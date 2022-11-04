import pygame 
from settings import *
from ententies import Entity

class Enemy(Entity):
    def __init__(self, monster_name, pos, groups):

        #Configurações gerais.
        super().__init__(groups)
        self.sprite_type = 'enemy'

        #Configurações gráficas.
        self.image = pygame.Surface((64,64))
        self.rect = self.image.get_rect(topleft = pos)
        

