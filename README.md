# Projeto-IP

Projeto de Introdução à Programação do semestre 2022.1, voltado para a utilização prática dos conhecimentos e ferramentas, com ênfase na Programação Orientada a Objetos aprendidos ao longo da cadeira, assim como da iniciação do trabalho colaborativo com o compartilhamento do código via GitHub e Git para a criação de um Sistema Interativo.

## Título do Projeto >> The Legend of Cin: Ocarina of Crachá

## Link do repositório no GitHub do projeto: [Clique aqui](https://github.com/ricardobizerra/projeto-ip.git)

## Organização técnica do Código

O código foi dividido em módulos, como aconselhado pelos professores em grandes projetos como esse em questão, os quais estão organizados em:

- **Main**: é o módulo "chefe", ele que inicia o jogo e, para isso, é o responsável por criar a tela em que o jogo passará, além de importar todos os outros módulos do projeto;
- **Settings**: contém as configurações básicas do jogo e que serão fixas, como largura e comprimento de tela, taxa de FPS;
- **Debug**: módulo direcionado para testar funcionalidades e erros que o jogo possa estar tendo, enviando para a tela informações mais "ocultas";
- **Graphics**: diretório com as imagens que serão apresentadas visualmente referentes à construção do mapa, do player, dos inimigos e coletáveis;
- **Map**: contém os arquivos CSV criados pelo Tiled para identificar a posição de cada elemento do mapa;
- **Player**: módulo com a classe do jogador, contendo atributos como sua imagem, hitbox, vida, inventário, e métodos de movimentação, combate (atacando, tomando dano), recuperação de vida e colisão;
- **Interface_usuario**: um grande módulo com a classe interface_usuario responsável por partes gráficas como o retângulo em que fica a vida do jogador, o inventário de armas, quantidade de bolas de ping pong;
- **Weapon**: módulo que consta com a classe de arma, que será utilizada para criar as diferentes armas utilizadas pelo jogador para causar dano e eliminar os inimigos, contendo atributos como imagem, rect (retângulo que conterá o objeto), hitbox, velocidade no caso de arremessáveis (como as bolas de ping pong), posições de ataque (esquerda, direita, cima, para baixo) e métodos de colisão, movimentação;
- **Enemies**: módulo com a classe dos inimigos, os quais serão os objetos que o jogador deverá eliminar, ele contem atributos como vida, posição, rect, hitbox, velocidade e métodos de colisão e dano;
- **Obstaculo**: contém uma classe, Obstáculo, que é utilizada pelo level para criar obstáculos colidíveis, visuais ou não, na tela do jogo, como paredes, árvores, colunas, blocos invisíveis que impedem que o jogador passe por certas áreas. Conta com os atributos de rect, hitbox, e imagem;
- **Support**: módulo com classes utilizadas pelo módulo level para ler os arquivos CSV do módulo map;
- **Coletaveis**: com a classe dos coletáveis, contando com os atributtos de rect, imagem, hitbox, tipo do coletável, identificar a colisão do personagem com ele, e os métodos referentes a cada tipo de coletável (recuperar vida, pegar a raquete ou pegar cinco bolas de ping pong) e apagar sua imagem após a coleta;
- **Level**: módulo robusto que importa boa parte dos outros módulos. Conta com a classe da câmera 2D top-down que acompanha a movimentação do personagem, renderiza a imagem do mapa que não interage com o personagem e inimigos. Possui também a classe de level, que possui os atributos dos sprites de inimigos, coletáveis, personagens que serão  renderizados com objeto dessa classe, além de utilizar os módulos de support para a leitura e desenho dos obstáculos;

## Ferramentas utilizadas

