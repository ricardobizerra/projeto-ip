## aqui fica a parte de import de bibliotecas externas (e dos outros arquivos do projeto)
import pygame.display

from settings import *

from entities import Entidade

# import entities
# import os

class Jogo:
    def __init__(self):

        #SETUP GERAL
        pygame.init()
        self.tela = pygame.display.set_mode((largura, altura)) #(x,y): tamanho da tela
        self.nome_jogo = pygame.display.set_caption('Nome do jogo')
        self.clock = pygame.time.Clock()

        self.entidade = Entidade()

    def mostrartela(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.tela.fill('black')
            self.entidade.mostratela()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':  #chave de segurança pro jogo só começar se for inciando no arquivo main
    jogo = Jogo()
    jogo.mostrartela()