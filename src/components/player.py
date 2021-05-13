import numpy as np
from settings import NULL_PIECE

from src.utils.minimax import min_val
from src.utils.expectminimax import expect_val

class Player():

  def __init__(self, name, piece):
    '''
    Inicializa jogador
    '''

    self.piece = piece
    self.name  = name

  def play_random(self, board, queue = []):
    '''
    Retorna posicao de uma jogada randômica
    '''

    table = board.table

    while True:

      rand = np.random.randint(0, board.size**2)

      row = rand%board.size
      col = rand//board.size

      pos = (row, col)

      if table[pos] == NULL_PIECE:
        return pos

  def play_greedy(self, board, queue = []):
    '''
    Retorna posicao de uma jogada gulosa
    '''
    
    for i in range(board.size):
      for j in range(board.size):
        
        pos = (i, j)
        piece = board.table[pos]

        if board.table[pos] == NULL_PIECE: return pos
  
  def play_yourself(self, board, queue = []):
    '''
    Requisita posição a ser jogada e a retorna
    '''

    possible = False

    try:
        pos = input('Digite a posição: ')
        pos = pos.split()
        pos[0] = int(pos[0])
        pos[1] = int(pos[1])
        pos = tuple(pos)

        possible = board.table[pos] == NULL_PIECE

    except:

        pos = None
        possible = False

    while not possible:

        try:
            pos = input('Não entendi, digite a posição (exemplo: \'0 2\' - sem aspas, para jogar na linha 0 e coluna 2): ')
            pos = pos.split()
            pos[0] = int(pos[0])
            pos[1] = int(pos[1])
            pos = tuple(pos)

            possible = board.table[pos] == NULL_PIECE

        except:

            pos = None
            possible = False

    return pos

  def play_minimax(self, board, debug = True):
    '''
    Retorna jogada resolvida pelo minimax
    '''

    if board.is_empty():
      return (0, 0)

    minimax_val = -999999
    minimax_pos = None

    for pos in board.available_pos:

      if debug: print('>>> Testando:', pos, end=' ')

      new_board = board.copy_board()

      new_board.add_piece(self.piece, pos)

      val = min_val(new_board, deep = 15, player_maximizer = self)

      if debug: print('=> val:', val)

      # arg_max
      if val > minimax_val:
        minimax_val = val
        minimax_pos = pos

    return minimax_pos

  def play_expectminimax(self, board, debug = True, max_expect_dist = 2):
    '''
    Retorna jogada resolvida pelo expectminimax
    '''

    if board.is_empty():
      return (0, 0)

    expectminimax_val = -999999
    expectminimax_pos = None

    for pos in board.available_pos:

      if debug: print('>>> Testando:', pos, end=' ')

      new_board = board.copy_board()

      new_board.add_piece(self.piece, pos)

      val = expect_val(board, new_board, deep = 15, origem = 'max', player_maximizer = self, expect_dist=0, max_expect_dist=max_expect_dist)

      if debug: print('=> val:', val)

      # arg_max
      if val > expectminimax_val:
        expectminimax_val = val
        expectminimax_pos = pos

    return expectminimax_pos