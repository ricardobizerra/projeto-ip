# Projeto-IP

Projeto de Introdução à Programação do semestre 2022.1, voltado para a utilização prática dos conhecimentos e ferramentas, com ênfase na Programação Orientada a Objetos aprendidos ao longo da cadeira, assim como da iniciação do trabalho colaborativo com o compartilhamento do código via GitHub e Git para a criação de um Sistema Interativo.

## Organização do Código

O código foi dividido em módulos como aconselhado pelos professores em grandes projetos como esse em questão, os quais estão organizados em:

- Main: é o módulo "chefe", ele que inicia o jogo e, para isso, precisa importar todos os outros módulos
- Settings: contém as configurações básicas do jogo e que serão fixas, como largura e comprimento de tela, taxa de FPS
- Debug: módulo direcionado para testar funcionalidades e erros que o jogo possa estar tendo
- Graphics: módulo com as imagens que serão as representações visuais do mapa, player, inimigos
- Player: módulo com a classe do jogador, referente as suas principais caracteristicas como movimentação, vida, também é aqui que está o código referente à câmera do jogo
- Obstaculos: 
- Entities: 

## Título do Projeto: Busca-Crachá
## Ferramentas utilizadas

O jogo foi desenvolvido em Python aliado ao Pygame, um conjunto de módulos para essa linguagem, escolhida pelas suas inúmeras ferramentas que permitem a criação de inúmeros jogos, o que foi mais prático para o grupo assim como pelo grande acervo em relação a documentação e tutoriais, dos quais, notadamente, nos inspiramos no vídeo do [Clear Code](https://www.youtube.com/c/ClearCode) criando um jogo estilo Zelda.
### Instalação do Pygame

Para rodar o jogo é necessário ter instalado o [Python3](https://www.python.org/downloads/) e o módulo [Pygame](https://www.pygame.org/)

Para instalar o Pygame, pode-se usar o comando
```sh
python3 -m pip install -U pygame --user
```

## Sobre o Projeto

O projeto é um jogo que foi inspirado no vídeo [como criar um jogo estilo Zelda em Python](https://www.youtube.com/watch?v=QU1pPzEGrqw), principalmente quanto às noções técnicas, organizacionais e de gênero de jogo.

Apesar das dificuldades de tratar de um projeto novo sem muita preparação, todos do grupo estão empenhados para expandir nossa base de conhecimentos e criar um projeto não só apresentável, mas divertido.

Além disso, foi criado um projeto no Notion para dar noção da espectativa e meta do projeto e, futuramente, divisão de tarefas.

O Busca-Crachá é um jogo 2D com câmera top-down que tem como foco o controle de um player, bolsista do Apple Academy, que passará por fases após combater inimigos a cada cenário e desbloquear acessos, coletáveis  e upgrades  para poder impedir o professor Calegário de obter informações confidenciais do Apple Academy.

## Contribuidores e funções

- Artur de Carvalho Lyra <a href="https://github.com/arcaly">(GitHub)</a>
    - Mantém GitHub
    - Atualiza a documentação
- João Luís Gomes Agra <a href="https://github.com/joca113">(GitHub)</a>
- Ricardo Bizerra de Lima Filho <a href="https://github.com/ricardobizerra">(GitHub)</a>
    - Criou nossa página no Notion
    - Responsável pelas armas
- Breno Gabriel de Melo Lima  <a href="https://github.com/breno-gabriel">(GitHub)</a>
    - Responsável pelos itens coletáveis
- Lucas Henrique do Nascimento Silva <a href="https://github.com/lucashnss ">(GitHub)</a>
    - Responsável pelo mapa e partes gráficas
- Severino Murilo da Silva <a href="https://github.com/Mur1loo">(GitHub)</a>
    - Adicionou base do código

## Conceitos vistos na disciplina e usados no código

    - Programação Orientada a Objetos foi um conceito visto em aula e fortemente utilizado, uma concepção de criar código utilizada em todo o jogo, com classes para os players, inimigos, coletáveis.
    - Listas: o uso de listas foi muito importante pois, com elas, conseguimos fazer uma matriz de listas e representar o mapa do nosso jogo

## Desafios e Erros
    - Maior erro do projeto:
    - Maior desafio do projeto:
    - Lições aprendidas: