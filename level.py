from curses import noecho
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
            'obstacle': import_csv_layout('map/map_Obstacles.csv')
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

        # Desenho do personagem no início
        self.personagem = Personagem((1300,2500),[self.sprites_visiveis],self.sprites_obstaculos, self.criar_ataque, 0, False)

        # Coletáveis no início
        self.bolinha_item1 = coletaveis((1600, 2500), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.bolinha_item2 = coletaveis((2000, 3000), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.bolinha_item3 = coletaveis((1950, 2320), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.bolinha_item4 = coletaveis((1240, 2930), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.bolinha_item5 = coletaveis((2428, 1980), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.raquete_item = coletaveis((1600, 2000),'raquete', [self.sprites_visiveis], self.sprites_obstaculos)

    # criação do ataque
    def criar_ataque(self, type):
        if self.personagem.inventario[type] > 0:
            Weapon(self.personagem, [self.sprites_visiveis], type, self.sprites_obstaculos)
            if type == 'bola':
                self.personagem.inventario['bola'] -= 1

    def run(self):
        #ATUALIZA E MOSTRA O JOGO
        self.sprites_visiveis.draw_personalizado(self.personagem)
        self.sprites_visiveis.update()

        #Fazendo os coletáveis sumirem
        self.bolinha_item1.apagar_col(self.personagem)
        self.bolinha_item2.apagar_col(self.personagem)
        self.bolinha_item3.apagar_col(self.personagem)
        self.bolinha_item4.apagar_col(self.personagem)
        self.bolinha_item5.apagar_col(self.personagem)
        self.raquete_item.apagar_col(self.personagem)

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
        self.floor_surf = pygame.image.load('graphics/tilemap/background_map.png')
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

    
