<h1> Quiz Game </h1>

Este é um jogo de perguntas e respostas simples em Python, implementado utilizando o paradigma de Programação Orientada a Objetos (POO). O jogo consiste em 10 perguntas sobre Ciencia da Computacao. Cada pergunta possui verdadeiro ou falso, sendo apenas uma a correta. O jogador ganha um ponto para cada resposta correta e, ao final do jogo, é exibida a pontuação final.


<br><h2> Funcionalidades </h2>

Sistema de perguntas de verdadeiro e falso
Contagem de pontos baseada nas respostas corretas
Feedback instantâneo após cada pergunta (correta/incorreta)
Interface de terminal simples
Fácil adição de novas perguntas

<br><h2> Tecnologias </h2>

Python 3.12

<br><h2> Requisitos </h2>

Python 3.12 instalado no sistema

<br><h2> Como Executar </h2>

Clone este repositório para sua máquina local:

git clone https://github.com/seu-usuario/quiz-game.git

Navegue até o diretório do projeto:

cd quiz-game

Execute o jogo:

python main.py

<br><h2> Estrutura de Arquivos </h2>

quiz-game/               <br>
 │                        <br>
├── main.py              # Arquivo principal do jogo                                                                           <br>
├── quiz_brain.py        # Classe QuizBrain onde sera realizada a logica de programacao do quiz                                <br>
├── question_model.py    # Classe Question com o construtor init, com as variaveis text e answer, entrando como parametros     <br>
├── data.py              # Arquivo com a lista, contendo perguntas e respostas                                                 <br>
└── README.md            # Arquivo de documentação              
 
<br><h2> Como Contribuir </h2>
 
Faça um fork deste repositório.
Crie uma nova branch com a sua feature: git checkout -b minha-feature.
Commit suas mudanças: git commit -m 'Adicionar nova feature'.
Faça um push para a branch: git push origin minha-feature.
Abra um Pull Request.

<br><h2> Licença </h2>

Este projeto está licenciado sob a MIT License.
