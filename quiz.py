# Quiz game
from random import randint
import os
clear = lambda: os.system('cls')

clear()
"""
O jogo fará varias perguntas ao jogador, qunado respondidas corretamente o jo-
gador ganha um ponto, ao final das perguntas mostramos quantos pontos foram
marcados.
"""

def invalid():
    print('A resposta que você colocou é invalida')
    print('Digite apenas uma letra que ache ser a resposta correta')
    print('O jogo deve ser reiniciado')
    quit()

def getRespostaUser():
    r = input('Digite a letra da resposta que ache estar correta: ')
    try:
        if int(r):
            invalid()

    except:
        if 0 >= len(r) > 1:
            invalid()
        return r.lower()
def querJogar():
    if vezes == 0:
        r = input('Olá, deseja jogar nosso quiz? (sim / nao) \n>>')
    else:
        r = input('Deseja jogar novamente? (sim / nao) \n>>')

    try:
        if int(r):
            print()
            print('Opção invalida, o jogo será encerrado. Responda apenas com "sim" ou "nao" para jogar.')
            print()
            quit()

    except:
        if 'sim' != r:
            return False   
        return True

perguntas = ['Normalmente, quantos litros de sangue uma pessoa tem?',
'De quem é a famosa frase “Penso, logo existo”?',
'Quanto tempo a luz do Sol demora para chegar à Terra?',
'Jim Morrison era vocalista de que grupo']

opcoes = [
    {
    'a':'Tem entre 2 a 4 litros',
    'b':'Tem entre 4 a 6 litros',
    'c':'Tem 10 litros',
    'd':'Tem 7 litros'},
    {
    'a':'Platão',
    'b':'Galileu Galilei',
    'c':'Descartes',
    'd':'Sócrates',
    },
    {
    'a':'12 minutos',
    'b':'1 dia',
    'c':'12 horas',
    'd':'8 minutos',
    },
    {
    'a':'The Police',
    'b':'Nirvana',
    'c':'The Doors',
    'd':'ACDC',
    }
]

respostas = ['Tem entre 4 a 6 litros','Descartes','8 minutos','The Doors']
pontos = 0
vezes = 0
play = querJogar()

while play:
    clear()
    print('Show, vamos lá!')
    print()
    for ind in range(len(perguntas)):
        options = opcoes[ind]
        resposta = respostas[ind]

        print(perguntas[ind])
        print()
        for k, v in options.items():
            print(f'{k}) {v}')
        
        print()
        respostaUser = getRespostaUser()
        print()
        try:
            if options[respostaUser] != resposta:
                clear()
                print(f'Você errou, a resposta era "{resposta}"')
                print()
            else:
                clear()
                print('Muito boa! Você acertou!')
                pontos += 1
                print()
        except:
            quit()
    vezes += 1
    print('Fim da rodada')
    print(f'Você conseguiu {pontos} pontos!')
    play = querJogar()

clear()
print('Fim do jogo, espero que tenha gostado!')