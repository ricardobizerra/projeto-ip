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
        self.nome_oficial = 'The Legend of Marcelo: CInvasion'
        self.nome_jogo = pygame.display.set_caption(self.nome_oficial)
        self.clock = pygame.time.Clock()

        self.game_active = False
        self.numero_partidas = 0
    
    def mensagem_tela(self, mensagem, pos_x, pos_y, color, tam_fonte):
        self.fonte = pygame.font.Font(None, tam_fonte)
        superficie = self.fonte.render(f'{mensagem}',True,color)
        rect = superficie.get_rect(center = (pos_x, pos_y))
        self.tela.blit(superficie, rect)

    def mostrartela(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and not self.game_active:
                    self.game_active = True
                    self.level = Level()
                    self.morte = False
                    self.numero_partidas += 1

            if self.game_active:
                self.tela.fill('black')
                self.level.run()

                if self.level.personagem.saude_atual <= 0 or self.level.personagem.usou_pendrive:
                    self.game_active = False

                    if self.level.personagem.saude_atual <= 0:
                        self.morte = True

                    self.level.personagem.saude_atual = 100

            else:
                # tela de início do jogo
                if not self.numero_partidas:

                    # imagem de fundo
                    superficie_fundo = pygame.image.load('graphics/display/background.png').convert_alpha()
                    rect_fundo = superficie_fundo.get_rect(topleft = (0, 0))
                    self.tela.blit(superficie_fundo, rect_fundo)

                    # título
                    self.mensagem_tela(self.nome_oficial, 640, 120, '#ffffff', 90)
                    
                    # descrição
                    self.mensagem_tela(
                        'O CIn foi invadido! Ajude Marcelo a recuperar os dados e trazer de volta a rotina do Centro',
                        640, 200, 'White', 40
                    )

                    # instruções
                    self.mensagem_tela(
                        'Use tudo o que você coletar como arma! Arremesse bolinhas de ping-pong e',
                        640, 260, 'White', 35
                    )

                    self.mensagem_tela(
                        'dê dano com o crachá e o vetor da base ortonormalizada de AVLC!',
                        640, 290, 'White', 35
                    )

                    self.mensagem_tela(
                        'Colete e coma seus salgados para recuperar sua vida e seu fôlego!',
                        640, 320, 'White', 35
                    )

                    self.mensagem_tela(
                        'Pegue e abra o pen-drive para vencer e nos salvar!',
                        640, 350, 'White', 35
                    )

                    self.mensagem_tela(
                        'O CIn conta com você. Boa sorte!',
                        640, 415, 'White', 40
                    )

                    self.mensagem_tela('ENTER para iniciar', 1020, 600, 'White', 60)

                else:
                    
                    # derrota
                    if self.morte:

                        # imagem de fundo
                        superficie_fundo = pygame.image.load('graphics/display/background_black.png').convert_alpha()
                        rect_fundo = superficie_fundo.get_rect(topleft = (0, 0))
                        self.tela.blit(superficie_fundo, rect_fundo)

                        # título
                        self.mensagem_tela(self.nome_oficial, 640, 120, '#ffffff', 90)
                        
                        self.mensagem_tela(
                            'Ah não, infelizmente, não deu! O CIn foi tomado por',
                            640, 270, 'White', 40
                        )

                        self.mensagem_tela(
                            'forças robóticas. Seu lucro e seus salgados foram perdidos. F, turma',
                            640, 305, 'White', 40
                        )

                        self.mensagem_tela(
                            'Mas vamos tentar de novo! Nós temos a força e o poder do conhecimento!',
                            640, 380, 'White', 40
                        )

                        self.mensagem_tela('ENTER para reiniciar', 1020, 600, 'White', 60)
                    
                    # vitória
                    else:

                        # imagem de fundo
                        superficie_fundo = pygame.image.load('graphics/display/background_gold.png').convert_alpha()
                        rect_fundo = superficie_fundo.get_rect(topleft = (0, 0))
                        self.tela.blit(superficie_fundo, rect_fundo)

                        # título
                        self.mensagem_tela(self.nome_oficial, 640, 120, '#ffffff', 90)
                        
                        self.mensagem_tela(
                            'BOAAAAAAAAAAAAAAAA!!!! Você conseguiu!',
                            640, 250, 'White', 40
                        )

                        self.mensagem_tela(
                            'Graças aos seus conhecimentos no CIn, o pendrive desativou todos os robôs!',
                            640, 285, 'White', 40
                        )

                        self.mensagem_tela(
                            'O Centro está salvo, Marcelo está cada vez mais próximo de se tornar um milionário',
                            640, 320, 'White', 40
                        )

                        self.mensagem_tela(
                            'e seu império de salgados sobrevive a mais um dia!',
                            640, 355, 'White', 40
                        )

                        self.mensagem_tela(
                            'Vem cá, mas quem foi que fez tudo isso, hein? Fica o mistério...',
                            640, 410, 'White', 40
                        )

                        self.mensagem_tela('ENTER para reiniciar', 1020, 600, 'White', 60)

            
            pygame.display.update()
            self.clock.tick(FPS)
