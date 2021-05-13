import numpy as np
from settings import NULL_PIECE

class Board():

  def __init__(self, size = 3):
    '''
    Inicializa tabuleiro
    '''

    self.size          = size
    self.table         = self.get_initial_table()
    self.all_pos       = self.get_all_pos()
    self.available_pos = self.get_available_pos()

  def set_players(self, p1, p2):
    '''
    Instancia fila de dois jogadores de forma aleatória
    '''

    self.players = np.random.choice([p1, p2], 2, replace=False)


  def get_all_pos(self):
    '''
    Retorna lista de todas as possiveis casas do tabuleiro
    '''

    all_pos = []

    for i in range(self.size):
      for j in range(self.size):
        
        pos = (i, j)
        all_pos.append(pos)

    return all_pos


  def get_available_pos(self):
    '''
    Retorna lista de todas as casas vazias do tabuleiro
    '''

    available_pos = []

    for pos in self.all_pos:
      if self.table[pos] == NULL_PIECE:
        
        available_pos.append(pos)
    
    return available_pos

  def copy_board(self):
    '''
    Retorna um novo Board com as mesmas configurações deste
    '''

    new_board = Board(size = self.size)

    for pos in new_board.all_pos:

      new_board.table[pos] = self.table[pos]
    
    new_board.available_pos = [pos for pos in self.available_pos]
    new_board.players       = self.players

    return new_board


  def get_initial_table(self):
    '''
    Retorna a matriz de posições iniciais do tabuleiro
    '''

    table = np.array([[NULL_PIECE for i in range(self.size)] for j in range(self.size)])

    return table

  def show(self):
    '''
    Exibe o tabuleiro
    '''

    print('#', end="   ")
    for i in range(self.size):
      print(f'{i}', end=" ")
    print()
    print(' ', end="   ")
    for i in range(self.size):
      print('―', end=" ")
    print()
    for j, row in enumerate(self.table):
      print(f'{j} |', end=" ")
      for piece in row:
        print(piece, end=" ")
      print()

  def add_piece(self, piece, pos):
    '''
    Adiciona peça ao tabuleiro e atualiza posições disponiveis
    '''

    if self.table[pos[0], pos[1]] != NULL_PIECE: return False

    self.table[pos[0], pos[1]] = piece
    self.available_pos.remove(pos)

    return True

  def restart(self):
    '''
    Reinicia o tabuleiro
    '''

    self.table         = self.get_initial_table()
    self.available_pos = self.get_available_pos()


  def finished_array(self, array, player_piece):
    '''
    Funcao auxiliar que checa se todos os elementos do array representam "player_piece"
    '''

    uniques = np.unique(array)
    if uniques.shape[0] == 1 and uniques[0] == player_piece:
      return True
    return False

  def is_empty(self):
    '''
    Verifica se o tabuleiro está vazio
    '''

    for row in self.table:
      for piece in row:
        if piece != NULL_PIECE:
          return False

    return True
    

  def is_done(self):
    '''
    Verifica se o tabuleiro está finalizado, retorna se sim, e caso isso aconteça, o vencedor se houver
    '''

    # check players
    for player in self.players:

      player_piece = player.piece

      # check rows:
      for row in self.table:

        is_winner = self.finished_array(row, player_piece)

        if is_winner: return True, player

      # check cols:
      for j in range(self.size):

        col = self.table[:, j]

        is_winner = self.finished_array(col, player_piece)

        if is_winner: return True, player

      # principal diagonal
      array = []
      for i in range(self.size):
        array.append(self.table[i, i])
      array = np.array(array)

      is_winner = self.finished_array(array, player_piece)

      if is_winner: return True, player

      # secondary diagonal
      array = []
      for i in range(self.size):
        array.append(self.table[self.size-i-1, i])
      array = np.array(array)

      is_winner = self.finished_array(array, player_piece)

      if is_winner: return True, player

    # check if is even
    is_even = True
    for row in self.table:
      for piece in row:
        if piece == NULL_PIECE: 
          is_even = False
          break
      if not is_even:
        break
    
    if is_even:
      return True, None

    return False, None