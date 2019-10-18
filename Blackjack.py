# Script para um jogo de 21 BOT VS 1 HUMANO
import random

naipes = ('Copas', 'Ouros', 'Espadas', 'Paus')
cartas = ('Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Valete', 'Dama', 'Rei', 'Ás')
valores = {'Dois': 2, 'Três': 3, 'Quatro': 4, 'Cinco': 5, 'Seis': 6, 'Sete': 7, 'Oito': 8, 'Nove': 9, 'Dez': 10,
           'Valete': 10, 'Dama': 10, 'Rei': 10, 'Ás': 11}

playing = True


class Carta:
    def __init__(self, naipes, cartas):
        self.naipes = naipes
        self.cartas = cartas

    def __str__(self):
        return self.cartas + ' de ' + self.naipes


class Deck:
    def __init__(self):
        self.deck = []
        for naipe in naipes:
            for carta in cartas:
                self.deck.append(Carta(naipe, carta))

    def __str__(self):
        deck_comp = ''
        for carta in self.deck:
            deck_comp += '\n' + carta.__str__()
        return 'O deck tem: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cartas = []
        self.valores = 0
        self.ases = 0

    def adc_carta(self, carta):
        self.cartas.append(carta)
        self.valores += valores[carta.cartas]

        if carta.cartas == 'Ás':
            self.ases += 1

    def ajustar_as(self):
        # se o valor passar de 21, a carta Ás toma valor 1
        while self.valores > 21 and self.ases:
            self.valores -= 10
            self.ases -= 1


# Somar ou subtrair fichas caso vitoria ou derrota
class Fichas:
    def __init__(self):
        self.total = int(input("Quantas fichas você tem? "))
        self.aposta = 0

    def vencer_aposta(self):
        self.total += self.aposta

    def perder_aposta(self):
        self.total -= self.aposta


# Função para aceitar aposta do jogador
def aceitar_aposta(fichas):
    while True:
        try:
            fichas.aposta = int(input('Quantas fichas você quer apostar? '))
        except:
            print('Desculpe, informe um número inteiro.')
        else:
            if fichas.aposta > fichas.total:
                print('Desculpe, você não tem fichas suficientes. Você possui {}'.format(fichas.total))
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.adc_carta(single_card)
    hand.ajustar_as()


def jogar_ou_parar(deck, hand):
    global playing

    while True:
        x = input('Mais carta ou parar? Digite C ou P. ')
        if x[0].lower() == 'c':
            hit(deck, hand)

        elif x[0].lower() == 'p':
            print('O jogador encerrou a jogada. Vez do Dealer.')
            playing = False

        else:
            print("Desculpe. Não entendi o comando. Por favor, digite apenas C ou P.")
            continue
        break


def jogador_estourou(jogador, dealer, fichas):
    print('JOGADOR ESTOUROU!')
    fichas.perder_aposta()


def jogador_venceu(jogador, dealer, fichas):
    print('JOGADOR VENCEU!')
    fichas.vencer_aposta()


def dealer_venceu(jogador, dealer, fichas):
    print('DEALER VENCEU!')
    fichas.perder_aposta()


def dealer_estourou(jogador, dealer, fichas):
    print('DEALER ESTOUROU!')
    fichas.vencer_aposta()


def push(jogador, dealer):
    print('JOGADOR E DEALER EMPATARAM! PUSH')


# Funções pra mostrar as cartas em jogo
def mostrar_algumas(jogador, dealer):
    print('\nMão do dealer:')
    print('<carta escondida>')
    print(dealer.cartas[1])
    print('\n')
    print('Mão do jogador:')
    for carta in jogador.cartas:
        print(carta)


def mostrar_todas(jogador, dealer):
    print('Mão do dealer:')
    for carta in dealer.cartas:
        print(carta)
    print('Pontuação: ', dealer.valores, sep='\n ')
    print('\n')
    print('Mão do jogador:')
    for carta in jogador.cartas:
        print(carta)
    print('Pontuação: ', jogador.valores, sep='\n ')


# Lógica do jogo 21
while True:
    # abertura do programa
    print('Bem vindo ao Blackjack!')

    # criar e embaralhar o baralho, dando 2 cartas pro jogador
    deck = Deck()
    deck.shuffle()

    mao_jogador = Hand()
    mao_jogador.adc_carta(deck.deal())
    mao_jogador.adc_carta(deck.deal())

    mao_dealer = Hand()
    mao_dealer.adc_carta(deck.deal())
    mao_dealer.adc_carta(deck.deal())

    # Definir fichas do jogador
    fichas_jogador = Fichas()

    # Solicitar quantidade de fichas da aposta
    aceitar_aposta(fichas_jogador)

    # Mostrar cartas, encobrindo uma do dealer
    mostrar_algumas(mao_jogador, mao_dealer)

    while playing:  # chamando esta variável global vinda da função 'jogar ou parar'
        # Solicitar escolha do jogador de parar ou jogar
        jogar_ou_parar(deck, mao_jogador)

        # Mostrar algumas cartas
        mostrar_algumas(mao_jogador, mao_dealer)

        # Caso o jogador passe de 21 pontos, recebera mensagem de derrota, caso não, comparar com valor do dealer para
        # definir vitoria ou derrota
        if mao_jogador.valores > 21:
            jogador_estourou(mao_jogador, mao_dealer, fichas_jogador)
            break

        # Se o jogador não estourar, deler joga até fazer 17 pontos
    if mao_jogador.valores <= 21:

        while mao_dealer.valores < mao_jogador.valores:
            hit(deck, mao_dealer)

        # Mostrar todas cartas do dealer
        mostrar_todas(mao_jogador, mao_dealer)

        if mao_dealer.valores > 21:
            dealer_estourou(mao_jogador, mao_dealer, fichas_jogador)
        elif mao_jogador.valores > mao_dealer.valores:
            jogador_venceu(mao_jogador, mao_dealer, fichas_jogador)
        elif mao_jogador.valores < mao_dealer.valores:
            dealer_venceu(mao_jogador, mao_dealer, fichas_jogador)
        else:
            push(mao_jogador, mao_dealer)

    # Informar o jogador a quantidade restante de fichas
    print('\n Fichas restantes do jogador: {}'.format(fichas_jogador.total))

    # Pergunta se o jogador deseja jogar novamente
    novo_jogo = input('Gostaria de jogar novamente? (Y/N) ')
    if novo_jogo[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Obrigado por jogar!')
        break
