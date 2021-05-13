
from settings import AVAILABLE_PLAYERS
from src.components.player import Player
from src.utils.play import play

def select_player():

    print('\nJogadores desponíveis:')
    for i, player_name in enumerate(AVAILABLE_PLAYERS):

        print(f'{i+1} - {player_name}')
    
    print()
    
    try:
        num = int(input('Digite o número do jogador que deseja adicionar: '))
    except:
        num = 0
    
    while num < 1 or num > len(AVAILABLE_PLAYERS):
        try:
            num = int(input('Não entendi, digite o número do jogador que deseja adicionar: '))
        except:
            num = 0
    
    player_name = AVAILABLE_PLAYERS[num-1]
    print(f'>> Jogador ~ {player_name} ~ escolhido.\n')

    return player_name


def select_players():

    # p1
    print('Escolha o primeiro jogador (joga com a peça \'1\'):')

    p1_name = select_player()
    p1 = Player(p1_name, 1)

    # p2
    print('Escolha o segundo jogador (joga com a peça \'2\'):')
    p2_name = select_player()
    p2 = Player(p2_name, 2)

    return p1, p2

def play_again():

    try:
        num = int(input('Digite 1 para jogar novamente ou 0 para sair: '))
    except:
        num = 0
    
    while num != 1 and num != 0:
        try:
            num = int(input('Não entendi, digite 1 para jogar novamente ou 0 para sair: '))
        except:
            num = 0

    if num == 1:
        return True
    
    return False



def main():

    print('#################################')
    print('#                               #')
    print('# Bem vindo/a ao Jogo da Velha! #')
    print('#                               #')
    print('#################################\n\n')

    while True:

        p1, p2 = select_players()

        data = play(p1, p2, size = 3, debug = False)

        winner = data['winner']

        if not winner:

            print('Deu velha!!')

        else:

            print(f'Parabêns ao vencedor: {winner.name} ({winner.piece})\n')

        if not play_again(): break