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
        self.barra_vida_rect = pygame.Rect(10, 30, largura_barra_vida, altura_barra_vida)

        #Convertendo o dicionario de armas para uma lista.
        self.lista_imagem_armas = []
        for arma in weapon_data.values():
            path = arma['graphic']
            arma = pygame.image.load(path).convert_alpha()
            self.lista_imagem_armas.append(arma)

    def mostrar_barra_vida(self,vida_atual,qnt_max,retangulo_fundo,cor):
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

    def mostrar_arma_caixa(self, inventario, arma_equipada):
        plano_fundo = self.caixa_selecao(10,610)
        retangulo_arma = self.superficie_tela.get_rect(center = plano_fundo.center)
        superficie_arma = pygame.image.load('graphics/coletaveis/raquete_item/full.png')
        self.superficie_tela.blit(superficie_arma, retangulo_arma)

    def desenho_bola(self):
        superficie_des_bola = pygame.image.load('graphics/coletaveis/bola_item/full.png')
        des_bola_rect = superficie_des_bola.get_rect(topleft=(15,90))
        self.display_superficie.blit(superficie_des_bola, des_bola_rect)

    def inventario_bolas(self, inventario):
        superficie_inventario = self.font.render(f"{str(inventario['bola'])}  'B' para arremessar", True, 'Black')
        inventario_rect = superficie_inventario.get_rect(topleft=(35, 90))
        self.display_superficie.blit(superficie_inventario, inventario_rect)

    def desenho_raquete(self):
        superficie_des_raquete = pygame.image.load('graphics/coletaveis/raquete_item/full.png')
        des_raquete_rect = superficie_des_raquete.get_rect(topleft=(10, 193))
        self.display_superficie.blit(superficie_des_raquete, des_raquete_rect)
    def inventario_raquetes(self, inventario):
        superficie_inventario = self.font.render('2', True, 'Black')
        inventario_rect = superficie_inventario.get_rect(topleft=(40, 205))
        self.display_superficie.blit(superficie_inventario, inventario_rect)

    def desenho_coxinha(self):
        superficie_des_coxinha = pygame.image.load(('graphics/coletaveis/coxinha_item/full.png'))
        des_coxinha_rect = superficie_des_coxinha.get_rect(topleft=(10, 110))
        self.display_superficie.blit(superficie_des_coxinha, des_coxinha_rect)

    def inventario_coxinhas(self, inventario):
        superficie_inventario = self.font.render(f"{str(inventario['coxinha'])}  'F' para curar", True, 'Black')
        inventario_rect = superficie_inventario.get_rect(topleft=(40, 120))
        self.display_superficie.blit(superficie_inventario, inventario_rect)

    def desenho_cracha1(self):
        superficie_des_cracha = pygame.image.load(('graphics/coletaveis/cracha_item/full.png'))
        des_cracha_rect = superficie_des_cracha.get_rect(topleft=(-5, 135))
        self.display_superficie.blit(superficie_des_cracha, des_cracha_rect)

    def inventario_cracha1(self, inventario):
        superficie_inventario = self.font.render('1', True, 'Black')
        inventario_rect = superficie_inventario.get_rect(topleft=(40, 160))
        self.display_superficie.blit(superficie_inventario, inventario_rect)

    def desenho_vetor(self):
        superficie_des_vetor = pygame.image.load(('graphics/coletaveis/vetor_item/full2.png'))
        des_vetor_rect = superficie_des_vetor.get_rect(topleft=(0, 240))
        self.display_superficie.blit(superficie_des_vetor, des_vetor_rect)

    def inventario_vetor(self, inventario):
        superficie_inventario = self.font.render('3', True, 'Black')
        inventario_rect = superficie_inventario.get_rect(topleft=(40, 250))
        self.display_superficie.blit(superficie_inventario, inventario_rect)

    def desenho_pendrive(self):
        superficie_des_pendrive = pygame.image.load(('graphics/coletaveis/pendrive_item/full.png'))
        des_pendrive_rect = superficie_des_pendrive.get_rect(topleft=(0, 295))
        self.display_superficie.blit(superficie_des_pendrive, des_pendrive_rect)

    def inventario_pendrive(self, inventario):
        superficie_inventario = self.font.render('X', True, 'Black')
        inventario_rect = superficie_inventario.get_rect(topleft=(40, 310))
        self.display_superficie.blit(superficie_inventario, inventario_rect)

    def display(self, personagem):
        self.desenho_bola()
        self.inventario_bolas(personagem.inventario)
        self.desenho_coxinha()
        self.inventario_coxinhas(personagem.inventario)
        if personagem.inventario["raquete"] == 1:
            self.desenho_raquete()
            self.inventario_raquetes(personagem.inventario)
        if personagem.inventario['cracha'] == 1:
            self.desenho_cracha1()
            self.inventario_cracha1(personagem.inventario)
        if personagem.inventario['vetor'] == 1:
            self.desenho_vetor()
            self.inventario_vetor(personagem.inventario)
        if personagem.inventario['pendrive'] == 1:
            self.desenho_pendrive()
            self.inventario_pendrive(personagem.inventario)
        self.mostrar_barra_vida(personagem.saude_atual,personagem.status_saude['saude'], self.barra_vida_rect, cor_barra_vida)
        self.caixa_selecao(10,610)
        self.mostrar_arma_caixa(personagem.inventario, personagem.arma_equipada)
