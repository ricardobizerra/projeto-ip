# from curses import noecho
import pygame
from obstaculo import Obstaculo
from player import Personagem
from settings import *
from support import *
from random import choice
from weapon import Weapon
from enemies import Inimigo
from debug import *
from interface_usuario import Interface_usuario
from coletaveis import *

class Level:
    def __init__(self):
        #definir o que vai para a tela do main
        self.superficie_tela = pygame.display.get_surface()

        #GRUPOS DE DE CONFIGURAÇÕES DE  SPRITES
        self.sprites_visiveis = YsortGrupoCamera()
        self.sprites_obstaculos = pygame.sprite.Group()

        #Attack sprites.
        self.ataque_atual = None 
        self.sprites_ataque = pygame.sprite.Group()
        self.sprites_atacaveis = pygame.sprite.Group()

        #CONFIGURAÇÃO DE SPRITE
        self.criar_mapa()
        
        #INTERFACE DO PERSONAGEM.
        self.iu = Interface_usuario()

    def criar_mapa(self):
        layouts = { 
            'boundary': import_csv_layout('map/map_Boundaries.csv'),
            'obstacle': import_csv_layout('map/map_Obstacles.csv'),
            'entities' : import_csv_layout('map/map_Entities.csv')
        }   
        graphics = {
            'grass': import_folder('graphics/Grass'),
            'objects': import_folder('graphics/objects')
        }

        #LOOP PRA CONSEGUIR INFORMACOES DAS COORDENADAS
        for style, layout in layouts.items():
            for index_linha, linha in enumerate(layout):
                for index_coluna, coluna in enumerate(linha):
                    if coluna != '-1':
                        x = index_coluna * escala
                        y = index_linha * escala
                        if style == 'boundary':
                            Obstaculo((x,y), [self.sprites_obstaculos], 'none')       
                        if style == 'obstacle' and coluna == '11':
                            surf = pygame.image.load('graphics/objects/12.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '12':
                            surf = pygame.image.load('graphics/objects/04.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '13':
                            surf = pygame.image.load('graphics/objects/03.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '2':
                            surf = pygame.image.load('graphics/blocks/boundary_block.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '4':
                            surf = pygame.image.load('graphics/blocks/red_block.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '28':
                            surf = pygame.image.load('graphics/spritespiskel/glass-top.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '133':
                            surf = pygame.image.load('graphics/spritespiskel/mesa hall.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '138':
                            surf = pygame.image.load('graphics/spritespiskel/mesapicnic.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '137':
                            surf = pygame.image.load('graphics/spritespiskel/escadaria.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '142':
                            surf = pygame.image.load('graphics/spritespiskel/placa.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '84':
                            surf = pygame.image.load('graphics/spritespiskel/couch.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '89':
                            surf = pygame.image.load('graphics/spritespiskel/chair.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '97':
                            surf = pygame.image.load('graphics/spritespiskel/chair (3).png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '44':
                            surf = pygame.image.load('graphics/spritespiskel/microondas.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '45':
                            surf = pygame.image.load('graphics/spritespiskel/sink.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '22':
                            surf = pygame.image.load('graphics/spritespiskel/Rect Table.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '47':
                            surf = pygame.image.load('graphics/spritespiskel/rect table y.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '107':
                            surf = pygame.image.load('graphics/spritespiskel/chair copa(2).png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '108':
                            surf = pygame.image.load('graphics/spritespiskel/chair copa(1).png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '110':
                            surf = pygame.image.load('graphics/spritespiskel/chair copa(3).png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '145':
                            surf = pygame.image.load('graphics/spritespiskel/refrigerator.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '91':
                            surf = pygame.image.load('graphics/spritespiskel/chair (2).png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '52':
                            surf = pygame.image.load('graphics/spritespiskel/mesa pc.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '17':
                            surf = pygame.image.load('graphics/spritespiskel/computador.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '141':
                            surf = pygame.image.load('graphics/spritespiskel/data center.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '66':
                            surf = pygame.image.load('graphics/spritespiskel/armario da.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '78':
                            surf = pygame.image.load('graphics/spritespiskel/mesa da caixa.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '61':
                            surf = pygame.image.load('graphics/spritespiskel/mesa ping pong.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '18':
                            surf = pygame.image.load('graphics/spritespiskel/mesa.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '67':
                            surf = pygame.image.load('graphics/spritespiskel/computador (2).png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '127':
                            surf = pygame.image.load('graphics/spritespiskel/cadeira convivencia.png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'obstacle' and coluna == '72':
                            surf = pygame.image.load('graphics/spritespiskel/mesa pc (5).png')
                            Obstaculo((x,y), [self.sprites_visiveis,self.sprites_obstaculos],'object',surf)
                        if style == 'entities':
                            if coluna == '0':
                                self.personagem = Personagem((2500,5000),[self.sprites_visiveis],self.sprites_obstaculos, self.criar_ataque)

        # Coletáveis no início
        self.bolinha_item1 = Coletaveis((1965, 5226), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.bolinha_item2 = Coletaveis((1801, 4590), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.bolinha_item3 = Coletaveis((1556, 2190), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.bolinha_item4 = Coletaveis((1556, 832), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.bolinha_item5 = Coletaveis((1556, 742), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.bolinha_item6 = Coletaveis((1066, 2355), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.bolinha_item7 = Coletaveis((2362, 3845), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.bolinha_item8 = Coletaveis((1982, 3535), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.bolinha_item9 = Coletaveis((1216, 3248), 'bola', [self.sprites_visiveis], self.sprites_obstaculos)
        self.raquete_item = Coletaveis((2236, 3979),'raquete', [self.sprites_visiveis], self.sprites_obstaculos)
        self.coxinha_item1 = Coletaveis((2244, 5875), 'coxinha', [self.sprites_visiveis], self.sprites_obstaculos)
        self.coxinha_item2 = Coletaveis((832, 2670), 'coxinha', [self.sprites_visiveis], self.sprites_obstaculos)
        self.coxinha_item3 = Coletaveis((1509, 2898), 'coxinha', [self.sprites_visiveis], self.sprites_obstaculos)
        self.coxinha_item4 = Coletaveis((1073, 1347), 'coxinha', [self.sprites_visiveis], self.sprites_obstaculos)
        self.coxinha_item5 = Coletaveis((1950, 4250), 'coxinha', [self.sprites_visiveis], self.sprites_obstaculos)
        self.coxinha_item6 = Coletaveis((2255, 2946), 'coxinha', [self.sprites_visiveis], self.sprites_obstaculos)
        self.coxinha_item7 = Coletaveis((1116, 3588), 'coxinha', [self.sprites_visiveis], self.sprites_obstaculos)
        self.cracha_item1 = Coletaveis((2500, 5200), 'cracha', [self.sprites_visiveis], self.sprites_obstaculos)
        self.vetor_item = Coletaveis((1090, 3004), 'vetor', [self.sprites_visiveis], self.sprites_obstaculos)
        self.pendrive = Coletaveis((1536, 668), 'pendrive', [self.sprites_visiveis], self.sprites_obstaculos)

        # Inimigos no inicio
        self.enemy_mob_externo1 = Inimigo('enemy_mob', (2400, 5500), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_boss_da = Inimigo('enemy_boss', (1428, 1006), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_boss_da2 = Inimigo('enemy_boss', (1246, 1016), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_knight_ccen = Inimigo('enemy_knight', (1024, 858), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_mob_danger1 = Inimigo('enemy_mob', (1156, 1926), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_mob_danger2 = Inimigo('enemy_mob', (1166, 2026), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_mob_externo2 = Inimigo('enemy_mob', (1852, 4600), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_mob_externo3 = Inimigo('enemy_mob', (1676, 5530), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_mob_externo4 = Inimigo('enemy_mob', (2156, 5530), [self.sprites_visiveis, self.sprites_atacaveis],  self.sprites_obstaculos, self.damage_player)
        self.enemy_knight_interno1 = Inimigo('enemy_knight', (1156, 3400), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_knight_interno2 = Inimigo('enemy_knight', (1156, 4266), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_knight_jardim1 = Inimigo('enemy_knight', (2164, 3667), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_knight_jardim2 = Inimigo('enemy_knight', (2394, 3677), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_knight_jardim3 = Inimigo('enemy_knight', (2108, 3431), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_mob_jardim1 = Inimigo('enemy_mob', (2483, 3426), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_knight_jardim4 = Inimigo('enemy_knight', (2483, 3126), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_mob_jardim2 = Inimigo('enemy_mob', (2815, 3038), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_boss_copa1 = Inimigo('enemy_boss', (862, 2876), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_boss_copa2 = Inimigo('enemy_boss', (1196, 2924), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_boss_copa3 = Inimigo('enemy_boss', (1200, 2584), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)
        self.enemy_boss_copa4 = Inimigo('enemy_boss', (1677, 2426), [self.sprites_visiveis, self.sprites_atacaveis], self.sprites_obstaculos, self.damage_player)

    # criação do ataque
    def criar_ataque(self, type):
        if self.personagem.inventario[type] > 0:
            Weapon(self.personagem, [self.sprites_visiveis, self.sprites_ataque], type, self.sprites_obstaculos)
            if type == 'bola':
                self.personagem.inventario['bola'] -= 1

    def logica_ataque(self):
        if self.sprites_ataque:
            for sprite_ataque in self.sprites_ataque:
                lista_sprites_colisao = pygame.sprite.spritecollide(sprite_ataque,self.sprites_atacaveis,False)
                if lista_sprites_colisao:
                    for alvo in lista_sprites_colisao:
                        alvo.levar_dano(self.personagem,sprite_ataque.sprite_type)

    def damage_player(self,amount,attack_type):
        if self.personagem.vulneravel:
            self.personagem.saude_atual -= amount
            self.personagem.vulneravel = False
            self.personagem.vulneravel_timer = pygame.time.get_ticks()

    def run(self):
        #ATUALIZA E MOSTRA O JOGO
        self.sprites_visiveis.draw_personalizado(self.personagem)
        self.sprites_visiveis.update()
        self.logica_ataque()
        self.sprites_visiveis.enemy_update(self.personagem)

        #Fazendo os coletáveis sumirem
        self.bolinha_item1.apagar_col(self.personagem)
        self.bolinha_item2.apagar_col(self.personagem)
        self.bolinha_item3.apagar_col(self.personagem)
        self.bolinha_item4.apagar_col(self.personagem)
        self.bolinha_item5.apagar_col(self.personagem)
        self.bolinha_item6.apagar_col(self.personagem)
        self.bolinha_item7.apagar_col(self.personagem)
        self.bolinha_item8.apagar_col(self.personagem)
        self.bolinha_item9.apagar_col(self.personagem)
        self.raquete_item.apagar_col(self.personagem)
        self.coxinha_item1.apagar_col(self.personagem)
        self.coxinha_item2.apagar_col(self.personagem)
        self.coxinha_item3.apagar_col(self.personagem)
        self.coxinha_item4.apagar_col(self.personagem)
        self.coxinha_item5.apagar_col(self.personagem)
        self.coxinha_item6.apagar_col(self.personagem)
        self.coxinha_item7.apagar_col(self.personagem)
        self.cracha_item1.apagar_col(self.personagem)
        self.vetor_item.apagar_col(self.personagem)
        self.pendrive.apagar_col(self.personagem)

        self.iu.display(self.personagem)

class YsortGrupoCamera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        #CONFIGS GERAIS
        self.superficie_tela = pygame.display.get_surface()
        self.half_widht = self.superficie_tela.get_size()[0] // 2
        self.half_height = self.superficie_tela.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
        # creating the floor
        self.floor_surf = pygame.image.load('graphics/tilemap/map.png')
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
        
    def draw_personalizado(self, personagem):

        #POSIÇÃO DA CÂMERA
        self.offset.x = personagem.rect.centerx - self.half_widht
        self.offset.y = personagem.rect.centery - self.half_height
        
         # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.superficie_tela.blit(self.floor_surf,floor_offset_pos)

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key= lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.superficie_tela.blit(sprite.image,offset_pos)

    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
    
