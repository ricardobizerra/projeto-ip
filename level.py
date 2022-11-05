# from curses import noecho
import pygame
from obstaculo import Obstaculo
from player import Personagem
from settings import *
from support import *
from random import choice
from weapon import Weapon
from enemies import Inimigo
from debug import *
from interface_usuario import Interface_usuario
from coletaveis import *

class Level:
    def __init__(self):
        #definir o que vai para a tela do main
        self.superficie_tela = pygame.display.get_surface()

        #GRUPOS DE DE CONFIGURAÇÕES DE  SPRITES
        self.sprites_visiveis = YsortGrupoCamera()
        self.sprites_obstaculos = pygame.sprite.Group()

        #Attack sprites.
        self.ataque_atual = None 
        self.sprites_ataque = pygame.sprite.Group()
        self.sprites_atacaveis = pygame.sprite.Group()

        #CONFIGURAÇÃO DE SPRITE
        self.criar_mapa()
        
        #INTERFACE DO PERSONAGEM.
        self.iu = Interface_usuario()

    def criar_mapa(self):
        layouts = { 
            'boundary': import_csv_layout('map/map_Boundaries.csv'),
            'obstacle': import_csv_layout('map/map_Obstacles.csv'),
            'entities' : import_csv_layout('map/map_Entities.csv')
        }   
        graphics = {
            'grass': import_folder('graphics/Grass'),
            'objects': import_folder('graphics/objects')
        }

        #LOOP PRA CONSEGUIR INFORMACOES DAS COORDENADAS
        for style, layout in layouts.items():
            for index_linha, linha in enumerate(layout):
                for index_coluna, coluna in enumerate(linha):
                    if coluna != '-1':
                        x = index_coluna * escala
                        y = index_linha * escala
                        if style == 'boundary':
                            Obstaculo((x,y), [self.sprites_obstaculos], 'none')       
                        if style == 'obstacle' and coluna == '11':
                                surf = pygame.image.load('graphics/objects/12.png')
                        if style == 'obstacle' and coluna == '12':
                            surf = pygame.image.load('graphics/objects/04.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '13':
                            surf = pygame.image.load('graphics/objects/03.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle':
                            if coluna == '2':
                                surf = pygame.image.load('graphics/blocks/boundary_block.png')
                            elif coluna == '4':
                                surf = pygame.image.load('graphics/blocks/red_block.png')
                            elif coluna == '9':
                                surf = pygame.image.load('graphics/blocks/wall_block.png')
                            elif coluna == '16':
                                surf = pygame.image.load('graphics/spritespiskel/catraca.png')
                            elif coluna == '18':
                                surf = pygame.image.load('graphics/spritespiskel/mesa.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'none',surf)
                        if style == 'entities':
                            if coluna == '0':
                                self.personagem = Personagem((2500,5000),[self.sprites_visiveis],self.sprites_obstaculos, self.criar_ataque)

        # Coletáveis no início
        self.bolinha_item1 = Coletaveis((2210, 2730), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.bolinha_item2 = Coletaveis((2700, 1050), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.bolinha_item3 = Coletaveis((1100, 700), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.bolinha_item4 = Coletaveis((1520, 3000), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.bolinha_item5 = Coletaveis((2428, 1480), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.raquete_item = Coletaveis((2000, 2000),'raquete', [self.sprites_visiveis], self.sprites_obstaculos)
        self.coxinha_item1 = Coletaveis((2300, 2500), 'coxinha', [self.sprites_visiveis], self.sprites_obstaculos)
        self.coxinha_item2 = Coletaveis((2500, 2700), 'coxinha', [self.sprites_visiveis], self.sprites_obstaculos)
        
        # Inimigos no inicio
        self.inimigo_melee = Inimigo('mob_melee', (2400, 5500), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos)
        self.inimigo_ranged = Inimigo('mob_ranged', (2600, 5500), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos)
        self.inimigo_elite = Inimigo('mob_elite', (2500, 5500), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos)
    # criação do ataque
    def criar_ataque(self, type):
        if self.personagem.inventario[type] > 0:
            Weapon(self.personagem, [self.sprites_visiveis, self.sprites_ataque], type, self.sprites_obstaculos)
            if type == 'bola':
                self.personagem.inventario['bola'] -= 1

    def logica_ataque(self):
        if self.sprites_ataque:
            for sprite_ataque in self.sprites_ataque:
               lista_sprites_colisao = pygame.sprite.spritecollide(sprite_ataque,self.sprites_atacaveis,True)
               if lista_sprites_colisao:
                for alvo in lista_sprites_colisao:
                    alvo.levar_dano(self.personagem,sprite_ataque.sprite_type)

    def run(self):
        #ATUALIZA E MOSTRA O JOGO
        self.sprites_visiveis.draw_personalizado(self.personagem)
        self.sprites_visiveis.update()
        self.logica_ataque()
        self.sprites_visiveis.enemy_update(self.personagem)

        #Fazendo os coletáveis sumirem
        self.bolinha_item1.apagar_col(self.personagem)
        self.bolinha_item2.apagar_col(self.personagem)
        self.bolinha_item3.apagar_col(self.personagem)
        self.bolinha_item4.apagar_col(self.personagem)
        self.bolinha_item5.apagar_col(self.personagem)
        self.raquete_item.apagar_col(self.personagem)
        self.coxinha_item1.apagar_col(self.personagem)
        self.coxinha_item2.apagar_col(self.personagem)


        debug(self.personagem.status)
        self.iu.display(self.personagem)

class YsortGrupoCamera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        #CONFIGS GERAIS
        self.superficie_tela = pygame.display.get_surface()
        self.half_widht = self.superficie_tela.get_size()[0] // 2
        self.half_height = self.superficie_tela.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
        # creating the floor
        self.floor_surf = pygame.image.load('graphics/tilemap/map.png')
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
        
    def draw_personalizado(self, personagem):

        #POSIÇÃO DA CÂMERA
        self.offset.x = personagem.rect.centerx - self.half_widht
        self.offset.y = personagem.rect.centery - self.half_height
        
         # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.superficie_tela.blit(self.floor_surf,floor_offset_pos)

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key= lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.superficie_tela.blit(sprite.image,offset_pos)

    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
    
