import pygame 
from settings import *
from entities import Entity
from support import *


class Inimigo(Entity):
    def __init__(self,nome_inimigo,pos,grupo_sprite,obstaculo_sprites,damage_player):
        super().__init__(grupo_sprite)
        self.sprite_type = 'enemy' 

        self.status = 'idle'

        self.image = pygame.image.load('graphics/inimigos/'+nome_inimigo+'/'+self.status+'/0.png').convert_alpha()

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
        self.attack_cooldown = info_tipo['cooldown_ataque']
        self.startup_timer = info_tipo['startup_ataque']

        #interacao com jogador
        self.can_attack = True 
        self.attack_time = 0
        self.attacking = False
        self.launch_attack = False
        self.interrupted = False
        self.speed_multiplier = 1
        self.damage_player = damage_player

        #tempo de invensibilidade
        self.vulneravel = True 
        self.tempo_ataque = 0
        self.tempo_invencibilidade = 300

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attacking_timer >= self.startup_timer:
                self.launch_attack = True
                self.attacking = False

        if not self.can_attack:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True 
    
        if not self.vulneravel:
            if current_time - self.tempo_ataque >= self.tempo_invencibilidade:
                self.vulneravel = True 

    def levar_dano(self, player, tipo_ataque):
        if self.vulneravel:
            self.interrupted = True
            self.direction = -(self.get_pos_dir(player)[1])
            if tipo_ataque == 'weapon':
                self.health -= player.get_full_weapon_damage()
            elif tipo_ataque == 'bola':
                self.health -= 10
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
        if distance <= self.attack_radius:
            self.status = 'attack'
            if distance <= self.withdraw_radius:
                self.status = 'withdraw'

        elif distance <= self.notice_radius:
            self.status = 'move'

        else:
            self.status = 'idle'
    
    def actions(self, player):
        if self.status == 'attack' and self.can_attack:
            if not self.attacking and not self.launch_attack:
                self.attacking = True
                self.attacking_timer = pygame.time.get_ticks()
                self.speed_multiplier = 0.5
        elif self.status == 'move':
            self.direction = self.get_pos_dir(player)[1]
        elif self.status == 'withdraw':
            self.direction = -(self.get_pos_dir(player)[1])
        else:
            self.direction = pygame.math.Vector2()

        if self.launch_attack and not self.interrupted:
            self.launch_attack = False
            self.attack_time = pygame.time.get_ticks()
            self.can_attack = False
            self.damage_player(self.dano,self.attack)
            self.speed_multiplier = 1
        if self.launch_attack and self.interrupted:
            self.launch_attack = False
            self.can_attack = True
            self.interrupted = False
            self.speed_multiplier = 1

    def update(self):
        self.move(self.speed*self.speed_multiplier)
        self.cooldowns()
        if not self.vulneravel:
            self.image = pygame.image.load('graphics/inimigos/'+self.tipo_inimigo+'/attack_sprites/hurt.png')
            alpha = self.flicker()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def enemy_update(self,player):
        self.get_status(player)
        self.actions(player)
        if self.status != 'attack':
            self.image = pygame.image.load('graphics/inimigos/'+self.tipo_inimigo+'/'+self.status+'/0.png')
        if self.attacking:
            self.image = pygame.image.load('graphics/inimigos/'+self.tipo_inimigo+'/attack_sprites/attacking.png')
        if not self.can_attack:
            self.image = pygame.image.load('graphics/inimigos/'+self.tipo_inimigo+'/attack_sprites/cooldown.png')
        self.verificar_morte()  
        self.reacao_dano()
