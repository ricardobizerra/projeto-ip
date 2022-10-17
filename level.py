import pygame
from obstaculo import Obstaculo
from player import Personagem
from settings import *
from weapon import Weapon
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
        
        #INTERFACE DO PERSONAGEM.
        self.ui = Interface_usuario()

    def criar_mapa(self):
        #LOOP PRA CONSEGUIR INFORMACOES DAS COORDENADAS
        for index_linha, linha in enumerate(mapa):
            for index_coluna, coluna in enumerate(linha):
                x = index_coluna * escala
                y = index_linha * escala
                if coluna == 'x':
                    Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos])
                if coluna == 'p':
                    self.personagem = Personagem((x,y), [self.sprites_visiveis], self.sprites_obstaculos, self.criar_ataque)
    
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

    def draw_personalizado(self, personagem):

        #POSIÇÃO DA CÂMERA
        self.offset.x = personagem.rect.centerx - self.half_widht
        self.offset.y = personagem.rect.centery - self.half_height

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key= lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.superficie_tela.blit(sprite.image,offset_pos)
