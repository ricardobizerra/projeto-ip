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
enemy_data = {
        'mob_melee' : {'health' : 75, 'dano' : 20, 'attack_type' : 'cracha_curto', 'resistance' : 5, 'speed' : 7, 'attack_radius' : 25, 'notice_radius' : 400, 'withdraw_radius' : 0},
        'mob_ranged' : {'health' : 50, 'dano' : 10, 'attack_type' : 'bola', 'resistance' : 2, 'speed' : 5, 'attack_radius' : 400, 'notice_radius' : 600, 'withdraw_radius' : 200},
        'mob_elite' : {'health' : 250, 'dano' : 30, 'attack_type' : 'cracha_retratil', 'resistance' : 7, 'speed' : 6, 'attack_radius' : 75, 'notice_radius' : 1500, 'withdraw_radius' : 50}
}
