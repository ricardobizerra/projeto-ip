import pygame
from settings import *

class Interface_usuario():
    def __init__(self):
        self.display_superficie = pygame.display.get_surface()
        self.font = pygame.font.Font(interface_fonte, tamanho_fonte_interface)
        self.retangulo_barra_saude = pygame.Rect(10,30,largura_barra_vida,altura_barra_vida)  

        #definir o que vai para a tela do main.
        self.superficie_tela = pygame.display.get_surface()
        self.fonte = pygame.font.Font(None, tamanho_fonte_interface)

        #Configurações da barra. (Aqui eu estou posicionando a barra de vida na tela, além de definir a sua altura e largura)
        self.barra_vida_rect = pygame.Rect(10, 30, barra_vida_largura, altura_barra_vida)

        #Convertendo o dicionario de armas para uma lista.
        self.lista_imagem_armas = []
        for arma in weapon_data.values():
            path = arma['graphic']
            arma = pygame.image.load(path).convert_alpha()
            self.lista_imagem_armas.append(arma)

    def mostrar_barra_vida(self,qnt_vida_atual, max_vida, fundo_barra_rect, cor): #Esse método busca construir a barra de vida.

    def mostrar_barra(self,vida_atual,qnt_max,retangulo_fundo,cor):
        pygame.draw.rect(self.display_superficie,cor_backgorund_interface,retangulo_fundo)

        razao = vida_atual / qnt_max
        comprimento_atual_barra = retangulo_fundo.width * razao
        retangulo_atual = retangulo_fundo.copy()
        retangulo_atual.width = comprimento_atual_barra

        pygame.draw.rect(self.display_superficie,cor,retangulo_atual)
        pygame.draw.rect(self.display_superficie,cor_bordas_interface,retangulo_atual,4)

        # display da quantidade de vida atualizada
        superficie_display_vida = self.font.render(f'Vida: {str(vida_atual)}', True, 'White')
        retangulo_display_vida = superficie_display_vida.get_rect(topleft=(10, 10))
        pygame.draw.rect(self.superficie_tela, '#000000', retangulo_display_vida)
        self.superficie_tela.blit(superficie_display_vida, retangulo_display_vida)
        pygame.draw.rect(self.display_superficie, '#000000', retangulo_display_vida)
        self.display_superficie.blit(superficie_display_vida, retangulo_display_vida)
 
    def caixa_selecao(self, x, y):
        plano_fundo = pygame.Rect(x, y, 80, 80)
        pygame.draw.rect(self.superficie_tela,cor_backgorund_interface,plano_fundo)
        pygame.draw.rect(self.superficie_tela,cor_bordas_interface,plano_fundo, 3)
        return plano_fundo

    def mostrar_arma_caixa(self, weapon_index):
        plano_fundo = self.caixa_selecao(10,610)
        superficie_arma = self.lista_imagem_armas[weapon_index]
        retangulo_arma = self.superficie_tela.get_rect(center = plano_fundo.center)

        self.superficie_tela.blit(superficie_arma, retangulo_arma)

    def desenho_bola(self):
        superficie_des_bola = pygame.image.load('graphics/coletaveis/bola_item/full.png')
        des_bola_rect = superficie_des_bola.get_rect(topleft=(10,90))
        self.display_superficie.blit(superficie_des_bola, des_bola_rect)

    def inventario_bolas(self, inventario):
        superficie_inventario = self.font.render(f"{str(inventario['bola'])}", True, 'White')
        inventario_rect = superficie_inventario.get_rect(topleft=(30, 90))
        self.display_superficie.blit(superficie_inventario, inventario_rect)

    def desenho_raquete(self):
        superficie_des_raquete = pygame.image.load('graphics/coletaveis/raquete_item/full.png')
        des_raquete_rect = superficie_des_raquete.get_rect(topleft=(10, 113))
        self.display_superficie.blit(superficie_des_raquete, des_raquete_rect)
    def inventario_raquetes(self, inventario):
        superficie_inventario = self.font.render('possui', True, 'White')
        inventario_rect = superficie_inventario.get_rect(topleft=(40, 130))
        self.display_superficie.blit(superficie_inventario, inventario_rect)

    def display(self, personagem):
        self.mostrar_barra(personagem.saude_atual, personagem.status_saude['saude'],self.retangulo_barra_saude, cor_barra_vida)
        if personagem.inventario['bola'] > 0:
            self.desenho_bola()
            self.inventario_bolas(personagem.inventario)
        if personagem.inventario["raquete"] == 1:
            self.desenho_raquete()
            self.inventario_raquetes(personagem.inventario)
        self.mostrar_barra_vida(personagem.saude,personagem.status_saude['saude'], self.barra_vida_rect, cor_barra_vida) 
        self.caixa_selecao(10,610)
        self.mostrar_arma_caixa(personagem.weapon_index)
