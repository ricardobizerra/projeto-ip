import pygame
from settings import *

class Weapon(pygame.sprite.Sprite):

    def __init__(self, player, groups, type):
        super().__init__(groups)
        direction = player.status.split('_')[1]

        # gráficos
        full_path = f'graphics/weapons/{type}/{direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()
        
        # posicionamento

        # variável de correção de posicionamento
        correcao_posicionamento = pygame.math.Vector2(0, 16)

        if direction == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + correcao_posicionamento)
        
        elif direction == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft + correcao_posicionamento)
        
        elif direction == 'up':
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + correcao_posicionamento)
        
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + correcao_posicionamento)
        
        else:
            self.rect = self.image.get_rect(center = player.rect.center)