O jogo foi desenvolvido em **Python** aliado ao **Pygame**, um conjunto de módulos para essa linguagem, escolhida pelas suas inúmeras ferramentas que permitem a criação de inúmeros jogos, o que foi mais prático para o grupo assim como pelo grande acervo em relação a documentação e tutoriais, dos quais, notadamente, nos inspiramos no vídeo do [Clear Code](https://www.youtube.com/c/ClearCode) criando um jogo estilo Zelda.
### Instalação do Pygame

Para rodar o jogo é necessário ter instalado o [Python3](https://www.python.org/downloads/) e o módulo [Pygame](https://www.pygame.org/)

Para instalar o Pygame, pode-se usar o comando
```sh
python3 -m pip install -U pygame --user
```

Outra ferramenta importante foi o **Tiled**, um software de código aberto utilizado para a criação do mapa a partir de pngs criados em outra ferramente, o **Piskel**, um editor online de para criação de pixel art e sprites, ou obtidos de bibliotecas de arte da internet. Com os pngs, podemos adicionar eles em diferentes camadas que serão sobrepostas, podemos tornar eles visíveis ou não, sendo identificados apenas com suas posições, entre inúmeras função muito poderosas. Depois de criado, pode-se exportar, em arquivos CSV, a localização de cada elemento do mapa como números de seus respectivos IDs e lê-los pelo código do jogo utilizando matrizes.

![Imagem da criação de mapa do Tiled](https://www.mapeditor.org/img/posts/2018-09-world-view.png)

## Sobre o Projeto

O projeto é um jogo que foi inspirado no vídeo [como criar um jogo estilo Zelda em Python](https://www.youtube.com/watch?v=QU1pPzEGrqw), principalmente quanto às noções técnicas, organizacionais e de gênero de jogo.

Apesar das dificuldades de tratar de um projeto novo sem muita preparação, todos do grupo estão empenhados para expandir nossa base de conhecimentos e criar um projeto não só apresentável, mas divertido.

Além disso, foi criado um projeto no Notion para dar noção da espectativa e meta do projeto e, futuramente, divisão de tarefas.

O The Legend of Cin: Ocarina of Crachá é um jogo 2D com câmera top-down que tem como foco o controle de um player, bolsista do Apple Academy, que passará por fases após combater inimigos a cada cenário e desbloquear acessos, coletáveis  e upgrades  para poder impedir o professor Calegário de obter informações confidenciais do Centro de Informática da Universidade Federal de Pernambuco.

## Contribuidores e suas respectivas funções

- Artur de Carvalho Lyra <a href="https://github.com/arcaly">(GitHub)</a>
    - Mantém GitHub.
    - Atualiza a documentação.
    - Responsável pelos inimigos.
- João Luís Gomes Agra <a href="https://github.com/joca113">(GitHub)</a>
    - Responsável pelos coletáveis
- Ricardo Bizerra de Lima Filho <a href="https://github.com/ricardobizerra">(GitHub)</a>
    - Criou nossa página no Notion.
    - Maior coordenador do processo de merge, criação de branches e ferramentas do Git/GitHub.
    - Responsável pelas armas.
    - Idealizou e criou o  GitHub Bot, responsável por enviar no Discord qualquer alteração no repositório do projeto.
- Breno Gabriel de Melo Lima  <a href="https://github.com/breno-gabriel">(GitHub)</a>
    - Responsável pela interação jogador-inimigo.
    - Responsável pela interface-usuário.
- Lucas Henrique do Nascimento Silva <a href="https://github.com/lucashnss ">(GitHub)</a>
    - Responsável pela construção do mapa e sua renderização.
    - Atualiza a documentação.
    - Criou o servidor no discord para organização do projeto.
- Severino Murilo da Silva <a href="https://github.com/Mur1loo">(GitHub)</a>
    - Adicionou base do código.
    - Responsável pela construção do mapa e sua renderização. 

## Conceitos vistos na disciplina e usados no código

- **Programação Orientada a Objetos**: foi um conceito visto em aula e fortemente utilizado, uma concepção de criar código utilizada em todo o jogo, com classes para o player, inimigos, coletáveis, level, cada um com uma infinidade de atributos e métodos, e foi visível a grande importância dessa forma de programação em grandes projetos como esse jogo, facilitando a organização, compartilhamento de caracteristícas, funções, herança, etc.
- **Condicionais**: utilizado fortemente em todo o código, para conferir se o jogador está vivo ou não, se está colidindo numa parede, em um inimigo, atacando, conferir o tipo de arquivo CSV que será lido, o tipo de coletável que será renderizado/apagado, enfim, são unidades fundamentais e estão por quase todos os módulos.
- **Iterações**: também muito utilizado, na criação da matriz com as numérações advindas dos arquivos CSV para construir a matriz do mapa junto com listas ou para conferir em um conjunto de sprites se cada um colidiu com algo.
- **Listas**: utilizado junto com as iterações para guardar as informações do mapa, transformando os dicionários em listas com armas.
- **Funções**: uso muito grande delas, visto que são importantíssimas em grandes projetos para uma organização de cada objetivo do código, além de estar presente como métodos dos objetos, temos funções para movimentação, atacar, recuperar vida, criação de mapa, etc.
- **Dicionários**: utilizado para guardar os tipos de armas com suas características, além de guardar quais CSV que vão ser lidos, isto é, de qual camada do mapa.
- **Módulos e pacotes**: como descrito na organização, o código foi dividido em diversos módulos de acordo com sua função.

## Desafios e Erros
- Maior erro do projeto:
- Maior desafio do projeto: a produção coletiva de um código, visto que até o momento não utilizávamos o Git/GitHub além de fazer códigos apenas sozinhos, assim para implementar nossas funções tivemos que nos comunicar constantemente para entender as realizações de cada. Contornamos esse desafio a partir da construção de grupo no Whatsapp, servidor no Discord, página Notion para descrição do passo a passo do projeto, divisão de tarefas e planejamento, além de reuniões ocasionais além dos checkpoints.
- Lições aprendidas: o projeto foi extremamente importante para todos, com ele conseguimos pôr em pratica e entender a importância da Programação Orientada a Objetos, além de consolidar os conceitos vistos na matéria. Em questão colaborativa na criação de código foi muito fundamental para divisão de tarefas, comunicação e planejamento entre os membros, entender o código de outras pessoas, bem como utilizá-los junto ao nosso. Além disso, percebemos que sempre devemos buscar aprender as tecnologias mais ideais para o nosso projeto, tal como a biblioteca Pygame, uso do Git/GitHub, tão fundamental na nossa área, assim como buscar o Piskel e Tiled, para, respectivamente, criação de pixel art e do mapa, e até mesmo organizacionais como o Notion e o Discord.
