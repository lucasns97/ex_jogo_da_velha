from src.components.board import Board

def play(p1, p2, size, draw = True, debug = True):
  '''
  Função para executar uma partida de dois jogadores
  '''

  if draw:
    print('\nIniciando o jogo!\n')

  board = Board(size=size)
  board.set_players(p1, p2)

  round = 0

  if draw: 
    print(f'> Round {round}:')
    board.show()
    print()

  while True:

    done, winner = board.is_done()

    if done: break

    for player in board.players:

      round += 1

      if draw: print(f'>> Vez de {player.name} ({player.piece}):')

      if player.name == 'Você':
        pos = player.play_yourself(board)

      elif player.name == 'Random':
        pos = player.play_random(board)

      elif player.name == 'Minimax':
        pos   = player.play_minimax(board, debug = debug)

      elif player.name == 'Greedy':
        pos   = player.play_greedy(board)

      elif player.name == 'ExpectMinimax':
        pos   = player.play_expectminimax(board)

      check = board.add_piece(player.piece, pos)

      if draw:
        print(f'>>> Posição jogada: {pos}\n> Round {round}:')
        board.show()
        print()

      if not check: print('ERRO!')

      done, winner = board.is_done()

      if done: break
  
  data = {
      'winner': winner,
      'rounds': round
  }

  return data