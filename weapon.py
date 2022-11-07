import pygame
from settings import *

class Weapon(pygame.sprite.Sprite):

    def __init__(self, player, groups, type, obstaculo_sprites):
        super().__init__(groups)
        self.direction = pygame.math.Vector2()
        self.attack_direction = player.status.split('_')[1]
        self.sprite_type = 'weapon' 
        if type == 'bola':
            self.sprite_type = 'bola'
        self.cooldown = weapon_data[player.arma_equipada]['cooldown']

        # gráficos
        full_path = f'graphics/weapons/{type}/{self.attack_direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()
        
        # variável de correção de posicionamento
        correcao_posicionamento = pygame.math.Vector2(0, 16)

        # posicionamento

        if self.attack_direction == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + correcao_posicionamento)
            self.direction.x = 1
            self.direction.y = 0

        elif self.attack_direction == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft + correcao_posicionamento)
            self.direction.x = -1
            self.direction.y = 0
        
        elif self.attack_direction == 'up':
            self.rect = self.image.get_rect(midbottom = player.rect.midtop + correcao_posicionamento)
            self.direction.x = 0
            self.direction.y = -1
        
        else:
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + correcao_posicionamento)
            self.direction.x = 0
            self.direction.y = 1
        
        # movimentação
        if type == 'bola':
            self.speed = 20

        # hitbox
        self.hitbox = self.rect.inflate(0,-10)
        if type == 'bola':
            self.obstaculo_sprites = obstaculo_sprites

        # contador de tempo
        self.inicio_ataque = pygame.time.get_ticks()

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

        self.colisao()

    def colisao(self):
        for sprite in self.obstaculo_sprites:
            if sprite.hitbox.colliderect(self.hitbox):
                self.kill()

    def timer(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.inicio_ataque >= self.cooldown:
            self.kill()

    def update(self):
        self.timer()
        self.input()
        if type == 'bola':
            self.move(self.speed)
