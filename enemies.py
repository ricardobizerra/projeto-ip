import pygame
from settings import *
from player import *

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, pos, grupo_sprite, obstaculo_sprites, criar_ataque):
        super().__init__(grupo_sprite)
        self.image = pygame.image.load('graphics/personagem/attack_down/attack_down.png').convert_alpha() # só mudei o arquivo para o programa rodar
        self.rect =  self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)

        #MOVIMENTO DO INIMIGO
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
        self.criar_ataque = criar_ataque

        #COLISÃO
        self.obstaculo_sprites = obstaculo_sprites
