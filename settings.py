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
