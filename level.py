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

class Level:
    def __init__(self):
        #definir o que vai para a tela do main
        self.superficie_tela = pygame.display.get_surface()

        #GRUPOS DE DE CONFIGURAÇÕES DE  SPRITES
        self.sprites_visiveis = YsortGrupoCamera()
        self.sprites_obstaculos = pygame.sprite.Group()

        #CONFIGURAÇÃO DE SPRITE
        self.criar_mapa()

    def criar_mapa(self):
        layouts = { 
            'boundary': import_csv_layout('map/map_level_1._Boundaries.csv'),
            'obstacle': import_csv_layout('map/map_level_1._Obstacle.csv')
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
                            Obstaculo((x,y), [self.sprites_obstaculos])       
                        if style == 'obstacle':
                            surf = pygame.image.load('graphics/blocks/column_block.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],surf)
                            
        self.personagem = Personagem((500,500),[self.sprites_visiveis],self.sprites_obstaculos, self.criar_ataque)
        
        #INTERFACE DO PERSONAGEM.
        self.ui = Interface_usuario()
    
    # criação do ataque
    def criar_ataque(self, type):
        Weapon(self.personagem, [self.sprites_visiveis], type)

    def run(self):
        #ATUALIZA E MOSTRA O JOGO
        self.sprites_visiveis.draw_personalizado(self.personagem)
        self.sprites_visiveis.update()
        self.ui.display(self.personagem)
        debug(self.personagem.status)

class YsortGrupoCamera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        #CONFIGS GERAIS
        self.superficie_tela = pygame.display.get_surface()
        self.half_widht = self.superficie_tela.get_size()[0] // 2
        self.half_height = self.superficie_tela.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
        # creating the floor
        self.floor_surf = pygame.image.load('graphics/tilemap/piso.png')
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
