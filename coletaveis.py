import pygame
from settings import *
from support import import_folder
from player import Personagem
from level import *



class Coletaveis(pygame.sprite.Sprite):
    def __init__(self, pos, coletavel, grupo_sprite, player_rect):
        super().__init__(grupo_sprite)
        self.image = pygame.image.load(f'graphics/coletaveis/{coletavel}_item/full.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.superficie_tela = pygame.display.get_surface()
        self.coletavel = coletavel
        self.colidiu = False

    def colisao_col(self, hitbox_coletavel, hitbox_player, coletavel, inventario):
        if hitbox_coletavel.colliderect(hitbox_player) and self.colidiu == False:
            self.kill()
            self.colidiu = True
            if coletavel == 'bola':
                inventario['bola'] += 5
            elif coletavel == 'raquete':
                inventario['raquete'] = 1
            elif coletavel == 'coxinha':
                inventario['coxinha'] += 1
            elif coletavel == 'cracha':
                inventario['cracha'] += 1
            elif coletavel == 'vetor':
                inventario['vetor'] += 1
    def apagar_col(self, personagem):
        self.colisao_col(self.hitbox, personagem.hitbox, self.coletavel, personagem.inventario)
