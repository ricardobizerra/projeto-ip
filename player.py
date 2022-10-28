import pygame
from settings import *
from support import import_folder

class Personagem(pygame.sprite.Sprite):
    def __init__(self, pos, grupo_sprite, obstaculo_sprites, criar_ataque):
        super().__init__(grupo_sprite)
        self.image = pygame.image.load('graphics/test/player.png').convert_alpha()
        self.rect =  self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)

        # setup gráfico
        self.import_player_assets()
        self.status = 'normal_down'
        self.frame_index = 0
        self.animation_speed = 0.15

        #MOVIMENTO DO PLAYER
        self.direction = pygame.math.Vector2()
        self.speed = 10
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        # armas
        self.criar_ataque = criar_ataque
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]

        #STATUS DO PERSONAGEM.
        self.status_saude = {'saude': 100}
        self.saude = self.status_saude['saude']

        #COLISÃO
        self.obstaculo_sprites = obstaculo_sprites
    
    # "unir" estados do jogador com pastas de imagens para animação
    def import_player_assets(self):
        character_path = 'graphics/personagem/'
        self.animations = {
            'attack_down': [],
            'attack_left': [],
            'attack_right': [],
            'attack_up': [],
            'idle_down': [],
            'idle_left': [],
            'idle_right': [],
            'idle_up': [],
            'normal_down': [],
            'normal_left': [],
            'normal_right': [],
            'normal_up': [],
        }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    #DETECTAR AS TECLAS DO TECLADO
    def input(self):

        if not self.attacking:
            keys = pygame.key.get_pressed()

            # input de movimento
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.direction.y = -1
                self.status = 'normal_up'
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.direction.y = 1
                self.status = 'normal_down'
            else:
                self.direction.y = 0

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.direction.x = 1
                self.status = 'normal_right'
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.direction.x = -1
                self.status = 'normal_left'
            else:
                self.direction.x = 0
            
            # input de ataque
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.criar_ataque('raquete')
            
            if keys[pygame.K_b]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.criar_ataque('bola')

    # estados do jogador
    def get_status(self):

        # ocioso (idle)
        if self.direction.x == 0 and self.direction.y == 0:

            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status.replace('normal_','idle_')
        
        # ataque
        if self.attacking:

            self.direction.x = 0
            self.direction.y = 0

            if not 'attack' in self.status:

                if 'idle' in self.status:
                    self.status = self.status.replace('idle_','attack_')
                else:
                    self.status = self.status.replace('normal_','attack_')
        
        else:

            if 'attack' in self.status:
                self.status = self.status.replace('attack_','normal_')

    def move(self, speed):

        #CORRIGIR A MOVIMENTAÇÃO QUANDO O PERSONAGEM ANDA NA DIAGONAL
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.colisao('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.colisao('vertical')
        self.rect.center = self.hitbox.center

    def colisao(self, direcao):
        if direcao == 'horizontal':
            for sprite in self.obstaculo_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #INDO PARA A DIREITA
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: #INDO PARA A ESQUERDA
                        self.hitbox.left = sprite.hitbox.right

        if direcao == 'vertical':
            for sprite in self.obstaculo_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: #INDO PARA BAIXO
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: #INDO PARA CIMA
                        self.hitbox.top = sprite.hitbox.bottom    

    # cooldown
    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    # animação de jogador
    def animate(self):
        animation = self.animations[self.status]

        # loop sobre o index do frame
        self.frame_index += self.animation_speed

        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        # definir a imagem
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        self.input()
        self.cooldowns()
        self.animate()
        self.get_status()
        self.move(self.speed)