from settings import *
import pygame 

#Essa classe é responsável pela criação da interface responsável por mostrar dados dos jogador (pontos de vida, energia, experiência e etc)
#A barra de vida será um retângulo vermelho, de mesma altura e largura que a barra de plano de fundo, que irá sobrepor a barra de plano de fundo, porém irá variar a sua largura de acordo com a razão entra os pontos de vida atual e os ponto de vida máximo.

class Interface_usuario:
    def __init__(self):

        #definir o que vai para a tela do main.
        self.superficie_tela = pygame.display.get_surface()
        self.fonte = pygame.font.Font(None, tamanho_fonte_interface)

        #Configurações da barra. (Aqui eu estou posicionando a barra de vida na tela, além de definir a sua altura e largura)
        self.barra_vida_rect = pygame.Rect(10, 30, barra_vida_largura, altura_barra_vida)

    def mostrar_barra_vida(self,qnt_vida_atual, max_vida, fundo_barra_rect, cor): #Esse método busca construir a barra de vida.

        #Mostrando o background da barra de vida. (aqui será gerado um retãngulo que será um plano de fundo para o que será de fato a barra de vida)
        pygame.draw.rect(self.superficie_tela, cor_backgorund_interface, fundo_barra_rect)

        # zera a vida, a fim não mostrar valor negativo
        if qnt_vida_atual <= 0:
            qnt_vida_atual = 0

        #Convertendo o status de saúde para pixel.
        razao = qnt_vida_atual / max_vida 
        qnt_vida_atual_width = fundo_barra_rect.width * razao
        qnt_vida_atual_rect = fundo_barra_rect.copy()
        qnt_vida_atual_rect.width = qnt_vida_atual_width

        #Agora vou, de fato, criar a barra de vida.
        pygame.draw.rect(self.superficie_tela, cor, qnt_vida_atual_rect)
        pygame.draw.rect(self.superficie_tela, cor_bordas_interface, fundo_barra_rect, 3)
        
        # display da quantidade de vida atualizada
        superficie_display_vida = self.fonte.render(f'Vida: {str(qnt_vida_atual)}', True, 'White')
        retangulo_display_vida = superficie_display_vida.get_rect(topleft=(10, 10))
        pygame.draw.rect(self.superficie_tela, '#000000', retangulo_display_vida)
        self.superficie_tela.blit(superficie_display_vida, retangulo_display_vida)
 
    def display(self,jogador): #Esse método busca fazer o méotodo anterior exibir a barra de vida construídda por ele.
        self.mostrar_barra_vida(jogador.saude,jogador.status_saude['saude'], self.barra_vida_rect, cor_barra_vida) 
