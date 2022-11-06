import pygame 
from settings import *
from ententies import Entity


class Inimigo(Entity):
    def __init__(self,nome_inimigo,pos,grupo_sprite,obstaculo_sprites):
        super().__init__(grupo_sprite)
        self.sprite_type = 'enemy' 
        self.status = 'idle'
        if nome_inimigo == 'mob_melee':
            self.image = pygame.image.load('graphics/test/enemy_melee.png').convert_alpha()
        elif nome_inimigo == 'mob_ranged':
            self.image = pygame.image.load('graphics/test/enemy_rannged.png').convert_alpha()
        elif nome_inimigo == 'mob_elite':
            self.image = pygame.image.load('graphics/test/enemy_elite.png').convert_alpha()
        self.rect =  self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.obstaculo_sprites = obstaculo_sprites
        self.direction = pygame.math.Vector2()
        
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

        #interacao com jogador
        self.can_attack = True 
        self.attack_time = 0
        self.attack_cooldown = 400

        #tempo de invensibilidade
        self.vulneravel = True 
        self.tempo_ataque = 0
        self.tempo_invencibilidade = 300

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if not self.can_attack:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True 
    
        if not self.vulneravel:
            if current_time - self.tempo_ataque >= self.tempo_invencibilidade:
                self.vulneravel = True 

    def levar_dano(self, jogador, tipo_ataque):
        if self.vulneravel:
            self.direction = self.get_pos_dir(jogador)[1]
            if tipo_ataque == 'weapon':
                self.health -= jogador.get_full_weapon_damage()
            self.tempo_ataque = pygame.time.get_ticks()
            self.vulneravel = False 
            
    def verificar_morte(self):
        if self.health <= 0:
            self.kill()

    def get_pos_dir(self,player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()
        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)

    def reacao_dano(self):
        if not self.vulneravel:
            self.direction *= -self.resistance

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
            self.attack_time = pygame.time.get_ticks()
            self.direction = pygame.math.Vector2()
            print('attack')
        elif self.status == 'move':
            self.direction = self.get_pos_dir(player)[1]
        elif self.status == 'withdraw':
            self.direction = -(self.get_pos_dir(player)[1])
        else:
            self.direction = pygame.math.Vector2()


                
    def update(self):
        self.move(self.speed)
        self.cooldowns()
        

    def enemy_update(self,player):
        self.get_status(player)
        self.actions(player)
        self.verificar_morte()  
        self.reacao_dano()