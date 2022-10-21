import pygame
from settings import *

class Interface_usuario():
    def __init__(self):
        self.display_superficie = pygame.display.get_surface()
        self.font = pygame.font.Font(interface_fonte, tamanho_fonte_interface)
        self.retangulo_barra_saude = pygame.Rect(10,10,largura_barra_vida,altura_barra_vida)  


    def mostrar_barra(self,vida_atual,qnt_max,retangulo_fundo,cor):
        pygame.draw.rect(self.display_superficie,cor_backgorund_interface,retangulo_fundo)

        razao = vida_atual / qnt_max
        comprimento_atual_barra = retangulo_fundo.width * razao
        retangulo_atual = retangulo_fundo.copy()
        retangulo_atual.width = comprimento_atual_barra

        pygame.draw.rect(self.display_superficie,cor,retangulo_atual)
        pygame.draw.rect(self.display_superficie,cor_bordas_interface,retangulo_atual,4)


    def display(self, personagem):
        self.mostrar_barra(personagem.saude_atual, personagem.status_saude['saude'],self.retangulo_barra_saude, cor_barra_vida)
