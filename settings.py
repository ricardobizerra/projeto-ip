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
        'cooldown': 2500,
        'dano': 10,
        'graphic': 'graphics/weapons/bola/full.png'
    },
    'cracha': {
        'cooldown': 50,
        'dano': 15,
        'graphic': 'graphics/weapons/cracha/full.png'
    },
    'vetor': {
        'cooldown': 200,
        'dano': 25,
        'graphic': 'graphics/weapons/vetor/full.png'
    }
    }

# dicionario de inimigos.
enemy_data = {
        'enemy_mob' : {'health' : 75, 'dano' : 10, 'attack_type' : 'swipe', 'resistance' : 2, 'speed' : 7, 'attack_radius' : 15, 'notice_radius' : 400, 'withdraw_radius' : 0, 'cooldown_ataque' : 800, 'startup_ataque' : 400},
        'enemy_knight' : {'health' : 150, 'dano' : 20, 'attack_type' : 'shot', 'resistance' : 5, 'speed' : 5, 'attack_radius' : 40, 'notice_radius' : 400, 'withdraw_radius' : 20, 'cooldown_ataque' : 600, 'startup_ataque' : 300},
        'enemy_boss' : {'health' : 250, 'dano' : 30, 'attack_type' : 'slash', 'resistance' : 7, 'speed' : 3, 'attack_radius' : 75, 'notice_radius' : 300, 'withdraw_radius' : 50, 'cooldown_ataque' : 400, 'startup_ataque' : 200},
}
