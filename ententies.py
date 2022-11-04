import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.frame_index = 0 
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()

    def move(self, speed):

        #CORRIGIR A MOVIMENTAÇÃO QUANDO O PERSONAGEM ANDA NA DIAGONAL
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.colisao('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.colisao('vertical')
        self.rect.center = self.hitbox.center

    def colisao(self, direcao):
        if direcao == 'horizontal':
            for sprite in self.obstaculo_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #INDO PARA A DIREITA
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: #INDO PARA A ESQUERDA
                        self.hitbox.left = sprite.hitbox.right

        if direcao == 'vertical':
            for sprite in self.obstaculo_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: #INDO PARA BAIXO
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: #INDO PARA CIMA
                        self.hitbox.top = sprite.hitbox.bottom    

