import pygame 
from settings import *
from ententies import Entity
from support import *

class Inimigo(Entity):
    def __init__(self,nome_inimigo,pos,grupo_sprite,obstaculo_sprites):
        super().__init__(grupo_sprite)
        self.sprite_type = 'enemy' 

        self.import_graphics(nome_inimigo)
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]

        self.rect =  self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.obstaculo_sprites = obstaculo_sprites

        # Status do inimigo:
        self.tipo_inimigo = nome_inimigo
        info_tipo = enemy_data[self.tipo_inimigo]
        self.health = info_tipo['health']
        self.dano = info_tipo['dano']
        self.attack = info_tipo['attack_type']
        self.resistance = info_tipo['resistance']
        self.speed = info_tipo['speed']
        self.attack_radius = info_tipo['attack_radius']
        self.notice_radius = info_tipo['notice_radius']
        self.withdraw_radius = info_tipo['withdraw_radius']
        self.attack_cooldown = info_tipo['attack_cooldown']

        # Interacao com player
        self.can_attack = True
        self.attack_time = None

    def import_graphics(self,name):
        self.animations = {'idle':[],'move':[],'attack':[],'withdraw':[]}
        main_path = f'./graphics/inimigos/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)
            print(self.animations)

    def get_pos_dir(self,player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()
        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)

    def get_status(self, player):
        distance = self.get_pos_dir(player)[0]
        print(distance)

        if distance <= self.attack_radius:
            self.status = 'attack'
            if distance <= self.withdraw_radius:
                self.status = 'withdraw'

        elif distance <= self.notice_radius:
            self.status = 'move'

        else:
            self.status = 'idle'
    
    def actions(self, player):
        if self.status == 'attack':
            self.direction = pygame.math.Vector2()
            print('attack')
        elif self.status == 'move':
            self.direction = self.get_pos_dir(player)[1]
        elif self.status == 'withdraw':
            self.direction = -(self.get_pos_dir(player)[1])
        else:
            self.direction = pygame.math.Vector2()
    
    # movimento e colisão que podem sair ao implentar a classe Entity
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

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        # definir a imagem
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)


    def update(self):
        self.move(self.speed)
        self.animate()

    def enemy_update(self,player):
        self.get_status(player)
        self.actions(player)  
