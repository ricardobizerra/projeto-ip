 ## aqui fica a parte de import de bibliotecas externas (e dos outros arquivos do projeto)
import pygame.display

from settings import *

from level import Level

from player import *

import sys

# import level
# import os

#game_active = True
#valor = 5

class Jogo:
    def __init__(self):

        #SETUP GERAL
        pygame.init()
        self.tela = pygame.display.set_mode((largura, altura)) #(x,y): tamanho da tela
        self.nome_jogo = pygame.display.set_caption('Nome do jogo')
        self.clock = pygame.time.Clock()

        self.game_active = False

    def mostrartela(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.game_active = True
                    self.level = Level()

            if self.game_active:
                self.tela.fill('black')
                self.level.run()

                if self.level.personagem.saude_atual == 0:
                    self.game_active = False
                    self.level.personagem.saude_atual = 100

            else:
                self.tela.fill((94,129,162))
            
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':  #chave de segurança pro jogo só começar se for inciando no arquivo main
    jogo = Jogo()
    jogo.mostrartela()
