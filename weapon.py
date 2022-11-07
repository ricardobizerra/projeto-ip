import pygame
from settings import *

class Weapon(pygame.sprite.Sprite):

    def __init__(self, player, groups, type, obstaculo_sprites):
        super().__init__(groups)
        self.attack_direction = player.status.split('_')[1]
        self.sprite_type = 'weapon' 

        # gráficos
        full_path = f'graphics/weapons/{type}/{self.attack_direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()
        
        # variável de correção de posicionamento
        correcao_posicionamento = pygame.math.Vector2(0, 16)

        # posicionamento

        if self.attack_direction == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + correcao_posicionamento)

        elif self.attack_direction == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft + correcao_posicionamento)
        
        elif self.attack_direction == 'up':
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + correcao_posicionamento)
        
        else:
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + correcao_posicionamento)
        
        # movimentação
        self.direction = pygame.math.Vector2()

        # hitbox
        self.hitbox = self.rect.inflate(0,-10)

        # contador de tempo
        self.inicio_ataque = pygame.time.get_ticks()
    
    def timer(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.inicio_ataque >= 200:
            self.kill()

    def update(self):
        self.timer()
