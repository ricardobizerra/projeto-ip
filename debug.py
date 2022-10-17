import pygame
pygame.init()
font = pygame.font.Font(None, 30)

#funcao para ter controle de cada elemento no jogo
def debug(info, y=10, x=10):
    superficie_display = pygame.display.get_surface()
    superficie_debug = font.render(str(info),True,'White')
    retangulo_debug = superficie_debug.get_rect(topleft = (x, y))
    pygame.draw.rect(superficie_display, 'Black', retangulo_debug)
    superficie_display.blit(superficie_debug, retangulo_debug)
