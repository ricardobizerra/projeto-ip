import pygame
from obstaculo import Obstaculo
from player import Personagem
from settings import *

class Entidade:
    def __init__(self):
        #definir o que vai para a tela do main
        self.superficie_tela = pygame.display.get_surface

        #GRUPOS DE DE CONFIGURAÇÕES DE  SPRITES
        self.sprites_visiveis = pygame.sprite.Group()
        self.sprites_obstaculos = pygame.sprite.Group()

        #CONFIGURAÇÃO DE SPRITE
        self.criar_mapa()

    def criar_mapa(self):
        #LOOP PRA CONSEGUIR INFORMACOES DAS COORDENADAS
        for index_linha, linha in enumerate(mapa):
            for index_coluna, coluna in enumerate(linha):
                x = index_coluna * escala
                y = index_linha * escala
                if coluna == 'x':
                    Obstaculo((x,y), [self.sprites_visiveis])
                if coluna == 'p':
                    Personagem((x,y), [self.sprites_visiveis])
                    

    def mostratela(self):
        #ATUALIZA E MOSTRA O JOGO
        self.sprites_visiveis.draw(self.superficie_tela)
        pass
