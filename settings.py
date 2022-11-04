#RESOLUCAO PARA HD
largura = 1280
altura = 720
FPS = 60
escala = 64   #64 PIXELS POR BLOCO (CONFIG PADRAO PARA JOGOS NESSE ESTILO)

#Interface de usuário.
altura_barra_vida = 20 
largura_barra_vida = 200
interface_fonte = None
tamanho_fonte_interface = 24

#Cores da interface de usuário.
cor_barra_vida = 'red'
cor_backgorund_interface = '#222222'
cor_bordas_interface = '#EEEEEE'

                #MAPA EM BRANCO(COMO SERÁ VAI DECIDIDO AINDA)
                #cada elemento da lista tem a distancia da escala para o inicio(0,0)
                

# dicionário de armas
weapon_data = {
    'raquete': {
        'cooldown': 100,
        'dano': 20,
        'graphic': 'graphics/weapons/raquete/full.png'
    },
    'bola': {
        'cooldown': 25,
        'dano': 2,
        'graphic': 'graphics/weapons/bola/full.png'
    }
}

# dicionario de inimigos.
monster_data = {
    'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash','speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}