import pygame
from settings import *

class Weapon(pygame.sprite.Sprite):

    def __init__(self, player, groups, type):
        super().__init__(groups)
        self.attack_direction = player.status.split('_')[1]

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
        self.speed = 20

        # colisão
        self.hitbox = self.rect.inflate(0,-10)
    
    def input(self):

        if self.attack_direction == 'right':
            self.direction.x = 1
            self.direction.y = 0

        elif self.attack_direction == 'left':
            self.direction.x = -1
            self.direction.y = 0
        
        elif self.attack_direction == 'up':
            self.direction.x = 0
            self.direction.y = -1
        
        else:
            self.direction.x = 0
            self.direction.y = 1
    
    def move(self, speed):
        self.hitbox.x += self.direction.x * speed
        self.hitbox.y += self.direction.y * speed
        self.rect.center = self.hitbox.center
    
    def update(self):
        self.input()
        self.move(self.speed)
