import pygame
from entities import  Entity
from settings import *
from support import import_folder

class Personagem(Entity):
    def __init__(self, pos, grupo_sprite, obstaculo_sprites, criar_ataque):
        super().__init__(grupo_sprite)
        self.image = pygame.image.load('graphics/player/down/down.png').convert_alpha()
        self.rect =  self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)
        self.superficie_tela = pygame.display.get_surface()

        # setup gráfico
        self.import_player_assets()
        self.status = 'normal_down'

        #MOVIMENTO DO PLAYER
        self.speed = 10
        
        # varáveis de cooldown
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        self.comendo = False
        self.comendo_time = None
        self.comendo_cooldown = 1000

        self.vulneravel = True
        self.vulneravel_timer = 0
        self.vulneravel_cooldown = 300

        # armas
        self.criar_ataque = criar_ataque

        # Inventário:
        self.inventario = {
            'bola': 0, 'raquete': 0, 'coxinha': 0, 'cracha': 0, 'vetor': 0, 'pendrive': 0
        }

        #STATUS DO PERSONAGEM.
        self.arma_equipada = 'cracha'
        self.status_saude = {'saude': 100, 'ataque': 5}
        self.saude_atual = self.status_saude['saude']
        self.razao = self.saude_atual / largura_barra_vida
        vida = self.saude_atual

        #COLISÃO
        self.obstaculo_sprites = obstaculo_sprites

        # zerar o jogo
        self.usou_pendrive = False

    #METODO PARA RECUPERAR VIDA.
    def curar(self, cura):
        if self.saude_atual + cura < self.status_saude['saude']:
            self.saude_atual += cura
        else:
            self.saude_atual = self.status_saude['saude']

    def get_full_weapon_damage(self):
        dano_base = self.status_saude['ataque']
        dano_arma = weapon_data[self.arma_equipada]['dano']
        return dano_base + dano_arma
        
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
        keys = pygame.key.get_pressed()

        # input de movimento
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
            if not self.attacking:
                self.status = 'normal_up'
            else:
                self.status = 'attack_up'

        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
            if not self.attacking:
                self.status = 'normal_down'
            else:
                self.status = 'attack_down'

        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            if not self.attacking: 
                self.status = 'normal_right'
            else:
                self.status = 'attack_right'

        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            if not self.attacking:
                self.status = 'normal_left'
            else: 
                self.status = 'attack_left'
        else:
            self.direction.x = 0
            
        # input de ataque
        if not self.attacking:
            if keys[pygame.K_SPACE] and not self.comendo:
                self.attacking = True
                self.speed *= 0.5
                self.attack_time = pygame.time.get_ticks()
                self.criar_ataque(self.arma_equipada)
            
            if keys[pygame.K_b] and not self.comendo:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                arma_anterior = self.arma_equipada
                self.arma_equipada = 'bola'
                self.criar_ataque(self.arma_equipada)
                self.arma_equipada = arma_anterior

            if keys[pygame.K_f] and not self.comendo:
                if self.inventario['coxinha'] > 0 and self.saude_atual < 100:
                    self.comendo = True
                    self.speed *= 0.5
                    self.comendo_time = pygame.time.get_ticks()
                    self.inventario['coxinha'] -= 1
            
            if keys[pygame.K_1]:
                self.arma_equipada = 'cracha'

            if keys[pygame.K_2]:
                self.arma_equipada = 'raquete'

            if keys[pygame.K_3]:
                self.arma_equipada = 'vetor'

            # input para zerar o jogo
            if keys[pygame.K_x] and self.inventario['pendrive'] == 1:
                self.usou_pendrive = True

    # estados do jogador
    def get_status(self):

        # ocioso (idle)
        if self.direction.x == 0 and self.direction.y == 0 and not self.attacking:

            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status.replace('normal_','idle_')
        
        # ataque
        if self.attacking:

            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('idle_','attack_')

                else:
                    self.status = self.status.replace('normal_','attack_')
        
        else:

            if 'attack' in self.status:
                self.status = self.status.replace('attack_','normal_')

   # cooldown
    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown + weapon_data[self.arma_equipada]['dano']:
                self.attacking = False
                
                if self.speed < 10:
                    self.speed *= 2
        
        if self.comendo:
            if current_time - self.comendo_time >= self.comendo_cooldown:
                self.curar(50)
                self.comendo = False

                if self.speed < 10:
                    self.speed *= 2

        if not self.vulneravel:
            if current_time - self.vulneravel_timer >= self.vulneravel_cooldown:
                self.vulneravel = True

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
        if not self.vulneravel:
            alpha = self.flicker()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)


    def update(self):
        self.input()
        self.cooldowns()
        self.animate()
        self.get_status()
        self.move(self.speed)
        
